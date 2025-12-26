import streamlit as st
import pandas as pd
import numpy as np
import requests
from io import BytesIO
from PIL import Image

# ===================== 全局配置 =====================
st.set_page_config(
    page_title="多功能控制中心",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===================== 侧边栏导航（改为按钮列表） =====================
st.sidebar.title("🚀 多功能控制中心")

# 初始化当前页面状态
if "current_page" not in st.session_state:
    st.session_state.current_page = "星际学员档案"

pages = [
    "星际学员档案",
    "南宁公园数据",
    "网络图片相册",
    "网易云音乐播放器",
    "喜羊羊视频中心",
    "个人简历生成器"
]

# 显示按钮导航（可选：加高亮标记）
for page in pages:
    if st.sidebar.button(
        f"{'👉 ' if page == st.session_state.current_page else ''}{page}",
        use_container_width=True,
        key=f"nav_{page}"
    ):
        st.session_state.current_page = page

app_mode = st.session_state.current_page

# ===================== 模块1：星际学员档案 =====================
def show_star_archives():
    st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #000000 0%, #0a1929 50%, #001220 100%); color: #ffffff; font-family: 'Courier New', monospace; }
    .block-container { padding: 1rem !important; max-width: 900px !important; }
    h1 { color: #00ffff; text-shadow: 0 0 5px #00ffff; font-size: 20px !important; margin-bottom: 0.5rem !important; }
    h2, h3 { color: #00ff99; border-bottom: 1px solid rgba(0,255,153,0.3); padding-bottom: 4px !important; margin-bottom: 0.5rem !important; font-size: 16px !important; }
    .sci-fi-card { background: rgba(10, 25, 41, 0.8); border: 1px solid #00ffff; border-radius: 8px; padding: 10px !important; margin-bottom: 10px !important; box-shadow: 0 0 8px rgba(0,255,255,0.2); }
    .status-normal { color: #00ff99; } .status-warning { color: #ffcc00; } .status-error { color: #ff4d4d; } .status-info { color: #00ffff; }
    </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        st.markdown("<div style='text-align:center; padding:10px; border:2px solid #00ff99; border-radius:8px; margin-bottom:10px;'>", unsafe_allow_html=True)
        st.markdown("<h3 style='margin:0;'>🆔 学员标识</h3>", unsafe_allow_html=True)
        st.markdown("<p class='status-normal'>NTD-2023-001</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("### 📋 核心档案")
        st.markdown(f"""
        - **等级**：<span class='status-normal'>星际开发者 Lv.8</span>
        - **权限**：<span class='status-warning'>β测试权限</span>
        - **注册时间**：2023-09-01
        - **最后同步**：{pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}
        - **加密状态**：<span class='status-info'>已加密 🔒</span>
        """, unsafe_allow_html=True)
        st.divider()
        st.markdown("<center><span class='status-info'>⚠️ 仅限授权访问</span></center>", unsafe_allow_html=True)

    st.markdown("<div class='sci-fi-card'>", unsafe_allow_html=True)
    st.title("🚀 星际学员 - 胡汉三 数字档案仪表盘")
    st.markdown("<p class='status-info' style='font-size:12px;margin:0;'>【档案类型：技术能力评估 | 版本：v2.1】</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    col1, col2 = st.columns([1.5, 2.5])
    with col1:
        st.markdown("<div class='sci-fi-card'>", unsafe_allow_html=True)
        st.subheader("📊 基础状态监测")
        basic_data = pd.DataFrame({
            "监测维度": ["生理状态", "精神阈值", "能量储备", "网络连接", "任务负载"],
            "当前状态": [
                "<span class='status-normal'>稳定 ✔️</span>",
                "<span class='status-normal'>92% 🟢</span>",
                "<span class='status-warning'>85% 🟡</span>",
                "<span class='status-normal'>加密连接 ✔️</span>",
                "<span class='status-error'>78% 🔴</span>"
            ]
        })
        st.write(basic_data.to_html(escape=False, index=False), unsafe_allow_html=True)
        st.markdown("### 📝 状态说明\n- 生理状态：各项指标在安全阈值内\n- 能量储备：中等，建议4小时后补充\n- 任务负载：高负载，建议优先完成紧急任务", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='sci-fi-card'>", unsafe_allow_html=True)
        st.subheader("🛠️ 编程技能矩阵")
        skill_col1, skill_col2, skill_col3 = st.columns(3)
        with skill_col1: st.metric(label="Python", value="95%", delta="+5% （本月）")
        with skill_col2: st.metric(label="C++", value="87%", delta="-2% （本月）")
        with skill_col3: st.metric(label="Java", value="68%", delta="+10% （本月）")
        st.markdown("### 📈 技能成长趋势\n- Python：持续提升，已达精通级别\n- C++：小幅回落，需加强实战训练\n- Java：快速提升，本月进步显著\n- 前端开发：75%（稳定提升）\n- 数据可视化：90%（核心优势技能）", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    col3, col4 = st.columns(2)
    with col3:
        st.markdown("<div class='sci-fi-card'>", unsafe_allow_html=True)
        st.subheader("📜 任务执行日志")
        task_data = pd.DataFrame({
            "任务ID": ["T-1234", "T-5678", "T-9012"],
            "任务名称": ["学生信息管理系统", "课程数据可视化", "AI错题分析工具"],
            "进度": ["<span class='status-normal'>85%</span>", "<span class='status-normal'>100%</span>", "<span class='status-warning'>60%</span>"],
            "优先级": ["高", "中", "紧急"]
        })
        st.write(task_data.to_html(escape=False, index=False), unsafe_allow_html=True)
        total_tasks = len(task_data)
        completed = len(task_data[task_data["进度"].str.contains("100%")])
        st.progress(completed / total_tasks if total_tasks > 0 else 0)
        st.markdown(f"- 总任务数：{total_tasks} | 已完成：<span class='status-normal'>{completed}</span>\n- 紧急任务：1项（AI错题分析工具）需优先处理", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col4:
        st.markdown("<div class='sci-fi-card'>", unsafe_allow_html=True)
        st.subheader("💻 核心任务执行代码")
        core_code = '''def star_task_executor(task_id: str, priority: str) -> bool:
    config = load_task_config(task_id)
    if priority == "紧急":
        allocate_high_resources()
        st.warning(f"[紧急任务] {task_id} 资源已超频")
    try:
        result = execute_task(config)
        st.success(f"[任务完成] {task_id} 执行成功")
        return True
    except Exception as e:
        st.error(f"[任务异常] {task_id} 错误：{e}")
        return False'''
        st.code(core_code, language="python")
        st.markdown("<center><i class='status-info'>核心引擎：v2.1 | 最后更新：2025-12-18</i></center>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
    <div style='text-align:center; color:#00ffff; font-size:10px; margin-top:10px; padding:5px; border-top:1px solid #00ff99;'>
    <p>星际学员档案系统 v2.1 | 数据加密级别：最高 | 系统状态：在线 ✔️</p>
    <p>© 2025 星际开发学院 - 未经授权禁止复制/传播</p>
    </div>
    """, unsafe_allow_html=True)

# ===================== 模块2：南宁公园数据 =====================
def show_nanning_parks():
    st.markdown("""
    <style>
    .main .block-container { max-width: 95% !important; width: 95% !important; padding-left: 2rem !important; padding-right: 2rem !important; }
    .dataframe { width: 100% !important; table-layout: auto !important; }
    .dataframe th, .dataframe td { white-space: nowrap !important; padding: 8px 12px !important; }
    </style>
    """, unsafe_allow_html=True)

    month_nums = list(range(1,13))
    month_names = [f"{i}月" for i in month_nums]
    month_num_to_name = dict(zip(month_nums, month_names))

    park_info = pd.DataFrame({
        "公园名称": ["青秀山风景区","南湖公园","南宁市人民公园","狮山公园","石门森林公园","良凤江国家森林公园"],
        "地址": ["青秀区凤岭南路6号","青秀区双拥路1号","兴宁区人民东路1号","兴宁区邕武路4号","青秀区民族大道118号","江南区友谊路78号"],
        "占地面积(公顷)": [437.6, 191.9, 50.1, 80.2, 160.0, 486.7],
        "年游客量(万人次)": [650, 820, 480, 320, 390, 210],
        "游客评分(5分制)": [4.8, 4.7, 4.6, 4.5, 4.4, 4.3],
        "纬度": [22.8167, 22.8469, 22.8728, 22.8958, 22.8397, 22.6522],
        "经度": [108.3572, 108.3267, 108.3225, 108.3017, 108.3508, 108.3689]
    })

    price_data = pd.DataFrame({
        "月份数字": month_nums,
        "青秀山风景区": [30]*12,
        "南湖公园": [0.1]*12,
        "南宁市人民公园": [0.1]*12,
        "狮山公园": [0.1]*12,
        "石门森林公园": [0.1]*12,
        "良凤江国家森林公园": [20,20,15,15,20,15,15,15,15,20,15,15]
    })
    price_data["月份"] = price_data["月份数字"].map(month_num_to_name)

    monthly_visitor_data = pd.DataFrame({
        "月份数字": month_nums,
        "青秀山风景区": [55,78,52,45,60,48,42,40,38,85,50,45],
        "南湖公园": [68,85,72,65,75,62,58,55,60,90,70,65],
        "南宁市人民公园": [40,55,42,38,45,35,32,30,28,60,42,38],
        "狮山公园": [28,35,30,25,32,26,24,22,20,40,28,25],
        "石门森林公园": [32,40,35,30,38,32,29,27,25,45,35,30],
        "良凤江国家森林公园": [18,25,20,16,22,18,15,14,12,30,19,16]
    })
    monthly_visitor_data["月份"] = monthly_visitor_data["月份数字"].map(month_num_to_name)

    with st.sidebar:
        st.header("🌳 选择公园")
        selected_parks = st.multiselect("勾选要查看的公园", park_info["公园名称"].tolist(), default=park_info["公园名称"].tolist())

    filtered_price_data = price_data[["月份数字", "月份"] + selected_parks]
    filtered_monthly_visitor = monthly_visitor_data[["月份数字", "月份"] + selected_parks]
    filtered_park_info = park_info[park_info["公园名称"].isin(selected_parks)]

    st.markdown("<h1 style='text-align: center; color: #2E8B57;'>🌳 南宁公园数据可视化仪表盘</h1>", unsafe_allow_html=True)
    st.divider()

    st.markdown("<h3 style='text-align: center;'>一、公园基础信息</h3>", unsafe_allow_html=True)
    st.dataframe(filtered_park_info.drop(["纬度","经度"],axis=1), use_container_width=True, hide_index=True)

    st.divider()
    st.markdown("<h3 style='text-align: center;'>二、12个月门票价格走势</h3>", unsafe_allow_html=True)
    color_map = {"青秀山风景区":"#E53E3E","良凤江国家森林公园":"#DD6B20","南湖公园":"#38A16980","南宁市人民公园":"#3182CE80","狮山公园":"#805AD580","石门森林公园":"#D69E2E80"}
    chart_colors = [color_map.get(p, "#ccc") for p in selected_parks]
    st.line_chart(filtered_price_data, x="月份数字", y=selected_parks, color=chart_colors, y_label="门票价格（元）", height=400)
    st.markdown("<p style='text-align: center;'>x轴：1=1月，...，12=12月</p>", unsafe_allow_html=True)

    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h3 style='text-align: center;'>三、年游客量对比</h3>", unsafe_allow_html=True)
        st.bar_chart(filtered_park_info.set_index("公园名称")["年游客量(万人次)"], color="#2E8B57", height=350)
    with col2:
        st.markdown("<h3 style='text-align: center;'>四、月度游客量趋势</h3>", unsafe_allow_html=True)
        st.area_chart(filtered_monthly_visitor, x="月份数字", y=selected_parks, color=chart_colors, y_label="月度游客量（万人次）", height=350)

    st.divider()
    st.markdown("<h3 style='text-align: center;'>五、公园位置分布</h3>", unsafe_allow_html=True)
    st.map(filtered_park_info, latitude="纬度", longitude="经度", zoom=11)
    st.markdown("<h3 style='text-align: center;'>📌 公园地址详情</h3>", unsafe_allow_html=True)
    st.dataframe(filtered_park_info[["公园名称","地址"]].set_index("公园名称"), use_container_width=True)

    st.markdown("<hr><p style='text-align: center; color: #666;'>© 2025 南宁公园数据可视化平台</p>", unsafe_allow_html=True)

# ===================== 模块3：网络图片相册 =====================
def show_photo_gallery():
    PHOTO_CONFIG = [
        {"url": "https://picsum.photos/800/500?random=1", "caption": "静谧的山间湖泊"},
        {"url": "https://picsum.photos/800/500?random=2", "caption": "城市天际线全景"},
        {"url": "https://picsum.photos/800/500?random=3", "caption": "秋日森林小径"},
        {"url": "https://picsum.photos/800/500?random=4", "caption": "海边日落美景"},
        {"url": "https://picsum.photos/800/500?random=5", "caption": "雪山之巅风光"}
    ]
    PHOTO_URLS = [item["url"] for item in PHOTO_CONFIG]
    PHOTO_CAPTIONS = [item["caption"] for item in PHOTO_CONFIG]

    if "current_index" not in st.session_state:
        st.session_state.current_index = 0

    def load_image_from_url(url):
        try:
            headers = {"User-Agent": "Mozilla/5.0"}
            response = requests.get(url, headers=headers, timeout=10)
            img = Image.open(BytesIO(response.content))
            return img
        except:
            return None

    st.markdown("<h1 style='text-align: center; color: #2E86AB;'>📷 网络图片相册</h1>", unsafe_allow_html=True)
    st.divider()

    col1, col2, col3 = st.columns([1,2,1])
    current_idx = st.session_state.current_index
    with col1:
        if st.button("⬅️ 上一张", use_container_width=True):
            st.session_state.current_index = max(0, current_idx - 1)
    with col2:
        st.markdown(f"<p style='text-align: center;'>第 {current_idx + 1} / {len(PHOTO_URLS)} 张</p>", unsafe_allow_html=True)
    with col3:
        if st.button("下一张 ➡️", use_container_width=True):
            st.session_state.current_index = min(len(PHOTO_URLS)-1, current_idx + 1)

    st.divider()
    img = load_image_from_url(PHOTO_URLS[current_idx])
    caption = PHOTO_CAPTIONS[current_idx]
    st.image(img if img else "https://picsum.photos/800/500?random=0", width=800, caption=caption)
    st.markdown(f"<p style='text-align: center; font-size: 16px; color: #2E86AB;'>图注：{caption}</p>", unsafe_allow_html=True)

# ===================== 模块4：音乐播放器 =====================
def show_music_player():
    music_list = [
        {"name": "关山酒", "url": "https://music.163.com/song/media/outer/url?id=3323746308", "cover": "http://p2.music.126.net/EpX1U8WYebXOzo-jJ8MW5w==/109951172371108092.jpg?param=130y130"},
        {"name": "如果呢", "url": "https://music.163.com/song/media/outer/url?id=1842728629", "cover": "http://p2.music.126.net/-xMsNLpquZTmMZlIztTgHg==/109951165953469081.jpg?param=130y130"},
        {"name": "执迷不悟", "url": "https://music.163.com/song/media/outer/url?id=1477539203", "cover": "http://p1.music.126.net/NQCtUkal5sPxK1Y25SW3-Q==/109951165303077538.jpg?param=130y130"}
    ]

    if "music_idx" not in st.session_state:
        st.session_state.music_idx = 0

    def switch_song(direction):
        idx = st.session_state.music_idx
        if direction == "prev":
            st.session_state.music_idx = (idx - 1) % len(music_list)
        else:
            st.session_state.music_idx = (idx + 1) % len(music_list)

    current = music_list[st.session_state.music_idx]
    st.title("🎶 简易网易云音乐播放器")
    st.image(current["cover"], width=280)
    st.subheader(current["name"])
    st.audio(current["url"])

    col1, col2, col3 = st.columns(3)
    with col1: st.button("上一首", on_click=switch_song, args=("prev",), use_container_width=True)
    with col3: st.button("下一首", on_click=switch_song, args=("next",), use_container_width=True)

# ===================== 模块5：视频播放器 =====================
def show_video_player():
    video_arr = [
        {'url': 'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/01/84/153468401/153468401_nb3-1-16.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&uipk=5&oi=1939826609&gen=playurlv3&os=bcache&og=cos&deadline=1766568458&platform=html5&nbs=1&trid=000011f7dee85e0e4500b50a469aa245b7cp&mid=0&upsig=28823198b82cdcfaaa99c68d7384ef73&uparams=e,uipk,oi,gen,os,og,deadline,platform,nbs,trid,mid&cdnid=6590&bvc=vod&nettype=0&bw=203166&dl=0&f=p_0_0&qn_dyeid=&agrr=1&buvid=&build=0&orderid=0,1', 'title': '喜羊羊与灰太狼-第1集'},
        {'url': 'http://upos-sz-mirrorcos.bilivideo.com/upgcxcode/22/49/34889204922/34889204922-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&mid=0&oi=144233936&deadline=1766569302&nbs=1&uipk=5&gen=playurlv3&platform=html5&os=08hbv&og=hw&trid=4c8f7fd2de1748d380ea94fc7b04b27O&upsig=ead28cac9166011725b1c8a204be65a0&uparams=e,mid,oi,deadline,nbs,uipk,gen,platform,os,og,trid&bvc=vod&nettype=1&bw=568430&agrr=1&buvid=&build=7330300&dl=0&f=O_0_0&orderid=0,3', 'title': '喜羊羊与灰太狼-第2集'},
        {'url': 'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/59/03/34761540359/34761540359-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&mid=0&gen=playurlv3&os=estgcos&og=cos&nbs=1&platform=html5&oi=2067284620&deadline=1766569368&uipk=5&trid=35e4d536387444449872dde85727dc6h&upsig=fe0c1ba3dfc102e3c16f0eaff5e53272&uparams=e,mid,gen,os,og,nbs,platform,oi,deadline,uipk,trid&bvc=vod&nettype=0&bw=679039&agrr=1&buvid=&build=0&dl=0&f=h_0_0&orderid=0,1', 'title': '喜羊羊与灰太狼-第3集'}
    ]

    if 'ind' not in st.session_state:
        st.session_state.ind = 0

    st.title(video_arr[st.session_state.ind]['title'])
    st.video(video_arr[st.session_state.ind]['url'])

    cols = st.columns(len(video_arr))
    for i, col in enumerate(cols):
        with col:
            st.button(f"第{i+1}集", key=f"btn_{i}", on_click=lambda idx=i: st.session_state.update(ind=idx), use_container_width=True)

# ===================== 模块6：简历生成器 =====================
def show_resume_builder():
    st.markdown("""
    <style>
    .stApp { background-color: #1e1e1e; color: #e6e6e6; }
    h1, h2, h3 { color: #00c8ff !important; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("# 🎯 个人简历生成器")

    col1, col2 = st.columns([1, 2])
    with col1:
        name = st.text_input("姓名", "陆杨平")
        position = st.text_input("职位", "软件测试")
        phone = st.text_input("电话", "17677169536")
        email = st.text_input("邮箱", "237917611@qq.com")
        birth_date = st.date_input("出生日期", value=None)
        gender = st.radio("性别", ["男", "女", "其他"], index=0)
        education = st.selectbox("学历", ["本科", "硕士", "博士"], index=0)
        languages = st.multiselect("语言能力", ["中文", "英语", "日语"], default=["中文", "英语"])
        skills = st.multiselect("技能", ["Java", "HTML/CSS", "机器学习", "Python", "SQL", "C++"], default=["Java", "HTML/CSS", "机器学习", "Python"])
        work_years = st.slider("工作经验（年）", 0, 30, 6)
        salary_range = st.slider("期望薪资范围（元）", 5000, 50000, (10123, 29390))
        bio = st.text_area("个人简介", "热爱技术，追求卓越。")
        max_online_time = st.number_input("每日最长联系时间（分钟）", 1, 1440, 120)
        uploaded_file = st.file_uploader("上传个人照片", type=["jpg", "jpeg", "png"])

    with col2:
        st.subheader("📄 简历实时预览")
        st.markdown(f"<h2 style='color:#00c8ff;'>{name}</h2>", unsafe_allow_html=True)
        if uploaded_file:
            st.image(uploaded_file, width=120)
        else:
            st.image("https://via.placeholder.com/150/000000/ffffff?text=Avatar", width=120)

        col_a, col_b = st.columns(2)
        with col_a:
            st.write("**性别**: ", gender)
            st.write("**学历**: ", education)
            st.write("**工作年限**: ", work_years, "年")
            st.write("**最佳联系时间**: ", max_online_time, "分钟")
        with col_b:
            st.write("**职位**: ", position)
            st.write("**电话**: ", phone)
            st.write("**邮箱**: ", email)
            st.write("**出生日期**: ", birth_date.strftime("%Y/%m/%d") if birth_date else "未填写")

        st.markdown("---")
        st.subheader("🛠️ 专业技能")
        for skill in skills:
            st.markdown(f"• {skill}")

        st.markdown("---")
        st.subheader("📝 个人简介")
        st.write(bio)

        st.markdown(f"<p style='color:#00c8ff; font-weight:bold;'>期望薪资范围: {salary_range[0]} - {salary_range[1]} 元</p>", unsafe_allow_html=True)
        st.markdown("<div style='text-align:right; color:#66ccff; font-style:italic;'>在算法的世界里，你是最优解 ✨</div>", unsafe_allow_html=True)

# ===================== 主逻辑：根据选择显示模块 =====================
if app_mode == "星际学员档案":
    show_star_archives()
elif app_mode == "南宁公园数据":
    show_nanning_parks()
elif app_mode == "网络图片相册":
    show_photo_gallery()
elif app_mode == "网易云音乐播放器":
    show_music_player()
elif app_mode == "喜羊羊视频中心":
    show_video_player()
elif app_mode == "个人简历生成器":
    show_resume_builder()
else:
    st.info("请选择左侧功能模块开始使用。")
