# coding=utf-8

#可视化是个非常专业的事情，图表主要还是用来说明问题
#常用的图表，柱状图Bar，折线图Line，饼图Pie，象形柱状图PictorialBar,散点图Scatter，云词WordCloud
#图表常见元素，如legend，tooltip，mark，xaxias，yxaxis，需要掌握
#各图表的数据类型和格式需要掌握，多数据需要了解
#图表美化，要掌握Theme，color
#练习以Bar


#以下是高级用法
#Dataset 数据集
#Grid 并行图表
#Overlap 层叠图表
#Page 顺序多图
#Tab 选项卡多图
#Theme 主题
#Timeline 时间线

import pandas as pd
from pyecharts import options as opts
from pyecharts.globals import ThemeType
class charts:
    def bar(x_data, y_data):
        from pyecharts.charts import Bar
        bar = Bar(init_opts=opts.InitOpts(width='900px',height='500px',
                                          page_title='测试',
                                          bg_color='White'
                                          ))
        bar.add_xaxis(xaxis_data=x_data)
        #bar.add_yaxis(series_name="系列2", yaxis_data=y_data2, stack="stack1")
        bar.add_yaxis(series_name='系列1',
                      yaxis_data=y_data,
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
        bar.set_global_opts(title_opts=opts.TitleOpts(title="Bar-旋转X轴标签", subtitle="解决标签名字过长的问题",
                                                      title_textstyle_opts=opts.TextStyleOpts(color='red')),
                            xaxis_opts=opts.AxisOpts(name='X轴',axislabel_opts=opts.LabelOpts(rotate=-15)),
                            yaxis_opts=opts.AxisOpts(name="Y轴",
                                                     type_="value",
                                                     axistick_opts=opts.AxisTickOpts(is_show=False),
                                                     splitline_opts=opts.SplitLineOpts(is_show=True)
                                                     ),
                            tooltip_opts = opts.TooltipOpts(is_show=True, trigger="mousemove|click", axis_pointer_type=None),
                            brush_opts=opts.BrushOpts(),
                            datazoom_opts=None,
                            toolbox_opts=opts.ToolboxOpts(),
                            legend_opts=opts.LegendOpts(is_show=True),
                            #visualmap_opts=opts.VisualMapOpts()
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
        pictorialBar.set_global_opts(title_opts=opts.TitleOpts(title='pictorialBar象形柱图'))
        return pictorialBar

    def line(x_data,y_data):
        from pyecharts.charts import Line
        line=Line()
        line.add_xaxis(xaxis_data=x_data)
        line.add_yaxis(series_name='line测试',y_axis=y_data)
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
        return pie

    def heatmap(self):
        from pyecharts.charts import HeatMap

    def wordcloud(x_data,y_data):
        from pyecharts.charts import WordCloud
        datalist = [list(z) for z in zip(x_data, y_data)]
        wordcloud=WordCloud()
        wordcloud.add(series_name='',data_pair=datalist)
        return wordcloud

    def tree(self):
        return

    def scatter(x_data,y_data):
        from pyecharts.charts import  Scatter
        scatter=Scatter()
        scatter.add_xaxis(xaxis_data=x_data)
        scatter.add_yaxis(series_name='scattercase',y_axis=y_data)
        scatter.set_global_opts(xaxis_opts=opts.AxisOpts(type_="value", splitline_opts=opts.SplitLineOpts(is_show=True)))
        return scatter

    def graph(self):
        return

a=['名称1','名称2','名称3','名称4']
b=[4,20,18,9]
b1=[46,29,34,79]
c=charts.wordcloud(a,b)
c.set_global_opts(title_opts=opts.TitleOpts(title="Bar-旋转X轴标签", subtitle="解决标签名字过长的问题"),
                  toolbox_opts=opts.ToolboxOpts(is_show=True))
c.render('case.html')

