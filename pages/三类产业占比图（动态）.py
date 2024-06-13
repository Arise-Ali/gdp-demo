from random import randint
from pyecharts import options as opts       
from pyecharts.charts import Pie, Timeline
from pyecharts.globals import ThemeType
import pandas as pd
import numpy as np
import streamlit as st
from streamlit_echarts import st_pyecharts
import streamlit.components.v1 as components
from bs4 import BeautifulSoup
import os


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
    <div id="4ecfbf0d124e43ef8c05bad3a8af3251" class="chart-container" style="width: 1500px; height:850px; "></div>
    <script>
        var chart_4ecfbf0d124e43ef8c05bad3a8af3251 = echarts.init(
            document.getElementById('4ecfbf0d124e43ef8c05bad3a8af3251'), 'light', {renderer: 'canvas'});
        var option_4ecfbf0d124e43ef8c05bad3a8af3251 = {
    "baseOption": {
        "series": [
            {
                "type": "pie",
                "colorBy": "data",
                "legendHoverLink": true,
                "selectedMode": false,
                "selectedOffset": 10,
                "clockwise": true,
                "startAngle": 90,
                "minAngle": 0,
                "minShowLabelAngle": 0,
                "avoidLabelOverlap": true,
                "stillShowZeroSum": true,
                "percentPrecision": 2,
                "showEmptyCircle": true,
                "emptyCircleStyle": {
                    "color": "lightgray",
                    "borderColor": "#000",
                    "borderWidth": 0,
                    "borderType": "solid",
                    "borderDashOffset": 0,
                    "borderCap": "butt",
                    "borderJoin": "bevel",
                    "borderMiterLimit": 10,
                    "opacity": 1
                },
                "data": [
                    {
                        "name": "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                        "value": 5
                    },
                    {
                        "name": "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                        "value": 33
                    },
                    {
                        "name": "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                        "value": 60
                    }
                ],
                "radius": [
                    "25%",
                    "75%"
                ],
                "center": [
                    "50%",
                    "50%"
                ],
                "roseType": "radius",
                "label": {
                    "show": true,
                    "margin": 8,
                    "fontSize": 30,
                    "formatter": "{b}:{d}%"
                },
                "labelLine": {
                    "show": true,
                    "showAbove": false,
                    "length": 15,
                    "length2": 15,
                    "smooth": false,
                    "minTurnAngle": 90,
                    "maxSurfaceAngle": 90
                },
                "rippleEffect": {
                    "show": true,
                    "brushType": "stroke",
                    "scale": 2.5,
                    "period": 4
                }
            }
        ],
        "timeline": {
            "axisType": "category",
            "currentIndex": 0,
            "orient": "horizontal",
            "autoPlay": false,
            "controlPosition": "left",
            "loop": false,
            "rewind": false,
            "show": true,
            "inverse": false,
            "playInterval": 100,
            "bottom": "-5px",
            "progress": {},
            "data": [
                "1978",
                "1979",
                "1980",
                "1981",
                "1982",
                "1983",
                "1984",
                "1985",
                "1986",
                "1987",
                "1988",
                "1989",
                "1990",
                "1991",
                "1992",
                "1993",
                "1994",
                "1995",
                "1996",
                "1997",
                "1998",
                "1999",
                "2000",
                "2001",
                "2002",
                "2003",
                "2004",
                "2005",
                "2006",
                "2007",
                "2008",
                "2009",
                "2010",
                "2011",
                "2012",
                "2013",
                "2014",
                "2015",
                "2016",
                "2017",
                "2018",
                "2019",
                "2020",
                "2021",
                "2022",
                "2023"
            ]
        },
        "legend": [
            {
                "data": [
                    "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                    "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                    "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)"
                ],
                "selected": {},
                "show": true,
                "left": "right",
                "orient": "vertical",
                "padding": 5,
                "itemGap": 10,
                "itemWidth": 25,
                "itemHeight": 14,
                "textStyle": {
                    "fontSize": 30
                },
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
        ]
    },
    "options": [
        {
            "series": [
                {
                    "type": "pie",
                    "colorBy": "data",
                    "legendHoverLink": true,
                    "selectedMode": false,
                    "selectedOffset": 10,
                    "clockwise": true,
                    "startAngle": 90,
                    "minAngle": 0,
                    "minShowLabelAngle": 0,
                    "avoidLabelOverlap": true,
                    "stillShowZeroSum": true,
                    "percentPrecision": 2,
                    "showEmptyCircle": true,
                    "emptyCircleStyle": {
                        "color": "lightgray",
                        "borderColor": "#000",
                        "borderWidth": 0,
                        "borderType": "solid",
                        "borderDashOffset": 0,
                        "borderCap": "butt",
                        "borderJoin": "bevel",
                        "borderMiterLimit": 10,
                        "opacity": 1
                    },
                    "data": [
                        {
                            "name": "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 9
                        },
                        {
                            "name": "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 61
                        },
                        {
                            "name": "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 28
                        }
                    ],
                    "radius": [
                        "25%",
                        "75%"
                    ],
                    "center": [
                        "50%",
                        "50%"
                    ],
                    "roseType": "radius",
                    "label": {
                        "show": true,
                        "margin": 8,
                        "fontSize": 30,
                        "formatter": "{b}:{d}%"
                    },
                    "labelLine": {
                        "show": true,
                        "showAbove": false,
                        "length": 15,
                        "length2": 15,
                        "smooth": false,
                        "minTurnAngle": 90,
                        "maxSurfaceAngle": 90
                    },
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                }
            ],
            "title": [
                {
                    "show": true,
                    "text": "\u4e09\u7c7b\u4ea7\u4e1a\u5360\u6bd4",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "left",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "fontSize": 50
                    }
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
                    "fontSize": 14
                },
                "borderWidth": 0,
                "padding": 5,
                "order": "seriesAsc"
            }
        },
        {
            "series": [
                {
                    "type": "pie",
                    "colorBy": "data",
                    "legendHoverLink": true,
                    "selectedMode": false,
                    "selectedOffset": 10,
                    "clockwise": true,
                    "startAngle": 90,
                    "minAngle": 0,
                    "minShowLabelAngle": 0,
                    "avoidLabelOverlap": true,
                    "stillShowZeroSum": true,
                    "percentPrecision": 2,
                    "showEmptyCircle": true,
                    "emptyCircleStyle": {
                        "color": "lightgray",
                        "borderColor": "#000",
                        "borderWidth": 0,
                        "borderType": "solid",
                        "borderDashOffset": 0,
                        "borderCap": "butt",
                        "borderJoin": "bevel",
                        "borderMiterLimit": 10,
                        "opacity": 1
                    },
                    "data": [
                        {
                            "name": "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 20
                        },
                        {
                            "name": "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 53
                        },
                        {
                            "name": "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 25
                        }
                    ],
                    "radius": [
                        "25%",
                        "75%"
                    ],
                    "center": [
                        "50%",
                        "50%"
                    ],
                    "roseType": "radius",
                    "label": {
                        "show": true,
                        "margin": 8,
                        "fontSize": 30,
                        "formatter": "{b}:{d}%"
                    },
                    "labelLine": {
                        "show": true,
                        "showAbove": false,
                        "length": 15,
                        "length2": 15,
                        "smooth": false,
                        "minTurnAngle": 90,
                        "maxSurfaceAngle": 90
                    },
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                }
            ],
            "title": [
                {
                    "show": true,
                    "text": "\u4e09\u7c7b\u4ea7\u4e1a\u5360\u6bd4",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "left",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "fontSize": 50
                    }
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
                    "fontSize": 14
                },
                "borderWidth": 0,
                "padding": 5,
                "order": "seriesAsc"
            }
        },
        {
            "series": [
                {
                    "type": "pie",
                    "colorBy": "data",
                    "legendHoverLink": true,
                    "selectedMode": false,
                    "selectedOffset": 10,
                    "clockwise": true,
                    "startAngle": 90,
                    "minAngle": 0,
                    "minShowLabelAngle": 0,
                    "avoidLabelOverlap": true,
                    "stillShowZeroSum": true,
                    "percentPrecision": 2,
                    "showEmptyCircle": true,
                    "emptyCircleStyle": {
                        "color": "lightgray",
                        "borderColor": "#000",
                        "borderWidth": 0,
                        "borderType": "solid",
                        "borderDashOffset": 0,
                        "borderCap": "butt",
                        "borderJoin": "bevel",
                        "borderMiterLimit": 10,
                        "opacity": 1
                    },
                    "data": [
                        {
                            "name": "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": -4
                        },
                        {
                            "name": "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 85
                        },
                        {
                            "name": "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 19
                        }
                    ],
                    "radius": [
                        "25%",
                        "75%"
                    ],
                    "center": [
                        "50%",
                        "50%"
                    ],
                    "roseType": "radius",
                    "label": {
                        "show": true,
                        "margin": 8,
                        "fontSize": 30,
                        "formatter": "{b}:{d}%"
                    },
                    "labelLine": {
                        "show": true,
                        "showAbove": false,
                        "length": 15,
                        "length2": 15,
                        "smooth": false,
                        "minTurnAngle": 90,
                        "maxSurfaceAngle": 90
                    },
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                }
            ],
            "title": [
                {
                    "show": true,
                    "text": "\u4e09\u7c7b\u4ea7\u4e1a\u5360\u6bd4",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "left",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "fontSize": 50
                    }
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
                    "fontSize": 14
                },
                "borderWidth": 0,
                "padding": 5,
                "order": "seriesAsc"
            }
        },
        {
            "series": [
                {
                    "type": "pie",
                    "colorBy": "data",
                    "legendHoverLink": true,
                    "selectedMode": false,
                    "selectedOffset": 10,
                    "clockwise": true,
                    "startAngle": 90,
                    "minAngle": 0,
                    "minShowLabelAngle": 0,
                    "avoidLabelOverlap": true,
                    "stillShowZeroSum": true,
                    "percentPrecision": 2,
                    "showEmptyCircle": true,
                    "emptyCircleStyle": {
                        "color": "lightgray",
                        "borderColor": "#000",
                        "borderWidth": 0,
                        "borderType": "solid",
                        "borderDashOffset": 0,
                        "borderCap": "butt",
                        "borderJoin": "bevel",
                        "borderMiterLimit": 10,
                        "opacity": 1
                    },
                    "data": [
                        {
                            "name": "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 40
                        },
                        {
                            "name": "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 17
                        },
                        {
                            "name": "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 41
                        }
                    ],
                    "radius": [
                        "25%",
                        "75%"
                    ],
                    "center": [
                        "50%",
                        "50%"
                    ],
                    "roseType": "radius",
                    "label": {
                        "show": true,
                        "margin": 8,
                        "fontSize": 30,
                        "formatter": "{b}:{d}%"
                    },
                    "labelLine": {
                        "show": true,
                        "showAbove": false,
                        "length": 15,
                        "length2": 15,
                        "smooth": false,
                        "minTurnAngle": 90,
                        "maxSurfaceAngle": 90
                    },
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                }
            ],
            "title": [
                {
                    "show": true,
                    "text": "\u4e09\u7c7b\u4ea7\u4e1a\u5360\u6bd4",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "left",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "fontSize": 50
                    }
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
                    "fontSize": 14
                },
                "borderWidth": 0,
                "padding": 5,
                "order": "seriesAsc"
            }
        },
        {
            "series": [
                {
                    "type": "pie",
                    "colorBy": "data",
                    "legendHoverLink": true,
                    "selectedMode": false,
                    "selectedOffset": 10,
                    "clockwise": true,
                    "startAngle": 90,
                    "minAngle": 0,
                    "minShowLabelAngle": 0,
                    "avoidLabelOverlap": true,
                    "stillShowZeroSum": true,
                    "percentPrecision": 2,
                    "showEmptyCircle": true,
                    "emptyCircleStyle": {
                        "color": "lightgray",
                        "borderColor": "#000",
                        "borderWidth": 0,
                        "borderType": "solid",
                        "borderDashOffset": 0,
                        "borderCap": "butt",
                        "borderJoin": "bevel",
                        "borderMiterLimit": 10,
                        "opacity": 1
                    },
                    "data": [
                        {
                            "name": "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 38
                        },
                        {
                            "name": "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 28
                        },
                        {
                            "name": "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 32
                        }
                    ],
                    "radius": [
                        "25%",
                        "75%"
                    ],
                    "center": [
                        "50%",
                        "50%"
                    ],
                    "roseType": "radius",
                    "label": {
                        "show": true,
                        "margin": 8,
                        "fontSize": 30,
                        "formatter": "{b}:{d}%"
                    },
                    "labelLine": {
                        "show": true,
                        "showAbove": false,
                        "length": 15,
                        "length2": 15,
                        "smooth": false,
                        "minTurnAngle": 90,
                        "maxSurfaceAngle": 90
                    },
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                }
            ],
            "title": [
                {
                    "show": true,
                    "text": "\u4e09\u7c7b\u4ea7\u4e1a\u5360\u6bd4",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "left",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "fontSize": 50
                    }
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
                    "fontSize": 14
                },
                "borderWidth": 0,
                "padding": 5,
                "order": "seriesAsc"
            }
        },
        {
            "series": [
                {
                    "type": "pie",
                    "colorBy": "data",
                    "legendHoverLink": true,
                    "selectedMode": false,
                    "selectedOffset": 10,
                    "clockwise": true,
                    "startAngle": 90,
                    "minAngle": 0,
                    "minShowLabelAngle": 0,
                    "avoidLabelOverlap": true,
                    "stillShowZeroSum": true,
                    "percentPrecision": 2,
                    "showEmptyCircle": true,
                    "emptyCircleStyle": {
                        "color": "lightgray",
                        "borderColor": "#000",
                        "borderWidth": 0,
                        "borderType": "solid",
                        "borderDashOffset": 0,
                        "borderCap": "butt",
                        "borderJoin": "bevel",
                        "borderMiterLimit": 10,
                        "opacity": 1
                    },
                    "data": [
                        {
                            "name": "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 23
                        },
                        {
                            "name": "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 43
                        },
                        {
                            "name": "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 32
                        }
                    ],
                    "radius": [
                        "25%",
                        "75%"
                    ],
                    "center": [
                        "50%",
                        "50%"
                    ],
                    "roseType": "radius",
                    "label": {
                        "show": true,
                        "margin": 8,
                        "fontSize": 30,
                        "formatter": "{b}:{d}%"
                    },
                    "labelLine": {
                        "show": true,
                        "showAbove": false,
                        "length": 15,
                        "length2": 15,
                        "smooth": false,
                        "minTurnAngle": 90,
                        "maxSurfaceAngle": 90
                    },
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                }
            ],
            "title": [
                {
                    "show": true,
                    "text": "\u4e09\u7c7b\u4ea7\u4e1a\u5360\u6bd4",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "left",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "fontSize": 50
                    }
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
                    "fontSize": 14
                },
                "borderWidth": 0,
                "padding": 5,
                "order": "seriesAsc"
            }
        },
        {
            "series": [
                {
                    "type": "pie",
                    "colorBy": "data",
                    "legendHoverLink": true,
                    "selectedMode": false,
                    "selectedOffset": 10,
                    "clockwise": true,
                    "startAngle": 90,
                    "minAngle": 0,
                    "minShowLabelAngle": 0,
                    "avoidLabelOverlap": true,
                    "stillShowZeroSum": true,
                    "percentPrecision": 2,
                    "showEmptyCircle": true,
                    "emptyCircleStyle": {
                        "color": "lightgray",
                        "borderColor": "#000",
                        "borderWidth": 0,
                        "borderType": "solid",
                        "borderDashOffset": 0,
                        "borderCap": "butt",
                        "borderJoin": "bevel",
                        "borderMiterLimit": 10,
                        "opacity": 1
                    },
                    "data": [
                        {
                            "name": "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 25
                        },
                        {
                            "name": "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 42
                        },
                        {
                            "name": "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 31
                        }
                    ],
                    "radius": [
                        "25%",
                        "75%"
                    ],
                    "center": [
                        "50%",
                        "50%"
                    ],
                    "roseType": "radius",
                    "label": {
                        "show": true,
                        "margin": 8,
                        "fontSize": 30,
                        "formatter": "{b}:{d}%"
                    },
                    "labelLine": {
                        "show": true,
                        "showAbove": false,
                        "length": 15,
                        "length2": 15,
                        "smooth": false,
                        "minTurnAngle": 90,
                        "maxSurfaceAngle": 90
                    },
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                }
            ],
            "title": [
                {
                    "show": true,
                    "text": "\u4e09\u7c7b\u4ea7\u4e1a\u5360\u6bd4",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "left",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "fontSize": 50
                    }
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
                    "fontSize": 14
                },
                "borderWidth": 0,
                "padding": 5,
                "order": "seriesAsc"
            }
        },
        {
            "series": [
                {
                    "type": "pie",
                    "colorBy": "data",
                    "legendHoverLink": true,
                    "selectedMode": false,
                    "selectedOffset": 10,
                    "clockwise": true,
                    "startAngle": 90,
                    "minAngle": 0,
                    "minShowLabelAngle": 0,
                    "avoidLabelOverlap": true,
                    "stillShowZeroSum": true,
                    "percentPrecision": 2,
                    "showEmptyCircle": true,
                    "emptyCircleStyle": {
                        "color": "lightgray",
                        "borderColor": "#000",
                        "borderWidth": 0,
                        "borderType": "solid",
                        "borderDashOffset": 0,
                        "borderCap": "butt",
                        "borderJoin": "bevel",
                        "borderMiterLimit": 10,
                        "opacity": 1
                    },
                    "data": [
                        {
                            "name": "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 4
                        },
                        {
                            "name": "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 61
                        },
                        {
                            "name": "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 34
                        }
                    ],
                    "radius": [
                        "25%",
                        "75%"
                    ],
                    "center": [
                        "50%",
                        "50%"
                    ],
                    "roseType": "radius",
                    "label": {
                        "show": true,
                        "margin": 8,
                        "fontSize": 30,
                        "formatter": "{b}:{d}%"
                    },
                    "labelLine": {
                        "show": true,
                        "showAbove": false,
                        "length": 15,
                        "length2": 15,
                        "smooth": false,
                        "minTurnAngle": 90,
                        "maxSurfaceAngle": 90
                    },
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                }
            ],
            "title": [
                {
                    "show": true,
                    "text": "\u4e09\u7c7b\u4ea7\u4e1a\u5360\u6bd4",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "left",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "fontSize": 50
                    }
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
                    "fontSize": 14
                },
                "borderWidth": 0,
                "padding": 5,
                "order": "seriesAsc"
            }
        },
        {
            "series": [
                {
                    "type": "pie",
                    "colorBy": "data",
                    "legendHoverLink": true,
                    "selectedMode": false,
                    "selectedOffset": 10,
                    "clockwise": true,
                    "startAngle": 90,
                    "minAngle": 0,
                    "minShowLabelAngle": 0,
                    "avoidLabelOverlap": true,
                    "stillShowZeroSum": true,
                    "percentPrecision": 2,
                    "showEmptyCircle": true,
                    "emptyCircleStyle": {
                        "color": "lightgray",
                        "borderColor": "#000",
                        "borderWidth": 0,
                        "borderType": "solid",
                        "borderDashOffset": 0,
                        "borderCap": "butt",
                        "borderJoin": "bevel",
                        "borderMiterLimit": 10,
                        "opacity": 1
                    },
                    "data": [
                        {
                            "name": "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 9
                        },
                        {
                            "name": "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 53
                        },
                        {
                            "name": "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 36
                        }
                    ],
                    "radius": [
                        "25%",
                        "75%"
                    ],
                    "center": [
                        "50%",
                        "50%"
                    ],
                    "roseType": "radius",
                    "label": {
                        "show": true,
                        "margin": 8,
                        "fontSize": 30,
                        "formatter": "{b}:{d}%"
                    },
                    "labelLine": {
                        "show": true,
                        "showAbove": false,
                        "length": 15,
                        "length2": 15,
                        "smooth": false,
                        "minTurnAngle": 90,
                        "maxSurfaceAngle": 90
                    },
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                }
            ],
            "title": [
                {
                    "show": true,
                    "text": "\u4e09\u7c7b\u4ea7\u4e1a\u5360\u6bd4",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "left",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "fontSize": 50
                    }
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
                    "fontSize": 14
                },
                "borderWidth": 0,
                "padding": 5,
                "order": "seriesAsc"
            }
        },
        {
            "series": [
                {
                    "type": "pie",
                    "colorBy": "data",
                    "legendHoverLink": true,
                    "selectedMode": false,
                    "selectedOffset": 10,
                    "clockwise": true,
                    "startAngle": 90,
                    "minAngle": 0,
                    "minShowLabelAngle": 0,
                    "avoidLabelOverlap": true,
                    "stillShowZeroSum": true,
                    "percentPrecision": 2,
                    "showEmptyCircle": true,
                    "emptyCircleStyle": {
                        "color": "lightgray",
                        "borderColor": "#000",
                        "borderWidth": 0,
                        "borderType": "solid",
                        "borderDashOffset": 0,
                        "borderCap": "butt",
                        "borderJoin": "bevel",
                        "borderMiterLimit": 10,
                        "opacity": 1
                    },
                    "data": [
                        {
                            "name": "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 10
                        },
                        {
                            "name": "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 55
                        },
                        {
                            "name": "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 34
                        }
                    ],
                    "radius": [
                        "25%",
                        "75%"
                    ],
                    "center": [
                        "50%",
                        "50%"
                    ],
                    "roseType": "radius",
                    "label": {
                        "show": true,
                        "margin": 8,
                        "fontSize": 30,
                        "formatter": "{b}:{d}%"
                    },
                    "labelLine": {
                        "show": true,
                        "showAbove": false,
                        "length": 15,
                        "length2": 15,
                        "smooth": false,
                        "minTurnAngle": 90,
                        "maxSurfaceAngle": 90
                    },
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                }
            ],
            "title": [
                {
                    "show": true,
                    "text": "\u4e09\u7c7b\u4ea7\u4e1a\u5360\u6bd4",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "left",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "fontSize": 50
                    }
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
                    "fontSize": 14
                },
                "borderWidth": 0,
                "padding": 5,
                "order": "seriesAsc"
            }
        },
        {
            "series": [
                {
                    "type": "pie",
                    "colorBy": "data",
                    "legendHoverLink": true,
                    "selectedMode": false,
                    "selectedOffset": 10,
                    "clockwise": true,
                    "startAngle": 90,
                    "minAngle": 0,
                    "minShowLabelAngle": 0,
                    "avoidLabelOverlap": true,
                    "stillShowZeroSum": true,
                    "percentPrecision": 2,
                    "showEmptyCircle": true,
                    "emptyCircleStyle": {
                        "color": "lightgray",
                        "borderColor": "#000",
                        "borderWidth": 0,
                        "borderType": "solid",
                        "borderDashOffset": 0,
                        "borderCap": "butt",
                        "borderJoin": "bevel",
                        "borderMiterLimit": 10,
                        "opacity": 1
                    },
                    "data": [
                        {
                            "name": "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 5
                        },
                        {
                            "name": "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 61
                        },
                        {
                            "name": "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 33
                        }
                    ],
                    "radius": [
                        "25%",
                        "75%"
                    ],
                    "center": [
                        "50%",
                        "50%"
                    ],
                    "roseType": "radius",
                    "label": {
                        "show": true,
                        "margin": 8,
                        "fontSize": 30,
                        "formatter": "{b}:{d}%"
                    },
                    "labelLine": {
                        "show": true,
                        "showAbove": false,
                        "length": 15,
                        "length2": 15,
                        "smooth": false,
                        "minTurnAngle": 90,
                        "maxSurfaceAngle": 90
                    },
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                }
            ],
            "title": [
                {
                    "show": true,
                    "text": "\u4e09\u7c7b\u4ea7\u4e1a\u5360\u6bd4",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "left",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "fontSize": 50
                    }
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
                    "fontSize": 14
                },
                "borderWidth": 0,
                "padding": 5,
                "order": "seriesAsc"
            }
        },
        {
            "series": [
                {
                    "type": "pie",
                    "colorBy": "data",
                    "legendHoverLink": true,
                    "selectedMode": false,
                    "selectedOffset": 10,
                    "clockwise": true,
                    "startAngle": 90,
                    "minAngle": 0,
                    "minShowLabelAngle": 0,
                    "avoidLabelOverlap": true,
                    "stillShowZeroSum": true,
                    "percentPrecision": 2,
                    "showEmptyCircle": true,
                    "emptyCircleStyle": {
                        "color": "lightgray",
                        "borderColor": "#000",
                        "borderWidth": 0,
                        "borderType": "solid",
                        "borderDashOffset": 0,
                        "borderCap": "butt",
                        "borderJoin": "bevel",
                        "borderMiterLimit": 10,
                        "opacity": 1
                    },
                    "data": [
                        {
                            "name": "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 15
                        },
                        {
                            "name": "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 44
                        },
                        {
                            "name": "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 40
                        }
                    ],
                    "radius": [
                        "25%",
                        "75%"
                    ],
                    "center": [
                        "50%",
                        "50%"
                    ],
                    "roseType": "radius",
                    "label": {
                        "show": true,
                        "margin": 8,
                        "fontSize": 30,
                        "formatter": "{b}:{d}%"
                    },
                    "labelLine": {
                        "show": true,
                        "showAbove": false,
                        "length": 15,
                        "length2": 15,
                        "smooth": false,
                        "minTurnAngle": 90,
                        "maxSurfaceAngle": 90
                    },
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                }
            ],
            "title": [
                {
                    "show": true,
                    "text": "\u4e09\u7c7b\u4ea7\u4e1a\u5360\u6bd4",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "left",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "fontSize": 50
                    }
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
                    "fontSize": 14
                },
                "borderWidth": 0,
                "padding": 5,
                "order": "seriesAsc"
            }
        },
        {
            "series": [
                {
                    "type": "pie",
                    "colorBy": "data",
                    "legendHoverLink": true,
                    "selectedMode": false,
                    "selectedOffset": 10,
                    "clockwise": true,
                    "startAngle": 90,
                    "minAngle": 0,
                    "minShowLabelAngle": 0,
                    "avoidLabelOverlap": true,
                    "stillShowZeroSum": true,
                    "percentPrecision": 2,
                    "showEmptyCircle": true,
                    "emptyCircleStyle": {
                        "color": "lightgray",
                        "borderColor": "#000",
                        "borderWidth": 0,
                        "borderType": "solid",
                        "borderDashOffset": 0,
                        "borderCap": "butt",
                        "borderJoin": "bevel",
                        "borderMiterLimit": 10,
                        "opacity": 1
                    },
                    "data": [
                        {
                            "name": "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 40
                        },
                        {
                            "name": "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 39
                        },
                        {
                            "name": "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 20
                        }
                    ],
                    "radius": [
                        "25%",
                        "75%"
                    ],
                    "center": [
                        "50%",
                        "50%"
                    ],
                    "roseType": "radius",
                    "label": {
                        "show": true,
                        "margin": 8,
                        "fontSize": 30,
                        "formatter": "{b}:{d}%"
                    },
                    "labelLine": {
                        "show": true,
                        "showAbove": false,
                        "length": 15,
                        "length2": 15,
                        "smooth": false,
                        "minTurnAngle": 90,
                        "maxSurfaceAngle": 90
                    },
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                }
            ],
            "title": [
                {
                    "show": true,
                    "text": "\u4e09\u7c7b\u4ea7\u4e1a\u5360\u6bd4",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "left",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "fontSize": 50
                    }
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
                    "fontSize": 14
                },
                "borderWidth": 0,
                "padding": 5,
                "order": "seriesAsc"
            }
        },
        {
            "series": [
                {
                    "type": "pie",
                    "colorBy": "data",
                    "legendHoverLink": true,
                    "selectedMode": false,
                    "selectedOffset": 10,
                    "clockwise": true,
                    "startAngle": 90,
                    "minAngle": 0,
                    "minShowLabelAngle": 0,
                    "avoidLabelOverlap": true,
                    "stillShowZeroSum": true,
                    "percentPrecision": 2,
                    "showEmptyCircle": true,
                    "emptyCircleStyle": {
                        "color": "lightgray",
                        "borderColor": "#000",
                        "borderWidth": 0,
                        "borderType": "solid",
                        "borderDashOffset": 0,
                        "borderCap": "butt",
                        "borderJoin": "bevel",
                        "borderMiterLimit": 10,
                        "opacity": 1
                    },
                    "data": [
                        {
                            "name": "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 6
                        },
                        {
                            "name": "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 61
                        },
                        {
                            "name": "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 32
                        }
                    ],
                    "radius": [
                        "25%",
                        "75%"
                    ],
                    "center": [
                        "50%",
                        "50%"
                    ],
                    "roseType": "radius",
                    "label": {
                        "show": true,
                        "margin": 8,
                        "fontSize": 30,
                        "formatter": "{b}:{d}%"
                    },
                    "labelLine": {
                        "show": true,
                        "showAbove": false,
                        "length": 15,
                        "length2": 15,
                        "smooth": false,
                        "minTurnAngle": 90,
                        "maxSurfaceAngle": 90
                    },
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                }
            ],
            "title": [
                {
                    "show": true,
                    "text": "\u4e09\u7c7b\u4ea7\u4e1a\u5360\u6bd4",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "left",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "fontSize": 50
                    }
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
                    "fontSize": 14
                },
                "borderWidth": 0,
                "padding": 5,
                "order": "seriesAsc"
            }
        },
        {
            "series": [
                {
                    "type": "pie",
                    "colorBy": "data",
                    "legendHoverLink": true,
                    "selectedMode": false,
                    "selectedOffset": 10,
                    "clockwise": true,
                    "startAngle": 90,
                    "minAngle": 0,
                    "minShowLabelAngle": 0,
                    "avoidLabelOverlap": true,
                    "stillShowZeroSum": true,
                    "percentPrecision": 2,
                    "showEmptyCircle": true,
                    "emptyCircleStyle": {
                        "color": "lightgray",
                        "borderColor": "#000",
                        "borderWidth": 0,
                        "borderType": "solid",
                        "borderDashOffset": 0,
                        "borderCap": "butt",
                        "borderJoin": "bevel",
                        "borderMiterLimit": 10,
                        "opacity": 1
                    },
                    "data": [
                        {
                            "name": "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 8
                        },
                        {
                            "name": "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 63
                        },
                        {
                            "name": "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 28
                        }
                    ],
                    "radius": [
                        "25%",
                        "75%"
                    ],
                    "center": [
                        "50%",
                        "50%"
                    ],
                    "roseType": "radius",
                    "label": {
                        "show": true,
                        "margin": 8,
                        "fontSize": 30,
                        "formatter": "{b}:{d}%"
                    },
                    "labelLine": {
                        "show": true,
                        "showAbove": false,
                        "length": 15,
                        "length2": 15,
                        "smooth": false,
                        "minTurnAngle": 90,
                        "maxSurfaceAngle": 90
                    },
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                }
            ],
            "title": [
                {
                    "show": true,
                    "text": "\u4e09\u7c7b\u4ea7\u4e1a\u5360\u6bd4",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "left",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "fontSize": 50
                    }
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
                    "fontSize": 14
                },
                "borderWidth": 0,
                "padding": 5,
                "order": "seriesAsc"
            }
        },
        {
            "series": [
                {
                    "type": "pie",
                    "colorBy": "data",
                    "legendHoverLink": true,
                    "selectedMode": false,
                    "selectedOffset": 10,
                    "clockwise": true,
                    "startAngle": 90,
                    "minAngle": 0,
                    "minShowLabelAngle": 0,
                    "avoidLabelOverlap": true,
                    "stillShowZeroSum": true,
                    "percentPrecision": 2,
                    "showEmptyCircle": true,
                    "emptyCircleStyle": {
                        "color": "lightgray",
                        "borderColor": "#000",
                        "borderWidth": 0,
                        "borderType": "solid",
                        "borderDashOffset": 0,
                        "borderCap": "butt",
                        "borderJoin": "bevel",
                        "borderMiterLimit": 10,
                        "opacity": 1
                    },
                    "data": [
                        {
                            "name": "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 7
                        },
                        {
                            "name": "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 64
                        },
                        {
                            "name": "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 28
                        }
                    ],
                    "radius": [
                        "25%",
                        "75%"
                    ],
                    "center": [
                        "50%",
                        "50%"
                    ],
                    "roseType": "radius",
                    "label": {
                        "show": true,
                        "margin": 8,
                        "fontSize": 30,
                        "formatter": "{b}:{d}%"
                    },
                    "labelLine": {
                        "show": true,
                        "showAbove": false,
                        "length": 15,
                        "length2": 15,
                        "smooth": false,
                        "minTurnAngle": 90,
                        "maxSurfaceAngle": 90
                    },
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                }
            ],
            "title": [
                {
                    "show": true,
                    "text": "\u4e09\u7c7b\u4ea7\u4e1a\u5360\u6bd4",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "left",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "fontSize": 50
                    }
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
                    "fontSize": 14
                },
                "borderWidth": 0,
                "padding": 5,
                "order": "seriesAsc"
            }
        },
        {
            "series": [
                {
                    "type": "pie",
                    "colorBy": "data",
                    "legendHoverLink": true,
                    "selectedMode": false,
                    "selectedOffset": 10,
                    "clockwise": true,
                    "startAngle": 90,
                    "minAngle": 0,
                    "minShowLabelAngle": 0,
                    "avoidLabelOverlap": true,
                    "stillShowZeroSum": true,
                    "percentPrecision": 2,
                    "showEmptyCircle": true,
                    "emptyCircleStyle": {
                        "color": "lightgray",
                        "borderColor": "#000",
                        "borderWidth": 0,
                        "borderType": "solid",
                        "borderDashOffset": 0,
                        "borderCap": "butt",
                        "borderJoin": "bevel",
                        "borderMiterLimit": 10,
                        "opacity": 1
                    },
                    "data": [
                        {
                            "name": "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 6
                        },
                        {
                            "name": "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 66
                        },
                        {
                            "name": "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 27
                        }
                    ],
                    "radius": [
                        "25%",
                        "75%"
                    ],
                    "center": [
                        "50%",
                        "50%"
                    ],
                    "roseType": "radius",
                    "label": {
                        "show": true,
                        "margin": 8,
                        "fontSize": 30,
                        "formatter": "{b}:{d}%"
                    },
                    "labelLine": {
                        "show": true,
                        "showAbove": false,
                        "length": 15,
                        "length2": 15,
                        "smooth": false,
                        "minTurnAngle": 90,
                        "maxSurfaceAngle": 90
                    },
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                }
            ],
            "title": [
                {
                    "show": true,
                    "text": "\u4e09\u7c7b\u4ea7\u4e1a\u5360\u6bd4",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "left",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "fontSize": 50
                    }
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
                    "fontSize": 14
                },
                "borderWidth": 0,
                "padding": 5,
                "order": "seriesAsc"
            }
        },
        {
            "series": [
                {
                    "type": "pie",
                    "colorBy": "data",
                    "legendHoverLink": true,
                    "selectedMode": false,
                    "selectedOffset": 10,
                    "clockwise": true,
                    "startAngle": 90,
                    "minAngle": 0,
                    "minShowLabelAngle": 0,
                    "avoidLabelOverlap": true,
                    "stillShowZeroSum": true,
                    "percentPrecision": 2,
                    "showEmptyCircle": true,
                    "emptyCircleStyle": {
                        "color": "lightgray",
                        "borderColor": "#000",
                        "borderWidth": 0,
                        "borderType": "solid",
                        "borderDashOffset": 0,
                        "borderCap": "butt",
                        "borderJoin": "bevel",
                        "borderMiterLimit": 10,
                        "opacity": 1
                    },
                    "data": [
                        {
                            "name": "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 8
                        },
                        {
                            "name": "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 62
                        },
                        {
                            "name": "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 28
                        }
                    ],
                    "radius": [
                        "25%",
                        "75%"
                    ],
                    "center": [
                        "50%",
                        "50%"
                    ],
                    "roseType": "radius",
                    "label": {
                        "show": true,
                        "margin": 8,
                        "fontSize": 30,
                        "formatter": "{b}:{d}%"
                    },
                    "labelLine": {
                        "show": true,
                        "showAbove": false,
                        "length": 15,
                        "length2": 15,
                        "smooth": false,
                        "minTurnAngle": 90,
                        "maxSurfaceAngle": 90
                    },
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                }
            ],
            "title": [
                {
                    "show": true,
                    "text": "\u4e09\u7c7b\u4ea7\u4e1a\u5360\u6bd4",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "left",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "fontSize": 50
                    }
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
                    "fontSize": 14
                },
                "borderWidth": 0,
                "padding": 5,
                "order": "seriesAsc"
            }
        },
        {
            "series": [
                {
                    "type": "pie",
                    "colorBy": "data",
                    "legendHoverLink": true,
                    "selectedMode": false,
                    "selectedOffset": 10,
                    "clockwise": true,
                    "startAngle": 90,
                    "minAngle": 0,
                    "minShowLabelAngle": 0,
                    "avoidLabelOverlap": true,
                    "stillShowZeroSum": true,
                    "percentPrecision": 2,
                    "showEmptyCircle": true,
                    "emptyCircleStyle": {
                        "color": "lightgray",
                        "borderColor": "#000",
                        "borderWidth": 0,
                        "borderType": "solid",
                        "borderDashOffset": 0,
                        "borderCap": "butt",
                        "borderJoin": "bevel",
                        "borderMiterLimit": 10,
                        "opacity": 1
                    },
                    "data": [
                        {
                            "name": "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 9
                        },
                        {
                            "name": "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 62
                        },
                        {
                            "name": "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 28
                        }
                    ],
                    "radius": [
                        "25%",
                        "75%"
                    ],
                    "center": [
                        "50%",
                        "50%"
                    ],
                    "roseType": "radius",
                    "label": {
                        "show": true,
                        "margin": 8,
                        "fontSize": 30,
                        "formatter": "{b}:{d}%"
                    },
                    "labelLine": {
                        "show": true,
                        "showAbove": false,
                        "length": 15,
                        "length2": 15,
                        "smooth": false,
                        "minTurnAngle": 90,
                        "maxSurfaceAngle": 90
                    },
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                }
            ],
            "title": [
                {
                    "show": true,
                    "text": "\u4e09\u7c7b\u4ea7\u4e1a\u5360\u6bd4",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "left",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "fontSize": 50
                    }
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
                    "fontSize": 14
                },
                "borderWidth": 0,
                "padding": 5,
                "order": "seriesAsc"
            }
        },
        {
            "series": [
                {
                    "type": "pie",
                    "colorBy": "data",
                    "legendHoverLink": true,
                    "selectedMode": false,
                    "selectedOffset": 10,
                    "clockwise": true,
                    "startAngle": 90,
                    "minAngle": 0,
                    "minShowLabelAngle": 0,
                    "avoidLabelOverlap": true,
                    "stillShowZeroSum": true,
                    "percentPrecision": 2,
                    "showEmptyCircle": true,
                    "emptyCircleStyle": {
                        "color": "lightgray",
                        "borderColor": "#000",
                        "borderWidth": 0,
                        "borderType": "solid",
                        "borderDashOffset": 0,
                        "borderCap": "butt",
                        "borderJoin": "bevel",
                        "borderMiterLimit": 10,
                        "opacity": 1
                    },
                    "data": [
                        {
                            "name": "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 6
                        },
                        {
                            "name": "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 59
                        },
                        {
                            "name": "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 34
                        }
                    ],
                    "radius": [
                        "25%",
                        "75%"
                    ],
                    "center": [
                        "50%",
                        "50%"
                    ],
                    "roseType": "radius",
                    "label": {
                        "show": true,
                        "margin": 8,
                        "fontSize": 30,
                        "formatter": "{b}:{d}%"
                    },
                    "labelLine": {
                        "show": true,
                        "showAbove": false,
                        "length": 15,
                        "length2": 15,
                        "smooth": false,
                        "minTurnAngle": 90,
                        "maxSurfaceAngle": 90
                    },
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                }
            ],
            "title": [
                {
                    "show": true,
                    "text": "\u4e09\u7c7b\u4ea7\u4e1a\u5360\u6bd4",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "left",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "fontSize": 50
                    }
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
                    "fontSize": 14
                },
                "borderWidth": 0,
                "padding": 5,
                "order": "seriesAsc"
            }
        },
        {
            "series": [
                {
                    "type": "pie",
                    "colorBy": "data",
                    "legendHoverLink": true,
                    "selectedMode": false,
                    "selectedOffset": 10,
                    "clockwise": true,
                    "startAngle": 90,
                    "minAngle": 0,
                    "minShowLabelAngle": 0,
                    "avoidLabelOverlap": true,
                    "stillShowZeroSum": true,
                    "percentPrecision": 2,
                    "showEmptyCircle": true,
                    "emptyCircleStyle": {
                        "color": "lightgray",
                        "borderColor": "#000",
                        "borderWidth": 0,
                        "borderType": "solid",
                        "borderDashOffset": 0,
                        "borderCap": "butt",
                        "borderJoin": "bevel",
                        "borderMiterLimit": 10,
                        "opacity": 1
                    },
                    "data": [
                        {
                            "name": "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 7
                        },
                        {
                            "name": "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 59
                        },
                        {
                            "name": "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 33
                        }
                    ],
                    "radius": [
                        "25%",
                        "75%"
                    ],
                    "center": [
                        "50%",
                        "50%"
                    ],
                    "roseType": "radius",
                    "label": {
                        "show": true,
                        "margin": 8,
                        "fontSize": 30,
                        "formatter": "{b}:{d}%"
                    },
                    "labelLine": {
                        "show": true,
                        "showAbove": false,
                        "length": 15,
                        "length2": 15,
                        "smooth": false,
                        "minTurnAngle": 90,
                        "maxSurfaceAngle": 90
                    },
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                }
            ],
            "title": [
                {
                    "show": true,
                    "text": "\u4e09\u7c7b\u4ea7\u4e1a\u5360\u6bd4",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "left",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "fontSize": 50
                    }
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
                    "fontSize": 14
                },
                "borderWidth": 0,
                "padding": 5,
                "order": "seriesAsc"
            }
        },
        {
            "series": [
                {
                    "type": "pie",
                    "colorBy": "data",
                    "legendHoverLink": true,
                    "selectedMode": false,
                    "selectedOffset": 10,
                    "clockwise": true,
                    "startAngle": 90,
                    "minAngle": 0,
                    "minShowLabelAngle": 0,
                    "avoidLabelOverlap": true,
                    "stillShowZeroSum": true,
                    "percentPrecision": 2,
                    "showEmptyCircle": true,
                    "emptyCircleStyle": {
                        "color": "lightgray",
                        "borderColor": "#000",
                        "borderWidth": 0,
                        "borderType": "solid",
                        "borderDashOffset": 0,
                        "borderCap": "butt",
                        "borderJoin": "bevel",
                        "borderMiterLimit": 10,
                        "opacity": 1
                    },
                    "data": [
                        {
                            "name": "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 5
                        },
                        {
                            "name": "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 56
                        },
                        {
                            "name": "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 37
                        }
                    ],
                    "radius": [
                        "25%",
                        "75%"
                    ],
                    "center": [
                        "50%",
                        "50%"
                    ],
                    "roseType": "radius",
                    "label": {
                        "show": true,
                        "margin": 8,
                        "fontSize": 30,
                        "formatter": "{b}:{d}%"
                    },
                    "labelLine": {
                        "show": true,
                        "showAbove": false,
                        "length": 15,
                        "length2": 15,
                        "smooth": false,
                        "minTurnAngle": 90,
                        "maxSurfaceAngle": 90
                    },
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                }
            ],
            "title": [
                {
                    "show": true,
                    "text": "\u4e09\u7c7b\u4ea7\u4e1a\u5360\u6bd4",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "left",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "fontSize": 50
                    }
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
                    "fontSize": 14
                },
                "borderWidth": 0,
                "padding": 5,
                "order": "seriesAsc"
            }
        },
        {
            "series": [
                {
                    "type": "pie",
                    "colorBy": "data",
                    "legendHoverLink": true,
                    "selectedMode": false,
                    "selectedOffset": 10,
                    "clockwise": true,
                    "startAngle": 90,
                    "minAngle": 0,
                    "minShowLabelAngle": 0,
                    "avoidLabelOverlap": true,
                    "stillShowZeroSum": true,
                    "percentPrecision": 2,
                    "showEmptyCircle": true,
                    "emptyCircleStyle": {
                        "color": "lightgray",
                        "borderColor": "#000",
                        "borderWidth": 0,
                        "borderType": "solid",
                        "borderDashOffset": 0,
                        "borderCap": "butt",
                        "borderJoin": "bevel",
                        "borderMiterLimit": 10,
                        "opacity": 1
                    },
                    "data": [
                        {
                            "name": "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 4
                        },
                        {
                            "name": "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 59
                        },
                        {
                            "name": "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 36
                        }
                    ],
                    "radius": [
                        "25%",
                        "75%"
                    ],
                    "center": [
                        "50%",
                        "50%"
                    ],
                    "roseType": "radius",
                    "label": {
                        "show": true,
                        "margin": 8,
                        "fontSize": 30,
                        "formatter": "{b}:{d}%"
                    },
                    "labelLine": {
                        "show": true,
                        "showAbove": false,
                        "length": 15,
                        "length2": 15,
                        "smooth": false,
                        "minTurnAngle": 90,
                        "maxSurfaceAngle": 90
                    },
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                }
            ],
            "title": [
                {
                    "show": true,
                    "text": "\u4e09\u7c7b\u4ea7\u4e1a\u5360\u6bd4",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "left",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "fontSize": 50
                    }
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
                    "fontSize": 14
                },
                "borderWidth": 0,
                "padding": 5,
                "order": "seriesAsc"
            }
        },
        {
            "series": [
                {
                    "type": "pie",
                    "colorBy": "data",
                    "legendHoverLink": true,
                    "selectedMode": false,
                    "selectedOffset": 10,
                    "clockwise": true,
                    "startAngle": 90,
                    "minAngle": 0,
                    "minShowLabelAngle": 0,
                    "avoidLabelOverlap": true,
                    "stillShowZeroSum": true,
                    "percentPrecision": 2,
                    "showEmptyCircle": true,
                    "emptyCircleStyle": {
                        "color": "lightgray",
                        "borderColor": "#000",
                        "borderWidth": 0,
                        "borderType": "solid",
                        "borderDashOffset": 0,
                        "borderCap": "butt",
                        "borderJoin": "bevel",
                        "borderMiterLimit": 10,
                        "opacity": 1
                    },
                    "data": [
                        {
                            "name": "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 4
                        },
                        {
                            "name": "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 46
                        },
                        {
                            "name": "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 49
                        }
                    ],
                    "radius": [
                        "25%",
                        "75%"
                    ],
                    "center": [
                        "50%",
                        "50%"
                    ],
                    "roseType": "radius",
                    "label": {
                        "show": true,
                        "margin": 8,
                        "fontSize": 30,
                        "formatter": "{b}:{d}%"
                    },
                    "labelLine": {
                        "show": true,
                        "showAbove": false,
                        "length": 15,
                        "length2": 15,
                        "smooth": false,
                        "minTurnAngle": 90,
                        "maxSurfaceAngle": 90
                    },
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                }
            ],
            "title": [
                {
                    "show": true,
                    "text": "\u4e09\u7c7b\u4ea7\u4e1a\u5360\u6bd4",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "left",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "fontSize": 50
                    }
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
                    "fontSize": 14
                },
                "borderWidth": 0,
                "padding": 5,
                "order": "seriesAsc"
            }
        },
        {
            "series": [
                {
                    "type": "pie",
                    "colorBy": "data",
                    "legendHoverLink": true,
                    "selectedMode": false,
                    "selectedOffset": 10,
                    "clockwise": true,
                    "startAngle": 90,
                    "minAngle": 0,
                    "minShowLabelAngle": 0,
                    "avoidLabelOverlap": true,
                    "stillShowZeroSum": true,
                    "percentPrecision": 2,
                    "showEmptyCircle": true,
                    "emptyCircleStyle": {
                        "color": "lightgray",
                        "borderColor": "#000",
                        "borderWidth": 0,
                        "borderType": "solid",
                        "borderDashOffset": 0,
                        "borderCap": "butt",
                        "borderJoin": "bevel",
                        "borderMiterLimit": 10,
                        "opacity": 1
                    },
                    "data": [
                        {
                            "name": "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 4
                        },
                        {
                            "name": "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 49
                        },
                        {
                            "name": "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 46
                        }
                    ],
                    "radius": [
                        "25%",
                        "75%"
                    ],
                    "center": [
                        "50%",
                        "50%"
                    ],
                    "roseType": "radius",
                    "label": {
                        "show": true,
                        "margin": 8,
                        "fontSize": 30,
                        "formatter": "{b}:{d}%"
                    },
                    "labelLine": {
                        "show": true,
                        "showAbove": false,
                        "length": 15,
                        "length2": 15,
                        "smooth": false,
                        "minTurnAngle": 90,
                        "maxSurfaceAngle": 90
                    },
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                }
            ],
            "title": [
                {
                    "show": true,
                    "text": "\u4e09\u7c7b\u4ea7\u4e1a\u5360\u6bd4",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "left",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "fontSize": 50
                    }
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
                    "fontSize": 14
                },
                "borderWidth": 0,
                "padding": 5,
                "order": "seriesAsc"
            }
        },
        {
            "series": [
                {
                    "type": "pie",
                    "colorBy": "data",
                    "legendHoverLink": true,
                    "selectedMode": false,
                    "selectedOffset": 10,
                    "clockwise": true,
                    "startAngle": 90,
                    "minAngle": 0,
                    "minShowLabelAngle": 0,
                    "avoidLabelOverlap": true,
                    "stillShowZeroSum": true,
                    "percentPrecision": 2,
                    "showEmptyCircle": true,
                    "emptyCircleStyle": {
                        "color": "lightgray",
                        "borderColor": "#000",
                        "borderWidth": 0,
                        "borderType": "solid",
                        "borderDashOffset": 0,
                        "borderCap": "butt",
                        "borderJoin": "bevel",
                        "borderMiterLimit": 10,
                        "opacity": 1
                    },
                    "data": [
                        {
                            "name": "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 3
                        },
                        {
                            "name": "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 57
                        },
                        {
                            "name": "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 39
                        }
                    ],
                    "radius": [
                        "25%",
                        "75%"
                    ],
                    "center": [
                        "50%",
                        "50%"
                    ],
                    "roseType": "radius",
                    "label": {
                        "show": true,
                        "margin": 8,
                        "fontSize": 30,
                        "formatter": "{b}:{d}%"
                    },
                    "labelLine": {
                        "show": true,
                        "showAbove": false,
                        "length": 15,
                        "length2": 15,
                        "smooth": false,
                        "minTurnAngle": 90,
                        "maxSurfaceAngle": 90
                    },
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                }
            ],
            "title": [
                {
                    "show": true,
                    "text": "\u4e09\u7c7b\u4ea7\u4e1a\u5360\u6bd4",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "left",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "fontSize": 50
                    }
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
                    "fontSize": 14
                },
                "borderWidth": 0,
                "padding": 5,
                "order": "seriesAsc"
            }
        },
        {
            "series": [
                {
                    "type": "pie",
                    "colorBy": "data",
                    "legendHoverLink": true,
                    "selectedMode": false,
                    "selectedOffset": 10,
                    "clockwise": true,
                    "startAngle": 90,
                    "minAngle": 0,
                    "minShowLabelAngle": 0,
                    "avoidLabelOverlap": true,
                    "stillShowZeroSum": true,
                    "percentPrecision": 2,
                    "showEmptyCircle": true,
                    "emptyCircleStyle": {
                        "color": "lightgray",
                        "borderColor": "#000",
                        "borderWidth": 0,
                        "borderType": "solid",
                        "borderDashOffset": 0,
                        "borderCap": "butt",
                        "borderJoin": "bevel",
                        "borderMiterLimit": 10,
                        "opacity": 1
                    },
                    "data": [
                        {
                            "name": "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 7
                        },
                        {
                            "name": "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 51
                        },
                        {
                            "name": "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 40
                        }
                    ],
                    "radius": [
                        "25%",
                        "75%"
                    ],
                    "center": [
                        "50%",
                        "50%"
                    ],
                    "roseType": "radius",
                    "label": {
                        "show": true,
                        "margin": 8,
                        "fontSize": 30,
                        "formatter": "{b}:{d}%"
                    },
                    "labelLine": {
                        "show": true,
                        "showAbove": false,
                        "length": 15,
                        "length2": 15,
                        "smooth": false,
                        "minTurnAngle": 90,
                        "maxSurfaceAngle": 90
                    },
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                }
            ],
            "title": [
                {
                    "show": true,
                    "text": "\u4e09\u7c7b\u4ea7\u4e1a\u5360\u6bd4",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "left",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "fontSize": 50
                    }
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
                    "fontSize": 14
                },
                "borderWidth": 0,
                "padding": 5,
                "order": "seriesAsc"
            }
        },
        {
            "series": [
                {
                    "type": "pie",
                    "colorBy": "data",
                    "legendHoverLink": true,
                    "selectedMode": false,
                    "selectedOffset": 10,
                    "clockwise": true,
                    "startAngle": 90,
                    "minAngle": 0,
                    "minShowLabelAngle": 0,
                    "avoidLabelOverlap": true,
                    "stillShowZeroSum": true,
                    "percentPrecision": 2,
                    "showEmptyCircle": true,
                    "emptyCircleStyle": {
                        "color": "lightgray",
                        "borderColor": "#000",
                        "borderWidth": 0,
                        "borderType": "solid",
                        "borderDashOffset": 0,
                        "borderCap": "butt",
                        "borderJoin": "bevel",
                        "borderMiterLimit": 10,
                        "opacity": 1
                    },
                    "data": [
                        {
                            "name": "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 5
                        },
                        {
                            "name": "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 50
                        },
                        {
                            "name": "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 44
                        }
                    ],
                    "radius": [
                        "25%",
                        "75%"
                    ],
                    "center": [
                        "50%",
                        "50%"
                    ],
                    "roseType": "radius",
                    "label": {
                        "show": true,
                        "margin": 8,
                        "fontSize": 30,
                        "formatter": "{b}:{d}%"
                    },
                    "labelLine": {
                        "show": true,
                        "showAbove": false,
                        "length": 15,
                        "length2": 15,
                        "smooth": false,
                        "minTurnAngle": 90,
                        "maxSurfaceAngle": 90
                    },
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                }
            ],
            "title": [
                {
                    "show": true,
                    "text": "\u4e09\u7c7b\u4ea7\u4e1a\u5360\u6bd4",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "left",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "fontSize": 50
                    }
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
                    "fontSize": 14
                },
                "borderWidth": 0,
                "padding": 5,
                "order": "seriesAsc"
            }
        },
        {
            "series": [
                {
                    "type": "pie",
                    "colorBy": "data",
                    "legendHoverLink": true,
                    "selectedMode": false,
                    "selectedOffset": 10,
                    "clockwise": true,
                    "startAngle": 90,
                    "minAngle": 0,
                    "minShowLabelAngle": 0,
                    "avoidLabelOverlap": true,
                    "stillShowZeroSum": true,
                    "percentPrecision": 2,
                    "showEmptyCircle": true,
                    "emptyCircleStyle": {
                        "color": "lightgray",
                        "borderColor": "#000",
                        "borderWidth": 0,
                        "borderType": "solid",
                        "borderDashOffset": 0,
                        "borderCap": "butt",
                        "borderJoin": "bevel",
                        "borderMiterLimit": 10,
                        "opacity": 1
                    },
                    "data": [
                        {
                            "name": "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 4
                        },
                        {
                            "name": "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 49
                        },
                        {
                            "name": "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 45
                        }
                    ],
                    "radius": [
                        "25%",
                        "75%"
                    ],
                    "center": [
                        "50%",
                        "50%"
                    ],
                    "roseType": "radius",
                    "label": {
                        "show": true,
                        "margin": 8,
                        "fontSize": 30,
                        "formatter": "{b}:{d}%"
                    },
                    "labelLine": {
                        "show": true,
                        "showAbove": false,
                        "length": 15,
                        "length2": 15,
                        "smooth": false,
                        "minTurnAngle": 90,
                        "maxSurfaceAngle": 90
                    },
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                }
            ],
            "title": [
                {
                    "show": true,
                    "text": "\u4e09\u7c7b\u4ea7\u4e1a\u5360\u6bd4",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "left",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "fontSize": 50
                    }
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
                    "fontSize": 14
                },
                "borderWidth": 0,
                "padding": 5,
                "order": "seriesAsc"
            }
        },
        {
            "series": [
                {
                    "type": "pie",
                    "colorBy": "data",
                    "legendHoverLink": true,
                    "selectedMode": false,
                    "selectedOffset": 10,
                    "clockwise": true,
                    "startAngle": 90,
                    "minAngle": 0,
                    "minShowLabelAngle": 0,
                    "avoidLabelOverlap": true,
                    "stillShowZeroSum": true,
                    "percentPrecision": 2,
                    "showEmptyCircle": true,
                    "emptyCircleStyle": {
                        "color": "lightgray",
                        "borderColor": "#000",
                        "borderWidth": 0,
                        "borderType": "solid",
                        "borderDashOffset": 0,
                        "borderCap": "butt",
                        "borderJoin": "bevel",
                        "borderMiterLimit": 10,
                        "opacity": 1
                    },
                    "data": [
                        {
                            "name": "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 2
                        },
                        {
                            "name": "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 50
                        },
                        {
                            "name": "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 47
                        }
                    ],
                    "radius": [
                        "25%",
                        "75%"
                    ],
                    "center": [
                        "50%",
                        "50%"
                    ],
                    "roseType": "radius",
                    "label": {
                        "show": true,
                        "margin": 8,
                        "fontSize": 30,
                        "formatter": "{b}:{d}%"
                    },
                    "labelLine": {
                        "show": true,
                        "showAbove": false,
                        "length": 15,
                        "length2": 15,
                        "smooth": false,
                        "minTurnAngle": 90,
                        "maxSurfaceAngle": 90
                    },
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                }
            ],
            "title": [
                {
                    "show": true,
                    "text": "\u4e09\u7c7b\u4ea7\u4e1a\u5360\u6bd4",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "left",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "fontSize": 50
                    }
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
                    "fontSize": 14
                },
                "borderWidth": 0,
                "padding": 5,
                "order": "seriesAsc"
            }
        },
        {
            "series": [
                {
                    "type": "pie",
                    "colorBy": "data",
                    "legendHoverLink": true,
                    "selectedMode": false,
                    "selectedOffset": 10,
                    "clockwise": true,
                    "startAngle": 90,
                    "minAngle": 0,
                    "minShowLabelAngle": 0,
                    "avoidLabelOverlap": true,
                    "stillShowZeroSum": true,
                    "percentPrecision": 2,
                    "showEmptyCircle": true,
                    "emptyCircleStyle": {
                        "color": "lightgray",
                        "borderColor": "#000",
                        "borderWidth": 0,
                        "borderType": "solid",
                        "borderDashOffset": 0,
                        "borderCap": "butt",
                        "borderJoin": "bevel",
                        "borderMiterLimit": 10,
                        "opacity": 1
                    },
                    "data": [
                        {
                            "name": "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 5
                        },
                        {
                            "name": "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 48
                        },
                        {
                            "name": "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 46
                        }
                    ],
                    "radius": [
                        "25%",
                        "75%"
                    ],
                    "center": [
                        "50%",
                        "50%"
                    ],
                    "roseType": "radius",
                    "label": {
                        "show": true,
                        "margin": 8,
                        "fontSize": 30,
                        "formatter": "{b}:{d}%"
                    },
                    "labelLine": {
                        "show": true,
                        "showAbove": false,
                        "length": 15,
                        "length2": 15,
                        "smooth": false,
                        "minTurnAngle": 90,
                        "maxSurfaceAngle": 90
                    },
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                }
            ],
            "title": [
                {
                    "show": true,
                    "text": "\u4e09\u7c7b\u4ea7\u4e1a\u5360\u6bd4",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "left",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "fontSize": 50
                    }
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
                    "fontSize": 14
                },
                "borderWidth": 0,
                "padding": 5,
                "order": "seriesAsc"
            }
        },
        {
            "series": [
                {
                    "type": "pie",
                    "colorBy": "data",
                    "legendHoverLink": true,
                    "selectedMode": false,
                    "selectedOffset": 10,
                    "clockwise": true,
                    "startAngle": 90,
                    "minAngle": 0,
                    "minShowLabelAngle": 0,
                    "avoidLabelOverlap": true,
                    "stillShowZeroSum": true,
                    "percentPrecision": 2,
                    "showEmptyCircle": true,
                    "emptyCircleStyle": {
                        "color": "lightgray",
                        "borderColor": "#000",
                        "borderWidth": 0,
                        "borderType": "solid",
                        "borderDashOffset": 0,
                        "borderCap": "butt",
                        "borderJoin": "bevel",
                        "borderMiterLimit": 10,
                        "opacity": 1
                    },
                    "data": [
                        {
                            "name": "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 4
                        },
                        {
                            "name": "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 52
                        },
                        {
                            "name": "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 43
                        }
                    ],
                    "radius": [
                        "25%",
                        "75%"
                    ],
                    "center": [
                        "50%",
                        "50%"
                    ],
                    "roseType": "radius",
                    "label": {
                        "show": true,
                        "margin": 8,
                        "fontSize": 30,
                        "formatter": "{b}:{d}%"
                    },
                    "labelLine": {
                        "show": true,
                        "showAbove": false,
                        "length": 15,
                        "length2": 15,
                        "smooth": false,
                        "minTurnAngle": 90,
                        "maxSurfaceAngle": 90
                    },
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                }
            ],
            "title": [
                {
                    "show": true,
                    "text": "\u4e09\u7c7b\u4ea7\u4e1a\u5360\u6bd4",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "left",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "fontSize": 50
                    }
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
                    "fontSize": 14
                },
                "borderWidth": 0,
                "padding": 5,
                "order": "seriesAsc"
            }
        },
        {
            "series": [
                {
                    "type": "pie",
                    "colorBy": "data",
                    "legendHoverLink": true,
                    "selectedMode": false,
                    "selectedOffset": 10,
                    "clockwise": true,
                    "startAngle": 90,
                    "minAngle": 0,
                    "minShowLabelAngle": 0,
                    "avoidLabelOverlap": true,
                    "stillShowZeroSum": true,
                    "percentPrecision": 2,
                    "showEmptyCircle": true,
                    "emptyCircleStyle": {
                        "color": "lightgray",
                        "borderColor": "#000",
                        "borderWidth": 0,
                        "borderType": "solid",
                        "borderDashOffset": 0,
                        "borderCap": "butt",
                        "borderJoin": "bevel",
                        "borderMiterLimit": 10,
                        "opacity": 1
                    },
                    "data": [
                        {
                            "name": "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 3
                        },
                        {
                            "name": "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 57
                        },
                        {
                            "name": "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 39
                        }
                    ],
                    "radius": [
                        "25%",
                        "75%"
                    ],
                    "center": [
                        "50%",
                        "50%"
                    ],
                    "roseType": "radius",
                    "label": {
                        "show": true,
                        "margin": 8,
                        "fontSize": 30,
                        "formatter": "{b}:{d}%"
                    },
                    "labelLine": {
                        "show": true,
                        "showAbove": false,
                        "length": 15,
                        "length2": 15,
                        "smooth": false,
                        "minTurnAngle": 90,
                        "maxSurfaceAngle": 90
                    },
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                }
            ],
            "title": [
                {
                    "show": true,
                    "text": "\u4e09\u7c7b\u4ea7\u4e1a\u5360\u6bd4",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "left",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "fontSize": 50
                    }
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
                    "fontSize": 14
                },
                "borderWidth": 0,
                "padding": 5,
                "order": "seriesAsc"
            }
        },
        {
            "series": [
                {
                    "type": "pie",
                    "colorBy": "data",
                    "legendHoverLink": true,
                    "selectedMode": false,
                    "selectedOffset": 10,
                    "clockwise": true,
                    "startAngle": 90,
                    "minAngle": 0,
                    "minShowLabelAngle": 0,
                    "avoidLabelOverlap": true,
                    "stillShowZeroSum": true,
                    "percentPrecision": 2,
                    "showEmptyCircle": true,
                    "emptyCircleStyle": {
                        "color": "lightgray",
                        "borderColor": "#000",
                        "borderWidth": 0,
                        "borderType": "solid",
                        "borderDashOffset": 0,
                        "borderCap": "butt",
                        "borderJoin": "bevel",
                        "borderMiterLimit": 10,
                        "opacity": 1
                    },
                    "data": [
                        {
                            "name": "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 4
                        },
                        {
                            "name": "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 52
                        },
                        {
                            "name": "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 43
                        }
                    ],
                    "radius": [
                        "25%",
                        "75%"
                    ],
                    "center": [
                        "50%",
                        "50%"
                    ],
                    "roseType": "radius",
                    "label": {
                        "show": true,
                        "margin": 8,
                        "fontSize": 30,
                        "formatter": "{b}:{d}%"
                    },
                    "labelLine": {
                        "show": true,
                        "showAbove": false,
                        "length": 15,
                        "length2": 15,
                        "smooth": false,
                        "minTurnAngle": 90,
                        "maxSurfaceAngle": 90
                    },
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                }
            ],
            "title": [
                {
                    "show": true,
                    "text": "\u4e09\u7c7b\u4ea7\u4e1a\u5360\u6bd4",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "left",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "fontSize": 50
                    }
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
                    "fontSize": 14
                },
                "borderWidth": 0,
                "padding": 5,
                "order": "seriesAsc"
            }
        },
        {
            "series": [
                {
                    "type": "pie",
                    "colorBy": "data",
                    "legendHoverLink": true,
                    "selectedMode": false,
                    "selectedOffset": 10,
                    "clockwise": true,
                    "startAngle": 90,
                    "minAngle": 0,
                    "minShowLabelAngle": 0,
                    "avoidLabelOverlap": true,
                    "stillShowZeroSum": true,
                    "percentPrecision": 2,
                    "showEmptyCircle": true,
                    "emptyCircleStyle": {
                        "color": "lightgray",
                        "borderColor": "#000",
                        "borderWidth": 0,
                        "borderType": "solid",
                        "borderDashOffset": 0,
                        "borderCap": "butt",
                        "borderJoin": "bevel",
                        "borderMiterLimit": 10,
                        "opacity": 1
                    },
                    "data": [
                        {
                            "name": "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 5
                        },
                        {
                            "name": "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 50
                        },
                        {
                            "name": "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 45
                        }
                    ],
                    "radius": [
                        "25%",
                        "75%"
                    ],
                    "center": [
                        "50%",
                        "50%"
                    ],
                    "roseType": "radius",
                    "label": {
                        "show": true,
                        "margin": 8,
                        "fontSize": 30,
                        "formatter": "{b}:{d}%"
                    },
                    "labelLine": {
                        "show": true,
                        "showAbove": false,
                        "length": 15,
                        "length2": 15,
                        "smooth": false,
                        "minTurnAngle": 90,
                        "maxSurfaceAngle": 90
                    },
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                }
            ],
            "title": [
                {
                    "show": true,
                    "text": "\u4e09\u7c7b\u4ea7\u4e1a\u5360\u6bd4",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "left",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "fontSize": 50
                    }
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
                    "fontSize": 14
                },
                "borderWidth": 0,
                "padding": 5,
                "order": "seriesAsc"
            }
        },
        {
            "series": [
                {
                    "type": "pie",
                    "colorBy": "data",
                    "legendHoverLink": true,
                    "selectedMode": false,
                    "selectedOffset": 10,
                    "clockwise": true,
                    "startAngle": 90,
                    "minAngle": 0,
                    "minShowLabelAngle": 0,
                    "avoidLabelOverlap": true,
                    "stillShowZeroSum": true,
                    "percentPrecision": 2,
                    "showEmptyCircle": true,
                    "emptyCircleStyle": {
                        "color": "lightgray",
                        "borderColor": "#000",
                        "borderWidth": 0,
                        "borderType": "solid",
                        "borderDashOffset": 0,
                        "borderCap": "butt",
                        "borderJoin": "bevel",
                        "borderMiterLimit": 10,
                        "opacity": 1
                    },
                    "data": [
                        {
                            "name": "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 4
                        },
                        {
                            "name": "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 48
                        },
                        {
                            "name": "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 47
                        }
                    ],
                    "radius": [
                        "25%",
                        "75%"
                    ],
                    "center": [
                        "50%",
                        "50%"
                    ],
                    "roseType": "radius",
                    "label": {
                        "show": true,
                        "margin": 8,
                        "fontSize": 30,
                        "formatter": "{b}:{d}%"
                    },
                    "labelLine": {
                        "show": true,
                        "showAbove": false,
                        "length": 15,
                        "length2": 15,
                        "smooth": false,
                        "minTurnAngle": 90,
                        "maxSurfaceAngle": 90
                    },
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                }
            ],
            "title": [
                {
                    "show": true,
                    "text": "\u4e09\u7c7b\u4ea7\u4e1a\u5360\u6bd4",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "left",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "fontSize": 50
                    }
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
                    "fontSize": 14
                },
                "borderWidth": 0,
                "padding": 5,
                "order": "seriesAsc"
            }
        },
        {
            "series": [
                {
                    "type": "pie",
                    "colorBy": "data",
                    "legendHoverLink": true,
                    "selectedMode": false,
                    "selectedOffset": 10,
                    "clockwise": true,
                    "startAngle": 90,
                    "minAngle": 0,
                    "minShowLabelAngle": 0,
                    "avoidLabelOverlap": true,
                    "stillShowZeroSum": true,
                    "percentPrecision": 2,
                    "showEmptyCircle": true,
                    "emptyCircleStyle": {
                        "color": "lightgray",
                        "borderColor": "#000",
                        "borderWidth": 0,
                        "borderType": "solid",
                        "borderDashOffset": 0,
                        "borderCap": "butt",
                        "borderJoin": "bevel",
                        "borderMiterLimit": 10,
                        "opacity": 1
                    },
                    "data": [
                        {
                            "name": "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 4
                        },
                        {
                            "name": "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 45
                        },
                        {
                            "name": "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 49
                        }
                    ],
                    "radius": [
                        "25%",
                        "75%"
                    ],
                    "center": [
                        "50%",
                        "50%"
                    ],
                    "roseType": "radius",
                    "label": {
                        "show": true,
                        "margin": 8,
                        "fontSize": 30,
                        "formatter": "{b}:{d}%"
                    },
                    "labelLine": {
                        "show": true,
                        "showAbove": false,
                        "length": 15,
                        "length2": 15,
                        "smooth": false,
                        "minTurnAngle": 90,
                        "maxSurfaceAngle": 90
                    },
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                }
            ],
            "title": [
                {
                    "show": true,
                    "text": "\u4e09\u7c7b\u4ea7\u4e1a\u5360\u6bd4",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "left",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "fontSize": 50
                    }
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
                    "fontSize": 14
                },
                "borderWidth": 0,
                "padding": 5,
                "order": "seriesAsc"
            }
        },
        {
            "series": [
                {
                    "type": "pie",
                    "colorBy": "data",
                    "legendHoverLink": true,
                    "selectedMode": false,
                    "selectedOffset": 10,
                    "clockwise": true,
                    "startAngle": 90,
                    "minAngle": 0,
                    "minShowLabelAngle": 0,
                    "avoidLabelOverlap": true,
                    "stillShowZeroSum": true,
                    "percentPrecision": 2,
                    "showEmptyCircle": true,
                    "emptyCircleStyle": {
                        "color": "lightgray",
                        "borderColor": "#000",
                        "borderWidth": 0,
                        "borderType": "solid",
                        "borderDashOffset": 0,
                        "borderCap": "butt",
                        "borderJoin": "bevel",
                        "borderMiterLimit": 10,
                        "opacity": 1
                    },
                    "data": [
                        {
                            "name": "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 4
                        },
                        {
                            "name": "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 39
                        },
                        {
                            "name": "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 55
                        }
                    ],
                    "radius": [
                        "25%",
                        "75%"
                    ],
                    "center": [
                        "50%",
                        "50%"
                    ],
                    "roseType": "radius",
                    "label": {
                        "show": true,
                        "margin": 8,
                        "fontSize": 30,
                        "formatter": "{b}:{d}%"
                    },
                    "labelLine": {
                        "show": true,
                        "showAbove": false,
                        "length": 15,
                        "length2": 15,
                        "smooth": false,
                        "minTurnAngle": 90,
                        "maxSurfaceAngle": 90
                    },
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                }
            ],
            "title": [
                {
                    "show": true,
                    "text": "\u4e09\u7c7b\u4ea7\u4e1a\u5360\u6bd4",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "left",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "fontSize": 50
                    }
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
                    "fontSize": 14
                },
                "borderWidth": 0,
                "padding": 5,
                "order": "seriesAsc"
            }
        },
        {
            "series": [
                {
                    "type": "pie",
                    "colorBy": "data",
                    "legendHoverLink": true,
                    "selectedMode": false,
                    "selectedOffset": 10,
                    "clockwise": true,
                    "startAngle": 90,
                    "minAngle": 0,
                    "minShowLabelAngle": 0,
                    "avoidLabelOverlap": true,
                    "stillShowZeroSum": true,
                    "percentPrecision": 2,
                    "showEmptyCircle": true,
                    "emptyCircleStyle": {
                        "color": "lightgray",
                        "borderColor": "#000",
                        "borderWidth": 0,
                        "borderType": "solid",
                        "borderDashOffset": 0,
                        "borderCap": "butt",
                        "borderJoin": "bevel",
                        "borderMiterLimit": 10,
                        "opacity": 1
                    },
                    "data": [
                        {
                            "name": "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 4
                        },
                        {
                            "name": "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 36
                        },
                        {
                            "name": "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 60
                        }
                    ],
                    "radius": [
                        "25%",
                        "75%"
                    ],
                    "center": [
                        "50%",
                        "50%"
                    ],
                    "roseType": "radius",
                    "label": {
                        "show": true,
                        "margin": 8,
                        "fontSize": 30,
                        "formatter": "{b}:{d}%"
                    },
                    "labelLine": {
                        "show": true,
                        "showAbove": false,
                        "length": 15,
                        "length2": 15,
                        "smooth": false,
                        "minTurnAngle": 90,
                        "maxSurfaceAngle": 90
                    },
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                }
            ],
            "title": [
                {
                    "show": true,
                    "text": "\u4e09\u7c7b\u4ea7\u4e1a\u5360\u6bd4",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "left",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "fontSize": 50
                    }
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
                    "fontSize": 14
                },
                "borderWidth": 0,
                "padding": 5,
                "order": "seriesAsc"
            }
        },
        {
            "series": [
                {
                    "type": "pie",
                    "colorBy": "data",
                    "legendHoverLink": true,
                    "selectedMode": false,
                    "selectedOffset": 10,
                    "clockwise": true,
                    "startAngle": 90,
                    "minAngle": 0,
                    "minShowLabelAngle": 0,
                    "avoidLabelOverlap": true,
                    "stillShowZeroSum": true,
                    "percentPrecision": 2,
                    "showEmptyCircle": true,
                    "emptyCircleStyle": {
                        "color": "lightgray",
                        "borderColor": "#000",
                        "borderWidth": 0,
                        "borderType": "solid",
                        "borderDashOffset": 0,
                        "borderCap": "butt",
                        "borderJoin": "bevel",
                        "borderMiterLimit": 10,
                        "opacity": 1
                    },
                    "data": [
                        {
                            "name": "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 4
                        },
                        {
                            "name": "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 34
                        },
                        {
                            "name": "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 61
                        }
                    ],
                    "radius": [
                        "25%",
                        "75%"
                    ],
                    "center": [
                        "50%",
                        "50%"
                    ],
                    "roseType": "radius",
                    "label": {
                        "show": true,
                        "margin": 8,
                        "fontSize": 30,
                        "formatter": "{b}:{d}%"
                    },
                    "labelLine": {
                        "show": true,
                        "showAbove": false,
                        "length": 15,
                        "length2": 15,
                        "smooth": false,
                        "minTurnAngle": 90,
                        "maxSurfaceAngle": 90
                    },
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                }
            ],
            "title": [
                {
                    "show": true,
                    "text": "\u4e09\u7c7b\u4ea7\u4e1a\u5360\u6bd4",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "left",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "fontSize": 50
                    }
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
                    "fontSize": 14
                },
                "borderWidth": 0,
                "padding": 5,
                "order": "seriesAsc"
            }
        },
        {
            "series": [
                {
                    "type": "pie",
                    "colorBy": "data",
                    "legendHoverLink": true,
                    "selectedMode": false,
                    "selectedOffset": 10,
                    "clockwise": true,
                    "startAngle": 90,
                    "minAngle": 0,
                    "minShowLabelAngle": 0,
                    "avoidLabelOverlap": true,
                    "stillShowZeroSum": true,
                    "percentPrecision": 2,
                    "showEmptyCircle": true,
                    "emptyCircleStyle": {
                        "color": "lightgray",
                        "borderColor": "#000",
                        "borderWidth": 0,
                        "borderType": "solid",
                        "borderDashOffset": 0,
                        "borderCap": "butt",
                        "borderJoin": "bevel",
                        "borderMiterLimit": 10,
                        "opacity": 1
                    },
                    "data": [
                        {
                            "name": "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 4
                        },
                        {
                            "name": "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 34
                        },
                        {
                            "name": "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 61
                        }
                    ],
                    "radius": [
                        "25%",
                        "75%"
                    ],
                    "center": [
                        "50%",
                        "50%"
                    ],
                    "roseType": "radius",
                    "label": {
                        "show": true,
                        "margin": 8,
                        "fontSize": 30,
                        "formatter": "{b}:{d}%"
                    },
                    "labelLine": {
                        "show": true,
                        "showAbove": false,
                        "length": 15,
                        "length2": 15,
                        "smooth": false,
                        "minTurnAngle": 90,
                        "maxSurfaceAngle": 90
                    },
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                }
            ],
            "title": [
                {
                    "show": true,
                    "text": "\u4e09\u7c7b\u4ea7\u4e1a\u5360\u6bd4",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "left",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "fontSize": 50
                    }
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
                    "fontSize": 14
                },
                "borderWidth": 0,
                "padding": 5,
                "order": "seriesAsc"
            }
        },
        {
            "series": [
                {
                    "type": "pie",
                    "colorBy": "data",
                    "legendHoverLink": true,
                    "selectedMode": false,
                    "selectedOffset": 10,
                    "clockwise": true,
                    "startAngle": 90,
                    "minAngle": 0,
                    "minShowLabelAngle": 0,
                    "avoidLabelOverlap": true,
                    "stillShowZeroSum": true,
                    "percentPrecision": 2,
                    "showEmptyCircle": true,
                    "emptyCircleStyle": {
                        "color": "lightgray",
                        "borderColor": "#000",
                        "borderWidth": 0,
                        "borderType": "solid",
                        "borderDashOffset": 0,
                        "borderCap": "butt",
                        "borderJoin": "bevel",
                        "borderMiterLimit": 10,
                        "opacity": 1
                    },
                    "data": [
                        {
                            "name": "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 3
                        },
                        {
                            "name": "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 32
                        },
                        {
                            "name": "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 63
                        }
                    ],
                    "radius": [
                        "25%",
                        "75%"
                    ],
                    "center": [
                        "50%",
                        "50%"
                    ],
                    "roseType": "radius",
                    "label": {
                        "show": true,
                        "margin": 8,
                        "fontSize": 30,
                        "formatter": "{b}:{d}%"
                    },
                    "labelLine": {
                        "show": true,
                        "showAbove": false,
                        "length": 15,
                        "length2": 15,
                        "smooth": false,
                        "minTurnAngle": 90,
                        "maxSurfaceAngle": 90
                    },
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                }
            ],
            "title": [
                {
                    "show": true,
                    "text": "\u4e09\u7c7b\u4ea7\u4e1a\u5360\u6bd4",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "left",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "fontSize": 50
                    }
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
                    "fontSize": 14
                },
                "borderWidth": 0,
                "padding": 5,
                "order": "seriesAsc"
            }
        },
        {
            "series": [
                {
                    "type": "pie",
                    "colorBy": "data",
                    "legendHoverLink": true,
                    "selectedMode": false,
                    "selectedOffset": 10,
                    "clockwise": true,
                    "startAngle": 90,
                    "minAngle": 0,
                    "minShowLabelAngle": 0,
                    "avoidLabelOverlap": true,
                    "stillShowZeroSum": true,
                    "percentPrecision": 2,
                    "showEmptyCircle": true,
                    "emptyCircleStyle": {
                        "color": "lightgray",
                        "borderColor": "#000",
                        "borderWidth": 0,
                        "borderType": "solid",
                        "borderDashOffset": 0,
                        "borderCap": "butt",
                        "borderJoin": "bevel",
                        "borderMiterLimit": 10,
                        "opacity": 1
                    },
                    "data": [
                        {
                            "name": "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 10
                        },
                        {
                            "name": "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 43
                        },
                        {
                            "name": "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 46
                        }
                    ],
                    "radius": [
                        "25%",
                        "75%"
                    ],
                    "center": [
                        "50%",
                        "50%"
                    ],
                    "roseType": "radius",
                    "label": {
                        "show": true,
                        "margin": 8,
                        "fontSize": 30,
                        "formatter": "{b}:{d}%"
                    },
                    "labelLine": {
                        "show": true,
                        "showAbove": false,
                        "length": 15,
                        "length2": 15,
                        "smooth": false,
                        "minTurnAngle": 90,
                        "maxSurfaceAngle": 90
                    },
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                }
            ],
            "title": [
                {
                    "show": true,
                    "text": "\u4e09\u7c7b\u4ea7\u4e1a\u5360\u6bd4",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "left",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "fontSize": 50
                    }
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
                    "fontSize": 14
                },
                "borderWidth": 0,
                "padding": 5,
                "order": "seriesAsc"
            }
        },
        {
            "series": [
                {
                    "type": "pie",
                    "colorBy": "data",
                    "legendHoverLink": true,
                    "selectedMode": false,
                    "selectedOffset": 10,
                    "clockwise": true,
                    "startAngle": 90,
                    "minAngle": 0,
                    "minShowLabelAngle": 0,
                    "avoidLabelOverlap": true,
                    "stillShowZeroSum": true,
                    "percentPrecision": 2,
                    "showEmptyCircle": true,
                    "emptyCircleStyle": {
                        "color": "lightgray",
                        "borderColor": "#000",
                        "borderWidth": 0,
                        "borderType": "solid",
                        "borderDashOffset": 0,
                        "borderCap": "butt",
                        "borderJoin": "bevel",
                        "borderMiterLimit": 10,
                        "opacity": 1
                    },
                    "data": [
                        {
                            "name": "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 6
                        },
                        {
                            "name": "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 38
                        },
                        {
                            "name": "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 54
                        }
                    ],
                    "radius": [
                        "25%",
                        "75%"
                    ],
                    "center": [
                        "50%",
                        "50%"
                    ],
                    "roseType": "radius",
                    "label": {
                        "show": true,
                        "margin": 8,
                        "fontSize": 30,
                        "formatter": "{b}:{d}%"
                    },
                    "labelLine": {
                        "show": true,
                        "showAbove": false,
                        "length": 15,
                        "length2": 15,
                        "smooth": false,
                        "minTurnAngle": 90,
                        "maxSurfaceAngle": 90
                    },
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                }
            ],
            "title": [
                {
                    "show": true,
                    "text": "\u4e09\u7c7b\u4ea7\u4e1a\u5360\u6bd4",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "left",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "fontSize": 50
                    }
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
                    "fontSize": 14
                },
                "borderWidth": 0,
                "padding": 5,
                "order": "seriesAsc"
            }
        },
        {
            "series": [
                {
                    "type": "pie",
                    "colorBy": "data",
                    "legendHoverLink": true,
                    "selectedMode": false,
                    "selectedOffset": 10,
                    "clockwise": true,
                    "startAngle": 90,
                    "minAngle": 0,
                    "minShowLabelAngle": 0,
                    "avoidLabelOverlap": true,
                    "stillShowZeroSum": true,
                    "percentPrecision": 2,
                    "showEmptyCircle": true,
                    "emptyCircleStyle": {
                        "color": "lightgray",
                        "borderColor": "#000",
                        "borderWidth": 0,
                        "borderType": "solid",
                        "borderDashOffset": 0,
                        "borderCap": "butt",
                        "borderJoin": "bevel",
                        "borderMiterLimit": 10,
                        "opacity": 1
                    },
                    "data": [
                        {
                            "name": "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 10
                        },
                        {
                            "name": "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 33
                        },
                        {
                            "name": "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 55
                        }
                    ],
                    "radius": [
                        "25%",
                        "75%"
                    ],
                    "center": [
                        "50%",
                        "50%"
                    ],
                    "roseType": "radius",
                    "label": {
                        "show": true,
                        "margin": 8,
                        "fontSize": 30,
                        "formatter": "{b}:{d}%"
                    },
                    "labelLine": {
                        "show": true,
                        "showAbove": false,
                        "length": 15,
                        "length2": 15,
                        "smooth": false,
                        "minTurnAngle": 90,
                        "maxSurfaceAngle": 90
                    },
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                }
            ],
            "title": [
                {
                    "show": true,
                    "text": "\u4e09\u7c7b\u4ea7\u4e1a\u5360\u6bd4",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "left",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "fontSize": 50
                    }
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
                    "fontSize": 14
                },
                "borderWidth": 0,
                "padding": 5,
                "order": "seriesAsc"
            }
        },
        {
            "series": [
                {
                    "type": "pie",
                    "colorBy": "data",
                    "legendHoverLink": true,
                    "selectedMode": false,
                    "selectedOffset": 10,
                    "clockwise": true,
                    "startAngle": 90,
                    "minAngle": 0,
                    "minShowLabelAngle": 0,
                    "avoidLabelOverlap": true,
                    "stillShowZeroSum": true,
                    "percentPrecision": 2,
                    "showEmptyCircle": true,
                    "emptyCircleStyle": {
                        "color": "lightgray",
                        "borderColor": "#000",
                        "borderWidth": 0,
                        "borderType": "solid",
                        "borderDashOffset": 0,
                        "borderCap": "butt",
                        "borderJoin": "bevel",
                        "borderMiterLimit": 10,
                        "opacity": 1
                    },
                    "data": [
                        {
                            "name": "\u7b2c\u4e00\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 5
                        },
                        {
                            "name": "\u7b2c\u4e8c\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 33
                        },
                        {
                            "name": "\u7b2c\u4e09\u4ea7\u4e1a\u5bf9GDP\u7684\u8d21\u732e\u7387(%)",
                            "value": 60
                        }
                    ],
                    "radius": [
                        "25%",
                        "75%"
                    ],
                    "center": [
                        "50%",
                        "50%"
                    ],
                    "roseType": "radius",
                    "label": {
                        "show": true,
                        "margin": 8,
                        "fontSize": 30,
                        "formatter": "{b}:{d}%"
                    },
                    "labelLine": {
                        "show": true,
                        "showAbove": false,
                        "length": 15,
                        "length2": 15,
                        "smooth": false,
                        "minTurnAngle": 90,
                        "maxSurfaceAngle": 90
                    },
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                }
            ],
            "title": [
                {
                    "show": true,
                    "text": "\u4e09\u7c7b\u4ea7\u4e1a\u5360\u6bd4",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "left",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "fontSize": 50
                    }
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
                    "fontSize": 14
                },
                "borderWidth": 0,
                "padding": 5,
                "order": "seriesAsc"
            }
        }
    ]
};
        chart_4ecfbf0d124e43ef8c05bad3a8af3251.setOption(option_4ecfbf0d124e43ef8c05bad3a8af3251);
    </script>
</body>
</html>

"""
components.html(html_content,height=1500, width=2000)



st.sidebar.header("绘图演示")