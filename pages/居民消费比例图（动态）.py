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
    <div id="e17017d929f646359e15dcb028f700f4" class="chart-container" style="width: 1500px; height:850px; "></div>
    <script>
        var chart_e17017d929f646359e15dcb028f700f4 = echarts.init(
            document.getElementById('e17017d929f646359e15dcb028f700f4'), 'light', {renderer: 'canvas'});
        var option_e17017d929f646359e15dcb028f700f4 = {
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
                        "name": "\u5c45\u6c11\u4eba\u5747\u670d\u52a1\u6027\u6d88\u8d39\u652f\u51fa(\u5143)",
                        "value": 12114
                    },
                    {
                        "name": "\u5c45\u6c11\u4eba\u5747\u98df\u54c1\u70df\u9152\u652f\u51fa(\u5143)",
                        "value": 7983
                    },
                    {
                        "name": "\u5c45\u6c11\u4eba\u5747\u8863\u7740\u652f\u51fa(\u5143)",
                        "value": 1479
                    },
                    {
                        "name": "\u5c45\u6c11\u4eba\u5747\u5c45\u4f4f\u652f\u51fa(\u5143)",
                        "value": 6095
                    },
                    {
                        "name": "\u5c45\u6c11\u4eba\u5747\u751f\u6d3b\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                        "value": 1526
                    },
                    {
                        "name": "\u5c45\u6c11\u4eba\u5747\u4ea4\u901a\u901a\u4fe1\u652f\u51fa(\u5143)",
                        "value": 3652
                    },
                    {
                        "name": "\u5c45\u6c11\u4eba\u5747\u6559\u80b2\u6587\u5316\u5a31\u4e50\u652f\u51fa(\u5143)",
                        "value": 2904
                    },
                    {
                        "name": "\u5c45\u6c11\u4eba\u5747\u533b\u7597\u4fdd\u5065\u652f\u51fa(\u5143)",
                        "value": 2460
                    },
                    {
                        "name": "\u5c45\u6c11\u4eba\u5747\u5176\u4ed6\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                        "value": 697
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
            "playInterval": 150,
            "bottom": "-5px",
            "progress": {},
            "data": [
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
        },
        "legend": [
            {
                "data": [
                    "\u5c45\u6c11\u4eba\u5747\u670d\u52a1\u6027\u6d88\u8d39\u652f\u51fa(\u5143)",
                    "\u5c45\u6c11\u4eba\u5747\u98df\u54c1\u70df\u9152\u652f\u51fa(\u5143)",
                    "\u5c45\u6c11\u4eba\u5747\u8863\u7740\u652f\u51fa(\u5143)",
                    "\u5c45\u6c11\u4eba\u5747\u5c45\u4f4f\u652f\u51fa(\u5143)",
                    "\u5c45\u6c11\u4eba\u5747\u751f\u6d3b\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                    "\u5c45\u6c11\u4eba\u5747\u4ea4\u901a\u901a\u4fe1\u652f\u51fa(\u5143)",
                    "\u5c45\u6c11\u4eba\u5747\u6559\u80b2\u6587\u5316\u5a31\u4e50\u652f\u51fa(\u5143)",
                    "\u5c45\u6c11\u4eba\u5747\u533b\u7597\u4fdd\u5065\u652f\u51fa(\u5143)",
                    "\u5c45\u6c11\u4eba\u5747\u5176\u4ed6\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)"
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
                            "name": "\u5c45\u6c11\u4eba\u5747\u670d\u52a1\u6027\u6d88\u8d39\u652f\u51fa(\u5143)",
                            "value": 0
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u98df\u54c1\u70df\u9152\u652f\u51fa(\u5143)",
                            "value": 1208
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u8863\u7740\u652f\u51fa(\u5143)",
                            "value": 225
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5c45\u4f4f\u652f\u51fa(\u5143)",
                            "value": 307
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u751f\u6d3b\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 174
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u4ea4\u901a\u901a\u4fe1\u652f\u51fa(\u5143)",
                            "value": 109
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u6559\u80b2\u6587\u5316\u5a31\u4e50\u652f\u51fa(\u5143)",
                            "value": 195
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u533b\u7597\u4fdd\u5065\u652f\u51fa(\u5143)",
                            "value": 213
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5176\u4ed6\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 86
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
                    "text": "\u5c45\u6c11\u6d88\u8d39\u5360\u6bd4",
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
                            "name": "\u5c45\u6c11\u4eba\u5747\u670d\u52a1\u6027\u6d88\u8d39\u652f\u51fa(\u5143)",
                            "value": 0
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u98df\u54c1\u70df\u9152\u652f\u51fa(\u5143)",
                            "value": 1210
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u8863\u7740\u652f\u51fa(\u5143)",
                            "value": 225
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5c45\u4f4f\u652f\u51fa(\u5143)",
                            "value": 335
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u751f\u6d3b\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 192
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u4ea4\u901a\u901a\u4fe1\u652f\u51fa(\u5143)",
                            "value": 130
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u6559\u80b2\u6587\u5316\u5a31\u4e50\u652f\u51fa(\u5143)",
                            "value": 223
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u533b\u7597\u4fdd\u5065\u652f\u51fa(\u5143)",
                            "value": 245
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5176\u4ed6\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 98
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
                    "text": "\u5c45\u6c11\u6d88\u8d39\u5360\u6bd4",
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
                            "name": "\u5c45\u6c11\u4eba\u5747\u670d\u52a1\u6027\u6d88\u8d39\u652f\u51fa(\u5143)",
                            "value": 0
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u98df\u54c1\u70df\u9152\u652f\u51fa(\u5143)",
                            "value": 1231
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u8863\u7740\u652f\u51fa(\u5143)",
                            "value": 238
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5c45\u4f4f\u652f\u51fa(\u5143)",
                            "value": 419
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u751f\u6d3b\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 184
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u4ea4\u901a\u901a\u4fe1\u652f\u51fa(\u5143)",
                            "value": 211
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u6559\u80b2\u6587\u5316\u5a31\u4e50\u652f\u51fa(\u5143)",
                            "value": 366
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u533b\u7597\u4fdd\u5065\u652f\u51fa(\u5143)",
                            "value": 173
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5176\u4ed6\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 91
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
                    "text": "\u5c45\u6c11\u6d88\u8d39\u5360\u6bd4",
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
                            "name": "\u5c45\u6c11\u4eba\u5747\u670d\u52a1\u6027\u6d88\u8d39\u652f\u51fa(\u5143)",
                            "value": 0
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u98df\u54c1\u70df\u9152\u652f\u51fa(\u5143)",
                            "value": 1270
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u8863\u7740\u652f\u51fa(\u5143)",
                            "value": 256
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5c45\u4f4f\u652f\u51fa(\u5143)",
                            "value": 448
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u751f\u6d3b\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 214
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u4ea4\u901a\u901a\u4fe1\u652f\u51fa(\u5143)",
                            "value": 237
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u6559\u80b2\u6587\u5316\u5a31\u4e50\u652f\u51fa(\u5143)",
                            "value": 387
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u533b\u7597\u4fdd\u5065\u652f\u51fa(\u5143)",
                            "value": 193
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5176\u4ed6\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 132
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
                    "text": "\u5c45\u6c11\u6d88\u8d39\u5360\u6bd4",
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
                            "name": "\u5c45\u6c11\u4eba\u5747\u670d\u52a1\u6027\u6d88\u8d39\u652f\u51fa(\u5143)",
                            "value": 0
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u98df\u54c1\u70df\u9152\u652f\u51fa(\u5143)",
                            "value": 1391
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u8863\u7740\u652f\u51fa(\u5143)",
                            "value": 285
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5c45\u4f4f\u652f\u51fa(\u5143)",
                            "value": 527
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u751f\u6d3b\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 202
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u4ea4\u901a\u901a\u4fe1\u652f\u51fa(\u5143)",
                            "value": 315
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u6559\u80b2\u6587\u5316\u5a31\u4e50\u652f\u51fa(\u5143)",
                            "value": 487
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u533b\u7597\u4fdd\u5065\u652f\u51fa(\u5143)",
                            "value": 237
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5176\u4ed6\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 103
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
                    "text": "\u5c45\u6c11\u6d88\u8d39\u5360\u6bd4",
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
                            "name": "\u5c45\u6c11\u4eba\u5747\u670d\u52a1\u6027\u6d88\u8d39\u652f\u51fa(\u5143)",
                            "value": 0
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u98df\u54c1\u70df\u9152\u652f\u51fa(\u5143)",
                            "value": 1483
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u8863\u7740\u652f\u51fa(\u5143)",
                            "value": 310
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5c45\u4f4f\u652f\u51fa(\u5143)",
                            "value": 606
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u751f\u6d3b\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 215
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u4ea4\u901a\u901a\u4fe1\u652f\u51fa(\u5143)",
                            "value": 378
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u6559\u80b2\u6587\u5316\u5a31\u4e50\u652f\u51fa(\u5143)",
                            "value": 527
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u533b\u7597\u4fdd\u5065\u652f\u51fa(\u5143)",
                            "value": 268
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5176\u4ed6\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 102
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
                    "text": "\u5c45\u6c11\u6d88\u8d39\u5360\u6bd4",
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
                            "name": "\u5c45\u6c11\u4eba\u5747\u670d\u52a1\u6027\u6d88\u8d39\u652f\u51fa(\u5143)",
                            "value": 0
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u98df\u54c1\u70df\u9152\u652f\u51fa(\u5143)",
                            "value": 1704
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u8863\u7740\u652f\u51fa(\u5143)",
                            "value": 339
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5c45\u4f4f\u652f\u51fa(\u5143)",
                            "value": 674
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u751f\u6d3b\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 224
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u4ea4\u901a\u901a\u4fe1\u652f\u51fa(\u5143)",
                            "value": 450
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u6559\u80b2\u6587\u5316\u5a31\u4e50\u652f\u51fa(\u5143)",
                            "value": 586
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u533b\u7597\u4fdd\u5065\u652f\u51fa(\u5143)",
                            "value": 305
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5176\u4ed6\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 114
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
                    "text": "\u5c45\u6c11\u6d88\u8d39\u5360\u6bd4",
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
                            "name": "\u5c45\u6c11\u4eba\u5747\u670d\u52a1\u6027\u6d88\u8d39\u652f\u51fa(\u5143)",
                            "value": 0
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u98df\u54c1\u70df\u9152\u652f\u51fa(\u5143)",
                            "value": 1877
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u8863\u7740\u652f\u51fa(\u5143)",
                            "value": 404
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5c45\u4f4f\u652f\u51fa(\u5143)",
                            "value": 796
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u751f\u6d3b\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 258
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u4ea4\u901a\u901a\u4fe1\u652f\u51fa(\u5143)",
                            "value": 547
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u6559\u80b2\u6587\u5316\u5a31\u4e50\u652f\u51fa(\u5143)",
                            "value": 657
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u533b\u7597\u4fdd\u5065\u652f\u51fa(\u5143)",
                            "value": 366
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5176\u4ed6\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 131
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
                    "text": "\u5c45\u6c11\u6d88\u8d39\u5360\u6bd4",
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
                            "name": "\u5c45\u6c11\u4eba\u5747\u670d\u52a1\u6027\u6d88\u8d39\u652f\u51fa(\u5143)",
                            "value": 0
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u98df\u54c1\u70df\u9152\u652f\u51fa(\u5143)",
                            "value": 2002
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u8863\u7740\u652f\u51fa(\u5143)",
                            "value": 459
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5c45\u4f4f\u652f\u51fa(\u5143)",
                            "value": 980
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u751f\u6d3b\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 293
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u4ea4\u901a\u901a\u4fe1\u652f\u51fa(\u5143)",
                            "value": 640
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u6559\u80b2\u6587\u5316\u5a31\u4e50\u652f\u51fa(\u5143)",
                            "value": 718
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u533b\u7597\u4fdd\u5065\u652f\u51fa(\u5143)",
                            "value": 395
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5176\u4ed6\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 146
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
                    "text": "\u5c45\u6c11\u6d88\u8d39\u5360\u6bd4",
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
                            "name": "\u5c45\u6c11\u4eba\u5747\u670d\u52a1\u6027\u6d88\u8d39\u652f\u51fa(\u5143)",
                            "value": 0
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u98df\u54c1\u70df\u9152\u652f\u51fa(\u5143)",
                            "value": 2346
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u8863\u7740\u652f\u51fa(\u5143)",
                            "value": 539
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5c45\u4f4f\u652f\u51fa(\u5143)",
                            "value": 1176
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u751f\u6d3b\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 359
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u4ea4\u901a\u901a\u4fe1\u652f\u51fa(\u5143)",
                            "value": 762
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u6559\u80b2\u6587\u5316\u5a31\u4e50\u652f\u51fa(\u5143)",
                            "value": 787
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u533b\u7597\u4fdd\u5065\u652f\u51fa(\u5143)",
                            "value": 452
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5176\u4ed6\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 170
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
                    "text": "\u5c45\u6c11\u6d88\u8d39\u5360\u6bd4",
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
                            "name": "\u5c45\u6c11\u4eba\u5747\u670d\u52a1\u6027\u6d88\u8d39\u652f\u51fa(\u5143)",
                            "value": 0
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u98df\u54c1\u70df\u9152\u652f\u51fa(\u5143)",
                            "value": 2741
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u8863\u7740\u652f\u51fa(\u5143)",
                            "value": 601
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5c45\u4f4f\u652f\u51fa(\u5143)",
                            "value": 1454
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u751f\u6d3b\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 418
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u4ea4\u901a\u901a\u4fe1\u652f\u51fa(\u5143)",
                            "value": 808
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u6559\u80b2\u6587\u5316\u5a31\u4e50\u652f\u51fa(\u5143)",
                            "value": 814
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u533b\u7597\u4fdd\u5065\u652f\u51fa(\u5143)",
                            "value": 519
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5176\u4ed6\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 193
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
                    "text": "\u5c45\u6c11\u6d88\u8d39\u5360\u6bd4",
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
                            "name": "\u5c45\u6c11\u4eba\u5747\u670d\u52a1\u6027\u6d88\u8d39\u652f\u51fa(\u5143)",
                            "value": 0
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u98df\u54c1\u70df\u9152\u652f\u51fa(\u5143)",
                            "value": 2875
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u8863\u7740\u652f\u51fa(\u5143)",
                            "value": 666
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5c45\u4f4f\u652f\u51fa(\u5143)",
                            "value": 1698
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u751f\u6d3b\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 486
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u4ea4\u901a\u901a\u4fe1\u652f\u51fa(\u5143)",
                            "value": 953
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u6559\u80b2\u6587\u5316\u5a31\u4e50\u652f\u51fa(\u5143)",
                            "value": 896
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u533b\u7597\u4fdd\u5065\u652f\u51fa(\u5143)",
                            "value": 586
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5176\u4ed6\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 216
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
                    "text": "\u5c45\u6c11\u6d88\u8d39\u5360\u6bd4",
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
                            "name": "\u5c45\u6c11\u4eba\u5747\u670d\u52a1\u6027\u6d88\u8d39\u652f\u51fa(\u5143)",
                            "value": 0
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u98df\u54c1\u70df\u9152\u652f\u51fa(\u5143)",
                            "value": 3137
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u8863\u7740\u652f\u51fa(\u5143)",
                            "value": 759
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5c45\u4f4f\u652f\u51fa(\u5143)",
                            "value": 1928
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u751f\u6d3b\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 569
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u4ea4\u901a\u901a\u4fe1\u652f\u51fa(\u5143)",
                            "value": 1130
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u6559\u80b2\u6587\u5316\u5a31\u4e50\u652f\u51fa(\u5143)",
                            "value": 1000
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u533b\u7597\u4fdd\u5065\u652f\u51fa(\u5143)",
                            "value": 625
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5176\u4ed6\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 231
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
                    "text": "\u5c45\u6c11\u6d88\u8d39\u5360\u6bd4",
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
                            "name": "\u5c45\u6c11\u4eba\u5747\u670d\u52a1\u6027\u6d88\u8d39\u652f\u51fa(\u5143)",
                            "value": 0
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u98df\u54c1\u70df\u9152\u652f\u51fa(\u5143)",
                            "value": 3633
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u8863\u7740\u652f\u51fa(\u5143)",
                            "value": 903
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5c45\u4f4f\u652f\u51fa(\u5143)",
                            "value": 2199
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u751f\u6d3b\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 675
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u4ea4\u901a\u901a\u4fe1\u652f\u51fa(\u5143)",
                            "value": 1259
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u6559\u80b2\u6587\u5316\u5a31\u4e50\u652f\u51fa(\u5143)",
                            "value": 1136
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u533b\u7597\u4fdd\u5065\u652f\u51fa(\u5143)",
                            "value": 744
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5176\u4ed6\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 272
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
                    "text": "\u5c45\u6c11\u6d88\u8d39\u5360\u6bd4",
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
                            "name": "\u5c45\u6c11\u4eba\u5747\u670d\u52a1\u6027\u6d88\u8d39\u652f\u51fa(\u5143)",
                            "value": 0
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u98df\u54c1\u70df\u9152\u652f\u51fa(\u5143)",
                            "value": 3983
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u8863\u7740\u652f\u51fa(\u5143)",
                            "value": 992
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5c45\u4f4f\u652f\u51fa(\u5143)",
                            "value": 2480
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u751f\u6d3b\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 741
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u4ea4\u901a\u901a\u4fe1\u652f\u51fa(\u5143)",
                            "value": 1451
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u6559\u80b2\u6587\u5316\u5a31\u4e50\u652f\u51fa(\u5143)",
                            "value": 1262
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u533b\u7597\u4fdd\u5065\u652f\u51fa(\u5143)",
                            "value": 838
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5176\u4ed6\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 307
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
                    "text": "\u5c45\u6c11\u6d88\u8d39\u5360\u6bd4",
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
                            "name": "\u5c45\u6c11\u4eba\u5747\u670d\u52a1\u6027\u6d88\u8d39\u652f\u51fa(\u5143)",
                            "value": 5246
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u98df\u54c1\u70df\u9152\u652f\u51fa(\u5143)",
                            "value": 4127
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u8863\u7740\u652f\u51fa(\u5143)",
                            "value": 1027
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5c45\u4f4f\u652f\u51fa(\u5143)",
                            "value": 2999
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u751f\u6d3b\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 806
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u4ea4\u901a\u901a\u4fe1\u652f\u51fa(\u5143)",
                            "value": 1627
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u6559\u80b2\u6587\u5316\u5a31\u4e50\u652f\u51fa(\u5143)",
                            "value": 1398
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u533b\u7597\u4fdd\u5065\u652f\u51fa(\u5143)",
                            "value": 912
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5176\u4ed6\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 325
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
                    "text": "\u5c45\u6c11\u6d88\u8d39\u5360\u6bd4",
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
                            "name": "\u5c45\u6c11\u4eba\u5747\u670d\u52a1\u6027\u6d88\u8d39\u652f\u51fa(\u5143)",
                            "value": 5842
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u98df\u54c1\u70df\u9152\u652f\u51fa(\u5143)",
                            "value": 4494
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u8863\u7740\u652f\u51fa(\u5143)",
                            "value": 1099
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5c45\u4f4f\u652f\u51fa(\u5143)",
                            "value": 3201
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u751f\u6d3b\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 890
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u4ea4\u901a\u901a\u4fe1\u652f\u51fa(\u5143)",
                            "value": 1869
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u6559\u80b2\u6587\u5316\u5a31\u4e50\u652f\u51fa(\u5143)",
                            "value": 1536
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u533b\u7597\u4fdd\u5065\u652f\u51fa(\u5143)",
                            "value": 1045
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5176\u4ed6\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 358
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
                    "text": "\u5c45\u6c11\u6d88\u8d39\u5360\u6bd4",
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
                            "name": "\u5c45\u6c11\u4eba\u5747\u670d\u52a1\u6027\u6d88\u8d39\u652f\u51fa(\u5143)",
                            "value": 6460
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u98df\u54c1\u70df\u9152\u652f\u51fa(\u5143)",
                            "value": 4814
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u8863\u7740\u652f\u51fa(\u5143)",
                            "value": 1164
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5c45\u4f4f\u652f\u51fa(\u5143)",
                            "value": 3419
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u751f\u6d3b\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 951
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u4ea4\u901a\u901a\u4fe1\u652f\u51fa(\u5143)",
                            "value": 2087
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u6559\u80b2\u6587\u5316\u5a31\u4e50\u652f\u51fa(\u5143)",
                            "value": 1723
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u533b\u7597\u4fdd\u5065\u652f\u51fa(\u5143)",
                            "value": 1165
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5176\u4ed6\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 389
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
                    "text": "\u5c45\u6c11\u6d88\u8d39\u5360\u6bd4",
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
                            "name": "\u5c45\u6c11\u4eba\u5747\u670d\u52a1\u6027\u6d88\u8d39\u652f\u51fa(\u5143)",
                            "value": 7157
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u98df\u54c1\u70df\u9152\u652f\u51fa(\u5143)",
                            "value": 5151
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u8863\u7740\u652f\u51fa(\u5143)",
                            "value": 1203
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5c45\u4f4f\u652f\u51fa(\u5143)",
                            "value": 3746
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u751f\u6d3b\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 1044
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u4ea4\u901a\u901a\u4fe1\u652f\u51fa(\u5143)",
                            "value": 2338
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u6559\u80b2\u6587\u5316\u5a31\u4e50\u652f\u51fa(\u5143)",
                            "value": 1915
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u533b\u7597\u4fdd\u5065\u652f\u51fa(\u5143)",
                            "value": 1307
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5176\u4ed6\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 406
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
                    "text": "\u5c45\u6c11\u6d88\u8d39\u5360\u6bd4",
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
                            "name": "\u5c45\u6c11\u4eba\u5747\u670d\u52a1\u6027\u6d88\u8d39\u652f\u51fa(\u5143)",
                            "value": 7803
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u98df\u54c1\u70df\u9152\u652f\u51fa(\u5143)",
                            "value": 5374
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u8863\u7740\u652f\u51fa(\u5143)",
                            "value": 1238
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5c45\u4f4f\u652f\u51fa(\u5143)",
                            "value": 4107
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u751f\u6d3b\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 1121
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u4ea4\u901a\u901a\u4fe1\u652f\u51fa(\u5143)",
                            "value": 2499
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u6559\u80b2\u6587\u5316\u5a31\u4e50\u652f\u51fa(\u5143)",
                            "value": 2086
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u533b\u7597\u4fdd\u5065\u652f\u51fa(\u5143)",
                            "value": 1451
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5176\u4ed6\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 447
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
                    "text": "\u5c45\u6c11\u6d88\u8d39\u5360\u6bd4",
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
                            "name": "\u5c45\u6c11\u4eba\u5747\u670d\u52a1\u6027\u6d88\u8d39\u652f\u51fa(\u5143)",
                            "value": 8781
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u98df\u54c1\u70df\u9152\u652f\u51fa(\u5143)",
                            "value": 5631
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u8863\u7740\u652f\u51fa(\u5143)",
                            "value": 1289
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5c45\u4f4f\u652f\u51fa(\u5143)",
                            "value": 4647
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u751f\u6d3b\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 1223
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u4ea4\u901a\u901a\u4fe1\u652f\u51fa(\u5143)",
                            "value": 2675
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u6559\u80b2\u6587\u5316\u5a31\u4e50\u652f\u51fa(\u5143)",
                            "value": 2226
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u533b\u7597\u4fdd\u5065\u652f\u51fa(\u5143)",
                            "value": 1685
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5176\u4ed6\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 477
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
                    "text": "\u5c45\u6c11\u6d88\u8d39\u5360\u6bd4",
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
                            "name": "\u5c45\u6c11\u4eba\u5747\u670d\u52a1\u6027\u6d88\u8d39\u652f\u51fa(\u5143)",
                            "value": 9886
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u98df\u54c1\u70df\u9152\u652f\u51fa(\u5143)",
                            "value": 6084
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u8863\u7740\u652f\u51fa(\u5143)",
                            "value": 1338
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5c45\u4f4f\u652f\u51fa(\u5143)",
                            "value": 5055
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u751f\u6d3b\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 1281
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u4ea4\u901a\u901a\u4fe1\u652f\u51fa(\u5143)",
                            "value": 2862
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u6559\u80b2\u6587\u5316\u5a31\u4e50\u652f\u51fa(\u5143)",
                            "value": 2513
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u533b\u7597\u4fdd\u5065\u652f\u51fa(\u5143)",
                            "value": 1902
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5176\u4ed6\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 524
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
                    "text": "\u5c45\u6c11\u6d88\u8d39\u5360\u6bd4",
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
                            "name": "\u5c45\u6c11\u4eba\u5747\u670d\u52a1\u6027\u6d88\u8d39\u652f\u51fa(\u5143)",
                            "value": 9037
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u98df\u54c1\u70df\u9152\u652f\u51fa(\u5143)",
                            "value": 6397
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u8863\u7740\u652f\u51fa(\u5143)",
                            "value": 1238
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5c45\u4f4f\u652f\u51fa(\u5143)",
                            "value": 5215
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u751f\u6d3b\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 1260
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u4ea4\u901a\u901a\u4fe1\u652f\u51fa(\u5143)",
                            "value": 2762
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u6559\u80b2\u6587\u5316\u5a31\u4e50\u652f\u51fa(\u5143)",
                            "value": 2032
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u533b\u7597\u4fdd\u5065\u652f\u51fa(\u5143)",
                            "value": 1843
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5176\u4ed6\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 462
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
                    "text": "\u5c45\u6c11\u6d88\u8d39\u5360\u6bd4",
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
                            "name": "\u5c45\u6c11\u4eba\u5747\u670d\u52a1\u6027\u6d88\u8d39\u652f\u51fa(\u5143)",
                            "value": 10645
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u98df\u54c1\u70df\u9152\u652f\u51fa(\u5143)",
                            "value": 7178
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u8863\u7740\u652f\u51fa(\u5143)",
                            "value": 1419
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5c45\u4f4f\u652f\u51fa(\u5143)",
                            "value": 5641
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u751f\u6d3b\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 1423
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u4ea4\u901a\u901a\u4fe1\u652f\u51fa(\u5143)",
                            "value": 3156
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u6559\u80b2\u6587\u5316\u5a31\u4e50\u652f\u51fa(\u5143)",
                            "value": 2599
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u533b\u7597\u4fdd\u5065\u652f\u51fa(\u5143)",
                            "value": 2115
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5176\u4ed6\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 569
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
                    "text": "\u5c45\u6c11\u6d88\u8d39\u5360\u6bd4",
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
                            "name": "\u5c45\u6c11\u4eba\u5747\u670d\u52a1\u6027\u6d88\u8d39\u652f\u51fa(\u5143)",
                            "value": 10590
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u98df\u54c1\u70df\u9152\u652f\u51fa(\u5143)",
                            "value": 7481
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u8863\u7740\u652f\u51fa(\u5143)",
                            "value": 1365
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5c45\u4f4f\u652f\u51fa(\u5143)",
                            "value": 5882
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u751f\u6d3b\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 1432
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u4ea4\u901a\u901a\u4fe1\u652f\u51fa(\u5143)",
                            "value": 3195
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u6559\u80b2\u6587\u5316\u5a31\u4e50\u652f\u51fa(\u5143)",
                            "value": 2469
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u533b\u7597\u4fdd\u5065\u652f\u51fa(\u5143)",
                            "value": 2120
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5176\u4ed6\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 595
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
                    "text": "\u5c45\u6c11\u6d88\u8d39\u5360\u6bd4",
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
                            "name": "\u5c45\u6c11\u4eba\u5747\u670d\u52a1\u6027\u6d88\u8d39\u652f\u51fa(\u5143)",
                            "value": 12114
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u98df\u54c1\u70df\u9152\u652f\u51fa(\u5143)",
                            "value": 7983
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u8863\u7740\u652f\u51fa(\u5143)",
                            "value": 1479
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5c45\u4f4f\u652f\u51fa(\u5143)",
                            "value": 6095
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u751f\u6d3b\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 1526
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u4ea4\u901a\u901a\u4fe1\u652f\u51fa(\u5143)",
                            "value": 3652
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u6559\u80b2\u6587\u5316\u5a31\u4e50\u652f\u51fa(\u5143)",
                            "value": 2904
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u533b\u7597\u4fdd\u5065\u652f\u51fa(\u5143)",
                            "value": 2460
                        },
                        {
                            "name": "\u5c45\u6c11\u4eba\u5747\u5176\u4ed6\u7528\u54c1\u53ca\u670d\u52a1\u652f\u51fa(\u5143)",
                            "value": 697
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
                    "text": "\u5c45\u6c11\u6d88\u8d39\u5360\u6bd4",
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
        chart_e17017d929f646359e15dcb028f700f4.setOption(option_e17017d929f646359e15dcb028f700f4);
    </script>
</body>
</html>

"""
components.html(html_content,height=1500, width=2000)



st.sidebar.header("绘图演示")