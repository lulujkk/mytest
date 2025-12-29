import streamlit as st
import pandas as pd
import joblib

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
        smoker = st.radio("是否吸烟", ["是", "否"], index=1)  # 默认“否”
        region = st.selectbox("区域", ["东南部", "东北部", "西北部", "西南部"], index=0)

    # 缓存模型（避免重复加载）
    @st.cache_resource
    def load_trained_model():
        return joblib.load("medical_cost_model.joblib")
    model = load_trained_model()

    # 预测按钮
    if st.button("预测费用"):
        # 构造输入数据（与训练时的特征列名一致）
        input_data = pd.DataFrame({
            "年龄": [age], "性别": [gender], "BMI": [bmi],
            "子女数量": [children], "是否吸烟": [smoker], "区域": [region]
        })
        # 执行预测并显示结果
        try:
            cost = model.predict(input_data)[0]
            st.success(f"✅ 预测医疗费用：{cost:.2f} 元")
        except Exception as e:
            st.error(f"预测失败：{str(e)}")
