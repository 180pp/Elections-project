# -*- coding:utf-8 -*-
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


def run_gallup():
    import matplotlib
    import platform
    # Window
    if platform.system() == 'Windows':
        matplotlib.rc('font', family='Malgun Gothic')
    elif platform.system() == 'Darwin':  # Mac
        matplotlib.rc('font', family='AppleGothic')
    else:  # linux
        matplotlib.rc('font', family='NanumGothic')
    # 그래프에 마이너스 표시가 되도록 변경
    matplotlib.rcParams['axes.unicode_minus'] = False


    st.markdown("# 데이터확인\n")

    df = pd.read_excel("data/이념적성향_변동.xlsx", )
    df['연도'] = df['연도'].astype('str')
    df['구분'] = df['구분'].replace({
        "매우보수적": "보수",
        "다소보수적": "보수",
        "매우진보적": "진보",
        "다소진보적": "진보",
        "중도적": "중도"
    })
    df2 = df.groupby(['세대', '연도', '구분'])['비율'].agg('sum').reset_index()
    st.dataframe(df2, width=800)


    st.write('')
    st.write('')

    st.write('')
    st.write('')

    st.markdown("# 20대와 30대의 비율 차이\n"
                "- 진보 지지 성향은 갈수록 줄어들고 있고, 반면에 보수는 계속 증가하고 있음\n"
                "- 데이터 출처 : 사회통합실태조사 한국행정연구원(KOSIS)\n"
                "- 데이터 보기 : https://kosis.kr/statHtml/statHtml.do?orgId=417&tblId=DT_417001_0030&conn_path=I3")

    df20s = df2[df2['세대'] == '19~29세']
    df30s = df2[df2['세대'] == '30~39세']

    # 여기서 줄 띄우기
    st.write('')
    st.write('')
    st.write('')
    st.write('')

    col1, col2, col3 = st.columns(3)
    with col1:
        color1 = st.color_picker('보수 색상 Color 변경', '#E61E2B')
    with col2:
        color2 = st.color_picker('중도 색상 Color 변경', '#808080')
    with col3:
        color3 = st.color_picker('진보 색상 Color 변경', '#004EA1')

    custom_palette = [color1, color2, color3]

    fig, ax = plt.subplots(figsize=(10, 6), ncols=2)
    sns.lineplot(data=df20s, x='연도', y='비율', hue='구분', ax=ax[0], palette=custom_palette)
    ax[0].set_title("19~29세의 이념성향 추이", size=22)
    ax[0].set_ylim(0, 100)

    sns.lineplot(data=df30s, x='연도', y='비율', hue='구분', ax=ax[1], palette=custom_palette)
    ax[1].set_title("30대의 이념성향 추이", size=22)
    ax[1].set_ylim(0, 100)
    plt.legend(loc="best")
    st.pyplot(fig)

    st.markdown("# 정당 지지도 추이")
    df2 = pd.read_excel('data/정당지지도_데이터.xlsx')
    df2["date"] = pd.to_datetime(df2["연도"].astype(str) + "-" + df2["월"].astype(str))
    df2["date"] = df2["date"] + pd.to_timedelta(df2["주"] * 7 - 6, unit="D")

    # 날짜 필터링
    st.dataframe(df2)

    custom_palette = ['#E61E2B', '#004EA1', '#FFED00', '#808080']

    import datetime

    start_date = st.date_input("기간")
    end_date = st.date_input("")

    start_datetime = pd.to_datetime(start_date)
    end_datetime = pd.to_datetime(end_date)

    filtered_df = df2[(df2["date"] >= start_datetime) & (df2["date"] <= end_datetime)]
    graph_options = ["10~20대", "30대", "남자", "여자",'서울','인천/경기','대전/세종/충청','광주/전라','대구/경북','부산/울산/경남']
    selected_graph = st.selectbox("요소별", graph_options)

    if selected_graph == "10~20대":
        st.markdown("# 10~20대")
        fig2, ax = plt.subplots(figsize=(10, 6))
        sns.lineplot(data=filtered_df, x='date', y='10~20', hue='정당', palette=custom_palette)
        ax.set_title("10-20대")
        st.pyplot(fig2)

    elif selected_graph == "30대":
        st.markdown("# 30대")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.lineplot(data=filtered_df, x='date', y='30대', hue='정당', palette=custom_palette)
        ax.set_title("30대")
        st.pyplot(fig)

    elif selected_graph == "남자":
        st.markdown("# 남자")
        fig3, ax = plt.subplots(figsize=(10, 6))
        sns.lineplot(data=filtered_df, x='date', y='남자', hue='정당', palette=custom_palette)
        ax.set_title("정당별 남자 지지도", size=22)
        st.pyplot(fig3)

    elif selected_graph == "여자":
        st.markdown("# 여자")
        fig4, ax = plt.subplots(figsize=(10, 6))
        sns.lineplot(data=filtered_df, x='date', y='여자', hue='정당', palette=custom_palette)
        ax.set_title("정당별 여자 지지도", size=22)
        st.pyplot(fig4)


    elif selected_graph == '서울':
        st.markdown("# 서울")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.lineplot(data=filtered_df, x='date', y='서울', hue='정당', palette=custom_palette, ax=ax)
        ax.set_title("서울")
        st.pyplot(fig)

    elif selected_graph == '인천/경기':
        st.markdown("# 인천/경기")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.lineplot(data=filtered_df, x='date', y='인천/경기', hue='정당', palette=custom_palette, ax=ax)
        ax.set_title("인천/경기")
        st.pyplot(fig)

    elif selected_graph == '대전/세종/충청':
        st.markdown("# 대전/세종/충청")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.lineplot(data=filtered_df, x='date', y='대전/세종/충청', hue='정당', palette=custom_palette, ax=ax)
        ax.set_title("대전/세종/충청")
        st.pyplot(fig)

    elif selected_graph == '광주/전라':
        st.markdown("# 광주/전라")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.lineplot(data=filtered_df, x='date', y='광주/전라', hue='정당', palette=custom_palette, ax=ax)
        ax.set_title("광주/전라")
        st.pyplot(fig)

    elif selected_graph == '대구/경북':
        st.markdown("# 대구/경북")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.lineplot(data=filtered_df, x='date', y='대구/경북', hue='정당', palette=custom_palette, ax=ax)
        ax.set_title("대구/경북")
        st.pyplot(fig)

    elif selected_graph == '부산/울산/경남':
        st.markdown("# 부산/울산/경남")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.lineplot(data=filtered_df, x='date', y='부산/울산/경남', hue='정당', palette=custom_palette, ax=ax)
        ax.set_title("부산/울산/경남")
        st.pyplot(fig)

