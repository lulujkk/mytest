import streamlit as st
import pandas as pd
import numpy as np
# ===================== 1. 页面核心配置（紧凑居中） =====================
st.set_page_config(
    page_title="星际学员数字档案",
    layout="centered",
    initial_sidebar_state="expanded",
    page_icon="🚀"
)
# ===================== 2. 科幻CSS（移除图片样式+紧凑布局） =====================
st.markdown("""
<style>
/* 全局样式 */
.stApp {
    background: linear-gradient(135deg, #000000 0%, #0a1929 50%, #001220 100%);
    color: #ffffff;
    font-family: 'Courier New', monospace;
    font-size: 12px !important;
}
/* 页面内边距压缩 */
.block-container {
    padding-top: 1rem !important;
    padding-bottom: 1rem !important;
    padding-left: 1rem !important;
    padding-right: 1rem !important;
    max-width: 900px !important;
}
/* 标题样式（精简） */
h1 {
    color: #00ffff;
    text-shadow: 0 0 5px #00ffff;
    font-size: 20px !important;
    margin-bottom: 0.5rem !important;
}
h2, h3 {
    color: #00ff99;
    text-shadow: 0 0 3px #00ff99;
    border-bottom: 1px solid rgba(0,255,153,0.3);
    padding-bottom: 4px !important;
    margin-bottom: 0.5rem !important;
    font-size: 16px !important;
}
/* 科幻卡片模块 */
.sci-fi-card {
    background: rgba(10, 25, 41, 0.8);
    border: 1px solid #00ffff;
    border-radius: 8px;
    padding: 10px !important;
    margin-bottom: 10px !important;
    box-shadow: 0 0 8px rgba(0,255,255,0.2);
}
/* Metric组件（紧凑） */
.stMetric {
    background: rgba(10, 25, 41, 0.9);
    border: 1px solid #00ffff;
    border-radius: 6px;
    padding: 8px !important;
    box-shadow: 0 0 5px rgba(0,255,255,0.3);
    text-align: center;
    margin-bottom: 5px !important;
}
.stMetric label {color: #00ff99 !important; font-size: 12px !important;}
.stMetric value {font-size: 18px !important; font-weight: bold;}
.stMetric delta {color: #ffff00 !important; font-size: 10px !important;}
/* 状态文字样式 */
.status-normal { color: #00ff99; font-size: 12px !important; }
.status-warning { color: #ffcc00; font-size: 12px !important; }
.status-error { color: #ff4d4d; font-size: 12px !important; }
.status-info { color: #00ffff; font-size: 12px !important; }
/* 表格/代码块紧凑 */
.stDataFrame {font-size: 11px !important;}
.stCode {font-size: 11px !important; padding: 8px !important;}
</style>
""", unsafe_allow_html=True)
# ===================== 3. 侧边栏（无图片+精简信息） =====================
with st.sidebar:
    # 替换图片为科幻文字标识
    st.markdown("<div style='text-align:center; padding:10px; border:2px solid #00ff99; border-radius:8px; margin-bottom:10px;'>", unsafe_allow_html=True)
    st.markdown("<h3 style='margin:0;'>🆔 学员标识</h3>", unsafe_allow_html=True)
    st.markdown("<p class='status-normal'>NTD-2023-001</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # 核心档案信息
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
# ===================== 4. 顶部标题区（无Banner） =====================
st.markdown("<div class='sci-fi-card'>", unsafe_allow_html=True)
st.title("🚀 星际学员 - 小陆 数字档案仪表盘")
st.markdown("<p class='status-info' style='font-size:12px;margin:0;'>【档案类型：技术能力评估 | 版本：v2.1】</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
# ===================== 5. 主体内容（无图片+紧凑布局） =====================
col1, col2 = st.columns([1.5, 2.5])
# 左侧：基础状态
with col1:
    st.markdown("<div class='sci-fi-card'>", unsafe_allow_html=True)
    st.subheader("📊 基础状态监测")
    
    # 基础状态表格
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
    
    # 状态说明（替换原监测图谱位置）
    st.markdown("### 📝 状态说明")
    st.markdown("""
    - 生理状态：各项指标在安全阈值内
    - 能量储备：中等，建议4小时后补充
    - 任务负载：高负载，建议优先完成紧急任务
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
# 右侧：技能矩阵
with col2:
    st.markdown("<div class='sci-fi-card'>", unsafe_allow_html=True)
    st.subheader("🛠️ 编程技能矩阵")
    
    # 核心技能Metric
    skill_col1, skill_col2, skill_col3 = st.columns(3)
    with skill_col1: st.metric(label="Python", value="95%", delta="+5% (本月)")
    with skill_col2: st.metric(label="C++", value="87%", delta="-2% (本月)")
    with skill_col3: st.metric(label="Java", value="68%", delta="+10% (本月)")
    
    # 技能趋势说明（替换原趋势图谱位置）
    st.markdown("### 📈 技能成长趋势")
    st.markdown("""
    - Python：持续提升，已达精通级别
    - C++：小幅回落，需加强实战训练
    - Java：快速提升，本月进步显著
    - 前端开发：75%（稳定提升）
    - 数据可视化：90%（核心优势技能）
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
# ===================== 6. 任务日志 + 核心代码 =====================
col3, col4 = st.columns(2)
# 左侧：任务日志
with col3:
    st.markdown("<div class='sci-fi-card'>", unsafe_allow_html=True)
    st.subheader("📜 任务执行日志")
    
    # 任务数据
    task_data = pd.DataFrame({
        "任务ID": ["T-1234", "T-5678", "T-9012"],
        "任务名称": ["学生信息管理系统", "课程数据可视化", "AI错题分析工具"],
        "进度": [
            "<span class='status-normal'>85%</span>",
            "<span class='status-normal'>100%</span>",
            "<span class='status-warning'>60%</span>"
        ],
        "优先级": ["高", "中", "紧急"]
    })
    st.write(task_data.to_html(escape=False, index=False), unsafe_allow_html=True)
    
    # 进度汇总
    st.markdown("### 📊 进度汇总")
    total_tasks = len(task_data)
    completed = len(task_data[task_data["进度"].str.contains("100%")])
    st.progress(completed / total_tasks)
    st.markdown(f"""
    - 总任务数：{total_tasks} | 已完成：<span class='status-normal'>{completed}</span>
    - 紧急任务：1项（AI错题分析工具）需优先处理
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
# 右侧：核心代码
with col4:
    st.markdown("<div class='sci-fi-card'>", unsafe_allow_html=True)
    st.subheader("💻 核心任务执行代码")
    
    # 核心代码
    core_code = '''def star_task_executor(task_id: str, priority: str) -> bool:
    """星际任务执行核心函数"""
    # 加载任务配置
    config = load_task_config(task_id)
    # 紧急任务资源超频
    if priority == "紧急":
        allocate_high_resources()
        st.warning(f"[紧急任务] {task_id} 资源已超频")
    # 执行任务并返回结果
    try:
        result = execute_task(config)
        st.success(f"[任务完成] {task_id} 执行成功")
        return True
    except Exception as e:
        st.error(f"[任务异常] {task_id} 错误：{e}")
        return False
'''
    st.code(core_code, language="python", line_numbers=True)
    
    # 代码说明
    st.markdown("<center><i class='status-info'>核心引擎：v2.1 | 最后更新：2025-12-18</i></center>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
# ===================== 页脚（精简） =====================
st.markdown("""
<div style='text-align:center; color:#00ffff; font-size:10px; margin-top:10px; padding:5px; border-top:1px solid #00ff99;'>
    <p>星际学员档案系统 v2.1 | 数据加密级别：最高 | 系统状态：在线 ✔️</p>
    <p>© 2025 星际开发学院 - 未经授权禁止复制/传播</p>
</div>
""", unsafe_allow_html=True)
