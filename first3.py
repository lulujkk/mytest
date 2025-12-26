import pandas as pd
import streamlit as st

def get_dataframe_from_excel():
    """从Excel文件读取数据并处理"""
    # 使用原始字符串 r"" 避免反斜杠转义问题
    excel_path = r"C:\Users\710\Downloads\supermarket_sales.xlsx"
    
    df = pd.read_excel(
        excel_path,
        sheet_name='销售数据',      # 工作表名称（请确认Excel中是否有这个工作表名）
        skiprows=1,                # 跳过第1行（标题行）
        index_col='订单号'          # 将"订单号"列作为索引
    )
    
    # 处理时间列
    df['时间'] = pd.to_datetime(df['时间'], format='%H:%M:%S')
    df['小时数'] = df['时间'].dt.hour
    
    return df

# 读取数据
try:
    sale_df = get_dataframe_from_excel()
    st.success("✅ 数据加载成功！")
except Exception as e:
    st.error(f"❌ 数据加载失败: {e}")
    st.stop()

# 打印前5行（仅在控制台显示，不影响网页）
print("销售数据前5行：")
print(sale_df.head())

# Streamlit 应用界面
st.title("📊 销售仪表板")

# 侧边栏筛选条件
st.sidebar.header("筛选条件")

# 城市筛选
selected_cities = st.sidebar.multiselect(
    "城市",
    options=sale_df['城市'].unique(),
    default=sale_df['城市'].unique()
)

# 顾客类型筛选
selected_customer_types = st.sidebar.multiselect(
    "顾客类型",
    options=sale_df['顾客类型'].unique(),
    default=sale_df['顾客类型'].unique()
)

# 性别筛选
selected_genders = st.sidebar.multiselect(
    "性别",
    options=sale_df['性别'].unique(),
    default=sale_df['性别'].unique()
)

# 产品类型筛选
selected_product_types = st.sidebar.multiselect(
    "产品类型",
    options=sale_df['产品类型'].unique(),
    default=sale_df['产品类型'].unique()
)

# 筛选数据
filtered_df = sale_df[
    (sale_df['城市'].isin(selected_cities)) &
    (sale_df['顾客类型'].isin(selected_customer_types)) &
    (sale_df['性别'].isin(selected_genders)) &
    (sale_df['产品类型'].isin(selected_product_types))
]

# 关键指标
st.header("关键指标")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("总销售额", f"¥{filtered_df['总价'].sum():,.0f}")
with col2:
    st.metric("平均评分", f"{filtered_df['评分'].mean():.1f} ★")
with col3:
    st.metric("每单平均销售额", f"¥{filtered_df['总价'].mean():,.2f}")

# 图表
st.header("销售分析")
col1, col2 = st.columns(2)

with col1:
    st.subheader("按小时数销售额")
    hourly_sales = filtered_df.groupby("小时数")["总价"].sum().reset_index()
    st.bar_chart(hourly_sales.set_index("小时数"))

with col2:
    st.subheader("按产品类型销售额")
    product_sales = filtered_df.groupby("产品类型")["总价"].sum().reset_index()
    st.bar_chart(product_sales.set_index("产品类型"))

# 原始数据表格
st.header("原始数据")
st.dataframe(filtered_df)
