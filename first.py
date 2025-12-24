import streamlit as st

# 页面配置：网易云风格音乐播放器
st.set_page_config(page_title="网易云音乐播放器", page_icon="🎶")

# 音乐列表
music_list = [
    {
        "name": "歌曲1 - 关山酒）",
        "url": "https://music.163.com/song/media/outer/url?id=3323746308",  # 替换为目标歌曲ID
        "cover": "http://p2.music.126.net/EpX1U8WYebXOzo-jJ8MW5w==/109951172371108092.jpg?param=130y130"  # 可替换为网易云歌曲封面
    },
    {
        "name": "歌曲2 - 如果呢",
        "url": "https://music.163.com/song/media/outer/url?id=1842728629",  # 示例：另一首歌的ID
        "cover": "http://p2.music.126.net/-xMsNLpquZTmMZlIztTgHg==/109951165953469081.jpg?param=130y130"
    }
,
    {
        "name": "歌曲2 - 执迷不悟",
        "url": "https://music.163.com/song/media/outer/url?id=1477539203",  # 示例：另一首歌的ID
        "cover": "http://p1.music.126.net/NQCtUkal5sPxK1Y25SW3-Q==/109951165303077538.jpg?param=130y130"
    }




    
]

# 初始化会话状态（保存播放进度和索引）
if "music_state" not in st.session_state:
    st.session_state["music_state"] = {
        "current_idx": 0,
        "is_playing": False
    }

# 切换歌曲函数
def switch_song(direction):
    current = st.session_state["music_state"]["current_idx"]
    if direction == "prev":
        new_idx = (current - 1) % len(music_list)
    else:  # next
        new_idx = (current + 1) % len(music_list)
    st.session_state["music_state"]["current_idx"] = new_idx

# 获取当前播放歌曲
current_song = music_list[st.session_state["music_state"]["current_idx"]]

# 页面布局
st.title("🎶 简易网易云音乐播放器")
# 显示歌曲封面（可从网易云歌曲页右键复制封面链接）
st.image(current_song["cover"], width=280)
# 显示歌曲名
st.subheader(current_song["name"])
# 音频播放组件（直接加载网易云链接）
st.audio(current_song["url"], format="audio/mp3", start_time=0)

# 控制按钮
col1, col2, col3 = st.columns(3, gap="small")
with col1:
    st.button("上一首", on_click=switch_song, args=("prev",), use_container_width=True)
with col2:
    play_btn_text = "暂停" if st.session_state["music_state"]["is_playing"] else "播放"
    if st.button(play_btn_text, use_container_width=True):
        st.session_state["music_state"]["is_playing"] = not st.session_state["music_state"]["is_playing"]
with col3:
    st.button("下一首", on_click=switch_song, args=("next",), use_container_width=True)
