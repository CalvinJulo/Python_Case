# coding:utf-8
# 抓取豆瓣影评进行云图分析

import jieba  # 分词包
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup as bs
from PIL import Image
import numpy as np
import matplotlib

matplotlib.rcParams['figure.figsize'] = (10.0, 5.0)
from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS  # 词云包


# 分析网页函数，返回的是最新上映的电影的字典列表
def getNowPlayingMovie_list():
    resp = requests.get('https://movie.douban.com/nowplaying/shanghai/')
    soup = bs(resp.content, 'html.parser')
    nowplaying_movie = soup.find_all('div', id='nowplaying')
    nowplaying_movie_list = nowplaying_movie[0].find_all('li', class_='list-item')
    nowplaying_list = []
    for item in nowplaying_movie_list:
        nowplaying_dict = {}
        nowplaying_dict['id'] = item['data-subject']
        for tag_img_item in item.find_all('img'):
            nowplaying_dict['name'] = tag_img_item['alt']
            nowplaying_list.append(nowplaying_dict)
    return  nowplaying_list
    print (nowplaying_list)

# 爬取评论函数，返回的是当前的所有评论，是一个string的list
def getCommentsById(movieId, pageNum):
    eachCommentList = []
    if pageNum > 0:
        start = (pageNum - 1) * 20
    else:
        return False

    requrl = 'https://movie.douban.com/subject/' + movieId + '/comments' + '?' + 'start=' + str(start) + '&limit=20'
    print(requrl)
    resp = requests.get(requrl)
    soup = bs(resp.content, 'html.parser')
    comment_div_lits = soup.find_all('div', class_='comment')
    for item in comment_div_lits:
        if item.find_all('p')[0].string is not None:
            eachCommentList.append(item.find_all('p')[0].string)
    return eachCommentList


def main():
    # 循环获取第一个电影的前10页评论
    commentList = []
    NowPlayingMovie_list = getNowPlayingMovie_list()
    for i in range(10):
        num = i + 1
        commentList_temp = getCommentsById(NowPlayingMovie_list[0]['id'], num)
        commentList.append(commentList_temp)


    # 将列表中的数据转换为字符串
    comments = ''
    for k in range(len(commentList)):
        comments = comments + (str(commentList[k])).strip()

    #结巴分词
    text=' '.join(jieba.cut(comments))


    background = np.array(Image.open('/Users/zcglook/Desktop/多特蒙德&耕3.jpg'))
    s=open("/Users/zcglook/Desktop/stopwords-list/stopwords.txt").read()
    s2=jieba.lcut(s)
    stopwords2=[]
    for i in s2: stopwords2.append(i)
    stopwords2.append('战争')

    stopwords1=['不是','还是','但是','诺兰','战争']
    wordcloud = WordCloud(font_path='/Users/zcglook/Documents/Py3/simhei.ttf',stopwords=stopwords2,background_color="white",mask=background).generate(text)
    wordcloud.recolor(color_func=ImageColorGenerator(background))
    plt.imshow(wordcloud)
    plt.show()

# 主函数
main()
