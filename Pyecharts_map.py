# coding=utf-8

from pyecharts import options as opts
import requests
import json
import pandas as pd
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot

str = '''
[{
    "featureType": "land",
    "elementType": "geometry",
    "stylers": {
        "color": "#fffff9ff"
    }
}, {
    "featureType": "water",
    "elementType": "geometry",
    "stylers": {
        "color": "#69b0acff"
    }
}, {
    "featureType": "highway",
    "elementType": "geometry.fill",
    "stylers": {
        "color": "#b5caa0ff"
    }
}, {
    "featureType": "highway",
    "elementType": "geometry.stroke",
    "stylers": {
        "color": "#94ad79ff"
    }
}, {
    "featureType": "nationalway",
    "elementType": "geometry.fill",
    "stylers": {
        "color": "#b5caa0ff"
    }
}, {
    "featureType": "arterial",
    "elementType": "geometry.fill",
    "stylers": {
        "color": "#d4e2c6ff"
    }
}, {
    "featureType": "cityhighway",
    "elementType": "geometry.fill",
    "stylers": {
        "color": "#d4e2c6ff"
    }
}, {
    "featureType": "provincialway",
    "elementType": "geometry.fill",
    "stylers": {
        "color": "#d4e2c6ff"
    }
}, {
    "featureType": "provincialway",
    "elementType": "geometry.stroke",
    "stylers": {
        "color": "#b5caa0ff"
    }
}, {
    "featureType": "tertiaryway",
    "elementType": "geometry.fill",
    "stylers": {
        "color": "#ffffffff"
    }
}, {
    "featureType": "tertiaryway",
    "elementType": "geometry.stroke",
    "stylers": {
        "color": "#b5caa0ff"
    }
}, {
    "featureType": "fourlevelway",
    "elementType": "geometry.fill",
    "stylers": {
        "color": "#ffffffff"
    }
}, {
    "featureType": "fourlevelway",
    "elementType": "geometry.stroke",
    "stylers": {
        "color": "#b5caa0ff"
    }
}, {
    "featureType": "subway",
    "elementType": "geometry",
    "stylers": {
        "visibility": "off"
    }
}, {
    "featureType": "railway",
    "elementType": "geometry",
    "stylers": {
        "visibility": "off"
    }
}, {
    "featureType": "highwaysign",
    "elementType": "labels",
    "stylers": {
        "visibility": "off"
    }
}, {
    "featureType": "highwaysign",
    "elementType": "labels.icon",
    "stylers": {
        "visibility": "off"
    }
}, {
    "featureType": "nationalwaysign",
    "elementType": "labels",
    "stylers": {
        "visibility": "off"
    }
}, {
    "featureType": "nationalwaysign",
    "elementType": "labels.icon",
    "stylers": {
        "visibility": "off"
    }
}, {
    "featureType": "provincialwaysign",
    "elementType": "labels",
    "stylers": {
        "visibility": "off"
    }
}, {
    "featureType": "provincialwaysign",
    "elementType": "labels.icon",
    "stylers": {
        "visibility": "off"
    }
}, {
    "featureType": "tertiarywaysign",
    "elementType": "labels",
    "stylers": {
        "visibility": "off"
    }
}, {
    "featureType": "tertiarywaysign",
    "elementType": "labels.icon",
    "stylers": {
        "visibility": "off"
    }
}, {
    "featureType": "subwaylabel",
    "elementType": "labels",
    "stylers": {
        "visibility": "off"
    }
}, {
    "featureType": "subwaylabel",
    "elementType": "labels.icon",
    "stylers": {
        "visibility": "off"
    }
}, {
    "featureType": "nationalway",
    "elementType": "geometry.stroke",
    "stylers": {
        "color": "#94ad79ff"
    }
}, {
    "featureType": "cityhighway",
    "elementType": "geometry.stroke",
    "stylers": {
        "color": "#b5caa0ff"
    }
}, {
    "featureType": "arterial",
    "elementType": "geometry.stroke",
    "stylers": {
        "color": "#b5caa0ff"
    }
}, {
    "featureType": "highway",
    "stylers": {
        "level": "6",
        "curZoomRegionId": "0",
        "curZoomRegion": "6-9"
    }
}, {
    "featureType": "highway",
    "stylers": {
        "level": "7",
        "curZoomRegionId": "0",
        "curZoomRegion": "6-9"
    }
}, {
    "featureType": "highway",
    "stylers": {
        "level": "8",
        "curZoomRegionId": "0",
        "curZoomRegion": "6-9"
    }
}, {
    "featureType": "highway",
    "stylers": {
        "level": "9",
        "curZoomRegionId": "0",
        "curZoomRegion": "6-9"
    }
}, {
    "featureType": "highway",
    "elementType": "geometry",
    "stylers": {
        "visibility": "off",
        "level": "6",
        "curZoomRegionId": "0",
        "curZoomRegion": "6-9"
    }
}, {
    "featureType": "highway",
    "elementType": "geometry",
    "stylers": {
        "visibility": "off",
        "level": "7",
        "curZoomRegionId": "0",
        "curZoomRegion": "6-9"
    }
}, {
    "featureType": "highway",
    "elementType": "geometry",
    "stylers": {
        "visibility": "off",
        "level": "8",
        "curZoomRegionId": "0",
        "curZoomRegion": "6-9"
    }
}, {
    "featureType": "highway",
    "elementType": "geometry",
    "stylers": {
        "visibility": "off",
        "level": "9",
        "curZoomRegionId": "0",
        "curZoomRegion": "6-9"
    }
}, {
    "featureType": "highway",
    "elementType": "labels",
    "stylers": {
        "visibility": "off",
        "level": "6",
        "curZoomRegionId": "0",
        "curZoomRegion": "6-9"
    }
}, {
    "featureType": "highway",
    "elementType": "labels",
    "stylers": {
        "visibility": "off",
        "level": "7",
        "curZoomRegionId": "0",
        "curZoomRegion": "6-9"
    }
}, {
    "featureType": "highway",
    "elementType": "labels",
    "stylers": {
        "visibility": "off",
        "level": "8",
        "curZoomRegionId": "0",
        "curZoomRegion": "6-9"
    }
}, {
    "featureType": "highway",
    "elementType": "labels",
    "stylers": {
        "visibility": "off",
        "level": "9",
        "curZoomRegionId": "0",
        "curZoomRegion": "6-9"
    }
}, {
    "featureType": "nationalway",
    "stylers": {
        "level": "6",
        "curZoomRegionId": "0",
        "curZoomRegion": "6-9"
    }
}, {
    "featureType": "nationalway",
    "stylers": {
        "level": "7",
        "curZoomRegionId": "0",
        "curZoomRegion": "6-9"
    }
}, {
    "featureType": "nationalway",
    "stylers": {
        "level": "8",
        "curZoomRegionId": "0",
        "curZoomRegion": "6-9"
    }
}, {
    "featureType": "nationalway",
    "stylers": {
        "level": "9",
        "curZoomRegionId": "0",
        "curZoomRegion": "6-9"
    }
}, {
    "featureType": "nationalway",
    "elementType": "geometry",
    "stylers": {
        "visibility": "off",
        "level": "6",
        "curZoomRegionId": "0",
        "curZoomRegion": "6-9"
    }
}, {
    "featureType": "nationalway",
    "elementType": "geometry",
    "stylers": {
        "visibility": "off",
        "level": "7",
        "curZoomRegionId": "0",
        "curZoomRegion": "6-9"
    }
}, {
    "featureType": "nationalway",
    "elementType": "geometry",
    "stylers": {
        "visibility": "off",
        "level": "8",
        "curZoomRegionId": "0",
        "curZoomRegion": "6-9"
    }
}, {
    "featureType": "nationalway",
    "elementType": "geometry",
    "stylers": {
        "visibility": "off",
        "level": "9",
        "curZoomRegionId": "0",
        "curZoomRegion": "6-9"
    }
}, {
    "featureType": "nationalway",
    "elementType": "labels",
    "stylers": {
        "visibility": "off",
        "level": "6",
        "curZoomRegionId": "0",
        "curZoomRegion": "6-9"
    }
}, {
    "featureType": "nationalway",
    "elementType": "labels",
    "stylers": {
        "visibility": "off",
        "level": "7",
        "curZoomRegionId": "0",
        "curZoomRegion": "6-9"
    }
}, {
    "featureType": "nationalway",
    "elementType": "labels",
    "stylers": {
        "visibility": "off",
        "level": "8",
        "curZoomRegionId": "0",
        "curZoomRegion": "6-9"
    }
}, {
    "featureType": "nationalway",
    "elementType": "labels",
    "stylers": {
        "visibility": "off",
        "level": "9",
        "curZoomRegionId": "0",
        "curZoomRegion": "6-9"
    }
}, {
    "featureType": "provincialway",
    "stylers": {
        "level": "8",
        "curZoomRegionId": "0",
        "curZoomRegion": "8-9"
    }
}, {
    "featureType": "provincialway",
    "stylers": {
        "level": "9",
        "curZoomRegionId": "0",
        "curZoomRegion": "8-9"
    }
}, {
    "featureType": "provincialway",
    "elementType": "geometry",
    "stylers": {
        "visibility": "off",
        "level": "8",
        "curZoomRegionId": "0",
        "curZoomRegion": "8-9"
    }
}, {
    "featureType": "provincialway",
    "elementType": "geometry",
    "stylers": {
        "visibility": "off",
        "level": "9",
        "curZoomRegionId": "0",
        "curZoomRegion": "8-9"
    }
}, {
    "featureType": "provincialway",
    "elementType": "labels",
    "stylers": {
        "visibility": "off",
        "level": "8",
        "curZoomRegionId": "0",
        "curZoomRegion": "8-9"
    }
}, {
    "featureType": "provincialway",
    "elementType": "labels",
    "stylers": {
        "visibility": "off",
        "level": "9",
        "curZoomRegionId": "0",
        "curZoomRegion": "8-9"
    }
}, {
    "featureType": "cityhighway",
    "stylers": {
        "level": "6",
        "curZoomRegionId": "0",
        "curZoomRegion": "6-9"
    }
}, {
    "featureType": "cityhighway",
    "stylers": {
        "level": "7",
        "curZoomRegionId": "0",
        "curZoomRegion": "6-9"
    }
}, {
    "featureType": "cityhighway",
    "stylers": {
        "level": "8",
        "curZoomRegionId": "0",
        "curZoomRegion": "6-9"
    }
}, {
    "featureType": "cityhighway",
    "stylers": {
        "level": "9",
        "curZoomRegionId": "0",
        "curZoomRegion": "6-9"
    }
}, {
    "featureType": "cityhighway",
    "elementType": "geometry",
    "stylers": {
        "visibility": "off",
        "level": "6",
        "curZoomRegionId": "0",
        "curZoomRegion": "6-9"
    }
}, {
    "featureType": "cityhighway",
    "elementType": "geometry",
    "stylers": {
        "visibility": "off",
        "level": "7",
        "curZoomRegionId": "0",
        "curZoomRegion": "6-9"
    }
}, {
    "featureType": "cityhighway",
    "elementType": "geometry",
    "stylers": {
        "visibility": "off",
        "level": "8",
        "curZoomRegionId": "0",
        "curZoomRegion": "6-9"
    }
}, {
    "featureType": "cityhighway",
    "elementType": "geometry",
    "stylers": {
        "visibility": "off",
        "level": "9",
        "curZoomRegionId": "0",
        "curZoomRegion": "6-9"
    }
}, {
    "featureType": "cityhighway",
    "elementType": "labels",
    "stylers": {
        "visibility": "off",
        "level": "6",
        "curZoomRegionId": "0",
        "curZoomRegion": "6-9"
    }
}, {
    "featureType": "cityhighway",
    "elementType": "labels",
    "stylers": {
        "visibility": "off",
        "level": "7",
        "curZoomRegionId": "0",
        "curZoomRegion": "6-9"
    }
}, {
    "featureType": "cityhighway",
    "elementType": "labels",
    "stylers": {
        "visibility": "off",
        "level": "8",
        "curZoomRegionId": "0",
        "curZoomRegion": "6-9"
    }
}, {
    "featureType": "cityhighway",
    "elementType": "labels",
    "stylers": {
        "visibility": "off",
        "level": "9",
        "curZoomRegionId": "0",
        "curZoomRegion": "6-9"
    }
}, {
    "featureType": "entertainment",
    "elementType": "geometry",
    "stylers": {
        "color": "#e4f0d7ff"
    }
}, {
    "featureType": "manmade",
    "elementType": "geometry",
    "stylers": {
        "color": "#effcf0ff"
    }
}, {
    "featureType": "education",
    "elementType": "geometry",
    "stylers": {
        "color": "#e3f7e4ff"
    }
}, {
    "featureType": "building",
    "elementType": "geometry.stroke",
    "stylers": {
        "color": "#a1cfa4ff"
    }
}, {
    "featureType": "poilabel",
    "elementType": "labels",
    "stylers": {
        "visibility": "off"
    }
}, {
    "featureType": "poilabel",
    "elementType": "labels.icon",
    "stylers": {
        "visibility": "off"
    }
}, {
    "featureType": "education",
    "elementType": "labels.text.fill",
    "stylers": {
        "color": "#7a7a7aff"
    }
}, {
    "featureType": "education",
    "elementType": "labels.text.stroke",
    "stylers": {
        "color": "#ffffffff"
    }
}, {
    "featureType": "education",
    "elementType": "labels.text",
    "stylers": {
        "fontsize": "26"
    }
}, {
    "featureType": "manmade",
    "elementType": "labels.text.fill",
    "stylers": {
        "color": "#afafafff"
    }
}, {
    "featureType": "manmade",
    "elementType": "labels.text",
    "stylers": {
        "fontsize": "26"
    }
}, {
    "featureType": "scenicspotslabel",
    "elementType": "labels.text.fill",
    "stylers": {
        "color": "#376b6dff"
    }
}, {
    "featureType": "scenicspots",
    "elementType": "labels",
    "stylers": {
        "visibility": "off"
    }
}, {
    "featureType": "scenicspotslabel",
    "elementType": "labels",
    "stylers": {
        "visibility": "on"
    }
}, {
    "featureType": "scenicspotslabel",
    "elementType": "labels.text.stroke",
    "stylers": {
        "color": "#ffffffff",
        "weight": "4"
    }
}, {
    "featureType": "country",
    "elementType": "labels.text.fill",
    "stylers": {
        "color": "#376b6dff"
    }
}, {
    "featureType": "country",
    "elementType": "labels.text.stroke",
    "stylers": {
        "color": "#ffffffff",
        "weight": "3"
    }
}, {
    "featureType": "water",
    "elementType": "labels.text.fill",
    "stylers": {
        "color": "#ffffffff"
    }
}, {
    "featureType": "water",
    "elementType": "labels.text.stroke",
    "stylers": {
        "color": "#ffffff00"
    }
}, {
    "featureType": "water",
    "elementType": "labels.text",
    "stylers": {
        "fontsize": "24"
    }
}]
'''

