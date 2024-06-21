import streamlit as st
import requests
import re

import inspect
import streamlit.components.v1 as components
st.set_page_config(
    page_title="预测模型",
    page_icon="",
)
st.title("基于2000-2023年国家数据多元回归模型")
year = st.number_input(label = '请输入您要预测的年份', 
                     min_value=0, 
                     value=2023, 
                     step=1, 
                    )


# if st.button('确认'):
if 'clicked' not in st.session_state:
    st.session_state.clicked = False

# 定义回调函数，当按钮被点击时，将clicked变量的值设置为True
def click_button():
    st.session_state.clicked = True

# 创建按钮，并使用on_click参数将回调函数与按钮关联起来


rate={'people':11522.998189155356,
'NX':11605.089390884033,
'I':-1432.7748805866022,
'G':-30126.459180035723,
'C':-130755.83974583271,
'education':374572.74571607384,
'un_work':-3899.6191412971243,
'hp':111358.20801253317,}


labor=-1724620.7074213848+ 896.1279314884637*year
C=-15097837.366087813+7594.836889310691*year
people=-2458007.424401325+1290.0804231789207*year
NX=-933292.2757727078+473.2104797738333*year
I=-24011795.247212224+12067.610939378508*year
G=-5566016.030743005+2822.492750338921*year
education=-3896341.5388862593+1951.6297802588665*year
hp=-811734.9238006438+406.4689723350932*year
un_work=-53.22454545439588+ 0.028357998590482103*year

people = st.number_input(label = '请输入您要预计年份的人口(万人)', 
                    min_value=0.0, 
                    
                    value=people, 
                    step=1.0, 
                    help="如果不输入，则以线性回归模型预计的值参与计算"
                    )
NX = st.number_input(label = '请输入预计年份的进出口差额（亿圆）', 
                    min_value=0.0, 
                    
                    value=NX, 
                    step=1.0, 
                    help="如果不输入，则以线性回归模型预计的值参与计算"
                    )
G = st.number_input(label = '请输入预计年份的财政支出（亿圆）', 
                    min_value=0.0, 
                    
                    value=G, 
                    step=1.0, 
                    help="如果不输入，则以线性回归模型预计的值参与计算"
                    )
C= st.number_input(label = '请输入预计年份的消费市场额度（亿圆）', 
                    min_value=0.0, 
                    
                    value=C, 
                    step=1.0, 
                    help="如果不输入，则以线性回归模型预计的值参与计算"
                    )
I= st.number_input(label = '请输入您要预计年份的市场总投资（亿圆）', 
                    min_value=0.0, 
                    
                    value=I, 
                    step=1.0, 
                    help="如果不输入，则以线性回归模型预计的值参与计算"
                    )
education= st.number_input(label = '请输入您要预计年份的教育支出', 
                    min_value=0.0, 
                    
                    value=education, 
                    step=1.0, 
                    help="如果不输入，则以线性回归模型预计的值参与计算"
                    )
un_work= st.number_input(label = "请输入您要预计年份的失业率", 
                    min_value=0.0, 
                    
                    value=un_work, 
                    step=1.0, 
                    help="如果不输入，则以线性回归模型预计的值参与计算"
                    )
hp= st.number_input(label = '请输入您要预计年份的商品房平均房价', 
                    min_value=0.0, 
                    
                    value=hp, 
                    step=1.0, 
                    help="如果不输入，则以线性回归模型预计的值参与计算"
                    )
gdp=rate['people']*people+rate['NX']*NX+rate['I']*I+rate['C']*C+rate['education']*education+rate['un_work']*un_work+rate['hp']*hp+564028.85263155
gdp=-gdp/10000
def getOutterIP():
    ip = ''    
    try:
        res = requests.get('https://myip.ipip.net', timeout=5).text
        ip = re.findall(r'(\d+\.\d+\.\d+\.\d+)', res)
        ip = ip[0] if ip else ''
    except:
        pass
    return ip

my_ip=getOutterIP()

if st.button('确认'):
    st.success(f'根据模型预估计{year}年GDP为: {gdp:.3f}亿元')
    
