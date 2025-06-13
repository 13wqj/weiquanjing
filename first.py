import streamlit as st
import pandas as pd  # 导入pandas 库
import time  # 导入time库
import numpy as np

st.set_page_config(page_title='职师院页面整合', page_icon='📑', layout='wide')

with st.sidebar:
    a = st.selectbox(
        "",
        ['首页', '个人简历生成器', '视频播放器', '南宁美食图', '数字档案'],
        index=0  # 默认选中第1个选项（'首页'）
    )

if a == "数字档案":
    st.title("🕶学生 小晶-数字档案")  # 使用title()函数设置标题

    st.header("🔑基础信息")  # 使用header()函数设置章节
    st.text("学生ID：ZSY-2023-13")  # 用text()函数写学生ID
    st.write("注册时间`2023-9-1 08：00：00`|精神状态：✅正常")  # 用write()函数写注册时间
    st.write("当前教室`实验楼301`|安全等级：`绝密`")  # 用write()函数教室和安全等级

    st.header("📊技能矩阵")  # 使用header()函数设置章节
    c1, c2, c3 = st.columns(3)  # 使用column()定义列3列布局
    c1.metric(label="C语言:revolving_hearts:", value="95%", delta="2%")  # 使用metric()函数书写第一列内容
    c2.metric(label="Python", value="87%", delta="-1%")  # 使用metric()函数书写第一列内容
    c3.metric(label="C语言:revolving_hearts:", value="68%", delta="-10%")  # 使用metric()函数书写第一列内容

    st.subheader("streamlit课程进度")  # 使用header()函数设置子章节
    progress_text_1 = "streamlit课程进度"  # 创建一个progress_text_1
    my_bar = st.progress(0, progress_text_1)  # 使用st.progress()函数初始化进度条的进度值和文本
    time.sleep(0.5)  # 使用sleep()函数设置时间间隔
    for percent in range(30):  # 循环
        time.sleep(
            0.1)  # 使用sleep()函数设置时间间隔      my_bar. progress(percent+1,text=f'{progress_text_1}')   #使用sprogress()函数设置进度条的进度值和文本

    st.header("📝任务日志")  # 使用header()函数设置章节
    data = {
        '日期': ['2023-10-01', '2023-10-02', '2023-10-03'],
        '任务': ['学生数字档案', '数据管理系统', '课程管理系统'],
        '状态': ['✅完成', '🕒进行时', '❌未完成'],
        '难度': ['★★☆☆☆', '★☆☆☆☆', '★★★☆☆']
    }  # 创建data写数据
    index = pd.Series(['0', '1', '2'], name='')  # 定义数据框所用的索引
    df = pd.DataFrame(data, index=index)  # 使用DataFrame()函数根据上面创建的data和index，创建数据框
    st.dataframe(df)  # 使用dataframe()函数生成数据框

    st.subheader("🔐最新代码成果")  # 使用header()函数设置子章节
    st.code('''
    def matrix_breach():
          while True:
                if detect_vulnerability():   
                    exploit()
                    reyurn"ACCESS GRANTED"
                else:
                    stealth_evade()
    ''', line_numbers=True)  # 使用code()函数创建一个代码块并展示代码

    st.markdown('***')  # 使用markdown()函数分割线

    st.write("`>>SYSTEM MESSAGE:`下一个目标已解锁...")  # 使用write()函数展示方法写信息
    st.write("`>>SYSTEM MESSAGE:`课程管理系统")  # 使用write()函数展示方法写信息#写信息
    st.write("`>>SYSTEM MESSAGE:`2025-06-04 17:39:58")  # 使用write()函数展示方法写信息
    st.write("系统状态：在线 连接状态：已加密")  # 使用write()函数展示方法写信息


