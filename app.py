# -*- coding:utf-8 -*-
import streamlit as st
from streamlit_option_menu import option_menu

import matplotlib.pyplot as plt
from gallup import run_gallup
from election import run_election
from PIL import Image

import base64
from pathlib import Path


def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded
def img_to_html(img_path):
    img_html = "<img src='data:image/png;base64,{}' class='img-fluid' width='50' height='50'>".format(
      img_to_bytes(img_path)
    )
    return img_html

def main():
    with st.sidebar:
        selected = option_menu("대시보드 메뉴", ['홈', '갤럽여론조사', '20대 대통령선거'],
                               icons=['house', 'file-bar-graph', 'graph-up-arrow'], menu_icon="cast", default_index=0)
    if selected == "홈":
        st.markdown("<h1 style='text-align: center; color: black;'>대통령 선거 데이터 분석</h1>", unsafe_allow_html=True)

        st.markdown("<h2 style='text-align: center; color: gray;'>10-30대는 어떻게 움직였는가? </h2>"
                    "<p style='text-align: center; color: grey;'>"+img_to_html('img/figure01.png')+"</p>",
                    unsafe_allow_html=True)

        st.write('')
        st.write('')

        st.write('')
        st.write('')


        st.markdown("# 갤럽 데이터 수집\n ")
        st.markdown(
                    "\n ####  데이터 수집항목 \n ##### - <span style = 'color:#585858'>2020년 1월 2째주 ~ 2022년 12월 3째주</span> \n"
                    "####  날짜 \n ##### - <span style = 'color:#585858'>연도, 월, 주</span> \n"
                    "####  정당 \n ##### - <span style='color:red'>국민의힘</span> / <span style='color:blue'>더불어민주당</span> / <span style='color:#F1C40F'>정의당</span> / <span style='color:gray'>무당층</span>\n"
                    "####  무당층 \n ##### - <span style = 'color:#585858'>기타 정당과 부동층을 포함</span>\n"
                    "####  지역 \n ##### - <span style = 'color:#585858'>서울, 인천/경기, 대전/세종/충청, 광주/전라,</span>"
                    "\n ##### <span style = 'color:#585858'>&#160;&#160; 대구/경북, 부산/울산</span> \n"
                    "#### 성별 \n ##### - <span style = 'color:#585858'>남자, 여자</span>\n"
                    "####  연령  \n ##### - <span style = 'color:#585858'>10대~30대<span>\n"
                    "####  웹싸이트 : <a href='https://www.gallup.co.kr/' style='color:blue'>https://www.gallup.co.kr/</a>",
                    unsafe_allow_html=True)


    elif selected == "갤럽여론조사":
        run_gallup()
    elif selected == "20대 대통령선거":
        run_election()
    else:
        print("error...")

if __name__ == "__main__":
    main()