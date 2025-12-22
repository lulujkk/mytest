import streamlit as st
import pandas as pd
import numpy as np
import json

# --------------------------
# 页面配置 + 深色主题自定义样式
# --------------------------
st.set_page_config(
    page_title="南宁美食数据仪表盘",
    page_icon="🍜",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 自定义深色主题CSS
st.markdown("""
<style>
    /* 全局深色背景 + 浅色文字 */
    .stApp {
        background-color: #121212;
        color: #ffffff;
    }
    h2, h3, h4 {
        color: #f0f0f0;
        font-weight: 600;
    }
    /* 图表背景透明 */
    .st-chart {
        background-color: transparent !important;
    }
    /* 数据模块背景 */
    .stMetric {
        background-color: #1E1E1E;
        color: #ffffff;
        border-radius: 8px;
        padding: 10px;
    }
    /* 分割线样式 */
    hr {
        border-top: 1px solid #333333;
    }
    /* X轴标签横向显示 */
    .st-chart svg g[class*="xtick"] text {
        writing-mode: horizontal-tb !important;
        transform: rotate(0deg) !important;
        text-anchor: middle !important;
        font-size: 14px !important;
    }
    .st-chart svg {
        padding-bottom: 20px !important;
    }
</style>
""", unsafe_allow_html=True)

# --------------------------
# 1. 数据准备（纯Python原生类型，避免numpy类型，分离地图数据）
# --------------------------
# （1）南宁美食店铺基础信息（6家，纯Python类型）
shops_raw_data = {
    "店铺名称": [
        "中山路老友粉总店",
        "复记老友粉七星路店",
        "南铁螺蛳粉总店",
        "邕州老街粉饺王",
        "甘家界柠檬鸭总店",
        "卷筒粉明园店"
    ],
    "评分": [4.8, 4.7, 4.6, 4.5, 4.9, 4.7],  # Python float
    "地址": [
        "南宁市青秀区中山路66号",
        "南宁市青秀区七星路89号",
        "南宁市西乡塘区南铁一街23号",
        "南宁市江南区邕州老街12号",
        "南宁市兴宁区邕武路18号",
        "南宁市青秀区民主路12号"
    ],
    "纬度": [22.8167, 22.8215, 22.8450, 22.7890, 22.8670, 22.8250],  # Python float
    "经度": [108.3220, 108.3280, 108.3020, 108.3450, 108.3350, 108.3300],  # Python float
    "招牌菜价格(元)": [18, 16, 15, 12, 68, 10]  # Python int
}
# 主数据框
df_shops = pd.DataFrame(shops_raw_data)
# 地图专用数据框（仅保留经纬度，避免多余列干扰序列化）
df_map = df_shops[["纬度", "经度"]].copy()
# 终极处理：将数据框转为字典再转回，清除pandas元数据
df_map = pd.DataFrame(json.loads(df_map.to_json()), index=df_map.index)

# （2）5家餐厅12个月价格走势（5条折线，纯Python类型）
months = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]
price_trend_data = {
    "月份": months,
    "中山路老友粉": [18, 18, 19, 19, 20, 20, 20, 19, 19, 18, 18, 18],
    "复记老友粉": [16, 16, 15, 15, 16, 16, 16, 15, 15, 16, 16, 15],
    "南铁螺蛳粉": [15, 15, 14, 14, 15, 15, 15, 14, 14, 15, 15, 14],
    "邕州老街粉饺王": [12, 12, 12, 11, 11, 12, 12, 11, 11, 12, 12, 12],
    "甘家界柠檬鸭": [68, 68, 70, 70, 72, 72, 72, 70, 70, 68, 68, 68]
}
df_price_trend = pd.DataFrame(price_trend_data)

# （3）用餐高峰时段数据（用于area_chart）
meal_time_data = {
    "时段": ["10:00", "11:00", "12:00", "13:00", "14:00", "17:00", "18:00", "19:00", "20:00", "21:00"],
    "客流": [50, 120, 200, 150, 80, 100, 220, 250, 180, 100]
}
df_meal_time = pd.DataFrame(meal_time_data)

# --------------------------
# 2. 界面布局（修复st.map，仅用经纬度，移除复杂参数）
# --------------------------
st.title("🍜 南宁美食数据仪表盘")
st.markdown("---")

# 模块1：餐厅分布地图（终极修复：仅用经纬度，无size/color动态参数）
st.subheader("📍 餐厅分布")
if len(df_map) == 0:
    st.warning("⚠️ 暂无餐厅数据，无法显示地图！")
else:
    # 仅传递经纬度，使用默认size/color，避免序列化问题
    st.map(
        df_map,
        latitude="纬度",
        longitude="经度",
        zoom=11  # 仅保留zoom，其余参数用默认
    )
st.markdown("---")

# 模块2：餐厅评分柱状图
st.subheader("⭐ 餐厅评分")
st.bar_chart(
    df_shops,
    x="店铺名称",
    y="评分",
    color="#4CAF50",
    height=350,
    use_container_width=True
)
st.markdown("---")

# 模块3：5家餐厅12个月价格走势折线图（5条折线）
st.subheader("📈 5家餐厅12个月价格走势（元）")
st.line_chart(
    df_price_trend,
    x="月份",
    y=df_price_trend.columns[1:],  # 5家餐厅的价格列（5条折线）
    color=["#2196F3", "#FF9800", "#4CAF50", "#F44336", "#9C27B0"],
    height=350,
    use_container_width=True
)
st.markdown("---")

# 模块4：用餐高峰时段面积图
st.subheader("⏰ 用餐高峰时段客流分布")
st.area_chart(
    df_meal_time,
    x="时段",
    y="客流",
    color="#2196F3",
    height=350,
    use_container_width=True
)
st.markdown("---")

# 模块5：餐厅评价概览
st.subheader("💬 餐厅评价概览")
col1, col2, col3 = st.columns(3)
with col1:
    max_rating_idx = df_shops["评分"].idxmax()
    st.metric("最高评分", f"{df_shops['评分'].max()}分", df_shops["店铺名称"][max_rating_idx])
with col2:
    avg_price = df_shops["招牌菜价格(元)"].mean()
    st.metric("平均招牌菜价格", f"¥{avg_price:.1f}")
with col3:
    st.metric("收录店铺数", f"{len(df_shops)}家")
st.markdown("---")

# 模块6：今日美食推荐
st.subheader("🥢 今日推荐：中山路老友粉")
st.markdown("**南宁特色：老友粉以酸、辣、咸、香著称，是南宁人的早餐首选！**")
st.image(
    "https://pic1.zhimg.com/80/v2-799c897990686609996688696877659c_1440w.jpg",
    caption="中山路老友粉总店 - 招牌老友粉",
    use_column_width=True
)
