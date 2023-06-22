# -*- coding:utf-8 -*-

import streamlit as st
from PIL import Image


def run_home1():
    # img = Image.open("image/mak.png")
    # st.image(img)
    tab1, tab2 = st.tabs(['홈', 'Workflow'])
    with tab1:
        st.markdown("<h1 style='color: black;'>대통령 선거 데이터 분석</h1>", unsafe_allow_html=True)
        st.markdown("<h2 style='color: gray;'>10 - 30대는 어떻게 움직였는가?</h2>", unsafe_allow_html=True)
        img1 = Image.open('img/figure01.png').resize((80, 80))
        st.image(img1)
        st.markdown("Member|Skills|GitHub & Blog \n |:--:|:--:|:--:| \n | 김미나 |분석 & 기획|  https://github.com/180pp   \n |권용석|분석 & 대시보드| https://github.com/MaestroYongseok  | \n |주강희|대시보드& PPT|  https://blog.naver.com/wnrkdgml10|")
        st.markdown("")
        col1, col2, col3 = st.columns(3)

        with col1:
            img1 = Image.open('image/1.jpg').resize((150,120))
            st.image(img1)
        with col2:
            img2 = Image.open('image/2.jpg').resize((150,120))
            st.image(img2)
        with col3:
            img3 = Image.open('image/3.jpg').resize((150,120))
            st.image(img3)

        st.markdown("### :house: 프로젝트 개요\n\n"
                    "- 2020년 부터 2022년까지의 갤럽 리서치 조사 자료를 통해 대표정당 3곳에 대한 지지도 변화를 알아봄.\n\n"
                    "- 지지도 변화를 바탕으로 대통령선거의 득표율과 비교")
        st.markdown("###  목표")
        st.markdown("- 득표율에 영향을 미치는 요소 분석")
        st.markdown("- 지역별 득표율의 차이 파악")
        st.markdown("- 선거기간 중 영향을 받은 이벤트 분석")
        st.markdown("- 대시보드를 통해 예상 득표율 변화를 확인")

        st.markdown("### 프로젝트 기간\n\n"
                    "- 2023.5.18 ~ 2023.6.23")

        st.markdown("### 프로젝트 목적\n\n"
                    "- 어떠한 요소가 당선에 더 많은 영향을 끼쳤는지를 시각화를 통해 분석\n"
                    "- 각 정당들은 자신들의 정당에 유리하게 선거 전략을 세울수 있음. ")

        st.markdown("### 사용 Tool")
        col4, col5, col6 = st.columns(3)
        with col4:
            img4 = Image.open('image/4.png')
            st.image(img4)
        with col5:
            img5 = Image.open('image/5.png')
            st.image(img5)
        with col6:
            img6 = Image.open('image/6.png')
            st.image(img6)
    with tab2:
        st.markdown("## 프로젝트 흐름 ")
        st.markdown("### 1. 데이터 수집")
        st.markdown("- 갤럽 리서치 자료를 이용하여 엑셀파일로 데이터 구성")
        st.markdown("**☞** 2020년도 1월 2째주 부터 2022년 3월 대선 전까지의 데이터")

        st.markdown("### 2. 데이터 전처리 및 EDA")
        st.markdown("- 당명이 바뀌거나 합당한 데이터 전처리")
        st.markdown("**☞** 국민의 힘이 2번 당명이 바뀌고 바른미래당과 합당을 함")
        st.markdown("- 데이터를 시/군/구로 묶기")

        st.markdown("### 3. 통계 분석")
        st.markdown("- 득표율과 다양한 요소와의 관계 분석")
        st.markdown("**☞** 기초 통계 분석활용 ")

        st.markdown("### 4. 시각화")
        st.markdown("- 다양한 분류를 기준으로 시각화")
        st.markdown("**☞** 지역별/성별별/연령별/정당별/날짜별...")
        st.markdown("- 이동 경로 지도(Route Map)/단계 구분도(Choropleth Map)")

        st.markdown("### 5. PPT")
        st.markdown("- 배포용 Dashboard 만들기")
        st.markdown("- 발표용 PPT 만들기")

        st.markdown("### 6. 마무리 토론")
        st.markdown("- 자체 평가/문제 발견")
        st.markdown("- 개선 방향 제시")