map_style = json.loads(str, strict=False)


class mapcharts:
    def bmap(x_data,y_data):
        from pyecharts.charts import BMap
        bmap = BMap()
        bmap.add_schema(
            baidu_ak='TEVm10a5xbaf4jtZEd9oGNStNlTTBIKe',
            center=[100, 31.236276],
            zoom=19,
            # is_roam=True,
            map_style={"styleJson": map_style})
        bmap.add(
            series_name='百度地图',
            data_pair=[list(z) for z in zip(x_data, y_data)],
            type_='scatter',  # 图类型，散点图scatter, effectScatter, 热力图heatmap, 直线图lines 4 种
            # is_selected=True,
            symbol='image://https://gss0.bdstatic.com/7Ls0a8Sm1A5BphGlnYG/sys/portrait/item/40d3c8bcc1c1d0c7d2b96440.jpg')
            # 标记图形形状，circle，triangle，rect，roundRect，diamond，arrow，pin
            # symbol_size=12, #标记图形大小
            # color='red', #系列label颜色
            # label_opts=opts.LabelOpts(formatter='{b}')
        bmap.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        bmap.add_control_panel()
        return bmap

    def bmap_location(addresses):
        from pyecharts.charts import BMap
        bmap = BMap()
        baidu_ak = 'TEVm10a5xbaf4jtZEd9oGNStNlTTBIKe'
        addresslist=[]
        for address in addresses:
            url='http://api.map.baidu.com/geocoding/v3/?address='+address+'&output=json&ak='+baidu_ak
            res = requests.get(url)
            jd = json.loads(res.text)['result']['location']
            addresslist.append({'地址':address,'经度':jd['lng'],'纬度':jd['lat']})
            bmap.add_coordinate(address, jd['lng'], jd['lat'])
        return addresslist

    def geo(x_data,y_data):
        from pyecharts.charts import Geo
        geo=Geo()
        geo.add_schema(maptype='china')
        geo.add(series_name='geo地图',
                data_pair=[list(z) for z in zip(x_data, y_data)])
        #geo.add(data_pair=[list(z) for z in zip(x_data, y_data)],type_=ChartType.EFFECT_SCATTER)
        geo.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        return geo


    def map(x_data,y_data):
        from pyecharts.charts import Map
        map=Map()
        map.add(series_name='map地图',
                data_pair=[list(z) for z in zip(x_data, y_data)],
                maptype='china')
        map.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        return map


x_data=['北京','上海','广州','成都']
y_data=[10,13,40,29]

c_bmap=mapcharts.bmap(x_data,y_data)
c_geo=mapcharts.geo(x_data,y_data)
c_map=mapcharts.map(x_data,y_data)


c_bmap.set_global_opts(title_opts=opts.TitleOpts(title='百度地图'),
                       visualmap_opts=opts.VisualMapOpts())
c_geo.set_global_opts(title_opts=opts.TitleOpts(title='geo地图'),
                       visualmap_opts=opts.VisualMapOpts())
c_map.set_global_opts(title_opts=opts.TitleOpts(title='map地图'),
                       visualmap_opts=opts.VisualMapOpts())

from pyecharts.charts import Tab
tab=Tab()
tab.add(c_bmap,'百度地图')
tab.add(c_geo,'geo地图')
tab.add(c_map,'map地图')

tab.render('Pyecharts地图可视化.html')
