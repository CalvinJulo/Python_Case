# coding=utf-8

import pandas as pd
from pyecharts import options as opts
from pyecharts.globals import ThemeType
from pyecharts.faker import Faker

'''
Pyecharts 生产图表教程
1、Pyecharts的数据类型，一般都是List，导入之前先生成list类型的数据
2、图表的数据属性在add_xaxis或add_yaxis修改，如文字样式，线的样式，标签样式
3、图表的Series属性在函数内完成，包括标记点，标记线、标签样式、线样式
4、图表的global属性在render之前完成，包括图表标题、工具箱、图例、x轴y轴配置、视觉映射、图表主题
5、图表render生成，先导出html，再下载。改变图表大小，在init里设置

高级设置
如何设置图表背景
如何设置图表主题
如何设置数据视觉变化
如何设置标签的图标
如何基于Json配置图表
如何设置Graphic图形组件
'''

class charts:
    #1、直方图的设置，如果数据系列在两个以内，直接bar(x_data, y_data1,y_data2=None)生成
    #2、数据系列大于三个及以上，重新增加bar.add_yaxis()
    #3、数据需要堆砌，则bar.add_yaxis()里增加stack；轴互换对调则ar.reversal_axis()；增加轴bar.extend_axis()
    def bar(x_data, y_data1,y_data2=None):
        from pyecharts.charts import Bar
        bar = Bar(init_opts=opts.InitOpts(width='900px',height='500px',
                                          page_title='测试',
                                          bg_color='White'
                                          ))
        bar.add_xaxis(xaxis_data=x_data)
        bar.add_yaxis(series_name='系列1',
                      yaxis_data=y_data1,
                      xaxis_index=None,
                      yaxis_index=None,
                      is_selected=True,
                      color=None,
                      stack=None,
                      category_gap='60%',
                      gap=None,
                      label_opts=opts.LabelOpts(is_show=True,
                                                position='top',
                                                color=None,
                                                font_size=12,
                                                font_style=None,
                                                font_family=None,
                                                font_weight=None,
                                                rotate=None,
                                                margin=8,
                                                interval=None,
                                                horizontal_align=None,
                                                vertical_align=None,
                                                formatter=None,
                                                rich=None,
                                                ),
                      markpoint_opts=opts.MarkPointOpts(#data=opts.MarkPointItem(),
                                                        symbol=None,
                                                        symbol_size=None,
                                                        #label_opts=opts.LabelOpts()
                                                        ),
                      markline_opts=opts.MarkLineOpts(is_silent=True,
                                                      #data=opts.MarkLineItem(),
                                                      symbol=None,
                                                      symbol_size=None,
                                                      precision=2,
                                                      # label_opts=opts.LabelOpts(),
                                                      #linestyle_opts=opts.LineStyleOpts()
                                                      ),
                      tooltip_opts=opts.TooltipOpts(is_show=False,
                                                    trigger="item",
                                                    trigger_on="mousemove|click",
                                                    axis_pointer_type="line",
                                                    formatter=None,
                                                    background_color=None,
                                                    border_color=None,
                                                    border_width=0,
                                                    #textstyle_opts=opts.TextStyleOpts()
                                                    ),
                      itemstyle_opts=opts.ItemStyleOpts(color=None,
                                                        color0=None,
                                                        border_color=None,
                                                        border_color0=None,
                                                        opacity=None
                                                        )
                      )
        if y_data2 !=None:
            bar.add_yaxis('系列2',y_data2)
        #bar.add_yaxis(series_name="系列2", yaxis_data=y_data2, stack="stack1")
        #bar.extend_axis()
        #bar.reversal_axis()
        bar.set_series_opts(label_opts=opts.LabelOpts(is_show=True,
                                                      position="right",
                                                      formatter=None),
                            linestyle_opts=opts.LineStyleOpts(),
                            splitline_opts=opts.SplitLineOpts(),
                            areastyle_opts=opts.AreaStyleOpts(),
                            axisline_opts={},
                            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max", name="最大值"),
                                                                    opts.MarkPointItem(type_="min", name="最小值")]),
                            tooltip_opts={},
                            itemstyle_opts={}
                            )
        return bar

    def pictorialBar(x_data,y_data):
        from pyecharts.charts import PictorialBar
        pictorialBar=PictorialBar()
        pictorialBar.add_xaxis(x_data)
        pictorialBar.add_yaxis(series_name='pictorialBar',
                               yaxis_data=y_data,
                               symbol='circle',
                               symbol_size=18,
                               symbol_repeat=True,
                               label_opts=opts.LabelOpts(position='right')
                               )
        pictorialBar.reversal_axis()
        #pictorialBar.set_series_opts()
        return pictorialBar

    def line(x_data,y_data):
        from pyecharts.charts import Line
        line=Line()
        line.add_xaxis(xaxis_data=x_data)
        line.add_yaxis(series_name='line测试',y_axis=y_data)
        #line.set_series_opts()
        return line

    def pie(x_data,y_data):
        from pyecharts.charts import Pie
        datalist=[list(z) for z in zip(x_data,y_data)]
        pie=Pie()
        pie.add(series_name='piechart',
                data_pair=datalist,
                center=["50%", "50%"],
                radius=["40%", "55%"],
                label_opts=opts.LabelOpts(position="inner")
                )
        #pie.set_series_opts()
        return pie

    def funnel(x_data,y_data):
        from pyecharts.charts import Funnel
        funnel=Funnel()
        funnel.add('漏斗图',[list(z) for z in zip(x_data, y_data)])
        return funnel

    def heatmap(x_data,y_data,z_data=None):
        from pyecharts.charts import HeatMap
        import random
        heatmap=HeatMap()
        heatmap.add_xaxis(xaxis_data=x_data)
        heatmap.add_yaxis(series_name='热力图',yaxis_data=y_data,
                          value=[[i, j, random.randint(0, 50)] for i in range(len(x_data)) for j in range(len(y_data))])
        return heatmap

    def wordcloud(x_data,y_data):
        from pyecharts.charts import WordCloud
        datalist = [list(z) for z in zip(x_data, y_data)]
        wordcloud=WordCloud()
        wordcloud.add(series_name='',data_pair=datalist)
        #wordcloud.set_series_opts()
        return wordcloud

    def tree(self):
        from pyecharts.charts import Tree

    def scatter(x_data,y_data):
        from pyecharts.charts import Scatter
        scatter=Scatter()
        scatter.add_xaxis(xaxis_data=x_data)
        scatter.add_yaxis(series_name='scattercase',y_axis=y_data)
        scatter.set_series_opts()
        return scatter

    def graph(self):
        return

    def grid(chart1,chart2):
        from pyecharts.charts import Grid
        grid=Grid()
        grid.add(chart1,grid_opts=opts.GridOpts(pos_bottom="60%"))
        grid.add(chart2,grid_opts=opts.GridOpts(pos_top="60%"))
        return grid

    def page(chart1,chart2):
        from pyecharts.charts import Page
        page=Page(layout=Page.DraggablePageLayout)
        page.add(chart1,chart2)
        return page



