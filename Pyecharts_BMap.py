#coding=utf-8

# 问题一,批量获得地址的经纬度
# 问题二,增加Map,Geo,Map的地点
# 问题三,美化底层的百度地图
# 问题四,优化图表的显示,标题、图例、标签
# 问题五,render输出图表的大小,格式



# coding=utf-8
from pyecharts.charts import BMap
from pyecharts import options as opts

bmap=BMap()

#跟进地址获得百度的经纬度
addresses=[
    '上海市黄浦区南京西路258号',
    '上海市静安区秣陵路228号',
    '上海市静安区南京西路555号',
    '上海普陀区长寿路868号',
    '上海市静安区延安西路200号',
    '静安区芷江西路788号',
    '上海市黄浦区黄陂北路227号'
]
baidu_ak = 'TEVm10a5xbaf4jtZEd9oGNStNlTTBIKe'

for address in addresses:
    url='http://api.map.baidu.com/geocoding/v3/?address='+address+'&output=json&ak='+baidu_ak
    res=requests.get(url)
    jd=json.loads(res.text)['result']['location']
    bmap.add_coordinate(address,jd['lng'],jd['lat'])

#百度地图
bmap.add_schema(
    baidu_ak='TEVm10a5xbaf4jtZEd9oGNStNlTTBIKe',
    center=[121.70,31.19],
    zoom=8,
    #is_roam=True,


    #map_style 用于调整百度地图上地图配置，包括地图背景、道路、行政标注和兴趣点，参照https://lbsyun.baidu.com/customv2/editor/
    #通过修改styleJson的文档来修改地图的配置，一个featureType的配置通常分两类geometry形状和labels文本
    #geometry形状类配置分visibility是否可见，geometry.fill填充，geometry.stroke描边
    #labels文本类配置分visibility是否可见，labels.icon文本形状，labels.text字体大小，labels.text.fill字体填充颜色，labels.text.stroke字体描边颜色
    map_style={
        "styleJson": [
            #地图背景的配置，backgroud,land water,green
            {"featureType": "background","elementType": "geometry","stylers": {"visibility": "off","color": "#c5adad7a"}},
            {'featureType': 'land', 'elementType': 'geometry', 'stylers': {"visibility": "off",'color': '#f5f6f7ff'}},
            {'featureType': 'water', 'elementType': 'geometry', 'stylers': {"visibility": "off",'color': '#c4d7f5ff'}},
            {'featureType': 'water', 'elementType': 'labels', 'stylers': {"visibility": "off", 'color': '#c4d7f5ff'}},
            {'featureType': 'water', 'elementType': 'labels.text.fill', 'stylers': {'color': '#9ca0a3ff'}},
            {'featureType': 'water', 'elementType': 'labels.text.stroke', 'stylers': {'color': '#ffffffff'}},

            # 道路的配置，road,highway,nationalway,cityhighway
            {'featureType': 'road', 'elementType': 'geometry', 'stylers': {"visibility": "off",'color': '#dcf2d5ff','weigh':3.2}},
            {'featureType': 'road', 'elementType': 'geometry.fill', 'stylers': {'color': '#ffe59eff'}},
            {'featureType': 'road', 'elementType': 'geometry.stroke', 'stylers': {'color': '#f5d48cff'}},
            {'featureType': 'road', 'elementType': 'labels', 'stylers': {"visibility": "off", 'color': '#dcf2d5ff'}},
            {'featureType': 'road', 'elementType': 'labels.text', 'stylers': {'fontsize': '24'}},
            {'featureType': 'road', 'elementType': 'labels.text.fill', 'stylers': {'color': '#c0792dff'}},
            {'featureType': 'road', 'elementType': 'labels.text.stroke', 'stylers': {'color': '#ffffff00'}},

            #兴趣点的配置 poilabel,airportlabel,businesstowerlabel
            {'featureType': 'poilabel', 'elementType': 'labels', 'stylers': {"visibility": "off", 'color': '#dcf2d5ff'}},
            {'featureType': 'poilabel', 'elementType': 'labels.text', 'stylers': {'fontsize': '24'}},
            {'featureType': 'poilabel', 'elementType': 'labels.text.fill', 'stylers': {'color': '#c0792dff'}},
            {'featureType': 'poilabel', 'elementType': 'labels.text.stroke', 'stylers': {'color': '#ffffff00'}},
            {'featureType': 'poilabel', 'elementType': 'labels.icon', 'stylers': {"visibility": "off"}},

            #行政标注的配置 districtlabel，city,country
            {'featureType': 'districtlabel', 'elementType': 'labels', 'stylers': {"visibility": "off", 'color': '#dcf2d5ff'}},
            {'featureType': 'districtlabel', 'elementType': 'labels.text', 'stylers': {'fontsize': '24'}},
            {'featureType': 'districtlabel', 'elementType': 'labels.text.fill', 'stylers': {'color': '#c0792dff'}},
            {'featureType': 'districtlabel', 'elementType': 'labels.text.stroke', 'stylers': {'color': '#ffffff00'}},
            {'featureType': 'districtlabel', 'elementType': 'labels.icon', 'stylers': {"visibility": "off"}},
        ]
    }
)



bmap.add(
    series_name='demo',
    data_pair=[('绩溪',100),('上海',100),('杭州',100)],
    #data_pair=[list(z) for z in zip(x_data, y_data)],
    type_='scatter',  #图类型，散点图scatter, effectScatter, 热力图heatmap, 直线图lines 4 种
    #is_selected=True,
    #symbol='circle', #标记图形形状，circle，triangle，rectangle，star
    #symbol_size=12, #标记图形大小
    #color='red', #系列label颜色
    label_opts=opts.LabelOpts(formatter='{b}'),
    itemstyle_opts=opts.ItemStyleOpts(color="purple"),
)

bmap.set_global_opts(
    title_opts=opts.TitleOpts(title='百度地图',
                              subtitle="data from PM25.in",
                              #subtitle_link="http://www.pm25.in",
                              #pos_left="center",
                              #title_textstyle_opts=opts.TextStyleOpts(color="#fff")
                              ),
    toolbox_opts=opts.ToolboxOpts(is_show=True),
    visualmap_opts=opts.VisualMapOpts(max_=len(df)),
)

'''
bmap.add_control_panel(
    copyright_control_opts=opts.BMapCopyrightTypeOpts(position=3),
    maptype_control_opts=opts.BMapTypeControlOpts(),
    scale_control_opts=opts.BMapScaleControlOpts(),
    overview_map_opts=opts.BMapOverviewMapControlOpts(is_open=True),
    navigation_control_opts=opts.BMapNavigationControlOpts(),
    geo_location_control_opts=opts.BMapGeoLocationControlOpts()
)
'''
bmap.render()
