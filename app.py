# -*- coding:utf-8 -*-
import streamlit as st
from streamlit_option_menu import option_menu

import matplotlib.pyplot as plt
from gallup import run_gallup
from election import run_election
from PIL import Image
import numpy as np

import base64
from pathlib import Path
# from home import run_home
from home1 import run_home1


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
       run_home1()


    elif selected == "갤럽여론조사":
        run_gallup()
    elif selected == "20대 대통령선거":
        run_election()
    else:
        print("error...")

if __name__ == "__main__":
    main()