x_data=['名称1','名称2','名称3','名称4']
y_data1=[4,20,18,9]
y_data2=[46,29,34,79]


c_bar=charts.bar( x_data,y_data1,y_data2)
c_pictorailBar=charts.pictorialBar(x_data,y_data1)
c_line=charts.line(x_data,y_data1)
c_wrodcloud=charts.wordcloud(x_data,y_data1)
c_pie=charts.pie(x_data,y_data1)
c_funnel=charts.funnel(x_data,y_data1)
c_heatmap=charts.heatmap(x_data,y_data1)
c_scatter=charts.scatter(x_data,y_data1)
c_bar_line=charts.bar(x_data,y_data2).overlap(charts.line(x_data,y_data1))
c_grid=charts.grid(charts.bar(x_data,y_data1),charts.line(x_data,y_data1))
c_page=charts.page(charts.bar(x_data,y_data1),charts.line(x_data,y_data1))


c_bar.set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="次标题",
                                              title_textstyle_opts=opts.TextStyleOpts(color='red')),
                    xaxis_opts=opts.AxisOpts(name='X轴', axislabel_opts=opts.LabelOpts(rotate=-15)),
                    yaxis_opts=opts.AxisOpts(name="Y轴",
                                             type_="value",
                                             axistick_opts=opts.AxisTickOpts(is_show=False),
                                             splitline_opts=opts.SplitLineOpts(is_show=True)
                                             ),
                    tooltip_opts=opts.TooltipOpts(is_show=True, trigger="mousemove|click", axis_pointer_type=None),
                    brush_opts=opts.BrushOpts(),
                    datazoom_opts=None,
                    toolbox_opts=opts.ToolboxOpts(),
                    legend_opts=opts.LegendOpts(is_show=True),
                    # visualmap_opts=opts.VisualMapOpts()
                    )
c_pictorailBar.set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="次标题"),
                  toolbox_opts=opts.ToolboxOpts(is_show=True))
c_line.set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="次标题"),
                  toolbox_opts=opts.ToolboxOpts(is_show=True))
c_wrodcloud.set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="次标题"),
                  toolbox_opts=opts.ToolboxOpts(is_show=True))
c_pie.set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="次标题"),
                  toolbox_opts=opts.ToolboxOpts(is_show=True))
c_funnel.set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="次标题"),
                  toolbox_opts=opts.ToolboxOpts(is_show=True))
c_heatmap.set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="次标题"),
                  toolbox_opts=opts.ToolboxOpts(is_show=True),visualmap_opts=opts.VisualMapOpts())
c_scatter.set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="次标题"),
                  toolbox_opts=opts.ToolboxOpts(is_show=True))
c_bar_line.set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="次标题"),
                  toolbox_opts=opts.ToolboxOpts(is_show=True))

from pyecharts.charts import Tab
tab=Tab()
tab.add(c_bar,'直方图')
tab.add(c_pictorailBar,'象形直方图')
tab.add(c_line,'折线图')
tab.add(c_wrodcloud,'云词')
tab.add(c_pie,'饼图')
tab.add(c_funnel,'漏斗图')
tab.add(c_heatmap,'热力图')
tab.add(c_scatter,'散点图')
tab.add(c_bar_line,'直方图折线图')
tab.add(c_grid,'组合图形')
tab.add(c_page,'页面组合')
tab.render('Pyecharts可视化.html')


#Dataset 数据集
#Page 顺序多图
#Theme 主题
#Timeline 时间线
#Table