elif a == "首页":
    st.title("主页")
    st.image("https://www.gxvnu.edu.cn/images/luowendamen.jpg",
             caption='广西职业师范学院（原广西经济管理干部学院）坐落于广西首府南宁市风景秀丽的邕江之滨、相思湖畔，是自治区人民政府直属、自治区教育厅主管的公办全日制普通本科学校，致力于培养区域经济社会发展所需要的高素质应用型、技术技能型人才和职业教育师资。学校随着广西的解放而诞生，其前身为创建于1951年5月的广西省行政干部训练班。其后，为适应不同历史时期广西经济建设需要，学校历经了广西人民革命大学、广西行政干部学校、广西经济干部学校、广西经济管理干部学院等历史沿革，并于2019年6月经教育部批准设置为“广西职业师范学院”。在不同历史时期，学校聚焦“服务广西经济建设”发展主线，不忘建校初心、勇担办学使命，为广西经济建设和社会发展作出了不可磨灭的突出贡献，享有良好的办学声誉和广泛的社会影响。近年来，学校围绕“地方性、应用型、职师类”办学定位，落实“以本为本、应用为先、职师特色”办学思路，在服务地方产业转型升级和职业教育提质增效上取得显著成效。学校拥有一支师德师风优良、学术水平较高、教学经验丰富的专兼职师资队伍，其中，取得硕士、博士学位教师427人。拥有包含自治区教学名师、模范教师、优秀专家、高校思想政治教育卓越教师等在内的高水平教师团队，其中，广西高等学校高水平创新团队2个，自治区课程思政教学团队5个，自治区劳模创新工作室1个。在近年教学成果评选中，获国家级、自治区级教学成果奖16项，其中，获国家级教学成果奖一等奖1项、二等奖1项；获自治区教学成果一等奖4项、二等奖6项，三等奖4项。近五年来，获厅级及以上纵向科研项目立项285项，其中国家级1项、省部级57项、厅级227项；获省部级科研成果奖6项，其中二等奖1项、三等奖5项。学校现有12个二级学院（部），普通本科专业33个，涵盖经济学、管理学、工学、理学、教育学、文学、法学、艺术学等八个学科。获教育部“新工科”研究与实践项目1个，自治区级新工科、新文科研究与实践项目2项，广西高等学校特色专业及课程一体化建设项目3个，自治区级本科一流课程4门，自治区级课程思政示范课5门,自治区级虚拟教研室建设试点2个，广西高校重点实验室1个，自治区级实验教学中心2个，自治区级协同育人平台1个，自治区中小学生研学实践教育基地、劳动教育实践基地各1个。建有新工科协同育人中心等100多个校内外实习实训基地，与多所广西中职学校共建职业教育实习基地。近年来，以加强创新创业教育为抓手，全面促进人才培养供给侧和产业发展需求侧结构要素全方位融合，应用型人才培养质量广受认可，连续被评为广西普通高校毕业生就业创业工作突出单位，也是全区普通高校招生录取工作表现突出单位。学校曾中标获得6项广西重大课题，并承担“推动广西经济高质量发展的重点方向和路径对策研究”等多项自治区党委、政府资政课题以及自治区工信厅、国家发展改革委、财政厅等部门专项课题的研究工作，完成自治区两化融合项目“广西新能源汽车监测平台”的建设，凸显了服务广西的特色和优势。与广西西江开发投资集团高质量共建“广西船联网工程技术研究中心”等多个校企深度合作项目，积极推进产教融合、科技创新成果转化工作，大力开展面向中小微企业的技术服务、咨询服务活动。学校还是广西干部教育培训高校基地、第七批自治区级专业技术人员继续教育基地、自治区职业教育师资培养培训基地、广西知识产权培训基地、广西生态环境保护综合行政执法实训基地以及企业经营管理人员培训基地，培训了一大批高素质党政干部、“双师型”职教师资和企业经营管理人才。面向未来，学校将坚守建校初心、牢记办学使命，紧扣“创新性驱动，特色化建设，内涵式提升，高质量发展”总要求，深化产教融合、校企合作，推进工学结合、知行合一，努力将学校办成特色鲜明的高水平普通本科学校，在全面建设新时代壮美广西新征程中再谱新篇、再续华章。（学校办公室提供，数据信息统计截至2025年3月14日）')

