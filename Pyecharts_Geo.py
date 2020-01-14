# coding=utf-8
from pyecharts.charts import Geo,Bar
from pyecharts import options as opts
import json

html='''
{"cmts":[{"approve":0,"approved":false,"assistAwardInfo":{"avatar":"","celebrityId":0,"celebrityName":"","rank":0,"title":""},"avatarurl":"https://img.meituan.net/avatar/2f6ce3e8ad6350a531aeada401601b0c21747.jpg","cityName":"呼和浩特","content":"完美完美完美","filmView":false,"gender":2,"id":1096231601,"isMajor":false,"juryLevel":0,"majorType":0,"movieId":1200486,"nick":"南楠19900520","nickName":"南楠19900520","oppose":0,"pro":false,"reply":0,"score":4.5,"spoiler":0,"startTime":"2020-01-14 15:25:12","supportComment":true,"supportLike":true,"sureViewed":1,"tagList":{"fixed":[{"id":1,"name":"好评"},{"id":4,"name":"购票"}]},"time":"2020-01-14 15:25","userId":94843213,"userLevel":2,"videoDuration":0,"vipType":0},{"approve":0,"approved":false,"assistAwardInfo":{"avatar":"","celebrityId":0,"celebrityName":"","rank":0,"title":""},"avatarurl":"https://img.meituan.net/maoyanuser/4be405f274fa8fca7358a9e579a8262411960.png","cityName":"沈阳","content":"很好看，值得推荐！","filmView":false,"id":1096224083,"isMajor":false,"juryLevel":0,"majorType":0,"movieId":1200486,"nick":"xhluan","nickName":"xhluan","oppose":0,"pro":false,"reply":0,"score":5.0,"spoiler":0,"startTime":"2020-01-14 14:59:02","supportComment":true,"supportLike":true,"sureViewed":1,"tagList":{"fixed":[{"id":1,"name":"好评"},{"id":4,"name":"购票"}]},"time":"2020-01-14 14:59","userId":60345158,"userLevel":1,"videoDuration":0,"vipType":0}],"total":689370}
'''

datas=json.loads(html,strict=False)['cmts']  #将类Json格式的字符串转化为Json格式

comments=[]
for i in datas:
    comment={
        'approve':i['approve'],
        'cityName':i['cityName'],

    }
    comments.append(comment)  #将Json格式的数据整理成列表格式,便于进行分析

#txt=pd.DataFrame(comments)
cities=[]
for comment in comments:
    cities.append(comment['cityName'])

attr=[]
for city in cities:
    if city=='':
        city='慈溪'
    attr.append((city,cities.count(city)),)

print(attr)

geo=Geo()  #Geo地图图表,from pyechart.charts import Geo
geo.add_schema(
    maptype='china',  #地图类型，具体参考 pyecharts.datasets.map_filenames.json 文件,一般为地名 maptype: str = "china"
    is_roam=True,  #是否开启鼠标缩放和平移漫游。is_roam: bool = True,
    zoom=1,  # 当前视角的缩放比例。默认为 1,zoom: Optional[Numeric] = None,
    center=[115.97, 29.71]  # 当前视角的中心点，用经纬度表示。例如：center: [115.97, 29.71]
)  

geo.add(
    series_name='china',  # 系列名称，用于 tooltip 的显示，legend 的图例筛选。
    data_pair=attr, # 数据项 (坐标点名称，坐标点值)
    type_='scatter', # Geo 图类型，有 scatter, effectScatter, heatmap, lines 4 种
    is_selected=True, # 是否选中图例
    symbol='circle', # 标记图形形状
    symbol_size=12, # 标记的大小
    color='white', #系列 label 颜色
    is_polyline=False, # 是否是多段线，在画 lines 图情况下
    is_large=False, # 是否启用大规模线图的优化，在数据图形特别多的时候（>=5k）可以开启
    trail_length=0.2 # 特效尾迹的长度。取从 0 到 1 的值，数值越大尾迹越长。默认值 0.2
    large_threshold=2000,# 开启绘制优化的阈值。
    progressive=400, # 配置该系列每一帧渲染的图形数
    progressive_threshold=3000, # 启用渐进式渲染的图形数量阈值，在单个系列的图形数量超过该阈值时启用渐进式渲染。
) 

geo.set_global_opts(
    title_opts=opts.TitleOpts(title='测试',title_link='www.baidu.com'),
)

geo.set_series_opts(
) 优化数据格式

geo.render()


    title_opts=opts.TitleOpts(title='测试',title_link='www.baidu.com',title_target='blank',subtitle='测试副标题'),
    legend_opts=opts.LegendOpts(),
    tooltip_opts=opts.TooltipOpts(),
    toolbox_opts=opts.ToolboxOpts(),
    brush_opts=opts.BrushOpts(),
    yaxis_opts=opts.,
    datazoom_opts=opts.DataZoomOpts(),
    graphic_opts=,
    axispointer_opts=,
    visualmap_opts=,
    xaxis_opts=,)
