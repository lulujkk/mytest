import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import pickle

# ----------------------------
# 【关键】修复中文乱码
# ----------------------------
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 设置页面配置
st.set_page_config(page_title="学生成绩分析与预测系统", layout="wide", page_icon="📊")

# ----------------------------
# 全局：加载数据和模型
# ----------------------------
DATA_PATH = "student_data_adjusted_rounded.csv"
MODEL_PATH = "model.pkl"

# 加载数据
try:
    df = pd.read_csv(DATA_PATH)
except Exception as e:
    st.error(f"❌ 无法加载数据文件: {e}")
    st.stop()

# 自定义CSS样式（深色主题）
custom_css = """
<style>
body {
    background-color: #0a0a0a;
    color: #e0e0e0;
    font-size: 12px;
}
.stApp {
    background-color: #0a0a0a;
}
.sidebar .sidebar-content {
    background-color: #121212;
    color: #ffffff;
}
.stButton>button {
    background-color: #ff4b4b;
    color: white;
    border: none;
    padding: 4px 10px;
    border-radius: 2px;
    font-size: 10px;
}
.stButton>button:hover {
    background-color: #e53935;
}
.stTextInput, .stSelectbox, .stSlider {
    background-color: #1e1e1e;
    color: white;
    border: 1px solid #333;
}
h1, h2, h3, h4, h5, h6 {
    color: #ffffff;
    margin-top: 0.5rem;
    margin-bottom: 0.5rem;
}
.stDataFrame {
    font-size: 11px;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ----------------------------
# 导航栏
# ----------------------------
with st.sidebar:
    st.title("🧭 导航菜单")
    page = st.radio("选择页面", ["项目介绍", "专业数据分析", "成绩预测"])

# ----------------------------
# 1. 项目介绍页
# ----------------------------
if page == "项目介绍":
    st.title("🎓 学生成绩分析与预测系统")
    
    st.markdown("""
    本项目是一个基于 Streamlit 的学生学业表现分析平台，通过数据可视化和机器学习技术，
    帮助教育工作者和学生深入了解学业表现，并预测期末考试成绩。
    """)

    # 图片切换控件和图片（放在右上角）
    col_main, col_sidebar = st.columns([3, 1])  # 主内容区占3/4，图片区占1/4
    
    with col_sidebar:
        st.markdown("### 图片预览")
        
        # 初始化session state
        if 'current_img_index' not in st.session_state:
            st.session_state.current_img_index = 0
        
        # 图片列表
        img_list = ["1.png", "2.png"]
        img_captions = ["学生数据可视化示意图", "系统架构图"]
        
        # 箭头按钮布局
        col_prev, col_next = st.columns([1, 1])
        with col_prev:
            if st.button("◀", key="prev_img"):
                st.session_state.current_img_index = (st.session_state.current_img_index - 1) % len(img_list)
        with col_next:
            if st.button("▶", key="next_img"):
                st.session_state.current_img_index = (st.session_state.current_img_index + 1) % len(img_list)
        
        # 显示当前图片索引
        st.write(f"图片 {st.session_state.current_img_index + 1}/{len(img_list)}")
        
        # 显示当前选中的小尺寸图片
        current_img = img_list[st.session_state.current_img_index]
        current_caption = img_captions[st.session_state.current_img_index]
        
        try:
            # 使用较小的固定宽度显示图片
            st.image(current_img, caption=current_caption, width=200)
        except FileNotFoundError:
            st.warning(f"图片文件 {current_img} 未找到")
            # 占位符图片
            st.image("https://via.placeholder.com/200x150?text=图片未找到", caption="图片加载失败", width=200)

    with col_main:
        st.header("🎯 项目目标")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("**目标一**\n- 分析影响成绩的关键因素\n- 探索成绩相关性\n- 提供教学支持决策")
        with col2:
            st.markdown("**目标二**\n- 可视化展示各专业数据\n- 性别比例分析\n- 学习行为对比")
        with col3:
            st.markdown("**目标三**\n- 基于机器学习模型预测\n- 个性化成绩预测\n- 及时干预建议")

        st.header("🛠️ 技术架构")
        tech_cols = st.columns(4)
        tech_cols[0].markdown("**前端框架**\nStreamlit")
        tech_cols[1].markdown("**数据处理**\nPandas\nNumPy")
        tech_cols[2].markdown("**可视化**\nMatplotlib\nPlotly")
        tech_cols[3].markdown("**机器学习**\nScikit-learn")

# ----------------------------
# 2. 专业数据分析页（✅ 图表缩小 + 表格水平对齐 + 保留1位小数）
# ----------------------------
elif page == "专业数据分析":
    st.title("📊 专业数据分析")
    st.markdown("#### 专业数据可视化分析")

    # 设置黑色背景图表样式
    plt.style.use('dark_background')

    # 1. 各专业男女性别比例
    st.subheader("1. 各专业男女性别比例")
    gender_count = df.groupby(["专业", "性别"]).size().unstack(fill_value=0)
    
    col_chart, col_table = st.columns([3, 1])
    with col_chart:
        fig1, ax1 = plt.subplots(figsize=(5.5, 2.8))
        gender_count.plot(kind='bar', ax=ax1, color=['skyblue', 'dodgerblue'], width=0.8)
        ax1.set_ylabel("人数", fontsize=8)
        ax1.set_title("性别分布", fontsize=9)
        ax1.legend(['女', '男'], fontsize=7, loc='upper right')
        ax1.tick_params(axis='both', which='major', labelsize=6)
        ax1.grid(axis='y', alpha=0.3)
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(fig1)
    with col_table:
        total = gender_count.sum(axis=1)
        ratio_df = pd.DataFrame({
            "女 (%)": (gender_count["女"] / total * 100).round(1),
            "男 (%)": (gender_count["男"] / total * 100).round(1)
        })
        st.markdown("##### 性别比例")
        st.table(ratio_df.style.format("{:.1f}").set_properties(**{'font-size': '9px'}))

    # 2. 各专业学习指标对比
    st.subheader("2. 各专业学习指标对比")
    metrics = ["每周学习时长（小时）", "期中考试分数", "期末考试分数"]
    detail_df = df.groupby("专业")[metrics].mean().round(1)
    avg_study = detail_df["每周学习时长（小时）"]
    avg_midterm = detail_df["期中考试分数"]
    avg_final = detail_df["期末考试分数"]
    
    col_chart, col_table = st.columns([3, 1])
    with col_chart:
        fig2, ax2 = plt.subplots(figsize=(5.5, 2.8))
        x = np.arange(len(avg_study))
        width = 0.35
        ax2.bar(x, avg_study, width, label='学习时长', alpha=0.8, color='lightblue')
        ax2.plot(x, avg_midterm, marker='o', linestyle='--', linewidth=1.2, label='期中', color='orange')
        ax2.plot(x, avg_final, marker='s', linestyle='-', linewidth=1.2, label='期末', color='green')
        ax2.set_xlabel('专业', fontsize=8)
        ax2.set_ylabel('值', fontsize=8)
        ax2.set_title('学习指标', fontsize=9)
        ax2.set_xticks(x)
        ax2.set_xticklabels(avg_study.index, rotation=45, fontsize=7)
        ax2.legend(fontsize=7, loc='upper right')
        ax2.grid(axis='y', alpha=0.3)
        plt.tight_layout()
        st.pyplot(fig2)
    with col_table:
        st.markdown("##### 平均值")
        st.table(detail_df.style.format("{:.1f}").set_properties(**{'font-size': '9px'}))

    # 3. 各专业出勤率分析
    st.subheader("3. 各专业出勤率分析")
    avg_attendance = df.groupby("专业")["上课出勤率"].mean()
    
    col_chart, col_table = st.columns([3, 1])
    with col_chart:
        fig3, ax3 = plt.subplots(figsize=(5.5, 2.8))
        colors = ['#FFD700', '#90EE90', '#4169E1', '#FF69B4', '#FFA500', '#87CEEB']
        ax3.bar(avg_attendance.index, avg_attendance.values, color=colors[:len(avg_attendance)])
        ax3.set_ylabel('出勤率', fontsize=8)
        ax3.set_title('出勤率分布', fontsize=9)
        ax3.set_xticklabels(avg_attendance.index, rotation=45, fontsize=7)
        ax3.grid(axis='y', alpha=0.3)
        plt.tight_layout()
        st.pyplot(fig3)
    with col_table:
        rank_df = avg_attendance.to_frame().reset_index()
        rank_df.columns = ["专业", "出勤率"]
        st.markdown("##### 排名")
        st.table(rank_df.style.format({"出勤率": "{:.1%}"}).set_properties(**{'font-size': '9px'}))

    # 4. 大数据管理专业专项分析
    st.subheader("4. 大数据管理专业专项分析")
    bigdata_df = df[df["专业"] == "大数据管理"]
    if not bigdata_df.empty:
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("出勤率", f"{bigdata_df['上课出勤率'].mean():.1%}")
        with col2:
            st.metric("期末成绩", f"{bigdata_df['期末考试分数'].mean():.1f}分")
        with col3:
            st.metric("及格率", f"{(bigdata_df['期末考试分数'] >= 60).mean():.1%}")
        with col4:
            st.metric("学习时长", f"{bigdata_df['每周学习时长（小时）'].mean():.1f}小时")

        col_hist, col_box = st.columns(2)
        with col_hist:
            fig4, ax4 = plt.subplots(figsize=(5, 2.5))
            scores = bigdata_df["期末考试分数"]
            ax4.hist(scores, bins=10, edgecolor='black', alpha=0.7, color='green')
            ax4.set_xlabel('期末成绩', fontsize=8)
            ax4.set_ylabel('频数', fontsize=8)
            ax4.set_title('成绩分布', fontsize=9)
            ax4.tick_params(labelsize=7)
            ax4.grid(axis='y', alpha=0.3)
            plt.tight_layout()
            st.pyplot(fig4)
        with col_box:
            fig5 = px.box(bigdata_df, y="期末考试分数", title="成绩箱线图")
            fig5.update_layout(
                height=250,
                margin=dict(t=30, b=10, l=10, r=10),
                title_font_size=10,
                font_size=8
            )
            st.plotly_chart(fig5, use_container_width=True)

    # 恢复默认样式（避免影响其他页面）
    plt.style.use('default')
# 3. 成绩预测页（✅ 图片尺寸调小）
# ----------------------------
else:
    st.title("🔮 期末成绩预测")
    st.info("请输入学生的学习信息，系统将预测其期末成绩并提供学习建议。")

    col1, col2 = st.columns([1, 2])
    with col1:
        student_id = st.text_input("学号", "2023123456", help="输入学生学号", max_chars=12)
        gender = st.selectbox("性别", ["男", "女"], help="选择性别")
        major = st.selectbox("专业", df["专业"].unique(), help="选择专业")
    with col2:
        study_hours = st.slider("每周学习时长(小时)", 5.0, 30.0, 15.0, 0.5, help="建议每天学习2-3小时")
        attendance = st.slider("上课出勤率", 0.5, 1.0, 0.8, 0.05, help="实际出勤比例")
        midterm_score = st.slider("期中考试分数", 0, 100, 75, help="期中考试成绩")
        homework_rate = st.slider("作业完成率", 0.6, 1.0, 0.9, 0.05, help="作业完成比例")

    # 加载模型
    try:
        with open(MODEL_PATH, "rb") as f:
            model = pickle.load(f)
    except Exception as e:
        st.error(f"❌ 模型加载失败: {e}")
        st.stop()

    if st.button("预测期末成绩", type="primary", help="点击预测期末成绩"):
        input_data = np.array([[study_hours, attendance, midterm_score, homework_rate]])
        predicted_score = model.predict(input_data)[0]
        
        if predicted_score >= 60:
            st.success(f"🎉 预测期末成绩: {predicted_score:.1f} 分")
            # 缩小图片尺寸
            st.image(
                "https://tse3-mm.cn.bing.net/th/id/OIP-C.SIPkPOfp_VwDxd738KjSmwHaF-?w=225&h=181&c=7&r=0&o=7&pid=1.7&rm=3",
                caption="恭喜你！预测结果显示你会及格！",
                width=200  # 设置图片宽度为200像素
            )
        else:
            st.error(f"⚠️ 预测期末成绩: {predicted_score:.1f} 分")
            # 缩小图片尺寸
            st.image(
                "https://img.ixintu.com/upload/jpg/20210524/1943a1b97fce8aabe8e016ef3fd3dbc9_49161_800_800.jpg!con",
                caption="加油！预测结果显示你需要努力了！",
                width=200  # 设置图片宽度为200像素
            )