elif a == "视频播放器":

    st.title("Streamlit视频播放器")

    # 判断内存中（session_state中）有没有a
    if 'a' not in st.session_state:
        st.session_state['a'] = 0
    # 数组  图片：链接、图注   音乐：链接、图片、歌手、专辑.....
    video_arr = [{
        'url': 'https://www.w3school.com.cn/example/html5/mov_bbb.mp4',
        'title': '兔子'
    }, {
        'url': 'https://www.w3schools.com/html/movie.mp4',
        'title': '熊'
    }, {
        'url': 'https://media.w3.org/2010/05/sintel/trailer.mp4',
        'title': '动画片段'
    }]

    video_arr1 = [{
        'url': 'https://www.w3school.com.cn/example/html5/mov_bbb.mp4',
        'title': '兔子看蝴蝶'
    }]

    video_arr2 = [{
        'url': 'https://www.w3schools.com/html/movie.mp4',
        'title': '熊抓鱼'
    }]

    video_arr3 = [{
        'url': 'https://media.w3.org/2010/05/sintel/trailer.mp4',
        'title': '动画片段2'
    }]


    def my_format_func(option):
        return f'{option}'


    t = st.selectbox(
        '点击选择想播放视频的类型：',
        options=['全部', '兔子', '熊', '动画片段'],
        format_func=my_format_func,
        index=0
    )
    if t == '全部':
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


elif a == "南宁美食图":

    st.header('🍜南宁美食地图🍜')

    st.map(pd.DataFrame({
        "latitude": [22.853838, 22.965046, 22.812200, 22.809105, 22.839699],
        "longitude": [108.222177, 108.353921, 108.266629, 108.378664, 108.245804]
    }))

    # 餐厅数据
    data = {
        "餐厅": ["星艺会尝不忘", "高峰柠檬鸭", "复记老友粉", "好友缘", "白妈螺狮粉"],
        "类型": ["中餐", "中餐", "快餐", "自助餐", "西餐"],
        "评分": [4.2, 4.5, 4.0, 4.7, 4.3],
        "人均消费(元)": [15, 20, 25, 35, 50],
        "位置X": [22.853838, 22.965046, 22.812200, 22.809105, 22.839699],
        "位置Y": [108.222177, 108.353921, 108.266629, 108.378664, 108.245804]
    }
    df = pd.DataFrame(data)
    index = pd.Series([1, 2, 3, 4, 5], name='评分')
    st.table(df)
    df.index = index

    st.header('⭐餐厅评分')
    st.bar_chart(
        data=df,
        x="餐厅",
        y="评分"
    )

    st.header('💰不同餐厅价格')
    st.line_chart(
        data=df,
        x="类型",
        y="人均消费(元)"
    )

    data1 = {
        "时间": ["11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00", "14:30",
                 "15:00", "15:30", "16:00", "16:30", "17:00", "17:30", "18:00", "18:30", "19:00"],
        "复记老友粉": [10, 30, 80, 95, 85, 70, 50, 40, 30, 25, 20, 30, 60, 85, 90, 75, 50],
        "星艺会尝不忘": [5, 15, 60, 85, 90, 80, 65, 50, 40, 30, 25, 40, 70, 95, 100, 85, 60],
        "高峰柠檬鸭": [15, 40, 75, 90, 95, 85, 70, 55, 45, 35, 30, 45, 75, 90, 85, 70, 45]
    }

    df1 = pd.DataFrame(data1)
    st.header('⏱用餐高峰时段')
    st.area_chart(
        data=df1,
        x="时间",
        y=["复记老友粉", "星艺会尝不忘", "高峰柠檬鸭"]
    )

    st.header('🍽餐厅详细')
    st.write("查看餐厅详细")


    def my_format_func(option):
        return f'{option}'


    t = st.selectbox('查看餐厅详细：', ['好友缘'], format_func=my_format_func, index=0)
    if t == '好友缘':
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("好友缘")
            st.metric("评分", "4.7/5.0")
            st.metric("人均消费", "35元")

        with col2:
            st.write("推荐菜品:")
            st.write("●特色套餐")
            st.write("●地方小吃")
            st.write("●时令蔬菜")

    # 进度条展示
    st.subheader("当前拥挤程度")

    st.progress(86, text="86%拥挤")

    st.header('🎲今日午餐推荐')
    if st.button('帮我点午餐'):
        st.markdown('<p class="title">今日推荐：星艺会尝不忘（中餐）</p>', unsafe_allow_html=True)
        st.image("https://blog-1251237404.cos.ap-guangzhou.myqcloud.com/C5TdgZ.jpg", caption='美味午餐等着你！')

