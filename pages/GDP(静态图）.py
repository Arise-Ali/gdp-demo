

import streamlit as st

import streamlit.components.v1 as components

st.set_page_config(page_title="绘图演示", page_icon="📈",layout="wide",)


html_content="""
<!DOCTYPE html>
<!-- saved from url=(0016)http://localhost -->
<html>
<head>
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"/>
    <meta charset="UTF-8">
    <title>Awesome-pyecharts</title>
                <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/echarts@latest/dist/echarts.min.js"></script>

</head>
<body >
    <div id="bd14e2173316479197e29fe816502561" class="chart-container" style="width: 1000px; height:650px; "></div>
    <script>
        var chart_bd14e2173316479197e29fe816502561 = echarts.init(
            document.getElementById('bd14e2173316479197e29fe816502561'), 'white', {renderer: 'canvas'});
        var option_bd14e2173316479197e29fe816502561 = {
    "animation": true,
    "animationThreshold": 2000,
    "animationDuration": 1000,
    "animationEasing": "cubicOut",
    "animationDelay": 0,
    "animationDurationUpdate": 300,
    "animationEasingUpdate": "cubicOut",
    "animationDelayUpdate": 0,
    "aria": {
        "enabled": false
    },
    "color": [
        "#5470c6",
        "#91cc75",
        "#fac858",
        "#ee6666",
        "#73c0de",
        "#3ba272",
        "#fc8452",
        "#9a60b4",
        "#ea7ccc"
    ],
    "series": [
        {
            "type": "line",
            "name": "\u4ebf\u5143",
            "connectNulls": false,
            "xAxisIndex": 0,
            "symbolSize": 4,
            "showSymbol": false,
            "smooth": true,
            "clip": true,
            "step": false,
            "data": [
                [
                    "1952\u5e74",
                    679.1
                ],
                [
                    "1953\u5e74",
                    824.4
                ],
                [
                    "1954\u5e74",
                    859.8
                ],
                [
                    "1955\u5e74",
                    911.6
                ],
                [
                    "1956\u5e74",
                    1030.7
                ],
                [
                    "1957\u5e74",
                    1071.4
                ],
                [
                    "1958\u5e74",
                    1312.3
                ],
                [
                    "1959\u5e74",
                    1447.5
                ],
                [
                    "1960\u5e74",
                    1470.1
                ],
                [
                    "1961\u5e74",
                    1232.3
                ],
                [
                    "1962\u5e74",
                    1162.2
                ],
                [
                    "1963\u5e74",
                    1248.3
                ],
                [
                    "1964\u5e74",
                    1469.9
                ],
                [
                    "1965\u5e74",
                    1734.0
                ],
                [
                    "1966\u5e74",
                    1888.7
                ],
                [
                    "1967\u5e74",
                    1794.2
                ],
                [
                    "1968\u5e74",
                    1744.1
                ],
                [
                    "1969\u5e74",
                    1962.2
                ],
                [
                    "1970\u5e74",
                    2279.7
                ],
                [
                    "1971\u5e74",
                    2456.9
                ],
                [
                    "1972\u5e74",
                    2552.4
                ],
                [
                    "1973\u5e74",
                    2756.2
                ],
                [
                    "1974\u5e74",
                    2827.7
                ],
                [
                    "1975\u5e74",
                    3039.5
                ],
                [
                    "1976\u5e74",
                    2988.6
                ],
                [
                    "1977\u5e74",
                    3250.0
                ],
                [
                    "1978\u5e74",
                    3678.7
                ],
                [
                    "1979\u5e74",
                    4100.5
                ],
                [
                    "1980\u5e74",
                    4586.1
                ],
                [
                    "1981\u5e74",
                    4933.7
                ],
                [
                    "1982\u5e74",
                    5380.5
                ],
                [
                    "1983\u5e74",
                    6043.8
                ],
                [
                    "1984\u5e74",
                    7314.2
                ],
                [
                    "1985\u5e74",
                    9123.6
                ],
                [
                    "1986\u5e74",
                    10375.4
                ],
                [
                    "1987\u5e74",
                    12166.6
                ],
                [
                    "1988\u5e74",
                    15174.4
                ],
                [
                    "1989\u5e74",
                    17188.4
                ],
                [
                    "1990\u5e74",
                    18923.3
                ],
                [
                    "1991\u5e74",
                    22050.3
                ],
                [
                    "1992\u5e74",
                    27208.2
                ],
                [
                    "1993\u5e74",
                    35599.2
                ],
                [
                    "1994\u5e74",
                    48548.2
                ],
                [
                    "1995\u5e74",
                    60356.6
                ],
                [
                    "1996\u5e74",
                    70779.6
                ],
                [
                    "1997\u5e74",
                    78802.9
                ],
                [
                    "1998\u5e74",
                    83817.6
                ],
                [
                    "1999\u5e74",
                    89366.5
                ],
                [
                    "2000\u5e74",
                    99066.1
                ],
                [
                    "2001\u5e74",
                    109276.2
                ],
                [
                    "2002\u5e74",
                    120480.4
                ],
                [
                    "2003\u5e74",
                    136576.3
                ],
                [
                    "2004\u5e74",
                    161415.4
                ],
                [
                    "2005\u5e74",
                    185998.9
                ],
                [
                    "2006\u5e74",
                    219028.5
                ],
                [
                    "2007\u5e74",
                    270704.0
                ],
                [
                    "2008\u5e74",
                    321229.5
                ],
                [
                    "2009\u5e74",
                    347934.9
                ],
                [
                    "2010\u5e74",
                    410354.1
                ],
                [
                    "2011\u5e74",
                    483392.8
                ],
                [
                    "2012\u5e74",
                    537329.0
                ],
                [
                    "2013\u5e74",
                    588141.2
                ],
                [
                    "2014\u5e74",
                    644380.2
                ],
                [
                    "2015\u5e74",
                    685571.2
                ],
                [
                    "2016\u5e74",
                    742694.1
                ],
                [
                    "2017\u5e74",
                    830945.7
                ],
                [
                    "2018\u5e74",
                    915243.5
                ],
                [
                    "2019\u5e74",
                    983751.2
                ],
                [
                    "2020\u5e74",
                    1005451.3
                ],
                [
                    "2021\u5e74",
                    1141230.8
                ],
                [
                    "2022\u5e74",
                    1194401.4
                ],
                [
                    "2023\u5e74",
                    1249990.6
                ]
            ],
            "hoverAnimation": true,
            "label": {
                "show": false,
                "position": "top",
                "color": "white",
                "margin": 8
            },
            "logBase": 10,
            "seriesLayoutBy": "column",
            "lineStyle": {
                "show": true,
                "width": 1,
                "opacity": 1,
                "curveness": 0,
                "type": "solid"
            },
            "areaStyle": {
                "opacity": 0
            },
            "zlevel": 0,
            "z": 0
        }
    ],
    "legend": [
        {
            "data": [
                "\u4ebf\u5143"
            ],
            "selected": {},
            "show": true,
            "padding": 5,
            "itemGap": 10,
            "itemWidth": 25,
            "itemHeight": 14,
            "backgroundColor": "transparent",
            "borderColor": "#ccc",
            "borderRadius": 0,
            "pageButtonItemGap": 5,
            "pageButtonPosition": "end",
            "pageFormatter": "{current}/{total}",
            "pageIconColor": "#2f4554",
            "pageIconInactiveColor": "#aaa",
            "pageIconSize": 15,
            "animationDurationUpdate": 800,
            "selector": false,
            "selectorPosition": "auto",
            "selectorItemGap": 7,
            "selectorButtonGap": 10
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "showContent": true,
        "alwaysShowContent": false,
        "showDelay": 0,
        "hideDelay": 100,
        "enterable": false,
        "confine": false,
        "appendToBody": false,
        "transitionDuration": 0.4,
        "textStyle": {
            "fontSize": 50
        },
        "borderWidth": 0,
        "padding": 5,
        "order": "seriesAsc"
    },
    "xAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": true,
                "lineStyle": {
                    "show": true,
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            },
            "data": [
                "1952\u5e74",
                "1953\u5e74",
                "1954\u5e74",
                "1955\u5e74",
                "1956\u5e74",
                "1957\u5e74",
                "1958\u5e74",
                "1959\u5e74",
                "1960\u5e74",
                "1961\u5e74",
                "1962\u5e74",
                "1963\u5e74",
                "1964\u5e74",
                "1965\u5e74",
                "1966\u5e74",
                "1967\u5e74",
                "1968\u5e74",
                "1969\u5e74",
                "1970\u5e74",
                "1971\u5e74",
                "1972\u5e74",
                "1973\u5e74",
                "1974\u5e74",
                "1975\u5e74",
                "1976\u5e74",
                "1977\u5e74",
                "1978\u5e74",
                "1979\u5e74",
                "1980\u5e74",
                "1981\u5e74",
                "1982\u5e74",
                "1983\u5e74",
                "1984\u5e74",
                "1985\u5e74",
                "1986\u5e74",
                "1987\u5e74",
                "1988\u5e74",
                "1989\u5e74",
                "1990\u5e74",
                "1991\u5e74",
                "1992\u5e74",
                "1993\u5e74",
                "1994\u5e74",
                "1995\u5e74",
                "1996\u5e74",
                "1997\u5e74",
                "1998\u5e74",
                "1999\u5e74",
                "2000\u5e74",
                "2001\u5e74",
                "2002\u5e74",
                "2003\u5e74",
                "2004\u5e74",
                "2005\u5e74",
                "2006\u5e74",
                "2007\u5e74",
                "2008\u5e74",
                "2009\u5e74",
                "2010\u5e74",
                "2011\u5e74",
                "2012\u5e74",
                "2013\u5e74",
                "2014\u5e74",
                "2015\u5e74",
                "2016\u5e74",
                "2017\u5e74",
                "2018\u5e74",
                "2019\u5e74",
                "2020\u5e74",
                "2021\u5e74",
                "2022\u5e74",
                "2023\u5e74"
            ]
        }
    ],
    "yAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": true,
                "lineStyle": {
                    "show": true,
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            }
        }
    ],
    "title": [
        {
            "show": true,
            "text": "GDP",
            "target": "blank",
            "subtarget": "blank",
            "padding": 5,
            "itemGap": 10,
            "textAlign": "auto",
            "textVerticalAlign": "auto",
            "triggerEvent": false
        }
    ]
};
        chart_bd14e2173316479197e29fe816502561.setOption(option_bd14e2173316479197e29fe816502561);
    </script>
</body>
</html>

"""
components.html(html_content, width=1000,height=650)



st.sidebar.header("绘图演示")
