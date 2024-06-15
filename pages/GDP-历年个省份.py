


import streamlit as st

import streamlit.components.v1 as components

st.set_page_config(page_title="绘图演示", page_icon="📈",layout="wide",)

html_content="""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Awesome-pyecharts</title>
                <script type="text/javascript" src="https://assets.pyecharts.org/assets/v5/echarts.min.js"></script>
            <script type="text/javascript" src="https://assets.pyecharts.org/assets/v5/maps/china.js"></script>

</head>
<body >
    <div id="6f8d2685d7d44ab2bc575cb96858ea09" class="chart-container" style="width:1600px; height:1000px; "></div>
    <script>
        var chart_6f8d2685d7d44ab2bc575cb96858ea09 = echarts.init(
            document.getElementById('6f8d2685d7d44ab2bc575cb96858ea09'), 'dark', {renderer: 'canvas'});
        var option_6f8d2685d7d44ab2bc575cb96858ea09 = {
    "baseOption": {
        "series": [
            {
                "type": "bar",
                "xAxisIndex": 0,
                "yAxisIndex": 0,
                "legendHoverLink": true,
                "data": [
                    {
                        "name": "\u5e7f\u4e1c\u7701",
                        "value": 97278.0
                    },
                    {
                        "name": "\u6c5f\u82cf\u7701",
                        "value": 92595.0
                    },
                    {
                        "name": "\u5c71\u4e1c\u7701",
                        "value": 76470.0
                    },
                    {
                        "name": "\u6d59\u6c5f\u7701",
                        "value": 56197.0
                    },
                    {
                        "name": "\u6cb3\u5357\u7701",
                        "value": 48056.0
                    },
                    {
                        "name": "\u56db\u5ddd\u7701",
                        "value": 40678.0
                    },
                    {
                        "name": "\u6e56\u5317\u7701",
                        "value": 39367.0
                    },
                    {
                        "name": "\u6e56\u5357\u7701",
                        "value": 36426.0
                    },
                    {
                        "name": "\u6cb3\u5317\u7701",
                        "value": 36010.0
                    },
                    {
                        "name": "\u798f\u5efa\u7701",
                        "value": 35804.0
                    },
                    {
                        "name": "\u4e0a\u6d77\u5e02",
                        "value": 32680.0
                    },
                    {
                        "name": "\u5317\u4eac\u5e02",
                        "value": 30320.0
                    },
                    {
                        "name": "\u5b89\u5fbd\u7701",
                        "value": 30007.0
                    },
                    {
                        "name": "\u8fbd\u5b81\u7701",
                        "value": 25315.0
                    },
                    {
                        "name": "\u9655\u897f\u7701",
                        "value": 24438.0
                    },
                    {
                        "name": "\u6c5f\u897f\u7701",
                        "value": 21985.0
                    },
                    {
                        "name": "\u91cd\u5e86\u5e02",
                        "value": 20363.0
                    },
                    {
                        "name": "\u5e7f\u897f\u58ee\u65cf\u81ea\u6cbb\u533a",
                        "value": 20353.0
                    },
                    {
                        "name": "\u5929\u6d25\u5e02",
                        "value": 18810.0
                    },
                    {
                        "name": "\u4e91\u5357\u7701",
                        "value": 17881.0
                    },
                    {
                        "name": "\u5185\u8499\u53e4",
                        "value": 17289.0
                    },
                    {
                        "name": "\u5c71\u897f\u7701",
                        "value": 16818.0
                    },
                    {
                        "name": "\u9ed1\u9f99\u6c5f\u7701",
                        "value": 16362.0
                    },
                    {
                        "name": "\u5409\u6797\u7701",
                        "value": 15075.0
                    },
                    {
                        "name": "\u8d35\u5dde\u7701",
                        "value": 14806.0
                    },
                    {
                        "name": "\u65b0\u7586\u7ef4\u543e\u5c14\u81ea\u6cbb\u533a",
                        "value": 12199.0
                    },
                    {
                        "name": "\u7518\u8083\u7701",
                        "value": 8246.0
                    },
                    {
                        "name": "\u6d77\u5357\u7701",
                        "value": 4832.0
                    },
                    {
                        "name": "\u5b81\u590f\u56de\u65cf\u81ea\u6cbb\u533a",
                        "value": 3705.0
                    },
                    {
                        "name": "\u9752\u6d77\u7701",
                        "value": 2865.0
                    },
                    {
                        "name": "\u897f\u85cf\u81ea\u6cbb\u533a",
                        "value": 1478.0
                    }
                ],
                "realtimeSort": false,
                "showBackground": false,
                "stackStrategy": "samesign",
                "cursor": "pointer",
                "barMinHeight": 0,
                "barCategoryGap": "20%",
                "barGap": "30%",
                "large": false,
                "largeThreshold": 400,
                "seriesLayoutBy": "column",
                "datasetIndex": 0,
                "clip": true,
                "zlevel": 0,
                "z": 2,
                "label": {
                    "show": true,
                    "position": "right",
                    "margin": 8,
                    "formatter": "{b} : {c}"
                }
            },
            {
                "type": "line",
                "connectNulls": false,
                "xAxisIndex": 1,
                "yAxisIndex": 1,
                "symbolSize": 4,
                "showSymbol": true,
                "smooth": false,
                "clip": true,
                "step": false,
                "data": [
                    [
                        "2013\u5e74",
                        63.4
                    ],
                    [
                        "2014\u5e74",
                        68.4
                    ],
                    [
                        "2015\u5e74",
                        72.3
                    ],
                    [
                        "2016\u5e74",
                        78
                    ],
                    [
                        "2017\u5e74",
                        84.7
                    ],
                    [
                        "2018\u5e74",
                        91.5
                    ]
                ],
                "hoverAnimation": true,
                "label": {
                    "show": false,
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
                "z": 0,
                "rippleEffect": {
                    "show": true,
                    "brushType": "stroke",
                    "scale": 2.5,
                    "period": 4
                }
            },
            {
                "type": "line",
                "connectNulls": false,
                "xAxisIndex": 1,
                "yAxisIndex": 1,
                "symbolSize": 4,
                "showSymbol": true,
                "smooth": false,
                "clip": true,
                "step": false,
                "data": [
                    [
                        "2013\u5e74",
                        ""
                    ],
                    [
                        "2014\u5e74",
                        ""
                    ],
                    [
                        "2015\u5e74",
                        ""
                    ],
                    [
                        "2016\u5e74",
                        ""
                    ],
                    [
                        "2017\u5e74",
                        ""
                    ],
                    [
                        "2018\u5e74",
                        91.5
                    ]
                ],
                "hoverAnimation": true,
                "label": {
                    "show": false,
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
                "markPoint": {
                    "label": {
                        "show": true,
                        "position": "inside",
                        "color": "#fff",
                        "margin": 8
                    },
                    "data": [
                        {
                            "type": "max"
                        }
                    ]
                },
                "zlevel": 0,
                "z": 0,
                "rippleEffect": {
                    "show": true,
                    "brushType": "stroke",
                    "scale": 2.5,
                    "period": 4
                }
            },
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
                        "name": "\u5e7f\u4e1c\u7701",
                        "value": 97278.0
                    },
                    {
                        "name": "\u6c5f\u82cf\u7701",
                        "value": 92595.0
                    },
                    {
                        "name": "\u5c71\u4e1c\u7701",
                        "value": 76470.0
                    },
                    {
                        "name": "\u6d59\u6c5f\u7701",
                        "value": 56197.0
                    },
                    {
                        "name": "\u6cb3\u5357\u7701",
                        "value": 48056.0
                    },
                    {
                        "name": "\u56db\u5ddd\u7701",
                        "value": 40678.0
                    },
                    {
                        "name": "\u6e56\u5317\u7701",
                        "value": 39367.0
                    },
                    {
                        "name": "\u6e56\u5357\u7701",
                        "value": 36426.0
                    },
                    {
                        "name": "\u6cb3\u5317\u7701",
                        "value": 36010.0
                    },
                    {
                        "name": "\u798f\u5efa\u7701",
                        "value": 35804.0
                    },
                    {
                        "name": "\u4e0a\u6d77\u5e02",
                        "value": 32680.0
                    },
                    {
                        "name": "\u5317\u4eac\u5e02",
                        "value": 30320.0
                    },
                    {
                        "name": "\u5b89\u5fbd\u7701",
                        "value": 30007.0
                    },
                    {
                        "name": "\u8fbd\u5b81\u7701",
                        "value": 25315.0
                    },
                    {
                        "name": "\u9655\u897f\u7701",
                        "value": 24438.0
                    },
                    {
                        "name": "\u6c5f\u897f\u7701",
                        "value": 21985.0
                    },
                    {
                        "name": "\u91cd\u5e86\u5e02",
                        "value": 20363.0
                    },
                    {
                        "name": "\u5e7f\u897f\u58ee\u65cf\u81ea\u6cbb\u533a",
                        "value": 20353.0
                    },
                    {
                        "name": "\u5929\u6d25\u5e02",
                        "value": 18810.0
                    },
                    {
                        "name": "\u4e91\u5357\u7701",
                        "value": 17881.0
                    },
                    {
                        "name": "\u5185\u8499\u53e4",
                        "value": 17289.0
                    },
                    {
                        "name": "\u5c71\u897f\u7701",
                        "value": 16818.0
                    },
                    {
                        "name": "\u9ed1\u9f99\u6c5f\u7701",
                        "value": 16362.0
                    },
                    {
                        "name": "\u5409\u6797\u7701",
                        "value": 15075.0
                    },
                    {
                        "name": "\u8d35\u5dde\u7701",
                        "value": 14806.0
                    },
                    {
                        "name": "\u65b0\u7586\u7ef4\u543e\u5c14\u81ea\u6cbb\u533a",
                        "value": 12199.0
                    },
                    {
                        "name": "\u7518\u8083\u7701",
                        "value": 8246.0
                    },
                    {
                        "name": "\u6d77\u5357\u7701",
                        "value": 4832.0
                    },
                    {
                        "name": "\u5b81\u590f\u56de\u65cf\u81ea\u6cbb\u533a",
                        "value": 3705.0
                    },
                    {
                        "name": "\u9752\u6d77\u7701",
                        "value": 2865.0
                    },
                    {
                        "name": "\u897f\u85cf\u81ea\u6cbb\u533a",
                        "value": 1478.0
                    }
                ],
                "radius": [
                    "15%",
                    "35%"
                ],
                "center": [
                    "80%",
                    "82%"
                ],
                "label": {
                    "show": true,
                    "margin": 8
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
                "itemStyle": {
                    "borderColor": "rgba(0,0,0,0.3)",
                    "borderWidth": 1
                },
                "xAxisIndex": 2,
                "yAxisIndex": 2
            },
            {
                "type": "map",
                "label": {
                    "show": true,
                    "margin": 8
                },
                "map": "china",
                "data": [
                    {
                        "name": "\u5e7f\u4e1c\u7701",
                        "value": [
                            97278.0,
                            10.63,
                            "\u5e7f\u4e1c\u7701"
                        ]
                    },
                    {
                        "name": "\u6c5f\u82cf\u7701",
                        "value": [
                            92595.0,
                            10.12,
                            "\u6c5f\u82cf\u7701"
                        ]
                    },
                    {
                        "name": "\u5c71\u4e1c\u7701",
                        "value": [
                            76470.0,
                            8.36,
                            "\u5c71\u4e1c\u7701"
                        ]
                    },
                    {
                        "name": "\u6d59\u6c5f\u7701",
                        "value": [
                            56197.0,
                            6.14,
                            "\u6d59\u6c5f\u7701"
                        ]
                    },
                    {
                        "name": "\u6cb3\u5357\u7701",
                        "value": [
                            48056.0,
                            5.25,
                            "\u6cb3\u5357\u7701"
                        ]
                    },
                    {
                        "name": "\u56db\u5ddd\u7701",
                        "value": [
                            40678.0,
                            4.45,
                            "\u56db\u5ddd\u7701"
                        ]
                    },
                    {
                        "name": "\u6e56\u5317\u7701",
                        "value": [
                            39367.0,
                            4.3,
                            "\u6e56\u5317\u7701"
                        ]
                    },
                    {
                        "name": "\u6e56\u5357\u7701",
                        "value": [
                            36426.0,
                            3.98,
                            "\u6e56\u5357\u7701"
                        ]
                    },
                    {
                        "name": "\u6cb3\u5317\u7701",
                        "value": [
                            36010.0,
                            3.94,
                            "\u6cb3\u5317\u7701"
                        ]
                    },
                    {
                        "name": "\u798f\u5efa\u7701",
                        "value": [
                            35804.0,
                            3.91,
                            "\u798f\u5efa\u7701"
                        ]
                    },
                    {
                        "name": "\u4e0a\u6d77\u5e02",
                        "value": [
                            32680.0,
                            3.57,
                            "\u4e0a\u6d77\u5e02"
                        ]
                    },
                    {
                        "name": "\u5317\u4eac\u5e02",
                        "value": [
                            30320.0,
                            3.31,
                            "\u5317\u4eac\u5e02"
                        ]
                    },
                    {
                        "name": "\u5b89\u5fbd\u7701",
                        "value": [
                            30007.0,
                            3.28,
                            "\u5b89\u5fbd\u7701"
                        ]
                    },
                    {
                        "name": "\u8fbd\u5b81\u7701",
                        "value": [
                            25315.0,
                            2.77,
                            "\u8fbd\u5b81\u7701"
                        ]
                    },
                    {
                        "name": "\u9655\u897f\u7701",
                        "value": [
                            24438.0,
                            2.67,
                            "\u9655\u897f\u7701"
                        ]
                    },
                    {
                        "name": "\u6c5f\u897f\u7701",
                        "value": [
                            21985.0,
                            2.4,
                            "\u6c5f\u897f\u7701"
                        ]
                    },
                    {
                        "name": "\u91cd\u5e86\u5e02",
                        "value": [
                            20363.0,
                            2.23,
                            "\u91cd\u5e86\u5e02"
                        ]
                    },
                    {
                        "name": "\u5e7f\u897f\u58ee\u65cf\u81ea\u6cbb\u533a",
                        "value": [
                            20353.0,
                            2.23,
                            "\u5e7f\u897f\u58ee\u65cf\u81ea\u6cbb\u533a"
                        ]
                    },
                    {
                        "name": "\u5929\u6d25\u5e02",
                        "value": [
                            18810.0,
                            2.06,
                            "\u5929\u6d25\u5e02"
                        ]
                    },
                    {
                        "name": "\u4e91\u5357\u7701",
                        "value": [
                            17881.0,
                            1.95,
                            "\u4e91\u5357\u7701"
                        ]
                    },
                    {
                        "name": "\u5185\u8499\u53e4",
                        "value": [
                            17289.0,
                            1.89,
                            "\u5185\u8499\u53e4"
                        ]
                    },
                    {
                        "name": "\u5c71\u897f\u7701",
                        "value": [
                            16818.0,
                            1.84,
                            "\u5c71\u897f\u7701"
                        ]
                    },
                    {
                        "name": "\u9ed1\u9f99\u6c5f\u7701",
                        "value": [
                            16362.0,
                            1.79,
                            "\u9ed1\u9f99\u6c5f\u7701"
                        ]
                    },
                    {
                        "name": "\u5409\u6797\u7701",
                        "value": [
                            15075.0,
                            1.65,
                            "\u5409\u6797\u7701"
                        ]
                    },
                    {
                        "name": "\u8d35\u5dde\u7701",
                        "value": [
                            14806.0,
                            1.62,
                            "\u8d35\u5dde\u7701"
                        ]
                    },
                    {
                        "name": "\u65b0\u7586\u7ef4\u543e\u5c14\u81ea\u6cbb\u533a",
                        "value": [
                            12199.0,
                            1.33,
                            "\u65b0\u7586\u7ef4\u543e\u5c14\u81ea\u6cbb\u533a"
                        ]
                    },
                    {
                        "name": "\u7518\u8083\u7701",
                        "value": [
                            8246.0,
                            0.9,
                            "\u7518\u8083\u7701"
                        ]
                    },
                    {
                        "name": "\u6d77\u5357\u7701",
                        "value": [
                            4832.0,
                            0.53,
                            "\u6d77\u5357\u7701"
                        ]
                    },
                    {
                        "name": "\u5b81\u590f\u56de\u65cf\u81ea\u6cbb\u533a",
                        "value": [
                            3705.0,
                            0.41,
                            "\u5b81\u590f\u56de\u65cf\u81ea\u6cbb\u533a"
                        ]
                    },
                    {
                        "name": "\u9752\u6d77\u7701",
                        "value": [
                            2865.0,
                            0.31,
                            "\u9752\u6d77\u7701"
                        ]
                    },
                    {
                        "name": "\u897f\u85cf\u81ea\u6cbb\u533a",
                        "value": [
                            1478.0,
                            0.16,
                            "\u897f\u85cf\u81ea\u6cbb\u533a"
                        ]
                    }
                ],
                "roam": true,
                "aspectScale": 0.75,
                "nameProperty": "name",
                "selectedMode": false,
                "center": [
                    119.5,
                    34.5
                ],
                "zoom": 1,
                "zlevel": 0,
                "z": 2,
                "seriesLayoutBy": "column",
                "datasetIndex": 0,
                "mapValueCalculation": "sum",
                "showLegendSymbol": false,
                "itemStyle": {
                    "normal": {
                        "areaColor": "#323c48",
                        "borderColor": "#404a59"
                    },
                    "emphasis": {
                        "label": {
                            "show": null
                        },
                        "areaColor": "rgba(255,255,255, 0.5)"
                    }
                },
                "emphasis": {},
                "xAxisIndex": 3,
                "yAxisIndex": 3
            }
        ],
        "timeline": {
            "axisType": "category",
            "currentIndex": 0,
            "orient": "vertical",
            "autoPlay": true,
            "controlPosition": "left",
            "loop": true,
            "rewind": false,
            "show": true,
            "inverse": true,
            "playInterval": 5000,
            "left": "null",
            "right": "5",
            "top": "20",
            "bottom": "20",
            "width": "60",
            "label": {
                "show": true,
                "color": "#fff",
                "margin": 8
            },
            "progress": {},
            "data": [
                "2013\u5e74",
                "2014\u5e74",
                "2015\u5e74",
                "2016\u5e74",
                "2017\u5e74",
                "2018\u5e74"
            ]
        },
        "grid": [
            {
                "show": false,
                "zlevel": 0,
                "z": 2,
                "left": "10",
                "top": "50%",
                "right": "45%",
                "bottom": "5",
                "containLabel": false,
                "backgroundColor": "transparent",
                "borderColor": "#ccc",
                "borderWidth": 1,
                "shadowOffsetX": 0,
                "shadowOffsetY": 0
            },
            {
                "show": false,
                "zlevel": 0,
                "z": 2,
                "left": "65%",
                "top": "10%",
                "right": "80",
                "bottom": "50%",
                "containLabel": false,
                "backgroundColor": "transparent",
                "borderColor": "#ccc",
                "borderWidth": 1,
                "shadowOffsetX": 0,
                "shadowOffsetY": 0
            },
            {
                "show": false,
                "zlevel": 0,
                "z": 2,
                "left": "45%",
                "top": "60%",
                "containLabel": false,
                "backgroundColor": "transparent",
                "borderColor": "#ccc",
                "borderWidth": 1,
                "shadowOffsetX": 0,
                "shadowOffsetY": 0
            },
            {
                "show": false,
                "zlevel": 0,
                "z": 2,
                "containLabel": false,
                "backgroundColor": "transparent",
                "borderColor": "#ccc",
                "borderWidth": 1,
                "shadowOffsetX": 0,
                "shadowOffsetY": 0
            }
        ],
        "xAxis": [
            {
                "show": true,
                "scale": false,
                "nameLocation": "end",
                "nameGap": 15,
                "gridIndex": 0,
                "axisLabel": {
                    "show": false,
                    "margin": 8
                },
                "inverse": false,
                "offset": 0,
                "splitNumber": 5,
                "max": 97300,
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
            },
            {
                "show": true,
                "scale": false,
                "nameLocation": "end",
                "nameGap": 15,
                "gridIndex": 1,
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
                    "2013\u5e74",
                    "2014\u5e74",
                    "2015\u5e74",
                    "2016\u5e74",
                    "2017\u5e74",
                    "2018\u5e74"
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
                "axisLabel": {
                    "show": false,
                    "margin": 8
                },
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
                    "\u5e7f\u4e1c\u7701",
                    "\u6c5f\u82cf\u7701",
                    "\u5c71\u4e1c\u7701",
                    "\u6d59\u6c5f\u7701",
                    "\u6cb3\u5357\u7701",
                    "\u56db\u5ddd\u7701",
                    "\u6e56\u5317\u7701",
                    "\u6e56\u5357\u7701",
                    "\u6cb3\u5317\u7701",
                    "\u798f\u5efa\u7701",
                    "\u4e0a\u6d77\u5e02",
                    "\u5317\u4eac\u5e02",
                    "\u5b89\u5fbd\u7701",
                    "\u8fbd\u5b81\u7701",
                    "\u9655\u897f\u7701",
                    "\u6c5f\u897f\u7701",
                    "\u91cd\u5e86\u5e02",
                    "\u5e7f\u897f\u58ee\u65cf\u81ea\u6cbb\u533a",
                    "\u5929\u6d25\u5e02",
                    "\u4e91\u5357\u7701",
                    "\u5185\u8499\u53e4",
                    "\u5c71\u897f\u7701",
                    "\u9ed1\u9f99\u6c5f\u7701",
                    "\u5409\u6797\u7701",
                    "\u8d35\u5dde\u7701",
                    "\u65b0\u7586\u7ef4\u543e\u5c14\u81ea\u6cbb\u533a",
                    "\u7518\u8083\u7701",
                    "\u6d77\u5357\u7701",
                    "\u5b81\u590f\u56de\u65cf\u81ea\u6cbb\u533a",
                    "\u9752\u6d77\u7701",
                    "\u897f\u85cf\u81ea\u6cbb\u533a"
                ]
            },
            {
                "show": true,
                "scale": false,
                "nameLocation": "end",
                "nameGap": 15,
                "gridIndex": 1,
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
        "visualMap": [
            {
                "show": true,
                "type": "continuous",
                "min": 30,
                "max": 97300,
                "text": [
                    "High",
                    "Low"
                ],
                "textStyle": {
                    "color": "#ddd"
                },
                "inRange": {
                    "color": [
                        "lightskyblue",
                        "yellow",
                        "orangered"
                    ]
                },
                "calculable": true,
                "inverse": false,
                "splitNumber": 5,
                "dimension": 0,
                "hoverLink": true,
                "orient": "vertical",
                "left": "10",
                "top": "top",
                "padding": 5,
                "showLabel": true,
                "itemWidth": 20,
                "itemHeight": 140,
                "borderWidth": 0
            },
            {
                "show": true,
                "type": "continuous",
                "min": 30,
                "max": 97300,
                "text": [
                    "High",
                    "Low"
                ],
                "textStyle": {
                    "color": "#ddd"
                },
                "inRange": {
                    "color": [
                        "lightskyblue",
                        "yellow",
                        "orangered"
                    ]
                },
                "calculable": true,
                "inverse": false,
                "splitNumber": 5,
                "dimension": 0,
                "hoverLink": true,
                "orient": "vertical",
                "left": "30",
                "top": "center",
                "padding": 5,
                "showLabel": true,
                "itemWidth": 20,
                "itemHeight": 140,
                "borderWidth": 0
            }
        ],
        "legend": [
            {
                "data": [
                    ""
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
            },
            {
                "data": [
                    "",
                    ""
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
            },
            {
                "data": [
                    "\u5e7f\u4e1c\u7701",
                    "\u6c5f\u82cf\u7701",
                    "\u5c71\u4e1c\u7701",
                    "\u6d59\u6c5f\u7701",
                    "\u6cb3\u5357\u7701",
                    "\u56db\u5ddd\u7701",
                    "\u6e56\u5317\u7701",
                    "\u6e56\u5357\u7701",
                    "\u6cb3\u5317\u7701",
                    "\u798f\u5efa\u7701",
                    "\u4e0a\u6d77\u5e02",
                    "\u5317\u4eac\u5e02",
                    "\u5b89\u5fbd\u7701",
                    "\u8fbd\u5b81\u7701",
                    "\u9655\u897f\u7701",
                    "\u6c5f\u897f\u7701",
                    "\u91cd\u5e86\u5e02",
                    "\u5e7f\u897f\u58ee\u65cf\u81ea\u6cbb\u533a",
                    "\u5929\u6d25\u5e02",
                    "\u4e91\u5357\u7701",
                    "\u5185\u8499\u53e4",
                    "\u5c71\u897f\u7701",
                    "\u9ed1\u9f99\u6c5f\u7701",
                    "\u5409\u6797\u7701",
                    "\u8d35\u5dde\u7701",
                    "\u65b0\u7586\u7ef4\u543e\u5c14\u81ea\u6cbb\u533a",
                    "\u7518\u8083\u7701",
                    "\u6d77\u5357\u7701",
                    "\u5b81\u590f\u56de\u65cf\u81ea\u6cbb\u533a",
                    "\u9752\u6d77\u7701",
                    "\u897f\u85cf\u81ea\u6cbb\u533a"
                ],
                "selected": {},
                "show": false,
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
            },
            {
                "data": [
                    ""
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
        ]
    },
    "options": [
        {
            "series": [
                {
                    "type": "bar",
                    "xAxisIndex": 0,
                    "yAxisIndex": 0,
                    "legendHoverLink": true,
                    "data": [
                        {
                            "name": "\u5e7f\u4e1c\u7701",
                            "value": 62475.0
                        },
                        {
                            "name": "\u6c5f\u82cf\u7701",
                            "value": 59753.0
                        },
                        {
                            "name": "\u5c71\u4e1c\u7701",
                            "value": 55230.0
                        },
                        {
                            "name": "\u6d59\u6c5f\u7701",
                            "value": 37757.0
                        },
                        {
                            "name": "\u6cb3\u5357\u7701",
                            "value": 32191.0
                        },
                        {
                            "name": "\u6cb3\u5317\u7701",
                            "value": 28443.0
                        },
                        {
                            "name": "\u8fbd\u5b81\u7701",
                            "value": 27213.0
                        },
                        {
                            "name": "\u56db\u5ddd\u7701",
                            "value": 26392.0
                        },
                        {
                            "name": "\u6e56\u5317\u7701",
                            "value": 24792.0
                        },
                        {
                            "name": "\u6e56\u5357\u7701",
                            "value": 24622.0
                        },
                        {
                            "name": "\u798f\u5efa\u7701",
                            "value": 21868.0
                        },
                        {
                            "name": "\u4e0a\u6d77\u5e02",
                            "value": 21818.0
                        },
                        {
                            "name": "\u5317\u4eac\u5e02",
                            "value": 19801.0
                        },
                        {
                            "name": "\u5b89\u5fbd\u7701",
                            "value": 19229.0
                        },
                        {
                            "name": "\u5185\u8499\u53e4",
                            "value": 16917.0
                        },
                        {
                            "name": "\u9655\u897f\u7701",
                            "value": 16205.0
                        },
                        {
                            "name": "\u9ed1\u9f99\u6c5f\u7701",
                            "value": 14455.0
                        },
                        {
                            "name": "\u5e7f\u897f\u58ee\u65cf\u81ea\u6cbb\u533a",
                            "value": 14450.0
                        },
                        {
                            "name": "\u5929\u6d25\u5e02",
                            "value": 14442.0
                        },
                        {
                            "name": "\u6c5f\u897f\u7701",
                            "value": 14410.0
                        },
                        {
                            "name": "\u5409\u6797\u7701",
                            "value": 13046.0
                        },
                        {
                            "name": "\u91cd\u5e86\u5e02",
                            "value": 12783.0
                        },
                        {
                            "name": "\u5c71\u897f\u7701",
                            "value": 12665.0
                        },
                        {
                            "name": "\u4e91\u5357\u7701",
                            "value": 11832.0
                        },
                        {
                            "name": "\u65b0\u7586\u7ef4\u543e\u5c14\u81ea\u6cbb\u533a",
                            "value": 8444.0
                        },
                        {
                            "name": "\u8d35\u5dde\u7701",
                            "value": 8087.0
                        },
                        {
                            "name": "\u7518\u8083\u7701",
                            "value": 6331.0
                        },
                        {
                            "name": "\u6d77\u5357\u7701",
                            "value": 3178.0
                        },
                        {
                            "name": "\u5b81\u590f\u56de\u65cf\u81ea\u6cbb\u533a",
                            "value": 2578.0
                        },
                        {
                            "name": "\u9752\u6d77\u7701",
                            "value": 2122.0
                        },
                        {
                            "name": "\u897f\u85cf\u81ea\u6cbb\u533a",
                            "value": 816.0
                        }
                    ],
                    "realtimeSort": false,
                    "showBackground": false,
                    "stackStrategy": "samesign",
                    "cursor": "pointer",
                    "barMinHeight": 0,
                    "barCategoryGap": "20%",
                    "barGap": "30%",
                    "large": false,
                    "largeThreshold": 400,
                    "seriesLayoutBy": "column",
                    "datasetIndex": 0,
                    "clip": true,
                    "zlevel": 0,
                    "z": 2,
                    "label": {
                        "show": true,
                        "position": "right",
                        "margin": 8,
                        "formatter": "{b} : {c}"
                    }
                },
                {
                    "type": "line",
                    "connectNulls": false,
                    "xAxisIndex": 1,
                    "yAxisIndex": 1,
                    "symbolSize": 4,
                    "showSymbol": true,
                    "smooth": false,
                    "clip": true,
                    "step": false,
                    "data": [
                        [
                            "2013\u5e74",
                            63.4
                        ],
                        [
                            "2014\u5e74",
                            68.4
                        ],
                        [
                            "2015\u5e74",
                            72.3
                        ],
                        [
                            "2016\u5e74",
                            78
                        ],
                        [
                            "2017\u5e74",
                            84.7
                        ],
                        [
                            "2018\u5e74",
                            91.5
                        ]
                    ],
                    "hoverAnimation": true,
                    "label": {
                        "show": false,
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
                    "z": 0,
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                },
                {
                    "type": "line",
                    "connectNulls": false,
                    "xAxisIndex": 1,
                    "yAxisIndex": 1,
                    "symbolSize": 4,
                    "showSymbol": true,
                    "smooth": false,
                    "clip": true,
                    "step": false,
                    "data": [
                        [
                            "2013\u5e74",
                            63.4
                        ],
                        [
                            "2014\u5e74",
                            ""
                        ],
                        [
                            "2015\u5e74",
                            ""
                        ],
                        [
                            "2016\u5e74",
                            ""
                        ],
                        [
                            "2017\u5e74",
                            ""
                        ],
                        [
                            "2018\u5e74",
                            ""
                        ]
                    ],
                    "hoverAnimation": true,
                    "label": {
                        "show": false,
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
                    "markPoint": {
                        "label": {
                            "show": true,
                            "position": "inside",
                            "color": "#fff",
                            "margin": 8
                        },
                        "data": [
                            {
                                "type": "max"
                            }
                        ]
                    },
                    "zlevel": 0,
                    "z": 0,
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                },
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
                            "name": "\u5e7f\u4e1c\u7701",
                            "value": 62475.0
                        },
                        {
                            "name": "\u6c5f\u82cf\u7701",
                            "value": 59753.0
                        },
                        {
                            "name": "\u5c71\u4e1c\u7701",
                            "value": 55230.0
                        },
                        {
                            "name": "\u6d59\u6c5f\u7701",
                            "value": 37757.0
                        },
                        {
                            "name": "\u6cb3\u5357\u7701",
                            "value": 32191.0
                        },
                        {
                            "name": "\u6cb3\u5317\u7701",
                            "value": 28443.0
                        },
                        {
                            "name": "\u8fbd\u5b81\u7701",
                            "value": 27213.0
                        },
                        {
                            "name": "\u56db\u5ddd\u7701",
                            "value": 26392.0
                        },
                        {
                            "name": "\u6e56\u5317\u7701",
                            "value": 24792.0
                        },
                        {
                            "name": "\u6e56\u5357\u7701",
                            "value": 24622.0
                        },
                        {
                            "name": "\u798f\u5efa\u7701",
                            "value": 21868.0
                        },
                        {
                            "name": "\u4e0a\u6d77\u5e02",
                            "value": 21818.0
                        },
                        {
                            "name": "\u5317\u4eac\u5e02",
                            "value": 19801.0
                        },
                        {
                            "name": "\u5b89\u5fbd\u7701",
                            "value": 19229.0
                        },
                        {
                            "name": "\u5185\u8499\u53e4",
                            "value": 16917.0
                        },
                        {
                            "name": "\u9655\u897f\u7701",
                            "value": 16205.0
                        },
                        {
                            "name": "\u9ed1\u9f99\u6c5f\u7701",
                            "value": 14455.0
                        },
                        {
                            "name": "\u5e7f\u897f\u58ee\u65cf\u81ea\u6cbb\u533a",
                            "value": 14450.0
                        },
                        {
                            "name": "\u5929\u6d25\u5e02",
                            "value": 14442.0
                        },
                        {
                            "name": "\u6c5f\u897f\u7701",
                            "value": 14410.0
                        },
                        {
                            "name": "\u5409\u6797\u7701",
                            "value": 13046.0
                        },
                        {
                            "name": "\u91cd\u5e86\u5e02",
                            "value": 12783.0
                        },
                        {
                            "name": "\u5c71\u897f\u7701",
                            "value": 12665.0
                        },
                        {
                            "name": "\u4e91\u5357\u7701",
                            "value": 11832.0
                        },
                        {
                            "name": "\u65b0\u7586\u7ef4\u543e\u5c14\u81ea\u6cbb\u533a",
                            "value": 8444.0
                        },
                        {
                            "name": "\u8d35\u5dde\u7701",
                            "value": 8087.0
                        },
                        {
                            "name": "\u7518\u8083\u7701",
                            "value": 6331.0
                        },
                        {
                            "name": "\u6d77\u5357\u7701",
                            "value": 3178.0
                        },
                        {
                            "name": "\u5b81\u590f\u56de\u65cf\u81ea\u6cbb\u533a",
                            "value": 2578.0
                        },
                        {
                            "name": "\u9752\u6d77\u7701",
                            "value": 2122.0
                        },
                        {
                            "name": "\u897f\u85cf\u81ea\u6cbb\u533a",
                            "value": 816.0
                        }
                    ],
                    "radius": [
                        "15%",
                        "35%"
                    ],
                    "center": [
                        "80%",
                        "82%"
                    ],
                    "label": {
                        "show": true,
                        "margin": 8
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
                    "itemStyle": {
                        "borderColor": "rgba(0,0,0,0.3)",
                        "borderWidth": 1
                    },
                    "xAxisIndex": 2,
                    "yAxisIndex": 2
                },
                {
                    "type": "map",
                    "label": {
                        "show": true,
                        "margin": 8
                    },
                    "map": "china",
                    "data": [
                        {
                            "name": "\u5e7f\u4e1c\u7701",
                            "value": [
                                62475.0,
                                9.85,
                                "\u5e7f\u4e1c\u7701"
                            ]
                        },
                        {
                            "name": "\u6c5f\u82cf\u7701",
                            "value": [
                                59753.0,
                                9.42,
                                "\u6c5f\u82cf\u7701"
                            ]
                        },
                        {
                            "name": "\u5c71\u4e1c\u7701",
                            "value": [
                                55230.0,
                                8.71,
                                "\u5c71\u4e1c\u7701"
                            ]
                        },
                        {
                            "name": "\u6d59\u6c5f\u7701",
                            "value": [
                                37757.0,
                                5.95,
                                "\u6d59\u6c5f\u7701"
                            ]
                        },
                        {
                            "name": "\u6cb3\u5357\u7701",
                            "value": [
                                32191.0,
                                5.07,
                                "\u6cb3\u5357\u7701"
                            ]
                        },
                        {
                            "name": "\u6cb3\u5317\u7701",
                            "value": [
                                28443.0,
                                4.48,
                                "\u6cb3\u5317\u7701"
                            ]
                        },
                        {
                            "name": "\u8fbd\u5b81\u7701",
                            "value": [
                                27213.0,
                                4.29,
                                "\u8fbd\u5b81\u7701"
                            ]
                        },
                        {
                            "name": "\u56db\u5ddd\u7701",
                            "value": [
                                26392.0,
                                4.16,
                                "\u56db\u5ddd\u7701"
                            ]
                        },
                        {
                            "name": "\u6e56\u5317\u7701",
                            "value": [
                                24792.0,
                                3.91,
                                "\u6e56\u5317\u7701"
                            ]
                        },
                        {
                            "name": "\u6e56\u5357\u7701",
                            "value": [
                                24622.0,
                                3.88,
                                "\u6e56\u5357\u7701"
                            ]
                        },
                        {
                            "name": "\u798f\u5efa\u7701",
                            "value": [
                                21868.0,
                                3.45,
                                "\u798f\u5efa\u7701"
                            ]
                        },
                        {
                            "name": "\u4e0a\u6d77\u5e02",
                            "value": [
                                21818.0,
                                3.44,
                                "\u4e0a\u6d77\u5e02"
                            ]
                        },
                        {
                            "name": "\u5317\u4eac\u5e02",
                            "value": [
                                19801.0,
                                3.12,
                                "\u5317\u4eac\u5e02"
                            ]
                        },
                        {
                            "name": "\u5b89\u5fbd\u7701",
                            "value": [
                                19229.0,
                                3.03,
                                "\u5b89\u5fbd\u7701"
                            ]
                        },
                        {
                            "name": "\u5185\u8499\u53e4",
                            "value": [
                                16917.0,
                                2.67,
                                "\u5185\u8499\u53e4"
                            ]
                        },
                        {
                            "name": "\u9655\u897f\u7701",
                            "value": [
                                16205.0,
                                2.55,
                                "\u9655\u897f\u7701"
                            ]
                        },
                        {
                            "name": "\u9ed1\u9f99\u6c5f\u7701",
                            "value": [
                                14455.0,
                                2.28,
                                "\u9ed1\u9f99\u6c5f\u7701"
                            ]
                        },
                        {
                            "name": "\u5e7f\u897f\u58ee\u65cf\u81ea\u6cbb\u533a",
                            "value": [
                                14450.0,
                                2.28,
                                "\u5e7f\u897f\u58ee\u65cf\u81ea\u6cbb\u533a"
                            ]
                        },
                        {
                            "name": "\u5929\u6d25\u5e02",
                            "value": [
                                14442.0,
                                2.28,
                                "\u5929\u6d25\u5e02"
                            ]
                        },
                        {
                            "name": "\u6c5f\u897f\u7701",
                            "value": [
                                14410.0,
                                2.27,
                                "\u6c5f\u897f\u7701"
                            ]
                        },
                        {
                            "name": "\u5409\u6797\u7701",
                            "value": [
                                13046.0,
                                2.06,
                                "\u5409\u6797\u7701"
                            ]
                        },
                        {
                            "name": "\u91cd\u5e86\u5e02",
                            "value": [
                                12783.0,
                                2.02,
                                "\u91cd\u5e86\u5e02"
                            ]
                        },
                        {
                            "name": "\u5c71\u897f\u7701",
                            "value": [
                                12665.0,
                                2.0,
                                "\u5c71\u897f\u7701"
                            ]
                        },
                        {
                            "name": "\u4e91\u5357\u7701",
                            "value": [
                                11832.0,
                                1.87,
                                "\u4e91\u5357\u7701"
                            ]
                        },
                        {
                            "name": "\u65b0\u7586\u7ef4\u543e\u5c14\u81ea\u6cbb\u533a",
                            "value": [
                                8444.0,
                                1.33,
                                "\u65b0\u7586\u7ef4\u543e\u5c14\u81ea\u6cbb\u533a"
                            ]
                        },
                        {
                            "name": "\u8d35\u5dde\u7701",
                            "value": [
                                8087.0,
                                1.27,
                                "\u8d35\u5dde\u7701"
                            ]
                        },
                        {
                            "name": "\u7518\u8083\u7701",
                            "value": [
                                6331.0,
                                1.0,
                                "\u7518\u8083\u7701"
                            ]
                        },
                        {
                            "name": "\u6d77\u5357\u7701",
                            "value": [
                                3178.0,
                                0.5,
                                "\u6d77\u5357\u7701"
                            ]
                        },
                        {
                            "name": "\u5b81\u590f\u56de\u65cf\u81ea\u6cbb\u533a",
                            "value": [
                                2578.0,
                                0.41,
                                "\u5b81\u590f\u56de\u65cf\u81ea\u6cbb\u533a"
                            ]
                        },
                        {
                            "name": "\u9752\u6d77\u7701",
                            "value": [
                                2122.0,
                                0.33,
                                "\u9752\u6d77\u7701"
                            ]
                        },
                        {
                            "name": "\u897f\u85cf\u81ea\u6cbb\u533a",
                            "value": [
                                816.0,
                                0.13,
                                "\u897f\u85cf\u81ea\u6cbb\u533a"
                            ]
                        }
                    ],
                    "roam": true,
                    "aspectScale": 0.75,
                    "nameProperty": "name",
                    "selectedMode": false,
                    "center": [
                        119.5,
                        34.5
                    ],
                    "zoom": 1,
                    "zlevel": 0,
                    "z": 2,
                    "seriesLayoutBy": "column",
                    "datasetIndex": 0,
                    "mapValueCalculation": "sum",
                    "showLegendSymbol": false,
                    "itemStyle": {
                        "normal": {
                            "areaColor": "#323c48",
                            "borderColor": "#404a59"
                        },
                        "emphasis": {
                            "label": {
                                "show": null
                            },
                            "areaColor": "rgba(255,255,255, 0.5)"
                        }
                    },
                    "emphasis": {},
                    "xAxisIndex": 3,
                    "yAxisIndex": 3
                }
            ],
            "xAxis": [
                {
                    "show": true,
                    "scale": false,
                    "nameLocation": "end",
                    "nameGap": 15,
                    "gridIndex": 0,
                    "axisLabel": {
                        "show": false,
                        "margin": 8
                    },
                    "inverse": false,
                    "offset": 0,
                    "splitNumber": 5,
                    "max": 97300,
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
                },
                {
                    "show": true,
                    "scale": false,
                    "nameLocation": "end",
                    "nameGap": 15,
                    "gridIndex": 1,
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
                        "2013\u5e74",
                        "2014\u5e74",
                        "2015\u5e74",
                        "2016\u5e74",
                        "2017\u5e74",
                        "2018\u5e74"
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
                    "axisLabel": {
                        "show": false,
                        "margin": 8
                    },
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
                        "\u5e7f\u4e1c\u7701",
                        "\u6c5f\u82cf\u7701",
                        "\u5c71\u4e1c\u7701",
                        "\u6d59\u6c5f\u7701",
                        "\u6cb3\u5357\u7701",
                        "\u6cb3\u5317\u7701",
                        "\u8fbd\u5b81\u7701",
                        "\u56db\u5ddd\u7701",
                        "\u6e56\u5317\u7701",
                        "\u6e56\u5357\u7701",
                        "\u798f\u5efa\u7701",
                        "\u4e0a\u6d77\u5e02",
                        "\u5317\u4eac\u5e02",
                        "\u5b89\u5fbd\u7701",
                        "\u5185\u8499\u53e4",
                        "\u9655\u897f\u7701",
                        "\u9ed1\u9f99\u6c5f\u7701",
                        "\u5e7f\u897f\u58ee\u65cf\u81ea\u6cbb\u533a",
                        "\u5929\u6d25\u5e02",
                        "\u6c5f\u897f\u7701",
                        "\u5409\u6797\u7701",
                        "\u91cd\u5e86\u5e02",
                        "\u5c71\u897f\u7701",
                        "\u4e91\u5357\u7701",
                        "\u65b0\u7586\u7ef4\u543e\u5c14\u81ea\u6cbb\u533a",
                        "\u8d35\u5dde\u7701",
                        "\u7518\u8083\u7701",
                        "\u6d77\u5357\u7701",
                        "\u5b81\u590f\u56de\u65cf\u81ea\u6cbb\u533a",
                        "\u9752\u6d77\u7701",
                        "\u897f\u85cf\u81ea\u6cbb\u533a"
                    ]
                },
                {
                    "show": true,
                    "scale": false,
                    "nameLocation": "end",
                    "nameGap": 15,
                    "gridIndex": 1,
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
                    "target": "blank",
                    "subtarget": "blank",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false
                },
                {
                    "show": true,
                    "text": "\u5168\u56fdGDP\u603b\u91cf2013\u5e74\uff08\u5355\u4f4d\uff1a\u4e07\u4ebf\uff09",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "50%",
                    "top": "5%",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false
                },
                {
                    "show": true,
                    "target": "blank",
                    "subtarget": "blank",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false
                },
                {
                    "show": true,
                    "text": "2013\u5e74\u5168\u56fd\u5206\u5730\u533aGPD\u60c5\u51b5\uff08\u5355\u4f4d\uff1a\u4ebf\uff09 \u6570\u636e\u6765\u6e90\uff1a\u56fd\u5bb6\u7edf\u8ba1\u5c40",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "center",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "color": "rgba(255,255,255, 0.9)",
                        "fontSize": 25
                    }
                }
            ],
            "tooltip": {
                "show": false,
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
            },
            "visualMap": [
                {
                    "show": true,
                    "type": "continuous",
                    "min": 30,
                    "max": 97300,
                    "text": [
                        "High",
                        "Low"
                    ],
                    "textStyle": {
                        "color": "#ddd"
                    },
                    "inRange": {
                        "color": [
                            "lightskyblue",
                            "yellow",
                            "orangered"
                        ]
                    },
                    "calculable": true,
                    "inverse": false,
                    "splitNumber": 5,
                    "dimension": 0,
                    "hoverLink": true,
                    "orient": "vertical",
                    "left": "10",
                    "top": "top",
                    "padding": 5,
                    "showLabel": true,
                    "itemWidth": 20,
                    "itemHeight": 140,
                    "borderWidth": 0
                },
                {
                    "show": true,
                    "type": "continuous",
                    "min": 30,
                    "max": 97300,
                    "text": [
                        "High",
                        "Low"
                    ],
                    "textStyle": {
                        "color": "#ddd"
                    },
                    "inRange": {
                        "color": [
                            "lightskyblue",
                            "yellow",
                            "orangered"
                        ]
                    },
                    "calculable": true,
                    "inverse": false,
                    "splitNumber": 5,
                    "dimension": 0,
                    "hoverLink": true,
                    "orient": "vertical",
                    "left": "30",
                    "top": "center",
                    "padding": 5,
                    "showLabel": true,
                    "itemWidth": 20,
                    "itemHeight": 140,
                    "borderWidth": 0
                }
            ],
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
            ]
        },
        {
            "series": [
                {
                    "type": "bar",
                    "xAxisIndex": 0,
                    "yAxisIndex": 0,
                    "legendHoverLink": true,
                    "data": [
                        {
                            "name": "\u5e7f\u4e1c\u7701",
                            "value": 67810.0
                        },
                        {
                            "name": "\u6c5f\u82cf\u7701",
                            "value": 65088.0
                        },
                        {
                            "name": "\u5c71\u4e1c\u7701",
                            "value": 59427.0
                        },
                        {
                            "name": "\u6d59\u6c5f\u7701",
                            "value": 40173.0
                        },
                        {
                            "name": "\u6cb3\u5357\u7701",
                            "value": 34938.0
                        },
                        {
                            "name": "\u6cb3\u5317\u7701",
                            "value": 29421.0
                        },
                        {
                            "name": "\u8fbd\u5b81\u7701",
                            "value": 28627.0
                        },
                        {
                            "name": "\u56db\u5ddd\u7701",
                            "value": 28537.0
                        },
                        {
                            "name": "\u6e56\u5317\u7701",
                            "value": 27379.0
                        },
                        {
                            "name": "\u6e56\u5357\u7701",
                            "value": 27037.0
                        },
                        {
                            "name": "\u798f\u5efa\u7701",
                            "value": 24056.0
                        },
                        {
                            "name": "\u4e0a\u6d77\u5e02",
                            "value": 23568.0
                        },
                        {
                            "name": "\u5317\u4eac\u5e02",
                            "value": 21331.0
                        },
                        {
                            "name": "\u5b89\u5fbd\u7701",
                            "value": 20849.0
                        },
                        {
                            "name": "\u5185\u8499\u53e4",
                            "value": 17770.0
                        },
                        {
                            "name": "\u9655\u897f\u7701",
                            "value": 17690.0
                        },
                        {
                            "name": "\u5929\u6d25\u5e02",
                            "value": 15727.0
                        },
                        {
                            "name": "\u6c5f\u897f\u7701",
                            "value": 15715.0
                        },
                        {
                            "name": "\u5e7f\u897f\u58ee\u65cf\u81ea\u6cbb\u533a",
                            "value": 15673.0
                        },
                        {
                            "name": "\u9ed1\u9f99\u6c5f\u7701",
                            "value": 15039.0
                        },
                        {
                            "name": "\u91cd\u5e86\u5e02",
                            "value": 14263.0
                        },
                        {
                            "name": "\u5409\u6797\u7701",
                            "value": 13803.0
                        },
                        {
                            "name": "\u4e91\u5357\u7701",
                            "value": 12815.0
                        },
                        {
                            "name": "\u5c71\u897f\u7701",
                            "value": 12761.0
                        },
                        {
                            "name": "\u65b0\u7586\u7ef4\u543e\u5c14\u81ea\u6cbb\u533a",
                            "value": 9273.0
                        },
                        {
                            "name": "\u8d35\u5dde\u7701",
                            "value": 9266.0
                        },
                        {
                            "name": "\u7518\u8083\u7701",
                            "value": 6837.0
                        },
                        {
                            "name": "\u6d77\u5357\u7701",
                            "value": 3501.0
                        },
                        {
                            "name": "\u5b81\u590f\u56de\u65cf\u81ea\u6cbb\u533a",
                            "value": 2752.0
                        },
                        {
                            "name": "\u9752\u6d77\u7701",
                            "value": 2303.0
                        },
                        {
                            "name": "\u897f\u85cf\u81ea\u6cbb\u533a",
                            "value": 921.0
                        }
                    ],
                    "realtimeSort": false,
                    "showBackground": false,
                    "stackStrategy": "samesign",
                    "cursor": "pointer",
                    "barMinHeight": 0,
                    "barCategoryGap": "20%",
                    "barGap": "30%",
                    "large": false,
                    "largeThreshold": 400,
                    "seriesLayoutBy": "column",
                    "datasetIndex": 0,
                    "clip": true,
                    "zlevel": 0,
                    "z": 2,
                    "label": {
                        "show": true,
                        "position": "right",
                        "margin": 8,
                        "formatter": "{b} : {c}"
                    }
                },
                {
                    "type": "line",
                    "connectNulls": false,
                    "xAxisIndex": 1,
                    "yAxisIndex": 1,
                    "symbolSize": 4,
                    "showSymbol": true,
                    "smooth": false,
                    "clip": true,
                    "step": false,
                    "data": [
                        [
                            "2013\u5e74",
                            63.4
                        ],
                        [
                            "2014\u5e74",
                            68.4
                        ],
                        [
                            "2015\u5e74",
                            72.3
                        ],
                        [
                            "2016\u5e74",
                            78
                        ],
                        [
                            "2017\u5e74",
                            84.7
                        ],
                        [
                            "2018\u5e74",
                            91.5
                        ]
                    ],
                    "hoverAnimation": true,
                    "label": {
                        "show": false,
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
                    "z": 0,
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                },
                {
                    "type": "line",
                    "connectNulls": false,
                    "xAxisIndex": 1,
                    "yAxisIndex": 1,
                    "symbolSize": 4,
                    "showSymbol": true,
                    "smooth": false,
                    "clip": true,
                    "step": false,
                    "data": [
                        [
                            "2013\u5e74",
                            ""
                        ],
                        [
                            "2014\u5e74",
                            68.4
                        ],
                        [
                            "2015\u5e74",
                            ""
                        ],
                        [
                            "2016\u5e74",
                            ""
                        ],
                        [
                            "2017\u5e74",
                            ""
                        ],
                        [
                            "2018\u5e74",
                            ""
                        ]
                    ],
                    "hoverAnimation": true,
                    "label": {
                        "show": false,
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
                    "markPoint": {
                        "label": {
                            "show": true,
                            "position": "inside",
                            "color": "#fff",
                            "margin": 8
                        },
                        "data": [
                            {
                                "type": "max"
                            }
                        ]
                    },
                    "zlevel": 0,
                    "z": 0,
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                },
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
                            "name": "\u5e7f\u4e1c\u7701",
                            "value": 67810.0
                        },
                        {
                            "name": "\u6c5f\u82cf\u7701",
                            "value": 65088.0
                        },
                        {
                            "name": "\u5c71\u4e1c\u7701",
                            "value": 59427.0
                        },
                        {
                            "name": "\u6d59\u6c5f\u7701",
                            "value": 40173.0
                        },
                        {
                            "name": "\u6cb3\u5357\u7701",
                            "value": 34938.0
                        },
                        {
                            "name": "\u6cb3\u5317\u7701",
                            "value": 29421.0
                        },
                        {
                            "name": "\u8fbd\u5b81\u7701",
                            "value": 28627.0
                        },
                        {
                            "name": "\u56db\u5ddd\u7701",
                            "value": 28537.0
                        },
                        {
                            "name": "\u6e56\u5317\u7701",
                            "value": 27379.0
                        },
                        {
                            "name": "\u6e56\u5357\u7701",
                            "value": 27037.0
                        },
                        {
                            "name": "\u798f\u5efa\u7701",
                            "value": 24056.0
                        },
                        {
                            "name": "\u4e0a\u6d77\u5e02",
                            "value": 23568.0
                        },
                        {
                            "name": "\u5317\u4eac\u5e02",
                            "value": 21331.0
                        },
                        {
                            "name": "\u5b89\u5fbd\u7701",
                            "value": 20849.0
                        },
                        {
                            "name": "\u5185\u8499\u53e4",
                            "value": 17770.0
                        },
                        {
                            "name": "\u9655\u897f\u7701",
                            "value": 17690.0
                        },
                        {
                            "name": "\u5929\u6d25\u5e02",
                            "value": 15727.0
                        },
                        {
                            "name": "\u6c5f\u897f\u7701",
                            "value": 15715.0
                        },
                        {
                            "name": "\u5e7f\u897f\u58ee\u65cf\u81ea\u6cbb\u533a",
                            "value": 15673.0
                        },
                        {
                            "name": "\u9ed1\u9f99\u6c5f\u7701",
                            "value": 15039.0
                        },
                        {
                            "name": "\u91cd\u5e86\u5e02",
                            "value": 14263.0
                        },
                        {
                            "name": "\u5409\u6797\u7701",
                            "value": 13803.0
                        },
                        {
                            "name": "\u4e91\u5357\u7701",
                            "value": 12815.0
                        },
                        {
                            "name": "\u5c71\u897f\u7701",
                            "value": 12761.0
                        },
                        {
                            "name": "\u65b0\u7586\u7ef4\u543e\u5c14\u81ea\u6cbb\u533a",
                            "value": 9273.0
                        },
                        {
                            "name": "\u8d35\u5dde\u7701",
                            "value": 9266.0
                        },
                        {
                            "name": "\u7518\u8083\u7701",
                            "value": 6837.0
                        },
                        {
                            "name": "\u6d77\u5357\u7701",
                            "value": 3501.0
                        },
                        {
                            "name": "\u5b81\u590f\u56de\u65cf\u81ea\u6cbb\u533a",
                            "value": 2752.0
                        },
                        {
                            "name": "\u9752\u6d77\u7701",
                            "value": 2303.0
                        },
                        {
                            "name": "\u897f\u85cf\u81ea\u6cbb\u533a",
                            "value": 921.0
                        }
                    ],
                    "radius": [
                        "15%",
                        "35%"
                    ],
                    "center": [
                        "80%",
                        "82%"
                    ],
                    "label": {
                        "show": true,
                        "margin": 8
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
                    "itemStyle": {
                        "borderColor": "rgba(0,0,0,0.3)",
                        "borderWidth": 1
                    },
                    "xAxisIndex": 2,
                    "yAxisIndex": 2
                },
                {
                    "type": "map",
                    "label": {
                        "show": true,
                        "margin": 8
                    },
                    "map": "china",
                    "data": [
                        {
                            "name": "\u5e7f\u4e1c\u7701",
                            "value": [
                                67810.0,
                                9.91,
                                "\u5e7f\u4e1c\u7701"
                            ]
                        },
                        {
                            "name": "\u6c5f\u82cf\u7701",
                            "value": [
                                65088.0,
                                9.51,
                                "\u6c5f\u82cf\u7701"
                            ]
                        },
                        {
                            "name": "\u5c71\u4e1c\u7701",
                            "value": [
                                59427.0,
                                8.68,
                                "\u5c71\u4e1c\u7701"
                            ]
                        },
                        {
                            "name": "\u6d59\u6c5f\u7701",
                            "value": [
                                40173.0,
                                5.87,
                                "\u6d59\u6c5f\u7701"
                            ]
                        },
                        {
                            "name": "\u6cb3\u5357\u7701",
                            "value": [
                                34938.0,
                                5.11,
                                "\u6cb3\u5357\u7701"
                            ]
                        },
                        {
                            "name": "\u6cb3\u5317\u7701",
                            "value": [
                                29421.0,
                                4.3,
                                "\u6cb3\u5317\u7701"
                            ]
                        },
                        {
                            "name": "\u8fbd\u5b81\u7701",
                            "value": [
                                28627.0,
                                4.18,
                                "\u8fbd\u5b81\u7701"
                            ]
                        },
                        {
                            "name": "\u56db\u5ddd\u7701",
                            "value": [
                                28537.0,
                                4.17,
                                "\u56db\u5ddd\u7701"
                            ]
                        },
                        {
                            "name": "\u6e56\u5317\u7701",
                            "value": [
                                27379.0,
                                4.0,
                                "\u6e56\u5317\u7701"
                            ]
                        },
                        {
                            "name": "\u6e56\u5357\u7701",
                            "value": [
                                27037.0,
                                3.95,
                                "\u6e56\u5357\u7701"
                            ]
                        },
                        {
                            "name": "\u798f\u5efa\u7701",
                            "value": [
                                24056.0,
                                3.52,
                                "\u798f\u5efa\u7701"
                            ]
                        },
                        {
                            "name": "\u4e0a\u6d77\u5e02",
                            "value": [
                                23568.0,
                                3.44,
                                "\u4e0a\u6d77\u5e02"
                            ]
                        },
                        {
                            "name": "\u5317\u4eac\u5e02",
                            "value": [
                                21331.0,
                                3.12,
                                "\u5317\u4eac\u5e02"
                            ]
                        },
                        {
                            "name": "\u5b89\u5fbd\u7701",
                            "value": [
                                20849.0,
                                3.05,
                                "\u5b89\u5fbd\u7701"
                            ]
                        },
                        {
                            "name": "\u5185\u8499\u53e4",
                            "value": [
                                17770.0,
                                2.6,
                                "\u5185\u8499\u53e4"
                            ]
                        },
                        {
                            "name": "\u9655\u897f\u7701",
                            "value": [
                                17690.0,
                                2.58,
                                "\u9655\u897f\u7701"
                            ]
                        },
                        {
                            "name": "\u5929\u6d25\u5e02",
                            "value": [
                                15727.0,
                                2.3,
                                "\u5929\u6d25\u5e02"
                            ]
                        },
                        {
                            "name": "\u6c5f\u897f\u7701",
                            "value": [
                                15715.0,
                                2.3,
                                "\u6c5f\u897f\u7701"
                            ]
                        },
                        {
                            "name": "\u5e7f\u897f\u58ee\u65cf\u81ea\u6cbb\u533a",
                            "value": [
                                15673.0,
                                2.29,
                                "\u5e7f\u897f\u58ee\u65cf\u81ea\u6cbb\u533a"
                            ]
                        },
                        {
                            "name": "\u9ed1\u9f99\u6c5f\u7701",
                            "value": [
                                15039.0,
                                2.2,
                                "\u9ed1\u9f99\u6c5f\u7701"
                            ]
                        },
                        {
                            "name": "\u91cd\u5e86\u5e02",
                            "value": [
                                14263.0,
                                2.08,
                                "\u91cd\u5e86\u5e02"
                            ]
                        },
                        {
                            "name": "\u5409\u6797\u7701",
                            "value": [
                                13803.0,
                                2.02,
                                "\u5409\u6797\u7701"
                            ]
                        },
                        {
                            "name": "\u4e91\u5357\u7701",
                            "value": [
                                12815.0,
                                1.87,
                                "\u4e91\u5357\u7701"
                            ]
                        },
                        {
                            "name": "\u5c71\u897f\u7701",
                            "value": [
                                12761.0,
                                1.86,
                                "\u5c71\u897f\u7701"
                            ]
                        },
                        {
                            "name": "\u65b0\u7586\u7ef4\u543e\u5c14\u81ea\u6cbb\u533a",
                            "value": [
                                9273.0,
                                1.36,
                                "\u65b0\u7586\u7ef4\u543e\u5c14\u81ea\u6cbb\u533a"
                            ]
                        },
                        {
                            "name": "\u8d35\u5dde\u7701",
                            "value": [
                                9266.0,
                                1.35,
                                "\u8d35\u5dde\u7701"
                            ]
                        },
                        {
                            "name": "\u7518\u8083\u7701",
                            "value": [
                                6837.0,
                                1.0,
                                "\u7518\u8083\u7701"
                            ]
                        },
                        {
                            "name": "\u6d77\u5357\u7701",
                            "value": [
                                3501.0,
                                0.51,
                                "\u6d77\u5357\u7701"
                            ]
                        },
                        {
                            "name": "\u5b81\u590f\u56de\u65cf\u81ea\u6cbb\u533a",
                            "value": [
                                2752.0,
                                0.4,
                                "\u5b81\u590f\u56de\u65cf\u81ea\u6cbb\u533a"
                            ]
                        },
                        {
                            "name": "\u9752\u6d77\u7701",
                            "value": [
                                2303.0,
                                0.34,
                                "\u9752\u6d77\u7701"
                            ]
                        },
                        {
                            "name": "\u897f\u85cf\u81ea\u6cbb\u533a",
                            "value": [
                                921.0,
                                0.13,
                                "\u897f\u85cf\u81ea\u6cbb\u533a"
                            ]
                        }
                    ],
                    "roam": true,
                    "aspectScale": 0.75,
                    "nameProperty": "name",
                    "selectedMode": false,
                    "center": [
                        119.5,
                        34.5
                    ],
                    "zoom": 1,
                    "zlevel": 0,
                    "z": 2,
                    "seriesLayoutBy": "column",
                    "datasetIndex": 0,
                    "mapValueCalculation": "sum",
                    "showLegendSymbol": false,
                    "itemStyle": {
                        "normal": {
                            "areaColor": "#323c48",
                            "borderColor": "#404a59"
                        },
                        "emphasis": {
                            "label": {
                                "show": null
                            },
                            "areaColor": "rgba(255,255,255, 0.5)"
                        }
                    },
                    "emphasis": {},
                    "xAxisIndex": 3,
                    "yAxisIndex": 3
                }
            ],
            "xAxis": [
                {
                    "show": true,
                    "scale": false,
                    "nameLocation": "end",
                    "nameGap": 15,
                    "gridIndex": 0,
                    "axisLabel": {
                        "show": false,
                        "margin": 8
                    },
                    "inverse": false,
                    "offset": 0,
                    "splitNumber": 5,
                    "max": 97300,
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
                },
                {
                    "show": true,
                    "scale": false,
                    "nameLocation": "end",
                    "nameGap": 15,
                    "gridIndex": 1,
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
                        "2013\u5e74",
                        "2014\u5e74",
                        "2015\u5e74",
                        "2016\u5e74",
                        "2017\u5e74",
                        "2018\u5e74"
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
                    "axisLabel": {
                        "show": false,
                        "margin": 8
                    },
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
                        "\u5e7f\u4e1c\u7701",
                        "\u6c5f\u82cf\u7701",
                        "\u5c71\u4e1c\u7701",
                        "\u6d59\u6c5f\u7701",
                        "\u6cb3\u5357\u7701",
                        "\u6cb3\u5317\u7701",
                        "\u8fbd\u5b81\u7701",
                        "\u56db\u5ddd\u7701",
                        "\u6e56\u5317\u7701",
                        "\u6e56\u5357\u7701",
                        "\u798f\u5efa\u7701",
                        "\u4e0a\u6d77\u5e02",
                        "\u5317\u4eac\u5e02",
                        "\u5b89\u5fbd\u7701",
                        "\u5185\u8499\u53e4",
                        "\u9655\u897f\u7701",
                        "\u5929\u6d25\u5e02",
                        "\u6c5f\u897f\u7701",
                        "\u5e7f\u897f\u58ee\u65cf\u81ea\u6cbb\u533a",
                        "\u9ed1\u9f99\u6c5f\u7701",
                        "\u91cd\u5e86\u5e02",
                        "\u5409\u6797\u7701",
                        "\u4e91\u5357\u7701",
                        "\u5c71\u897f\u7701",
                        "\u65b0\u7586\u7ef4\u543e\u5c14\u81ea\u6cbb\u533a",
                        "\u8d35\u5dde\u7701",
                        "\u7518\u8083\u7701",
                        "\u6d77\u5357\u7701",
                        "\u5b81\u590f\u56de\u65cf\u81ea\u6cbb\u533a",
                        "\u9752\u6d77\u7701",
                        "\u897f\u85cf\u81ea\u6cbb\u533a"
                    ]
                },
                {
                    "show": true,
                    "scale": false,
                    "nameLocation": "end",
                    "nameGap": 15,
                    "gridIndex": 1,
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
                    "target": "blank",
                    "subtarget": "blank",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false
                },
                {
                    "show": true,
                    "text": "\u5168\u56fdGDP\u603b\u91cf2014\u5e74\uff08\u5355\u4f4d\uff1a\u4e07\u4ebf\uff09",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "50%",
                    "top": "5%",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false
                },
                {
                    "show": true,
                    "target": "blank",
                    "subtarget": "blank",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false
                },
                {
                    "show": true,
                    "text": "2014\u5e74\u5168\u56fd\u5206\u5730\u533aGPD\u60c5\u51b5\uff08\u5355\u4f4d\uff1a\u4ebf\uff09 \u6570\u636e\u6765\u6e90\uff1a\u56fd\u5bb6\u7edf\u8ba1\u5c40",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "center",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "color": "rgba(255,255,255, 0.9)",
                        "fontSize": 25
                    }
                }
            ],
            "tooltip": {
                "show": false,
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
            },
            "visualMap": [
                {
                    "show": true,
                    "type": "continuous",
                    "min": 30,
                    "max": 97300,
                    "text": [
                        "High",
                        "Low"
                    ],
                    "textStyle": {
                        "color": "#ddd"
                    },
                    "inRange": {
                        "color": [
                            "lightskyblue",
                            "yellow",
                            "orangered"
                        ]
                    },
                    "calculable": true,
                    "inverse": false,
                    "splitNumber": 5,
                    "dimension": 0,
                    "hoverLink": true,
                    "orient": "vertical",
                    "left": "10",
                    "top": "top",
                    "padding": 5,
                    "showLabel": true,
                    "itemWidth": 20,
                    "itemHeight": 140,
                    "borderWidth": 0
                },
                {
                    "show": true,
                    "type": "continuous",
                    "min": 30,
                    "max": 97300,
                    "text": [
                        "High",
                        "Low"
                    ],
                    "textStyle": {
                        "color": "#ddd"
                    },
                    "inRange": {
                        "color": [
                            "lightskyblue",
                            "yellow",
                            "orangered"
                        ]
                    },
                    "calculable": true,
                    "inverse": false,
                    "splitNumber": 5,
                    "dimension": 0,
                    "hoverLink": true,
                    "orient": "vertical",
                    "left": "30",
                    "top": "center",
                    "padding": 5,
                    "showLabel": true,
                    "itemWidth": 20,
                    "itemHeight": 140,
                    "borderWidth": 0
                }
            ],
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
            ]
        },
        {
            "series": [
                {
                    "type": "bar",
                    "xAxisIndex": 0,
                    "yAxisIndex": 0,
                    "legendHoverLink": true,
                    "data": [
                        {
                            "name": "\u5e7f\u4e1c\u7701",
                            "value": 72813.0
                        },
                        {
                            "name": "\u6c5f\u82cf\u7701",
                            "value": 70116.0
                        },
                        {
                            "name": "\u5c71\u4e1c\u7701",
                            "value": 63002.0
                        },
                        {
                            "name": "\u6d59\u6c5f\u7701",
                            "value": 42886.0
                        },
                        {
                            "name": "\u6cb3\u5357\u7701",
                            "value": 37002.0
                        },
                        {
                            "name": "\u56db\u5ddd\u7701",
                            "value": 30053.0
                        },
                        {
                            "name": "\u6cb3\u5317\u7701",
                            "value": 29806.0
                        },
                        {
                            "name": "\u6e56\u5317\u7701",
                            "value": 29550.0
                        },
                        {
                            "name": "\u6e56\u5357\u7701",
                            "value": 28902.0
                        },
                        {
                            "name": "\u8fbd\u5b81\u7701",
                            "value": 28669.0
                        },
                        {
                            "name": "\u798f\u5efa\u7701",
                            "value": 25980.0
                        },
                        {
                            "name": "\u4e0a\u6d77\u5e02",
                            "value": 25123.0
                        },
                        {
                            "name": "\u5317\u4eac\u5e02",
                            "value": 23015.0
                        },
                        {
                            "name": "\u5b89\u5fbd\u7701",
                            "value": 22006.0
                        },
                        {
                            "name": "\u9655\u897f\u7701",
                            "value": 18022.0
                        },
                        {
                            "name": "\u5185\u8499\u53e4",
                            "value": 17832.0
                        },
                        {
                            "name": "\u5e7f\u897f\u58ee\u65cf\u81ea\u6cbb\u533a",
                            "value": 16803.0
                        },
                        {
                            "name": "\u6c5f\u897f\u7701",
                            "value": 16724.0
                        },
                        {
                            "name": "\u5929\u6d25\u5e02",
                            "value": 16538.0
                        },
                        {
                            "name": "\u91cd\u5e86\u5e02",
                            "value": 15717.0
                        },
                        {
                            "name": "\u9ed1\u9f99\u6c5f\u7701",
                            "value": 15084.0
                        },
                        {
                            "name": "\u5409\u6797\u7701",
                            "value": 14063.0
                        },
                        {
                            "name": "\u4e91\u5357\u7701",
                            "value": 13619.0
                        },
                        {
                            "name": "\u5c71\u897f\u7701",
                            "value": 12766.0
                        },
                        {
                            "name": "\u8d35\u5dde\u7701",
                            "value": 10503.0
                        },
                        {
                            "name": "\u65b0\u7586\u7ef4\u543e\u5c14\u81ea\u6cbb\u533a",
                            "value": 9325.0
                        },
                        {
                            "name": "\u7518\u8083\u7701",
                            "value": 6790.0
                        },
                        {
                            "name": "\u6d77\u5357\u7701",
                            "value": 3703.0
                        },
                        {
                            "name": "\u5b81\u590f\u56de\u65cf\u81ea\u6cbb\u533a",
                            "value": 2912.0
                        },
                        {
                            "name": "\u9752\u6d77\u7701",
                            "value": 2417.0
                        },
                        {
                            "name": "\u897f\u85cf\u81ea\u6cbb\u533a",
                            "value": 1026.0
                        }
                    ],
                    "realtimeSort": false,
                    "showBackground": false,
                    "stackStrategy": "samesign",
                    "cursor": "pointer",
                    "barMinHeight": 0,
                    "barCategoryGap": "20%",
                    "barGap": "30%",
                    "large": false,
                    "largeThreshold": 400,
                    "seriesLayoutBy": "column",
                    "datasetIndex": 0,
                    "clip": true,
                    "zlevel": 0,
                    "z": 2,
                    "label": {
                        "show": true,
                        "position": "right",
                        "margin": 8,
                        "formatter": "{b} : {c}"
                    }
                },
                {
                    "type": "line",
                    "connectNulls": false,
                    "xAxisIndex": 1,
                    "yAxisIndex": 1,
                    "symbolSize": 4,
                    "showSymbol": true,
                    "smooth": false,
                    "clip": true,
                    "step": false,
                    "data": [
                        [
                            "2013\u5e74",
                            63.4
                        ],
                        [
                            "2014\u5e74",
                            68.4
                        ],
                        [
                            "2015\u5e74",
                            72.3
                        ],
                        [
                            "2016\u5e74",
                            78
                        ],
                        [
                            "2017\u5e74",
                            84.7
                        ],
                        [
                            "2018\u5e74",
                            91.5
                        ]
                    ],
                    "hoverAnimation": true,
                    "label": {
                        "show": false,
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
                    "z": 0,
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                },
                {
                    "type": "line",
                    "connectNulls": false,
                    "xAxisIndex": 1,
                    "yAxisIndex": 1,
                    "symbolSize": 4,
                    "showSymbol": true,
                    "smooth": false,
                    "clip": true,
                    "step": false,
                    "data": [
                        [
                            "2013\u5e74",
                            ""
                        ],
                        [
                            "2014\u5e74",
                            ""
                        ],
                        [
                            "2015\u5e74",
                            72.3
                        ],
                        [
                            "2016\u5e74",
                            ""
                        ],
                        [
                            "2017\u5e74",
                            ""
                        ],
                        [
                            "2018\u5e74",
                            ""
                        ]
                    ],
                    "hoverAnimation": true,
                    "label": {
                        "show": false,
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
                    "markPoint": {
                        "label": {
                            "show": true,
                            "position": "inside",
                            "color": "#fff",
                            "margin": 8
                        },
                        "data": [
                            {
                                "type": "max"
                            }
                        ]
                    },
                    "zlevel": 0,
                    "z": 0,
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                },
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
                            "name": "\u5e7f\u4e1c\u7701",
                            "value": 72813.0
                        },
                        {
                            "name": "\u6c5f\u82cf\u7701",
                            "value": 70116.0
                        },
                        {
                            "name": "\u5c71\u4e1c\u7701",
                            "value": 63002.0
                        },
                        {
                            "name": "\u6d59\u6c5f\u7701",
                            "value": 42886.0
                        },
                        {
                            "name": "\u6cb3\u5357\u7701",
                            "value": 37002.0
                        },
                        {
                            "name": "\u56db\u5ddd\u7701",
                            "value": 30053.0
                        },
                        {
                            "name": "\u6cb3\u5317\u7701",
                            "value": 29806.0
                        },
                        {
                            "name": "\u6e56\u5317\u7701",
                            "value": 29550.0
                        },
                        {
                            "name": "\u6e56\u5357\u7701",
                            "value": 28902.0
                        },
                        {
                            "name": "\u8fbd\u5b81\u7701",
                            "value": 28669.0
                        },
                        {
                            "name": "\u798f\u5efa\u7701",
                            "value": 25980.0
                        },
                        {
                            "name": "\u4e0a\u6d77\u5e02",
                            "value": 25123.0
                        },
                        {
                            "name": "\u5317\u4eac\u5e02",
                            "value": 23015.0
                        },
                        {
                            "name": "\u5b89\u5fbd\u7701",
                            "value": 22006.0
                        },
                        {
                            "name": "\u9655\u897f\u7701",
                            "value": 18022.0
                        },
                        {
                            "name": "\u5185\u8499\u53e4",
                            "value": 17832.0
                        },
                        {
                            "name": "\u5e7f\u897f\u58ee\u65cf\u81ea\u6cbb\u533a",
                            "value": 16803.0
                        },
                        {
                            "name": "\u6c5f\u897f\u7701",
                            "value": 16724.0
                        },
                        {
                            "name": "\u5929\u6d25\u5e02",
                            "value": 16538.0
                        },
                        {
                            "name": "\u91cd\u5e86\u5e02",
                            "value": 15717.0
                        },
                        {
                            "name": "\u9ed1\u9f99\u6c5f\u7701",
                            "value": 15084.0
                        },
                        {
                            "name": "\u5409\u6797\u7701",
                            "value": 14063.0
                        },
                        {
                            "name": "\u4e91\u5357\u7701",
                            "value": 13619.0
                        },
                        {
                            "name": "\u5c71\u897f\u7701",
                            "value": 12766.0
                        },
                        {
                            "name": "\u8d35\u5dde\u7701",
                            "value": 10503.0
                        },
                        {
                            "name": "\u65b0\u7586\u7ef4\u543e\u5c14\u81ea\u6cbb\u533a",
                            "value": 9325.0
                        },
                        {
                            "name": "\u7518\u8083\u7701",
                            "value": 6790.0
                        },
                        {
                            "name": "\u6d77\u5357\u7701",
                            "value": 3703.0
                        },
                        {
                            "name": "\u5b81\u590f\u56de\u65cf\u81ea\u6cbb\u533a",
                            "value": 2912.0
                        },
                        {
                            "name": "\u9752\u6d77\u7701",
                            "value": 2417.0
                        },
                        {
                            "name": "\u897f\u85cf\u81ea\u6cbb\u533a",
                            "value": 1026.0
                        }
                    ],
                    "radius": [
                        "15%",
                        "35%"
                    ],
                    "center": [
                        "80%",
                        "82%"
                    ],
                    "label": {
                        "show": true,
                        "margin": 8
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
                    "itemStyle": {
                        "borderColor": "rgba(0,0,0,0.3)",
                        "borderWidth": 1
                    },
                    "xAxisIndex": 2,
                    "yAxisIndex": 2
                },
                {
                    "type": "map",
                    "label": {
                        "show": true,
                        "margin": 8
                    },
                    "map": "china",
                    "data": [
                        {
                            "name": "\u5e7f\u4e1c\u7701",
                            "value": [
                                72813.0,
                                10.07,
                                "\u5e7f\u4e1c\u7701"
                            ]
                        },
                        {
                            "name": "\u6c5f\u82cf\u7701",
                            "value": [
                                70116.0,
                                9.7,
                                "\u6c5f\u82cf\u7701"
                            ]
                        },
                        {
                            "name": "\u5c71\u4e1c\u7701",
                            "value": [
                                63002.0,
                                8.72,
                                "\u5c71\u4e1c\u7701"
                            ]
                        },
                        {
                            "name": "\u6d59\u6c5f\u7701",
                            "value": [
                                42886.0,
                                5.93,
                                "\u6d59\u6c5f\u7701"
                            ]
                        },
                        {
                            "name": "\u6cb3\u5357\u7701",
                            "value": [
                                37002.0,
                                5.12,
                                "\u6cb3\u5357\u7701"
                            ]
                        },
                        {
                            "name": "\u56db\u5ddd\u7701",
                            "value": [
                                30053.0,
                                4.16,
                                "\u56db\u5ddd\u7701"
                            ]
                        },
                        {
                            "name": "\u6cb3\u5317\u7701",
                            "value": [
                                29806.0,
                                4.12,
                                "\u6cb3\u5317\u7701"
                            ]
                        },
                        {
                            "name": "\u6e56\u5317\u7701",
                            "value": [
                                29550.0,
                                4.09,
                                "\u6e56\u5317\u7701"
                            ]
                        },
                        {
                            "name": "\u6e56\u5357\u7701",
                            "value": [
                                28902.0,
                                4.0,
                                "\u6e56\u5357\u7701"
                            ]
                        },
                        {
                            "name": "\u8fbd\u5b81\u7701",
                            "value": [
                                28669.0,
                                3.97,
                                "\u8fbd\u5b81\u7701"
                            ]
                        },
                        {
                            "name": "\u798f\u5efa\u7701",
                            "value": [
                                25980.0,
                                3.59,
                                "\u798f\u5efa\u7701"
                            ]
                        },
                        {
                            "name": "\u4e0a\u6d77\u5e02",
                            "value": [
                                25123.0,
                                3.48,
                                "\u4e0a\u6d77\u5e02"
                            ]
                        },
                        {
                            "name": "\u5317\u4eac\u5e02",
                            "value": [
                                23015.0,
                                3.18,
                                "\u5317\u4eac\u5e02"
                            ]
                        },
                        {
                            "name": "\u5b89\u5fbd\u7701",
                            "value": [
                                22006.0,
                                3.04,
                                "\u5b89\u5fbd\u7701"
                            ]
                        },
                        {
                            "name": "\u9655\u897f\u7701",
                            "value": [
                                18022.0,
                                2.49,
                                "\u9655\u897f\u7701"
                            ]
                        },
                        {
                            "name": "\u5185\u8499\u53e4",
                            "value": [
                                17832.0,
                                2.47,
                                "\u5185\u8499\u53e4"
                            ]
                        },
                        {
                            "name": "\u5e7f\u897f\u58ee\u65cf\u81ea\u6cbb\u533a",
                            "value": [
                                16803.0,
                                2.32,
                                "\u5e7f\u897f\u58ee\u65cf\u81ea\u6cbb\u533a"
                            ]
                        },
                        {
                            "name": "\u6c5f\u897f\u7701",
                            "value": [
                                16724.0,
                                2.31,
                                "\u6c5f\u897f\u7701"
                            ]
                        },
                        {
                            "name": "\u5929\u6d25\u5e02",
                            "value": [
                                16538.0,
                                2.29,
                                "\u5929\u6d25\u5e02"
                            ]
                        },
                        {
                            "name": "\u91cd\u5e86\u5e02",
                            "value": [
                                15717.0,
                                2.17,
                                "\u91cd\u5e86\u5e02"
                            ]
                        },
                        {
                            "name": "\u9ed1\u9f99\u6c5f\u7701",
                            "value": [
                                15084.0,
                                2.09,
                                "\u9ed1\u9f99\u6c5f\u7701"
                            ]
                        },
                        {
                            "name": "\u5409\u6797\u7701",
                            "value": [
                                14063.0,
                                1.95,
                                "\u5409\u6797\u7701"
                            ]
                        },
                        {
                            "name": "\u4e91\u5357\u7701",
                            "value": [
                                13619.0,
                                1.88,
                                "\u4e91\u5357\u7701"
                            ]
                        },
                        {
                            "name": "\u5c71\u897f\u7701",
                            "value": [
                                12766.0,
                                1.77,
                                "\u5c71\u897f\u7701"
                            ]
                        },
                        {
                            "name": "\u8d35\u5dde\u7701",
                            "value": [
                                10503.0,
                                1.45,
                                "\u8d35\u5dde\u7701"
                            ]
                        },
                        {
                            "name": "\u65b0\u7586\u7ef4\u543e\u5c14\u81ea\u6cbb\u533a",
                            "value": [
                                9325.0,
                                1.29,
                                "\u65b0\u7586\u7ef4\u543e\u5c14\u81ea\u6cbb\u533a"
                            ]
                        },
                        {
                            "name": "\u7518\u8083\u7701",
                            "value": [
                                6790.0,
                                0.94,
                                "\u7518\u8083\u7701"
                            ]
                        },
                        {
                            "name": "\u6d77\u5357\u7701",
                            "value": [
                                3703.0,
                                0.51,
                                "\u6d77\u5357\u7701"
                            ]
                        },
                        {
                            "name": "\u5b81\u590f\u56de\u65cf\u81ea\u6cbb\u533a",
                            "value": [
                                2912.0,
                                0.4,
                                "\u5b81\u590f\u56de\u65cf\u81ea\u6cbb\u533a"
                            ]
                        },
                        {
                            "name": "\u9752\u6d77\u7701",
                            "value": [
                                2417.0,
                                0.33,
                                "\u9752\u6d77\u7701"
                            ]
                        },
                        {
                            "name": "\u897f\u85cf\u81ea\u6cbb\u533a",
                            "value": [
                                1026.0,
                                0.14,
                                "\u897f\u85cf\u81ea\u6cbb\u533a"
                            ]
                        }
                    ],
                    "roam": true,
                    "aspectScale": 0.75,
                    "nameProperty": "name",
                    "selectedMode": false,
                    "center": [
                        119.5,
                        34.5
                    ],
                    "zoom": 1,
                    "zlevel": 0,
                    "z": 2,
                    "seriesLayoutBy": "column",
                    "datasetIndex": 0,
                    "mapValueCalculation": "sum",
                    "showLegendSymbol": false,
                    "itemStyle": {
                        "normal": {
                            "areaColor": "#323c48",
                            "borderColor": "#404a59"
                        },
                        "emphasis": {
                            "label": {
                                "show": null
                            },
                            "areaColor": "rgba(255,255,255, 0.5)"
                        }
                    },
                    "emphasis": {},
                    "xAxisIndex": 3,
                    "yAxisIndex": 3
                }
            ],
            "xAxis": [
                {
                    "show": true,
                    "scale": false,
                    "nameLocation": "end",
                    "nameGap": 15,
                    "gridIndex": 0,
                    "axisLabel": {
                        "show": false,
                        "margin": 8
                    },
                    "inverse": false,
                    "offset": 0,
                    "splitNumber": 5,
                    "max": 97300,
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
                },
                {
                    "show": true,
                    "scale": false,
                    "nameLocation": "end",
                    "nameGap": 15,
                    "gridIndex": 1,
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
                        "2013\u5e74",
                        "2014\u5e74",
                        "2015\u5e74",
                        "2016\u5e74",
                        "2017\u5e74",
                        "2018\u5e74"
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
                    "axisLabel": {
                        "show": false,
                        "margin": 8
                    },
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
                        "\u5e7f\u4e1c\u7701",
                        "\u6c5f\u82cf\u7701",
                        "\u5c71\u4e1c\u7701",
                        "\u6d59\u6c5f\u7701",
                        "\u6cb3\u5357\u7701",
                        "\u56db\u5ddd\u7701",
                        "\u6cb3\u5317\u7701",
                        "\u6e56\u5317\u7701",
                        "\u6e56\u5357\u7701",
                        "\u8fbd\u5b81\u7701",
                        "\u798f\u5efa\u7701",
                        "\u4e0a\u6d77\u5e02",
                        "\u5317\u4eac\u5e02",
                        "\u5b89\u5fbd\u7701",
                        "\u9655\u897f\u7701",
                        "\u5185\u8499\u53e4",
                        "\u5e7f\u897f\u58ee\u65cf\u81ea\u6cbb\u533a",
                        "\u6c5f\u897f\u7701",
                        "\u5929\u6d25\u5e02",
                        "\u91cd\u5e86\u5e02",
                        "\u9ed1\u9f99\u6c5f\u7701",
                        "\u5409\u6797\u7701",
                        "\u4e91\u5357\u7701",
                        "\u5c71\u897f\u7701",
                        "\u8d35\u5dde\u7701",
                        "\u65b0\u7586\u7ef4\u543e\u5c14\u81ea\u6cbb\u533a",
                        "\u7518\u8083\u7701",
                        "\u6d77\u5357\u7701",
                        "\u5b81\u590f\u56de\u65cf\u81ea\u6cbb\u533a",
                        "\u9752\u6d77\u7701",
                        "\u897f\u85cf\u81ea\u6cbb\u533a"
                    ]
                },
                {
                    "show": true,
                    "scale": false,
                    "nameLocation": "end",
                    "nameGap": 15,
                    "gridIndex": 1,
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
                    "target": "blank",
                    "subtarget": "blank",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false
                },
                {
                    "show": true,
                    "text": "\u5168\u56fdGDP\u603b\u91cf2015\u5e74\uff08\u5355\u4f4d\uff1a\u4e07\u4ebf\uff09",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "50%",
                    "top": "5%",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false
                },
                {
                    "show": true,
                    "target": "blank",
                    "subtarget": "blank",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false
                },
                {
                    "show": true,
                    "text": "2015\u5e74\u5168\u56fd\u5206\u5730\u533aGPD\u60c5\u51b5\uff08\u5355\u4f4d\uff1a\u4ebf\uff09 \u6570\u636e\u6765\u6e90\uff1a\u56fd\u5bb6\u7edf\u8ba1\u5c40",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "center",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "color": "rgba(255,255,255, 0.9)",
                        "fontSize": 25
                    }
                }
            ],
            "tooltip": {
                "show": false,
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
            },
            "visualMap": [
                {
                    "show": true,
                    "type": "continuous",
                    "min": 30,
                    "max": 97300,
                    "text": [
                        "High",
                        "Low"
                    ],
                    "textStyle": {
                        "color": "#ddd"
                    },
                    "inRange": {
                        "color": [
                            "lightskyblue",
                            "yellow",
                            "orangered"
                        ]
                    },
                    "calculable": true,
                    "inverse": false,
                    "splitNumber": 5,
                    "dimension": 0,
                    "hoverLink": true,
                    "orient": "vertical",
                    "left": "10",
                    "top": "top",
                    "padding": 5,
                    "showLabel": true,
                    "itemWidth": 20,
                    "itemHeight": 140,
                    "borderWidth": 0
                },
                {
                    "show": true,
                    "type": "continuous",
                    "min": 30,
                    "max": 97300,
                    "text": [
                        "High",
                        "Low"
                    ],
                    "textStyle": {
                        "color": "#ddd"
                    },
                    "inRange": {
                        "color": [
                            "lightskyblue",
                            "yellow",
                            "orangered"
                        ]
                    },
                    "calculable": true,
                    "inverse": false,
                    "splitNumber": 5,
                    "dimension": 0,
                    "hoverLink": true,
                    "orient": "vertical",
                    "left": "30",
                    "top": "center",
                    "padding": 5,
                    "showLabel": true,
                    "itemWidth": 20,
                    "itemHeight": 140,
                    "borderWidth": 0
                }
            ],
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
            ]
        },
        {
            "series": [
                {
                    "type": "bar",
                    "xAxisIndex": 0,
                    "yAxisIndex": 0,
                    "legendHoverLink": true,
                    "data": [
                        {
                            "name": "\u5e7f\u4e1c\u7701",
                            "value": 80855.0
                        },
                        {
                            "name": "\u6c5f\u82cf\u7701",
                            "value": 77388.0
                        },
                        {
                            "name": "\u5c71\u4e1c\u7701",
                            "value": 68024.0
                        },
                        {
                            "name": "\u6d59\u6c5f\u7701",
                            "value": 47251.0
                        },
                        {
                            "name": "\u6cb3\u5357\u7701",
                            "value": 40472.0
                        },
                        {
                            "name": "\u56db\u5ddd\u7701",
                            "value": 32935.0
                        },
                        {
                            "name": "\u6e56\u5317\u7701",
                            "value": 32665.0
                        },
                        {
                            "name": "\u6cb3\u5317\u7701",
                            "value": 32070.0
                        },
                        {
                            "name": "\u6e56\u5357\u7701",
                            "value": 31551.0
                        },
                        {
                            "name": "\u798f\u5efa\u7701",
                            "value": 28811.0
                        },
                        {
                            "name": "\u4e0a\u6d77\u5e02",
                            "value": 28179.0
                        },
                        {
                            "name": "\u5317\u4eac\u5e02",
                            "value": 25669.0
                        },
                        {
                            "name": "\u5b89\u5fbd\u7701",
                            "value": 24408.0
                        },
                        {
                            "name": "\u8fbd\u5b81\u7701",
                            "value": 22247.0
                        },
                        {
                            "name": "\u9655\u897f\u7701",
                            "value": 19400.0
                        },
                        {
                            "name": "\u6c5f\u897f\u7701",
                            "value": 18499.0
                        },
                        {
                            "name": "\u5e7f\u897f\u58ee\u65cf\u81ea\u6cbb\u533a",
                            "value": 18318.0
                        },
                        {
                            "name": "\u5185\u8499\u53e4",
                            "value": 18128.0
                        },
                        {
                            "name": "\u5929\u6d25\u5e02",
                            "value": 17885.0
                        },
                        {
                            "name": "\u91cd\u5e86\u5e02",
                            "value": 17741.0
                        },
                        {
                            "name": "\u9ed1\u9f99\u6c5f\u7701",
                            "value": 15386.0
                        },
                        {
                            "name": "\u4e91\u5357\u7701",
                            "value": 14788.0
                        },
                        {
                            "name": "\u5409\u6797\u7701",
                            "value": 14777.0
                        },
                        {
                            "name": "\u5c71\u897f\u7701",
                            "value": 13050.0
                        },
                        {
                            "name": "\u8d35\u5dde\u7701",
                            "value": 11777.0
                        },
                        {
                            "name": "\u65b0\u7586\u7ef4\u543e\u5c14\u81ea\u6cbb\u533a",
                            "value": 9650.0
                        },
                        {
                            "name": "\u7518\u8083\u7701",
                            "value": 7200.0
                        },
                        {
                            "name": "\u6d77\u5357\u7701",
                            "value": 4053.0
                        },
                        {
                            "name": "\u5b81\u590f\u56de\u65cf\u81ea\u6cbb\u533a",
                            "value": 3169.0
                        },
                        {
                            "name": "\u9752\u6d77\u7701",
                            "value": 2572.0
                        },
                        {
                            "name": "\u897f\u85cf\u81ea\u6cbb\u533a",
                            "value": 1151.0
                        }
                    ],
                    "realtimeSort": false,
                    "showBackground": false,
                    "stackStrategy": "samesign",
                    "cursor": "pointer",
                    "barMinHeight": 0,
                    "barCategoryGap": "20%",
                    "barGap": "30%",
                    "large": false,
                    "largeThreshold": 400,
                    "seriesLayoutBy": "column",
                    "datasetIndex": 0,
                    "clip": true,
                    "zlevel": 0,
                    "z": 2,
                    "label": {
                        "show": true,
                        "position": "right",
                        "margin": 8,
                        "formatter": "{b} : {c}"
                    }
                },
                {
                    "type": "line",
                    "connectNulls": false,
                    "xAxisIndex": 1,
                    "yAxisIndex": 1,
                    "symbolSize": 4,
                    "showSymbol": true,
                    "smooth": false,
                    "clip": true,
                    "step": false,
                    "data": [
                        [
                            "2013\u5e74",
                            63.4
                        ],
                        [
                            "2014\u5e74",
                            68.4
                        ],
                        [
                            "2015\u5e74",
                            72.3
                        ],
                        [
                            "2016\u5e74",
                            78
                        ],
                        [
                            "2017\u5e74",
                            84.7
                        ],
                        [
                            "2018\u5e74",
                            91.5
                        ]
                    ],
                    "hoverAnimation": true,
                    "label": {
                        "show": false,
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
                    "z": 0,
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                },
                {
                    "type": "line",
                    "connectNulls": false,
                    "xAxisIndex": 1,
                    "yAxisIndex": 1,
                    "symbolSize": 4,
                    "showSymbol": true,
                    "smooth": false,
                    "clip": true,
                    "step": false,
                    "data": [
                        [
                            "2013\u5e74",
                            ""
                        ],
                        [
                            "2014\u5e74",
                            ""
                        ],
                        [
                            "2015\u5e74",
                            ""
                        ],
                        [
                            "2016\u5e74",
                            78
                        ],
                        [
                            "2017\u5e74",
                            ""
                        ],
                        [
                            "2018\u5e74",
                            ""
                        ]
                    ],
                    "hoverAnimation": true,
                    "label": {
                        "show": false,
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
                    "markPoint": {
                        "label": {
                            "show": true,
                            "position": "inside",
                            "color": "#fff",
                            "margin": 8
                        },
                        "data": [
                            {
                                "type": "max"
                            }
                        ]
                    },
                    "zlevel": 0,
                    "z": 0,
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                },
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
                            "name": "\u5e7f\u4e1c\u7701",
                            "value": 80855.0
                        },
                        {
                            "name": "\u6c5f\u82cf\u7701",
                            "value": 77388.0
                        },
                        {
                            "name": "\u5c71\u4e1c\u7701",
                            "value": 68024.0
                        },
                        {
                            "name": "\u6d59\u6c5f\u7701",
                            "value": 47251.0
                        },
                        {
                            "name": "\u6cb3\u5357\u7701",
                            "value": 40472.0
                        },
                        {
                            "name": "\u56db\u5ddd\u7701",
                            "value": 32935.0
                        },
                        {
                            "name": "\u6e56\u5317\u7701",
                            "value": 32665.0
                        },
                        {
                            "name": "\u6cb3\u5317\u7701",
                            "value": 32070.0
                        },
                        {
                            "name": "\u6e56\u5357\u7701",
                            "value": 31551.0
                        },
                        {
                            "name": "\u798f\u5efa\u7701",
                            "value": 28811.0
                        },
                        {
                            "name": "\u4e0a\u6d77\u5e02",
                            "value": 28179.0
                        },
                        {
                            "name": "\u5317\u4eac\u5e02",
                            "value": 25669.0
                        },
                        {
                            "name": "\u5b89\u5fbd\u7701",
                            "value": 24408.0
                        },
                        {
                            "name": "\u8fbd\u5b81\u7701",
                            "value": 22247.0
                        },
                        {
                            "name": "\u9655\u897f\u7701",
                            "value": 19400.0
                        },
                        {
                            "name": "\u6c5f\u897f\u7701",
                            "value": 18499.0
                        },
                        {
                            "name": "\u5e7f\u897f\u58ee\u65cf\u81ea\u6cbb\u533a",
                            "value": 18318.0
                        },
                        {
                            "name": "\u5185\u8499\u53e4",
                            "value": 18128.0
                        },
                        {
                            "name": "\u5929\u6d25\u5e02",
                            "value": 17885.0
                        },
                        {
                            "name": "\u91cd\u5e86\u5e02",
                            "value": 17741.0
                        },
                        {
                            "name": "\u9ed1\u9f99\u6c5f\u7701",
                            "value": 15386.0
                        },
                        {
                            "name": "\u4e91\u5357\u7701",
                            "value": 14788.0
                        },
                        {
                            "name": "\u5409\u6797\u7701",
                            "value": 14777.0
                        },
                        {
                            "name": "\u5c71\u897f\u7701",
                            "value": 13050.0
                        },
                        {
                            "name": "\u8d35\u5dde\u7701",
                            "value": 11777.0
                        },
                        {
                            "name": "\u65b0\u7586\u7ef4\u543e\u5c14\u81ea\u6cbb\u533a",
                            "value": 9650.0
                        },
                        {
                            "name": "\u7518\u8083\u7701",
                            "value": 7200.0
                        },
                        {
                            "name": "\u6d77\u5357\u7701",
                            "value": 4053.0
                        },
                        {
                            "name": "\u5b81\u590f\u56de\u65cf\u81ea\u6cbb\u533a",
                            "value": 3169.0
                        },
                        {
                            "name": "\u9752\u6d77\u7701",
                            "value": 2572.0
                        },
                        {
                            "name": "\u897f\u85cf\u81ea\u6cbb\u533a",
                            "value": 1151.0
                        }
                    ],
                    "radius": [
                        "15%",
                        "35%"
                    ],
                    "center": [
                        "80%",
                        "82%"
                    ],
                    "label": {
                        "show": true,
                        "margin": 8
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
                    "itemStyle": {
                        "borderColor": "rgba(0,0,0,0.3)",
                        "borderWidth": 1
                    },
                    "xAxisIndex": 2,
                    "yAxisIndex": 2
                },
                {
                    "type": "map",
                    "label": {
                        "show": true,
                        "margin": 8
                    },
                    "map": "china",
                    "data": [
                        {
                            "name": "\u5e7f\u4e1c\u7701",
                            "value": [
                                80855.0,
                                10.37,
                                "\u5e7f\u4e1c\u7701"
                            ]
                        },
                        {
                            "name": "\u6c5f\u82cf\u7701",
                            "value": [
                                77388.0,
                                9.92,
                                "\u6c5f\u82cf\u7701"
                            ]
                        },
                        {
                            "name": "\u5c71\u4e1c\u7701",
                            "value": [
                                68024.0,
                                8.72,
                                "\u5c71\u4e1c\u7701"
                            ]
                        },
                        {
                            "name": "\u6d59\u6c5f\u7701",
                            "value": [
                                47251.0,
                                6.06,
                                "\u6d59\u6c5f\u7701"
                            ]
                        },
                        {
                            "name": "\u6cb3\u5357\u7701",
                            "value": [
                                40472.0,
                                5.19,
                                "\u6cb3\u5357\u7701"
                            ]
                        },
                        {
                            "name": "\u56db\u5ddd\u7701",
                            "value": [
                                32935.0,
                                4.22,
                                "\u56db\u5ddd\u7701"
                            ]
                        },
                        {
                            "name": "\u6e56\u5317\u7701",
                            "value": [
                                32665.0,
                                4.19,
                                "\u6e56\u5317\u7701"
                            ]
                        },
                        {
                            "name": "\u6cb3\u5317\u7701",
                            "value": [
                                32070.0,
                                4.11,
                                "\u6cb3\u5317\u7701"
                            ]
                        },
                        {
                            "name": "\u6e56\u5357\u7701",
                            "value": [
                                31551.0,
                                4.04,
                                "\u6e56\u5357\u7701"
                            ]
                        },
                        {
                            "name": "\u798f\u5efa\u7701",
                            "value": [
                                28811.0,
                                3.69,
                                "\u798f\u5efa\u7701"
                            ]
                        },
                        {
                            "name": "\u4e0a\u6d77\u5e02",
                            "value": [
                                28179.0,
                                3.61,
                                "\u4e0a\u6d77\u5e02"
                            ]
                        },
                        {
                            "name": "\u5317\u4eac\u5e02",
                            "value": [
                                25669.0,
                                3.29,
                                "\u5317\u4eac\u5e02"
                            ]
                        },
                        {
                            "name": "\u5b89\u5fbd\u7701",
                            "value": [
                                24408.0,
                                3.13,
                                "\u5b89\u5fbd\u7701"
                            ]
                        },
                        {
                            "name": "\u8fbd\u5b81\u7701",
                            "value": [
                                22247.0,
                                2.85,
                                "\u8fbd\u5b81\u7701"
                            ]
                        },
                        {
                            "name": "\u9655\u897f\u7701",
                            "value": [
                                19400.0,
                                2.49,
                                "\u9655\u897f\u7701"
                            ]
                        },
                        {
                            "name": "\u6c5f\u897f\u7701",
                            "value": [
                                18499.0,
                                2.37,
                                "\u6c5f\u897f\u7701"
                            ]
                        },
                        {
                            "name": "\u5e7f\u897f\u58ee\u65cf\u81ea\u6cbb\u533a",
                            "value": [
                                18318.0,
                                2.35,
                                "\u5e7f\u897f\u58ee\u65cf\u81ea\u6cbb\u533a"
                            ]
                        },
                        {
                            "name": "\u5185\u8499\u53e4",
                            "value": [
                                18128.0,
                                2.32,
                                "\u5185\u8499\u53e4"
                            ]
                        },
                        {
                            "name": "\u5929\u6d25\u5e02",
                            "value": [
                                17885.0,
                                2.29,
                                "\u5929\u6d25\u5e02"
                            ]
                        },
                        {
                            "name": "\u91cd\u5e86\u5e02",
                            "value": [
                                17741.0,
                                2.27,
                                "\u91cd\u5e86\u5e02"
                            ]
                        },
                        {
                            "name": "\u9ed1\u9f99\u6c5f\u7701",
                            "value": [
                                15386.0,
                                1.97,
                                "\u9ed1\u9f99\u6c5f\u7701"
                            ]
                        },
                        {
                            "name": "\u4e91\u5357\u7701",
                            "value": [
                                14788.0,
                                1.9,
                                "\u4e91\u5357\u7701"
                            ]
                        },
                        {
                            "name": "\u5409\u6797\u7701",
                            "value": [
                                14777.0,
                                1.89,
                                "\u5409\u6797\u7701"
                            ]
                        },
                        {
                            "name": "\u5c71\u897f\u7701",
                            "value": [
                                13050.0,
                                1.67,
                                "\u5c71\u897f\u7701"
                            ]
                        },
                        {
                            "name": "\u8d35\u5dde\u7701",
                            "value": [
                                11777.0,
                                1.51,
                                "\u8d35\u5dde\u7701"
                            ]
                        },
                        {
                            "name": "\u65b0\u7586\u7ef4\u543e\u5c14\u81ea\u6cbb\u533a",
                            "value": [
                                9650.0,
                                1.24,
                                "\u65b0\u7586\u7ef4\u543e\u5c14\u81ea\u6cbb\u533a"
                            ]
                        },
                        {
                            "name": "\u7518\u8083\u7701",
                            "value": [
                                7200.0,
                                0.92,
                                "\u7518\u8083\u7701"
                            ]
                        },
                        {
                            "name": "\u6d77\u5357\u7701",
                            "value": [
                                4053.0,
                                0.52,
                                "\u6d77\u5357\u7701"
                            ]
                        },
                        {
                            "name": "\u5b81\u590f\u56de\u65cf\u81ea\u6cbb\u533a",
                            "value": [
                                3169.0,
                                0.41,
                                "\u5b81\u590f\u56de\u65cf\u81ea\u6cbb\u533a"
                            ]
                        },
                        {
                            "name": "\u9752\u6d77\u7701",
                            "value": [
                                2572.0,
                                0.33,
                                "\u9752\u6d77\u7701"
                            ]
                        },
                        {
                            "name": "\u897f\u85cf\u81ea\u6cbb\u533a",
                            "value": [
                                1151.0,
                                0.15,
                                "\u897f\u85cf\u81ea\u6cbb\u533a"
                            ]
                        }
                    ],
                    "roam": true,
                    "aspectScale": 0.75,
                    "nameProperty": "name",
                    "selectedMode": false,
                    "center": [
                        119.5,
                        34.5
                    ],
                    "zoom": 1,
                    "zlevel": 0,
                    "z": 2,
                    "seriesLayoutBy": "column",
                    "datasetIndex": 0,
                    "mapValueCalculation": "sum",
                    "showLegendSymbol": false,
                    "itemStyle": {
                        "normal": {
                            "areaColor": "#323c48",
                            "borderColor": "#404a59"
                        },
                        "emphasis": {
                            "label": {
                                "show": null
                            },
                            "areaColor": "rgba(255,255,255, 0.5)"
                        }
                    },
                    "emphasis": {},
                    "xAxisIndex": 3,
                    "yAxisIndex": 3
                }
            ],
            "xAxis": [
                {
                    "show": true,
                    "scale": false,
                    "nameLocation": "end",
                    "nameGap": 15,
                    "gridIndex": 0,
                    "axisLabel": {
                        "show": false,
                        "margin": 8
                    },
                    "inverse": false,
                    "offset": 0,
                    "splitNumber": 5,
                    "max": 97300,
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
                },
                {
                    "show": true,
                    "scale": false,
                    "nameLocation": "end",
                    "nameGap": 15,
                    "gridIndex": 1,
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
                        "2013\u5e74",
                        "2014\u5e74",
                        "2015\u5e74",
                        "2016\u5e74",
                        "2017\u5e74",
                        "2018\u5e74"
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
                    "axisLabel": {
                        "show": false,
                        "margin": 8
                    },
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
                        "\u5e7f\u4e1c\u7701",
                        "\u6c5f\u82cf\u7701",
                        "\u5c71\u4e1c\u7701",
                        "\u6d59\u6c5f\u7701",
                        "\u6cb3\u5357\u7701",
                        "\u56db\u5ddd\u7701",
                        "\u6e56\u5317\u7701",
                        "\u6cb3\u5317\u7701",
                        "\u6e56\u5357\u7701",
                        "\u798f\u5efa\u7701",
                        "\u4e0a\u6d77\u5e02",
                        "\u5317\u4eac\u5e02",
                        "\u5b89\u5fbd\u7701",
                        "\u8fbd\u5b81\u7701",
                        "\u9655\u897f\u7701",
                        "\u6c5f\u897f\u7701",
                        "\u5e7f\u897f\u58ee\u65cf\u81ea\u6cbb\u533a",
                        "\u5185\u8499\u53e4",
                        "\u5929\u6d25\u5e02",
                        "\u91cd\u5e86\u5e02",
                        "\u9ed1\u9f99\u6c5f\u7701",
                        "\u4e91\u5357\u7701",
                        "\u5409\u6797\u7701",
                        "\u5c71\u897f\u7701",
                        "\u8d35\u5dde\u7701",
                        "\u65b0\u7586\u7ef4\u543e\u5c14\u81ea\u6cbb\u533a",
                        "\u7518\u8083\u7701",
                        "\u6d77\u5357\u7701",
                        "\u5b81\u590f\u56de\u65cf\u81ea\u6cbb\u533a",
                        "\u9752\u6d77\u7701",
                        "\u897f\u85cf\u81ea\u6cbb\u533a"
                    ]
                },
                {
                    "show": true,
                    "scale": false,
                    "nameLocation": "end",
                    "nameGap": 15,
                    "gridIndex": 1,
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
                    "target": "blank",
                    "subtarget": "blank",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false
                },
                {
                    "show": true,
                    "text": "\u5168\u56fdGDP\u603b\u91cf2016\u5e74\uff08\u5355\u4f4d\uff1a\u4e07\u4ebf\uff09",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "50%",
                    "top": "5%",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false
                },
                {
                    "show": true,
                    "target": "blank",
                    "subtarget": "blank",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false
                },
                {
                    "show": true,
                    "text": "2016\u5e74\u5168\u56fd\u5206\u5730\u533aGPD\u60c5\u51b5\uff08\u5355\u4f4d\uff1a\u4ebf\uff09 \u6570\u636e\u6765\u6e90\uff1a\u56fd\u5bb6\u7edf\u8ba1\u5c40",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "center",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "color": "rgba(255,255,255, 0.9)",
                        "fontSize": 25
                    }
                }
            ],
            "tooltip": {
                "show": false,
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
            },
            "visualMap": [
                {
                    "show": true,
                    "type": "continuous",
                    "min": 30,
                    "max": 97300,
                    "text": [
                        "High",
                        "Low"
                    ],
                    "textStyle": {
                        "color": "#ddd"
                    },
                    "inRange": {
                        "color": [
                            "lightskyblue",
                            "yellow",
                            "orangered"
                        ]
                    },
                    "calculable": true,
                    "inverse": false,
                    "splitNumber": 5,
                    "dimension": 0,
                    "hoverLink": true,
                    "orient": "vertical",
                    "left": "10",
                    "top": "top",
                    "padding": 5,
                    "showLabel": true,
                    "itemWidth": 20,
                    "itemHeight": 140,
                    "borderWidth": 0
                },
                {
                    "show": true,
                    "type": "continuous",
                    "min": 30,
                    "max": 97300,
                    "text": [
                        "High",
                        "Low"
                    ],
                    "textStyle": {
                        "color": "#ddd"
                    },
                    "inRange": {
                        "color": [
                            "lightskyblue",
                            "yellow",
                            "orangered"
                        ]
                    },
                    "calculable": true,
                    "inverse": false,
                    "splitNumber": 5,
                    "dimension": 0,
                    "hoverLink": true,
                    "orient": "vertical",
                    "left": "30",
                    "top": "center",
                    "padding": 5,
                    "showLabel": true,
                    "itemWidth": 20,
                    "itemHeight": 140,
                    "borderWidth": 0
                }
            ],
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
            ]
        },
        {
            "series": [
                {
                    "type": "bar",
                    "xAxisIndex": 0,
                    "yAxisIndex": 0,
                    "legendHoverLink": true,
                    "data": [
                        {
                            "name": "\u5e7f\u4e1c\u7701",
                            "value": 89705.0
                        },
                        {
                            "name": "\u6c5f\u82cf\u7701",
                            "value": 85870.0
                        },
                        {
                            "name": "\u5c71\u4e1c\u7701",
                            "value": 72634.0
                        },
                        {
                            "name": "\u6d59\u6c5f\u7701",
                            "value": 51768.0
                        },
                        {
                            "name": "\u6cb3\u5357\u7701",
                            "value": 44553.0
                        },
                        {
                            "name": "\u56db\u5ddd\u7701",
                            "value": 36980.0
                        },
                        {
                            "name": "\u6e56\u5317\u7701",
                            "value": 35478.0
                        },
                        {
                            "name": "\u6cb3\u5317\u7701",
                            "value": 34016.0
                        },
                        {
                            "name": "\u6e56\u5357\u7701",
                            "value": 33903.0
                        },
                        {
                            "name": "\u798f\u5efa\u7701",
                            "value": 32182.0
                        },
                        {
                            "name": "\u4e0a\u6d77\u5e02",
                            "value": 30633.0
                        },
                        {
                            "name": "\u5317\u4eac\u5e02",
                            "value": 28015.0
                        },
                        {
                            "name": "\u5b89\u5fbd\u7701",
                            "value": 27018.0
                        },
                        {
                            "name": "\u8fbd\u5b81\u7701",
                            "value": 23409.0
                        },
                        {
                            "name": "\u9655\u897f\u7701",
                            "value": 21899.0
                        },
                        {
                            "name": "\u6c5f\u897f\u7701",
                            "value": 20006.0
                        },
                        {
                            "name": "\u91cd\u5e86\u5e02",
                            "value": 19425.0
                        },
                        {
                            "name": "\u5929\u6d25\u5e02",
                            "value": 18549.0
                        },
                        {
                            "name": "\u5e7f\u897f\u58ee\u65cf\u81ea\u6cbb\u533a",
                            "value": 18523.0
                        },
                        {
                            "name": "\u4e91\u5357\u7701",
                            "value": 16376.0
                        },
                        {
                            "name": "\u5185\u8499\u53e4",
                            "value": 16096.0
                        },
                        {
                            "name": "\u9ed1\u9f99\u6c5f\u7701",
                            "value": 15903.0
                        },
                        {
                            "name": "\u5c71\u897f\u7701",
                            "value": 15528.0
                        },
                        {
                            "name": "\u5409\u6797\u7701",
                            "value": 14945.0
                        },
                        {
                            "name": "\u8d35\u5dde\u7701",
                            "value": 13541.0
                        },
                        {
                            "name": "\u65b0\u7586\u7ef4\u543e\u5c14\u81ea\u6cbb\u533a",
                            "value": 10882.0
                        },
                        {
                            "name": "\u7518\u8083\u7701",
                            "value": 7460.0
                        },
                        {
                            "name": "\u6d77\u5357\u7701",
                            "value": 4463.0
                        },
                        {
                            "name": "\u5b81\u590f\u56de\u65cf\u81ea\u6cbb\u533a",
                            "value": 3444.0
                        },
                        {
                            "name": "\u9752\u6d77\u7701",
                            "value": 2625.0
                        },
                        {
                            "name": "\u897f\u85cf\u81ea\u6cbb\u533a",
                            "value": 1311.0
                        }
                    ],
                    "realtimeSort": false,
                    "showBackground": false,
                    "stackStrategy": "samesign",
                    "cursor": "pointer",
                    "barMinHeight": 0,
                    "barCategoryGap": "20%",
                    "barGap": "30%",
                    "large": false,
                    "largeThreshold": 400,
                    "seriesLayoutBy": "column",
                    "datasetIndex": 0,
                    "clip": true,
                    "zlevel": 0,
                    "z": 2,
                    "label": {
                        "show": true,
                        "position": "right",
                        "margin": 8,
                        "formatter": "{b} : {c}"
                    }
                },
                {
                    "type": "line",
                    "connectNulls": false,
                    "xAxisIndex": 1,
                    "yAxisIndex": 1,
                    "symbolSize": 4,
                    "showSymbol": true,
                    "smooth": false,
                    "clip": true,
                    "step": false,
                    "data": [
                        [
                            "2013\u5e74",
                            63.4
                        ],
                        [
                            "2014\u5e74",
                            68.4
                        ],
                        [
                            "2015\u5e74",
                            72.3
                        ],
                        [
                            "2016\u5e74",
                            78
                        ],
                        [
                            "2017\u5e74",
                            84.7
                        ],
                        [
                            "2018\u5e74",
                            91.5
                        ]
                    ],
                    "hoverAnimation": true,
                    "label": {
                        "show": false,
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
                    "z": 0,
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                },
                {
                    "type": "line",
                    "connectNulls": false,
                    "xAxisIndex": 1,
                    "yAxisIndex": 1,
                    "symbolSize": 4,
                    "showSymbol": true,
                    "smooth": false,
                    "clip": true,
                    "step": false,
                    "data": [
                        [
                            "2013\u5e74",
                            ""
                        ],
                        [
                            "2014\u5e74",
                            ""
                        ],
                        [
                            "2015\u5e74",
                            ""
                        ],
                        [
                            "2016\u5e74",
                            ""
                        ],
                        [
                            "2017\u5e74",
                            84.7
                        ],
                        [
                            "2018\u5e74",
                            ""
                        ]
                    ],
                    "hoverAnimation": true,
                    "label": {
                        "show": false,
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
                    "markPoint": {
                        "label": {
                            "show": true,
                            "position": "inside",
                            "color": "#fff",
                            "margin": 8
                        },
                        "data": [
                            {
                                "type": "max"
                            }
                        ]
                    },
                    "zlevel": 0,
                    "z": 0,
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                },
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
                            "name": "\u5e7f\u4e1c\u7701",
                            "value": 89705.0
                        },
                        {
                            "name": "\u6c5f\u82cf\u7701",
                            "value": 85870.0
                        },
                        {
                            "name": "\u5c71\u4e1c\u7701",
                            "value": 72634.0
                        },
                        {
                            "name": "\u6d59\u6c5f\u7701",
                            "value": 51768.0
                        },
                        {
                            "name": "\u6cb3\u5357\u7701",
                            "value": 44553.0
                        },
                        {
                            "name": "\u56db\u5ddd\u7701",
                            "value": 36980.0
                        },
                        {
                            "name": "\u6e56\u5317\u7701",
                            "value": 35478.0
                        },
                        {
                            "name": "\u6cb3\u5317\u7701",
                            "value": 34016.0
                        },
                        {
                            "name": "\u6e56\u5357\u7701",
                            "value": 33903.0
                        },
                        {
                            "name": "\u798f\u5efa\u7701",
                            "value": 32182.0
                        },
                        {
                            "name": "\u4e0a\u6d77\u5e02",
                            "value": 30633.0
                        },
                        {
                            "name": "\u5317\u4eac\u5e02",
                            "value": 28015.0
                        },
                        {
                            "name": "\u5b89\u5fbd\u7701",
                            "value": 27018.0
                        },
                        {
                            "name": "\u8fbd\u5b81\u7701",
                            "value": 23409.0
                        },
                        {
                            "name": "\u9655\u897f\u7701",
                            "value": 21899.0
                        },
                        {
                            "name": "\u6c5f\u897f\u7701",
                            "value": 20006.0
                        },
                        {
                            "name": "\u91cd\u5e86\u5e02",
                            "value": 19425.0
                        },
                        {
                            "name": "\u5929\u6d25\u5e02",
                            "value": 18549.0
                        },
                        {
                            "name": "\u5e7f\u897f\u58ee\u65cf\u81ea\u6cbb\u533a",
                            "value": 18523.0
                        },
                        {
                            "name": "\u4e91\u5357\u7701",
                            "value": 16376.0
                        },
                        {
                            "name": "\u5185\u8499\u53e4",
                            "value": 16096.0
                        },
                        {
                            "name": "\u9ed1\u9f99\u6c5f\u7701",
                            "value": 15903.0
                        },
                        {
                            "name": "\u5c71\u897f\u7701",
                            "value": 15528.0
                        },
                        {
                            "name": "\u5409\u6797\u7701",
                            "value": 14945.0
                        },
                        {
                            "name": "\u8d35\u5dde\u7701",
                            "value": 13541.0
                        },
                        {
                            "name": "\u65b0\u7586\u7ef4\u543e\u5c14\u81ea\u6cbb\u533a",
                            "value": 10882.0
                        },
                        {
                            "name": "\u7518\u8083\u7701",
                            "value": 7460.0
                        },
                        {
                            "name": "\u6d77\u5357\u7701",
                            "value": 4463.0
                        },
                        {
                            "name": "\u5b81\u590f\u56de\u65cf\u81ea\u6cbb\u533a",
                            "value": 3444.0
                        },
                        {
                            "name": "\u9752\u6d77\u7701",
                            "value": 2625.0
                        },
                        {
                            "name": "\u897f\u85cf\u81ea\u6cbb\u533a",
                            "value": 1311.0
                        }
                    ],
                    "radius": [
                        "15%",
                        "35%"
                    ],
                    "center": [
                        "80%",
                        "82%"
                    ],
                    "label": {
                        "show": true,
                        "margin": 8
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
                    "itemStyle": {
                        "borderColor": "rgba(0,0,0,0.3)",
                        "borderWidth": 1
                    },
                    "xAxisIndex": 2,
                    "yAxisIndex": 2
                },
                {
                    "type": "map",
                    "label": {
                        "show": true,
                        "margin": 8
                    },
                    "map": "china",
                    "data": [
                        {
                            "name": "\u5e7f\u4e1c\u7701",
                            "value": [
                                89705.0,
                                10.59,
                                "\u5e7f\u4e1c\u7701"
                            ]
                        },
                        {
                            "name": "\u6c5f\u82cf\u7701",
                            "value": [
                                85870.0,
                                10.14,
                                "\u6c5f\u82cf\u7701"
                            ]
                        },
                        {
                            "name": "\u5c71\u4e1c\u7701",
                            "value": [
                                72634.0,
                                8.57,
                                "\u5c71\u4e1c\u7701"
                            ]
                        },
                        {
                            "name": "\u6d59\u6c5f\u7701",
                            "value": [
                                51768.0,
                                6.11,
                                "\u6d59\u6c5f\u7701"
                            ]
                        },
                        {
                            "name": "\u6cb3\u5357\u7701",
                            "value": [
                                44553.0,
                                5.26,
                                "\u6cb3\u5357\u7701"
                            ]
                        },
                        {
                            "name": "\u56db\u5ddd\u7701",
                            "value": [
                                36980.0,
                                4.37,
                                "\u56db\u5ddd\u7701"
                            ]
                        },
                        {
                            "name": "\u6e56\u5317\u7701",
                            "value": [
                                35478.0,
                                4.19,
                                "\u6e56\u5317\u7701"
                            ]
                        },
                        {
                            "name": "\u6cb3\u5317\u7701",
                            "value": [
                                34016.0,
                                4.02,
                                "\u6cb3\u5317\u7701"
                            ]
                        },
                        {
                            "name": "\u6e56\u5357\u7701",
                            "value": [
                                33903.0,
                                4.0,
                                "\u6e56\u5357\u7701"
                            ]
                        },
                        {
                            "name": "\u798f\u5efa\u7701",
                            "value": [
                                32182.0,
                                3.8,
                                "\u798f\u5efa\u7701"
                            ]
                        },
                        {
                            "name": "\u4e0a\u6d77\u5e02",
                            "value": [
                                30633.0,
                                3.62,
                                "\u4e0a\u6d77\u5e02"
                            ]
                        },
                        {
                            "name": "\u5317\u4eac\u5e02",
                            "value": [
                                28015.0,
                                3.31,
                                "\u5317\u4eac\u5e02"
                            ]
                        },
                        {
                            "name": "\u5b89\u5fbd\u7701",
                            "value": [
                                27018.0,
                                3.19,
                                "\u5b89\u5fbd\u7701"
                            ]
                        },
                        {
                            "name": "\u8fbd\u5b81\u7701",
                            "value": [
                                23409.0,
                                2.76,
                                "\u8fbd\u5b81\u7701"
                            ]
                        },
                        {
                            "name": "\u9655\u897f\u7701",
                            "value": [
                                21899.0,
                                2.59,
                                "\u9655\u897f\u7701"
                            ]
                        },
                        {
                            "name": "\u6c5f\u897f\u7701",
                            "value": [
                                20006.0,
                                2.36,
                                "\u6c5f\u897f\u7701"
                            ]
                        },
                        {
                            "name": "\u91cd\u5e86\u5e02",
                            "value": [
                                19425.0,
                                2.29,
                                "\u91cd\u5e86\u5e02"
                            ]
                        },
                        {
                            "name": "\u5929\u6d25\u5e02",
                            "value": [
                                18549.0,
                                2.19,
                                "\u5929\u6d25\u5e02"
                            ]
                        },
                        {
                            "name": "\u5e7f\u897f\u58ee\u65cf\u81ea\u6cbb\u533a",
                            "value": [
                                18523.0,
                                2.19,
                                "\u5e7f\u897f\u58ee\u65cf\u81ea\u6cbb\u533a"
                            ]
                        },
                        {
                            "name": "\u4e91\u5357\u7701",
                            "value": [
                                16376.0,
                                1.93,
                                "\u4e91\u5357\u7701"
                            ]
                        },
                        {
                            "name": "\u5185\u8499\u53e4",
                            "value": [
                                16096.0,
                                1.9,
                                "\u5185\u8499\u53e4"
                            ]
                        },
                        {
                            "name": "\u9ed1\u9f99\u6c5f\u7701",
                            "value": [
                                15903.0,
                                1.88,
                                "\u9ed1\u9f99\u6c5f\u7701"
                            ]
                        },
                        {
                            "name": "\u5c71\u897f\u7701",
                            "value": [
                                15528.0,
                                1.83,
                                "\u5c71\u897f\u7701"
                            ]
                        },
                        {
                            "name": "\u5409\u6797\u7701",
                            "value": [
                                14945.0,
                                1.76,
                                "\u5409\u6797\u7701"
                            ]
                        },
                        {
                            "name": "\u8d35\u5dde\u7701",
                            "value": [
                                13541.0,
                                1.6,
                                "\u8d35\u5dde\u7701"
                            ]
                        },
                        {
                            "name": "\u65b0\u7586\u7ef4\u543e\u5c14\u81ea\u6cbb\u533a",
                            "value": [
                                10882.0,
                                1.28,
                                "\u65b0\u7586\u7ef4\u543e\u5c14\u81ea\u6cbb\u533a"
                            ]
                        },
                        {
                            "name": "\u7518\u8083\u7701",
                            "value": [
                                7460.0,
                                0.88,
                                "\u7518\u8083\u7701"
                            ]
                        },
                        {
                            "name": "\u6d77\u5357\u7701",
                            "value": [
                                4463.0,
                                0.53,
                                "\u6d77\u5357\u7701"
                            ]
                        },
                        {
                            "name": "\u5b81\u590f\u56de\u65cf\u81ea\u6cbb\u533a",
                            "value": [
                                3444.0,
                                0.41,
                                "\u5b81\u590f\u56de\u65cf\u81ea\u6cbb\u533a"
                            ]
                        },
                        {
                            "name": "\u9752\u6d77\u7701",
                            "value": [
                                2625.0,
                                0.31,
                                "\u9752\u6d77\u7701"
                            ]
                        },
                        {
                            "name": "\u897f\u85cf\u81ea\u6cbb\u533a",
                            "value": [
                                1311.0,
                                0.15,
                                "\u897f\u85cf\u81ea\u6cbb\u533a"
                            ]
                        }
                    ],
                    "roam": true,
                    "aspectScale": 0.75,
                    "nameProperty": "name",
                    "selectedMode": false,
                    "center": [
                        119.5,
                        34.5
                    ],
                    "zoom": 1,
                    "zlevel": 0,
                    "z": 2,
                    "seriesLayoutBy": "column",
                    "datasetIndex": 0,
                    "mapValueCalculation": "sum",
                    "showLegendSymbol": false,
                    "itemStyle": {
                        "normal": {
                            "areaColor": "#323c48",
                            "borderColor": "#404a59"
                        },
                        "emphasis": {
                            "label": {
                                "show": null
                            },
                            "areaColor": "rgba(255,255,255, 0.5)"
                        }
                    },
                    "emphasis": {},
                    "xAxisIndex": 3,
                    "yAxisIndex": 3
                }
            ],
            "xAxis": [
                {
                    "show": true,
                    "scale": false,
                    "nameLocation": "end",
                    "nameGap": 15,
                    "gridIndex": 0,
                    "axisLabel": {
                        "show": false,
                        "margin": 8
                    },
                    "inverse": false,
                    "offset": 0,
                    "splitNumber": 5,
                    "max": 97300,
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
                },
                {
                    "show": true,
                    "scale": false,
                    "nameLocation": "end",
                    "nameGap": 15,
                    "gridIndex": 1,
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
                        "2013\u5e74",
                        "2014\u5e74",
                        "2015\u5e74",
                        "2016\u5e74",
                        "2017\u5e74",
                        "2018\u5e74"
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
                    "axisLabel": {
                        "show": false,
                        "margin": 8
                    },
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
                        "\u5e7f\u4e1c\u7701",
                        "\u6c5f\u82cf\u7701",
                        "\u5c71\u4e1c\u7701",
                        "\u6d59\u6c5f\u7701",
                        "\u6cb3\u5357\u7701",
                        "\u56db\u5ddd\u7701",
                        "\u6e56\u5317\u7701",
                        "\u6cb3\u5317\u7701",
                        "\u6e56\u5357\u7701",
                        "\u798f\u5efa\u7701",
                        "\u4e0a\u6d77\u5e02",
                        "\u5317\u4eac\u5e02",
                        "\u5b89\u5fbd\u7701",
                        "\u8fbd\u5b81\u7701",
                        "\u9655\u897f\u7701",
                        "\u6c5f\u897f\u7701",
                        "\u91cd\u5e86\u5e02",
                        "\u5929\u6d25\u5e02",
                        "\u5e7f\u897f\u58ee\u65cf\u81ea\u6cbb\u533a",
                        "\u4e91\u5357\u7701",
                        "\u5185\u8499\u53e4",
                        "\u9ed1\u9f99\u6c5f\u7701",
                        "\u5c71\u897f\u7701",
                        "\u5409\u6797\u7701",
                        "\u8d35\u5dde\u7701",
                        "\u65b0\u7586\u7ef4\u543e\u5c14\u81ea\u6cbb\u533a",
                        "\u7518\u8083\u7701",
                        "\u6d77\u5357\u7701",
                        "\u5b81\u590f\u56de\u65cf\u81ea\u6cbb\u533a",
                        "\u9752\u6d77\u7701",
                        "\u897f\u85cf\u81ea\u6cbb\u533a"
                    ]
                },
                {
                    "show": true,
                    "scale": false,
                    "nameLocation": "end",
                    "nameGap": 15,
                    "gridIndex": 1,
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
                    "target": "blank",
                    "subtarget": "blank",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false
                },
                {
                    "show": true,
                    "text": "\u5168\u56fdGDP\u603b\u91cf2017\u5e74\uff08\u5355\u4f4d\uff1a\u4e07\u4ebf\uff09",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "50%",
                    "top": "5%",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false
                },
                {
                    "show": true,
                    "target": "blank",
                    "subtarget": "blank",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false
                },
                {
                    "show": true,
                    "text": "2017\u5e74\u5168\u56fd\u5206\u5730\u533aGPD\u60c5\u51b5\uff08\u5355\u4f4d\uff1a\u4ebf\uff09 \u6570\u636e\u6765\u6e90\uff1a\u56fd\u5bb6\u7edf\u8ba1\u5c40",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "center",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "color": "rgba(255,255,255, 0.9)",
                        "fontSize": 25
                    }
                }
            ],
            "tooltip": {
                "show": false,
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
            },
            "visualMap": [
                {
                    "show": true,
                    "type": "continuous",
                    "min": 30,
                    "max": 97300,
                    "text": [
                        "High",
                        "Low"
                    ],
                    "textStyle": {
                        "color": "#ddd"
                    },
                    "inRange": {
                        "color": [
                            "lightskyblue",
                            "yellow",
                            "orangered"
                        ]
                    },
                    "calculable": true,
                    "inverse": false,
                    "splitNumber": 5,
                    "dimension": 0,
                    "hoverLink": true,
                    "orient": "vertical",
                    "left": "10",
                    "top": "top",
                    "padding": 5,
                    "showLabel": true,
                    "itemWidth": 20,
                    "itemHeight": 140,
                    "borderWidth": 0
                },
                {
                    "show": true,
                    "type": "continuous",
                    "min": 30,
                    "max": 97300,
                    "text": [
                        "High",
                        "Low"
                    ],
                    "textStyle": {
                        "color": "#ddd"
                    },
                    "inRange": {
                        "color": [
                            "lightskyblue",
                            "yellow",
                            "orangered"
                        ]
                    },
                    "calculable": true,
                    "inverse": false,
                    "splitNumber": 5,
                    "dimension": 0,
                    "hoverLink": true,
                    "orient": "vertical",
                    "left": "30",
                    "top": "center",
                    "padding": 5,
                    "showLabel": true,
                    "itemWidth": 20,
                    "itemHeight": 140,
                    "borderWidth": 0
                }
            ],
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
            ]
        },
        {
            "series": [
                {
                    "type": "bar",
                    "xAxisIndex": 0,
                    "yAxisIndex": 0,
                    "legendHoverLink": true,
                    "data": [
                        {
                            "name": "\u5e7f\u4e1c\u7701",
                            "value": 97278.0
                        },
                        {
                            "name": "\u6c5f\u82cf\u7701",
                            "value": 92595.0
                        },
                        {
                            "name": "\u5c71\u4e1c\u7701",
                            "value": 76470.0
                        },
                        {
                            "name": "\u6d59\u6c5f\u7701",
                            "value": 56197.0
                        },
                        {
                            "name": "\u6cb3\u5357\u7701",
                            "value": 48056.0
                        },
                        {
                            "name": "\u56db\u5ddd\u7701",
                            "value": 40678.0
                        },
                        {
                            "name": "\u6e56\u5317\u7701",
                            "value": 39367.0
                        },
                        {
                            "name": "\u6e56\u5357\u7701",
                            "value": 36426.0
                        },
                        {
                            "name": "\u6cb3\u5317\u7701",
                            "value": 36010.0
                        },
                        {
                            "name": "\u798f\u5efa\u7701",
                            "value": 35804.0
                        },
                        {
                            "name": "\u4e0a\u6d77\u5e02",
                            "value": 32680.0
                        },
                        {
                            "name": "\u5317\u4eac\u5e02",
                            "value": 30320.0
                        },
                        {
                            "name": "\u5b89\u5fbd\u7701",
                            "value": 30007.0
                        },
                        {
                            "name": "\u8fbd\u5b81\u7701",
                            "value": 25315.0
                        },
                        {
                            "name": "\u9655\u897f\u7701",
                            "value": 24438.0
                        },
                        {
                            "name": "\u6c5f\u897f\u7701",
                            "value": 21985.0
                        },
                        {
                            "name": "\u91cd\u5e86\u5e02",
                            "value": 20363.0
                        },
                        {
                            "name": "\u5e7f\u897f\u58ee\u65cf\u81ea\u6cbb\u533a",
                            "value": 20353.0
                        },
                        {
                            "name": "\u5929\u6d25\u5e02",
                            "value": 18810.0
                        },
                        {
                            "name": "\u4e91\u5357\u7701",
                            "value": 17881.0
                        },
                        {
                            "name": "\u5185\u8499\u53e4",
                            "value": 17289.0
                        },
                        {
                            "name": "\u5c71\u897f\u7701",
                            "value": 16818.0
                        },
                        {
                            "name": "\u9ed1\u9f99\u6c5f\u7701",
                            "value": 16362.0
                        },
                        {
                            "name": "\u5409\u6797\u7701",
                            "value": 15075.0
                        },
                        {
                            "name": "\u8d35\u5dde\u7701",
                            "value": 14806.0
                        },
                        {
                            "name": "\u65b0\u7586\u7ef4\u543e\u5c14\u81ea\u6cbb\u533a",
                            "value": 12199.0
                        },
                        {
                            "name": "\u7518\u8083\u7701",
                            "value": 8246.0
                        },
                        {
                            "name": "\u6d77\u5357\u7701",
                            "value": 4832.0
                        },
                        {
                            "name": "\u5b81\u590f\u56de\u65cf\u81ea\u6cbb\u533a",
                            "value": 3705.0
                        },
                        {
                            "name": "\u9752\u6d77\u7701",
                            "value": 2865.0
                        },
                        {
                            "name": "\u897f\u85cf\u81ea\u6cbb\u533a",
                            "value": 1478.0
                        }
                    ],
                    "realtimeSort": false,
                    "showBackground": false,
                    "stackStrategy": "samesign",
                    "cursor": "pointer",
                    "barMinHeight": 0,
                    "barCategoryGap": "20%",
                    "barGap": "30%",
                    "large": false,
                    "largeThreshold": 400,
                    "seriesLayoutBy": "column",
                    "datasetIndex": 0,
                    "clip": true,
                    "zlevel": 0,
                    "z": 2,
                    "label": {
                        "show": true,
                        "position": "right",
                        "margin": 8,
                        "formatter": "{b} : {c}"
                    }
                },
                {
                    "type": "line",
                    "connectNulls": false,
                    "xAxisIndex": 1,
                    "yAxisIndex": 1,
                    "symbolSize": 4,
                    "showSymbol": true,
                    "smooth": false,
                    "clip": true,
                    "step": false,
                    "data": [
                        [
                            "2013\u5e74",
                            63.4
                        ],
                        [
                            "2014\u5e74",
                            68.4
                        ],
                        [
                            "2015\u5e74",
                            72.3
                        ],
                        [
                            "2016\u5e74",
                            78
                        ],
                        [
                            "2017\u5e74",
                            84.7
                        ],
                        [
                            "2018\u5e74",
                            91.5
                        ]
                    ],
                    "hoverAnimation": true,
                    "label": {
                        "show": false,
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
                    "z": 0,
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                },
                {
                    "type": "line",
                    "connectNulls": false,
                    "xAxisIndex": 1,
                    "yAxisIndex": 1,
                    "symbolSize": 4,
                    "showSymbol": true,
                    "smooth": false,
                    "clip": true,
                    "step": false,
                    "data": [
                        [
                            "2013\u5e74",
                            ""
                        ],
                        [
                            "2014\u5e74",
                            ""
                        ],
                        [
                            "2015\u5e74",
                            ""
                        ],
                        [
                            "2016\u5e74",
                            ""
                        ],
                        [
                            "2017\u5e74",
                            ""
                        ],
                        [
                            "2018\u5e74",
                            91.5
                        ]
                    ],
                    "hoverAnimation": true,
                    "label": {
                        "show": false,
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
                    "markPoint": {
                        "label": {
                            "show": true,
                            "position": "inside",
                            "color": "#fff",
                            "margin": 8
                        },
                        "data": [
                            {
                                "type": "max"
                            }
                        ]
                    },
                    "zlevel": 0,
                    "z": 0,
                    "rippleEffect": {
                        "show": true,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }
                },
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
                            "name": "\u5e7f\u4e1c\u7701",
                            "value": 97278.0
                        },
                        {
                            "name": "\u6c5f\u82cf\u7701",
                            "value": 92595.0
                        },
                        {
                            "name": "\u5c71\u4e1c\u7701",
                            "value": 76470.0
                        },
                        {
                            "name": "\u6d59\u6c5f\u7701",
                            "value": 56197.0
                        },
                        {
                            "name": "\u6cb3\u5357\u7701",
                            "value": 48056.0
                        },
                        {
                            "name": "\u56db\u5ddd\u7701",
                            "value": 40678.0
                        },
                        {
                            "name": "\u6e56\u5317\u7701",
                            "value": 39367.0
                        },
                        {
                            "name": "\u6e56\u5357\u7701",
                            "value": 36426.0
                        },
                        {
                            "name": "\u6cb3\u5317\u7701",
                            "value": 36010.0
                        },
                        {
                            "name": "\u798f\u5efa\u7701",
                            "value": 35804.0
                        },
                        {
                            "name": "\u4e0a\u6d77\u5e02",
                            "value": 32680.0
                        },
                        {
                            "name": "\u5317\u4eac\u5e02",
                            "value": 30320.0
                        },
                        {
                            "name": "\u5b89\u5fbd\u7701",
                            "value": 30007.0
                        },
                        {
                            "name": "\u8fbd\u5b81\u7701",
                            "value": 25315.0
                        },
                        {
                            "name": "\u9655\u897f\u7701",
                            "value": 24438.0
                        },
                        {
                            "name": "\u6c5f\u897f\u7701",
                            "value": 21985.0
                        },
                        {
                            "name": "\u91cd\u5e86\u5e02",
                            "value": 20363.0
                        },
                        {
                            "name": "\u5e7f\u897f\u58ee\u65cf\u81ea\u6cbb\u533a",
                            "value": 20353.0
                        },
                        {
                            "name": "\u5929\u6d25\u5e02",
                            "value": 18810.0
                        },
                        {
                            "name": "\u4e91\u5357\u7701",
                            "value": 17881.0
                        },
                        {
                            "name": "\u5185\u8499\u53e4",
                            "value": 17289.0
                        },
                        {
                            "name": "\u5c71\u897f\u7701",
                            "value": 16818.0
                        },
                        {
                            "name": "\u9ed1\u9f99\u6c5f\u7701",
                            "value": 16362.0
                        },
                        {
                            "name": "\u5409\u6797\u7701",
                            "value": 15075.0
                        },
                        {
                            "name": "\u8d35\u5dde\u7701",
                            "value": 14806.0
                        },
                        {
                            "name": "\u65b0\u7586\u7ef4\u543e\u5c14\u81ea\u6cbb\u533a",
                            "value": 12199.0
                        },
                        {
                            "name": "\u7518\u8083\u7701",
                            "value": 8246.0
                        },
                        {
                            "name": "\u6d77\u5357\u7701",
                            "value": 4832.0
                        },
                        {
                            "name": "\u5b81\u590f\u56de\u65cf\u81ea\u6cbb\u533a",
                            "value": 3705.0
                        },
                        {
                            "name": "\u9752\u6d77\u7701",
                            "value": 2865.0
                        },
                        {
                            "name": "\u897f\u85cf\u81ea\u6cbb\u533a",
                            "value": 1478.0
                        }
                    ],
                    "radius": [
                        "15%",
                        "35%"
                    ],
                    "center": [
                        "80%",
                        "82%"
                    ],
                    "label": {
                        "show": true,
                        "margin": 8
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
                    "itemStyle": {
                        "borderColor": "rgba(0,0,0,0.3)",
                        "borderWidth": 1
                    },
                    "xAxisIndex": 2,
                    "yAxisIndex": 2
                },
                {
                    "type": "map",
                    "label": {
                        "show": true,
                        "margin": 8
                    },
                    "map": "china",
                    "data": [
                        {
                            "name": "\u5e7f\u4e1c\u7701",
                            "value": [
                                97278.0,
                                10.63,
                                "\u5e7f\u4e1c\u7701"
                            ]
                        },
                        {
                            "name": "\u6c5f\u82cf\u7701",
                            "value": [
                                92595.0,
                                10.12,
                                "\u6c5f\u82cf\u7701"
                            ]
                        },
                        {
                            "name": "\u5c71\u4e1c\u7701",
                            "value": [
                                76470.0,
                                8.36,
                                "\u5c71\u4e1c\u7701"
                            ]
                        },
                        {
                            "name": "\u6d59\u6c5f\u7701",
                            "value": [
                                56197.0,
                                6.14,
                                "\u6d59\u6c5f\u7701"
                            ]
                        },
                        {
                            "name": "\u6cb3\u5357\u7701",
                            "value": [
                                48056.0,
                                5.25,
                                "\u6cb3\u5357\u7701"
                            ]
                        },
                        {
                            "name": "\u56db\u5ddd\u7701",
                            "value": [
                                40678.0,
                                4.45,
                                "\u56db\u5ddd\u7701"
                            ]
                        },
                        {
                            "name": "\u6e56\u5317\u7701",
                            "value": [
                                39367.0,
                                4.3,
                                "\u6e56\u5317\u7701"
                            ]
                        },
                        {
                            "name": "\u6e56\u5357\u7701",
                            "value": [
                                36426.0,
                                3.98,
                                "\u6e56\u5357\u7701"
                            ]
                        },
                        {
                            "name": "\u6cb3\u5317\u7701",
                            "value": [
                                36010.0,
                                3.94,
                                "\u6cb3\u5317\u7701"
                            ]
                        },
                        {
                            "name": "\u798f\u5efa\u7701",
                            "value": [
                                35804.0,
                                3.91,
                                "\u798f\u5efa\u7701"
                            ]
                        },
                        {
                            "name": "\u4e0a\u6d77\u5e02",
                            "value": [
                                32680.0,
                                3.57,
                                "\u4e0a\u6d77\u5e02"
                            ]
                        },
                        {
                            "name": "\u5317\u4eac\u5e02",
                            "value": [
                                30320.0,
                                3.31,
                                "\u5317\u4eac\u5e02"
                            ]
                        },
                        {
                            "name": "\u5b89\u5fbd\u7701",
                            "value": [
                                30007.0,
                                3.28,
                                "\u5b89\u5fbd\u7701"
                            ]
                        },
                        {
                            "name": "\u8fbd\u5b81\u7701",
                            "value": [
                                25315.0,
                                2.77,
                                "\u8fbd\u5b81\u7701"
                            ]
                        },
                        {
                            "name": "\u9655\u897f\u7701",
                            "value": [
                                24438.0,
                                2.67,
                                "\u9655\u897f\u7701"
                            ]
                        },
                        {
                            "name": "\u6c5f\u897f\u7701",
                            "value": [
                                21985.0,
                                2.4,
                                "\u6c5f\u897f\u7701"
                            ]
                        },
                        {
                            "name": "\u91cd\u5e86\u5e02",
                            "value": [
                                20363.0,
                                2.23,
                                "\u91cd\u5e86\u5e02"
                            ]
                        },
                        {
                            "name": "\u5e7f\u897f\u58ee\u65cf\u81ea\u6cbb\u533a",
                            "value": [
                                20353.0,
                                2.23,
                                "\u5e7f\u897f\u58ee\u65cf\u81ea\u6cbb\u533a"
                            ]
                        },
                        {
                            "name": "\u5929\u6d25\u5e02",
                            "value": [
                                18810.0,
                                2.06,
                                "\u5929\u6d25\u5e02"
                            ]
                        },
                        {
                            "name": "\u4e91\u5357\u7701",
                            "value": [
                                17881.0,
                                1.95,
                                "\u4e91\u5357\u7701"
                            ]
                        },
                        {
                            "name": "\u5185\u8499\u53e4",
                            "value": [
                                17289.0,
                                1.89,
                                "\u5185\u8499\u53e4"
                            ]
                        },
                        {
                            "name": "\u5c71\u897f\u7701",
                            "value": [
                                16818.0,
                                1.84,
                                "\u5c71\u897f\u7701"
                            ]
                        },
                        {
                            "name": "\u9ed1\u9f99\u6c5f\u7701",
                            "value": [
                                16362.0,
                                1.79,
                                "\u9ed1\u9f99\u6c5f\u7701"
                            ]
                        },
                        {
                            "name": "\u5409\u6797\u7701",
                            "value": [
                                15075.0,
                                1.65,
                                "\u5409\u6797\u7701"
                            ]
                        },
                        {
                            "name": "\u8d35\u5dde\u7701",
                            "value": [
                                14806.0,
                                1.62,
                                "\u8d35\u5dde\u7701"
                            ]
                        },
                        {
                            "name": "\u65b0\u7586\u7ef4\u543e\u5c14\u81ea\u6cbb\u533a",
                            "value": [
                                12199.0,
                                1.33,
                                "\u65b0\u7586\u7ef4\u543e\u5c14\u81ea\u6cbb\u533a"
                            ]
                        },
                        {
                            "name": "\u7518\u8083\u7701",
                            "value": [
                                8246.0,
                                0.9,
                                "\u7518\u8083\u7701"
                            ]
                        },
                        {
                            "name": "\u6d77\u5357\u7701",
                            "value": [
                                4832.0,
                                0.53,
                                "\u6d77\u5357\u7701"
                            ]
                        },
                        {
                            "name": "\u5b81\u590f\u56de\u65cf\u81ea\u6cbb\u533a",
                            "value": [
                                3705.0,
                                0.41,
                                "\u5b81\u590f\u56de\u65cf\u81ea\u6cbb\u533a"
                            ]
                        },
                        {
                            "name": "\u9752\u6d77\u7701",
                            "value": [
                                2865.0,
                                0.31,
                                "\u9752\u6d77\u7701"
                            ]
                        },
                        {
                            "name": "\u897f\u85cf\u81ea\u6cbb\u533a",
                            "value": [
                                1478.0,
                                0.16,
                                "\u897f\u85cf\u81ea\u6cbb\u533a"
                            ]
                        }
                    ],
                    "roam": true,
                    "aspectScale": 0.75,
                    "nameProperty": "name",
                    "selectedMode": false,
                    "center": [
                        119.5,
                        34.5
                    ],
                    "zoom": 1,
                    "zlevel": 0,
                    "z": 2,
                    "seriesLayoutBy": "column",
                    "datasetIndex": 0,
                    "mapValueCalculation": "sum",
                    "showLegendSymbol": false,
                    "itemStyle": {
                        "normal": {
                            "areaColor": "#323c48",
                            "borderColor": "#404a59"
                        },
                        "emphasis": {
                            "label": {
                                "show": null
                            },
                            "areaColor": "rgba(255,255,255, 0.5)"
                        }
                    },
                    "emphasis": {},
                    "xAxisIndex": 3,
                    "yAxisIndex": 3
                }
            ],
            "xAxis": [
                {
                    "show": true,
                    "scale": false,
                    "nameLocation": "end",
                    "nameGap": 15,
                    "gridIndex": 0,
                    "axisLabel": {
                        "show": false,
                        "margin": 8
                    },
                    "inverse": false,
                    "offset": 0,
                    "splitNumber": 5,
                    "max": 97300,
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
                },
                {
                    "show": true,
                    "scale": false,
                    "nameLocation": "end",
                    "nameGap": 15,
                    "gridIndex": 1,
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
                        "2013\u5e74",
                        "2014\u5e74",
                        "2015\u5e74",
                        "2016\u5e74",
                        "2017\u5e74",
                        "2018\u5e74"
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
                    "axisLabel": {
                        "show": false,
                        "margin": 8
                    },
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
                        "\u5e7f\u4e1c\u7701",
                        "\u6c5f\u82cf\u7701",
                        "\u5c71\u4e1c\u7701",
                        "\u6d59\u6c5f\u7701",
                        "\u6cb3\u5357\u7701",
                        "\u56db\u5ddd\u7701",
                        "\u6e56\u5317\u7701",
                        "\u6e56\u5357\u7701",
                        "\u6cb3\u5317\u7701",
                        "\u798f\u5efa\u7701",
                        "\u4e0a\u6d77\u5e02",
                        "\u5317\u4eac\u5e02",
                        "\u5b89\u5fbd\u7701",
                        "\u8fbd\u5b81\u7701",
                        "\u9655\u897f\u7701",
                        "\u6c5f\u897f\u7701",
                        "\u91cd\u5e86\u5e02",
                        "\u5e7f\u897f\u58ee\u65cf\u81ea\u6cbb\u533a",
                        "\u5929\u6d25\u5e02",
                        "\u4e91\u5357\u7701",
                        "\u5185\u8499\u53e4",
                        "\u5c71\u897f\u7701",
                        "\u9ed1\u9f99\u6c5f\u7701",
                        "\u5409\u6797\u7701",
                        "\u8d35\u5dde\u7701",
                        "\u65b0\u7586\u7ef4\u543e\u5c14\u81ea\u6cbb\u533a",
                        "\u7518\u8083\u7701",
                        "\u6d77\u5357\u7701",
                        "\u5b81\u590f\u56de\u65cf\u81ea\u6cbb\u533a",
                        "\u9752\u6d77\u7701",
                        "\u897f\u85cf\u81ea\u6cbb\u533a"
                    ]
                },
                {
                    "show": true,
                    "scale": false,
                    "nameLocation": "end",
                    "nameGap": 15,
                    "gridIndex": 1,
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
                    "target": "blank",
                    "subtarget": "blank",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false
                },
                {
                    "show": true,
                    "text": "\u5168\u56fdGDP\u603b\u91cf2018\u5e74\uff08\u5355\u4f4d\uff1a\u4e07\u4ebf\uff09",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "50%",
                    "top": "5%",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false
                },
                {
                    "show": true,
                    "target": "blank",
                    "subtarget": "blank",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false
                },
                {
                    "show": true,
                    "text": "2018\u5e74\u5168\u56fd\u5206\u5730\u533aGPD\u60c5\u51b5\uff08\u5355\u4f4d\uff1a\u4ebf\uff09 \u6570\u636e\u6765\u6e90\uff1a\u56fd\u5bb6\u7edf\u8ba1\u5c40",
                    "target": "blank",
                    "subtarget": "blank",
                    "left": "center",
                    "top": "top",
                    "padding": 5,
                    "itemGap": 10,
                    "textAlign": "auto",
                    "textVerticalAlign": "auto",
                    "triggerEvent": false,
                    "textStyle": {
                        "color": "rgba(255,255,255, 0.9)",
                        "fontSize": 25
                    }
                }
            ],
            "tooltip": {
                "show": false,
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
            },
            "visualMap": [
                {
                    "show": true,
                    "type": "continuous",
                    "min": 30,
                    "max": 97300,
                    "text": [
                        "High",
                        "Low"
                    ],
                    "textStyle": {
                        "color": "#ddd"
                    },
                    "inRange": {
                        "color": [
                            "lightskyblue",
                            "yellow",
                            "orangered"
                        ]
                    },
                    "calculable": true,
                    "inverse": false,
                    "splitNumber": 5,
                    "dimension": 0,
                    "hoverLink": true,
                    "orient": "vertical",
                    "left": "10",
                    "top": "top",
                    "padding": 5,
                    "showLabel": true,
                    "itemWidth": 20,
                    "itemHeight": 140,
                    "borderWidth": 0
                },
                {
                    "show": true,
                    "type": "continuous",
                    "min": 30,
                    "max": 97300,
                    "text": [
                        "High",
                        "Low"
                    ],
                    "textStyle": {
                        "color": "#ddd"
                    },
                    "inRange": {
                        "color": [
                            "lightskyblue",
                            "yellow",
                            "orangered"
                        ]
                    },
                    "calculable": true,
                    "inverse": false,
                    "splitNumber": 5,
                    "dimension": 0,
                    "hoverLink": true,
                    "orient": "vertical",
                    "left": "30",
                    "top": "center",
                    "padding": 5,
                    "showLabel": true,
                    "itemWidth": 20,
                    "itemHeight": 140,
                    "borderWidth": 0
                }
            ],
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
            ]
        }
    ]
};
        chart_6f8d2685d7d44ab2bc575cb96858ea09.setOption(option_6f8d2685d7d44ab2bc575cb96858ea09);
    </script>
</body>
</html>

"""
components.html(html_content, width=1600,height=1000)



st.sidebar.header("绘图演示")