else:
    st.title("个人简历生成器")


    def my_format_func(option):
        return f'选{option}'


    st.title("🎨个人简历生成器")
    st.write('使用streamlit创建你的个性化简历')

    c1, c2 = st.columns([1, 2])  # 分栏
    with c1:
        st.header("个人信息表单")

        st.markdown(  # 分割线
            """
            <hr style='border: 2px solid blue; margin: 10px 0;'>
            """,
            unsafe_allow_html=True
        )

        st.session_state['xm'] = st.text_input('姓名')
        st.session_state['zw'] = st.text_input('职位')
        st.session_state['dh'] = st.text_input('电话')
        st.session_state['yx'] = st.text_input('邮箱')
        st.session_state['csrq'] = st.date_input("出生日期", value=None)

        st.session_state['xb'] = st.radio('性别', ['女', '男'])

        st.session_state['xl'] = st.selectbox(
            '学历',
            options=['初中', '高中', '大学', '研究生', '博士'],
            index=0
        )
        st.session_state['yynl'] = st.selectbox(
            '语言能力',
            options=['优秀', '良好', '及格'],
            index=0
        )
        st.session_state['jn'] = st.multiselect(
            '技能（可多选）',
            options=['python', 'java', 'c语言', 'c++'],
            default=['python']
        )

        st.session_state['gzjy'] = st.slider('工作经验（年）', 0, 30)  # 数值滑块选择

        st.session_state['qwxz'] = st.slider(
            '期望薪资',
            5000, 50000, (10000, 20000))
        st.session_state['grjj'] = st.session_state['grjl'] = st.text_area(label='个人简历',
                                                                           placeholder='请简要介绍您的专业背景、只有目标和个人特点...')

        st.session_state['zjlxsj'] = st.time_input("每日最佳联系时间段")

        uploaded_file = st.file_uploader(  # 上传照片
            label="上传个人照片",
            type=["jpg", "jpeg", "png"],
            accept_multiple_files=False,
            help="Limit 200MB per file • JPG, JPEG, PNG"
        )
        if uploaded_file is not None:
            st.success("文件上传成功！")
            st.image(uploaded_file, caption="上传的图片", use_column_width=True)

    with c2:
        st.header("简历实时预览")

        st.markdown(  # 分割线
            """
            <hr style='border: 2px solid blue; margin: 10px 0;'>
            """,
            unsafe_allow_html=True
        )

        d1, d2 = st.columns(2)
        with d1:
            placeholder = st.empty()  # 与前面填写实时更新显示
            if st.session_state['zw']:
                placeholder.markdown(f"职位:{st.session_state['zw']}")
            else:
                placeholder.write("职位:")

            placeholder = st.empty()
            if st.session_state['dh']:
                placeholder.markdown(f"电话:{st.session_state['dh']}")
            else:
                placeholder.write("电话:")

            placeholder = st.empty()
            if st.session_state['yx']:
                placeholder.markdown(f"邮箱:{st.session_state['yx']}")
            else:
                placeholder.write("邮箱:")

            placeholder = st.empty()
            if st.session_state['csrq']:
                placeholder.markdown(f"出生日期:{st.session_state['csrq']}")
            else:
                placeholder.write("出生日期:")

        with d2:
            placeholder = st.empty()
            if st.session_state['xb']:
                placeholder.markdown(f"职位:{st.session_state['xb']}")

            placeholder = st.empty()
            if st.session_state['xl']:
                placeholder.markdown(f"学历:{st.session_state['xl']}")

            placeholder = st.empty()
            if st.session_state['gzjy']:
                placeholder.markdown(f"工作经验:{st.session_state['gzjy']}")
            else:
                placeholder.write("工作经验:0")

            placeholder = st.empty()
            if st.session_state['qwxz']:
                placeholder.markdown(f"期望薪资:{st.session_state['qwxz']}")

            placeholder = st.empty()
            if st.session_state['zjlxsj']:
                placeholder.markdown(f"最佳联系时间:{st.session_state['zjlxsj']}")

            placeholder = st.empty()
            if st.session_state['yynl']:
                placeholder.markdown(f"语言能力:{st.session_state['yynl']}")

        st.markdown('***')  # 使用markdown()函数分割线
        st.header("个人简历")
        placeholder = st.empty()
        if st.session_state['grjj']:
            placeholder.markdown(f"`{st.session_state['grjj']}`")
        else:
            placeholder.write("这个人很神秘，没有留下任何介绍...")

        st.markdown('***')  # 使用markdown()函数分割线