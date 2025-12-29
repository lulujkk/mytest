import streamlit as st
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression

# 页面配置
st.set_page_config(page_title="医疗费用预测", layout="wide")

# 侧边栏导航
st.sidebar.title("导航")
nav = st.sidebar.radio("", ["简介", "预测医疗费用"])

# 「简介」页面
if nav == "简介":
    st.title("应用简介")
    st.write("这个应用利用机器学习模型预测医疗费用，可为保险公司的保险定价提供参考。")
    st.write("通过输入被保险人的年龄、性别、BMI等信息，即可快速得到医疗费用的预测结果。")

# 「预测医疗费用」页面
else:
    st.title("预测医疗费用")
    st.write("请输入被保险人信息，点击按钮获取预测结果：")

    # 分栏布局输入控件
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("年龄", min_value=0, max_value=120, value=25)
        gender = st.radio("性别", ["男性", "女性"], index=0)
        bmi = st.number_input("BMI", min_value=0.0, max_value=50.0, value=22.00, format="%.2f")
    with col2:
        children = st.number_input("子女数量", min_value=0, max_value=10, value=0)
        smoker = st.radio("是否吸烟", ["是", "否"], index=1)
        region = st.selectbox("区域", ["东南部", "东北部", "西北部", "西南部"], index=0)

    # 云端直接训练模型（无需上传pkl）
    @st.cache_resource
    def train_model_on_cloud():
        # 加载云端的数据集
        try:
            df = pd.read_csv("insurance-chinese.csv", encoding="gbk")
        except:
            # 备用：直接用内置示例数据（避免CSV编码问题）
            data = {
                "年龄": [19,18,28,33,32,31,46,37,37,60],
                "性别": ["女性","男性","男性","男性","男性","女性","女性","女性","男性","女性"],
                "BMI": [27.9,33.77,33.0,22.705,28.88,25.74,33.44,27.74,29.83,25.84],
                "子女数量": [0,1,3,0,0,0,1,3,2,0],
                "是否吸烟": ["是","否","否","否","否","否","否","否","否","否"],
                "区域": ["西南部","东南部","东南部","西北部","西北部","东南部","东南部","西北部","东北部","西北部"],
                "医疗费用": [16884.924,1725.5523,4449.462,21984.47061,3866.8552,3756.6216,8240.5896,7281.5056,6406.4107,28923.13692]
            }
            df = pd.DataFrame(data)
        
        X = df.drop("医疗费用", axis=1)
        y = df["医疗费用"]
        
        # 预处理+训练
        categorical_cols = ["性别", "是否吸烟", "区域"]
        numerical_cols = ["年龄", "BMI", "子女数量"]
        preprocessor = ColumnTransformer(
            transformers=[
                ("num", "passthrough", numerical_cols),
                ("cat", OneHotEncoder(drop="first"), categorical_cols)
            ]
        )
        model = Pipeline(steps=[
            ("preprocessor", preprocessor),
            ("regressor", LinearRegression())
        ])
        model.fit(X, y)
        return model
    
    model = train_model_on_cloud()

    # 预测按钮
    if st.button("预测费用"):
        input_data = pd.DataFrame({
            "年龄": [age], "性别": [gender], "BMI": [bmi],
            "子女数量": [children], "是否吸烟": [smoker], "区域": [region]
        })
        try:
            cost = model.predict(input_data)[0]
            st.success(f"✅ 预测医疗费用：{cost:.2f} 元")
        except Exception as e:
            st.error(f"预测失败：{str(e)}")
