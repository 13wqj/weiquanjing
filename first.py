import streamlit as st

st.set_page_config(page_title='Streamlit视频播放器', page_icon='🎬')

st.title("Streamlit视频播放器")

# 判断内存中（session_state中）有没有a
if 'a' not in st.session_state:
    st.session_state['a'] = 0
# 数组  图片：链接、图注   音乐：链接、图片、歌手、专辑.....
video_arr = [{
        'url': 'https://www.w3school.com.cn/example/html5/mov_bbb.mp4',
        'title': '兔子'
    },{
        'url': 'https://www.w3schools.com/html/movie.mp4',
        'title': '熊'
    },{
        'url': 'https://media.w3.org/2010/05/sintel/trailer.mp4',
        'title': '动画片段'
    }]

video_arr1 = [{
        'url': 'https://www.w3school.com.cn/example/html5/mov_bbb.mp4',
        'title': '兔子看蝴蝶'
    },{
        'url': 'https://www.w3schools.com/html/movie.mp4',
        'title': '兔子跳'
    }]

video_arr2 = [{
        'url': 'https://www.w3school.com.cn/example/html5/mov_bbb.mp4',
        'title': '熊吃'
    },{
        'url': 'https://www.w3schools.com/html/movie.mp4',
        'title': '熊抓鱼'
    }]

video_arr3 = [{
        'url': 'https://www.w3school.com.cn/example/html5/mov_bbb.mp4',
        'title': '动画片段1'
    },{
        'url': 'https://media.w3.org/2010/05/sintel/trailer.mp4',
        'title': '动画片段2'
    }]

def my_format_func(option):
    return f'{option}'
t = st.selectbox(
    '点击选择想播放视频的类型：',
    options=['全部','兔子', '熊', '动画片段'],
    format_func=my_format_func,
    index=0
)
if t== '全部':
    st.video(video_arr[st.session_state['a']]['url'])  # 显示视频
    st.write(video_arr[st.session_state['a']]['title'])  # 显示标题

    def next():
        # 声明a使用的是外面的全局变量a
        global a
        # 做什么事？？   = a + 1
        st.session_state['a'] = (st.session_state['a'] + 1) % len(video_arr)


    c1, c2 = st.columns(2)

    with c1:
        st.button('上一个视频', use_container_width=True)

    with c2:
        st.button('下一个视频', on_click=next, use_container_width=True)

if t == '兔子':
    st.video(video_arr1[st.session_state['a']]['url'])  # 显示视频
    st.write(video_arr1[st.session_state['a']]['title'])  # 显示标题


    def next():
        # 声明a使用的是外面的全局变量a
        global a
        # 做什么事？？   = a + 1
        st.session_state['a'] = (st.session_state['a'] + 1) % len(video_arr1)


    c1, c2 = st.columns(2)

    with c1:
        st.button('上一个视频', use_container_width=True)

    with c2:
        st.button('下一个视频', on_click=next, use_container_width=True)

if t == '熊':
    st.video(video_arr2[st.session_state['a']]['url'])  # 显示视频
    st.write(video_arr2[st.session_state['a']]['title'])  # 显示标题


    def next():
        # 声明a使用的是外面的全局变量a
        global a
        # 做什么事？？   = a + 1
        st.session_state['a'] = (st.session_state['a'] + 1) % len(video_arr2)


    c1, c2 = st.columns(2)

    with c1:
        st.button('上一个视频', use_container_width=True)

    with c2:
        st.button('下一个视频', on_click=next, use_container_width=True)

if t == '动画片段':
    st.video(video_arr3[st.session_state['a']]['url'])  # 显示视频
    st.write(video_arr3[st.session_state['a']]['title'])  # 显示标题


    def next():
        # 声明a使用的是外面的全局变量a
        global a
        # 做什么事？？   = a + 1
        st.session_state['a'] = (st.session_state['a'] + 1) % len(video_arr3)


    c1, c2 = st.columns(2)

    with c1:
        st.button('上一个视频', use_container_width=True)

    with c2:
        st.button('下一个视频', on_click=next, use_container_width=True)