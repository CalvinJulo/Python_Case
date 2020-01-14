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

geo=Geo()
geo.add_schema('china',zoom=1)  #add_schema确认地图类型
geo.add('china',attr)  #确认展示方式
get.set_series_opts() 优化数据格式
geo.render()
