#!/usr/bin/python
"""
This is module
"""
# 专业的爬虫 beautifal Soup, Scapy
# 断点调试

import re
from urllib import request

class Spider():
    """
    This is class
    """
    url="https://www.9xiu.com/"
    # 加上问好 ? 是非贪婪模式（匹配到第一个</p>）    python 默认是贪婪模式(匹配到最后一个</p>)
    root_pattern='<p class="itemText">([\s\S]*?)</p>'  # 加上 () 圆括号 ：加入组， 就只匹配到了中间的内容，不包括这个标签
    name_pattern='<b>([\s\S]*?)</b>'
    number_pattern='<em>([\s\S]*?)</em>'
    def __fetch_content(self):
        """
        This is method
        :return:
        """
        # This is a HTTP request
        result=request.urlopen(Spider.url)  # This is a HTTP request
        htmls=result.read()
        htmls=str(htmls,encoding="utf-8")
        return htmls

    def __analysis(self,htmls):
        root_html=re.findall(Spider.root_pattern,htmls)
        anchors=[]
        for item in root_html:
            name = re.findall(Spider.name_pattern,item)
            number= re.findall(spider.number_pattern,item)
            anchor={"name":name,"number":number}
            anchors.append(anchor)
        return anchors

    def __refine(self,anchors):
        """前面的name和number输出结果还有多余的空格等其它字符的话,此函数再处理掉这些不需要的字符"""
        #法一： for.....
        #法二：定义一个lambda的表达式????????????????????????????????????????????????????
        l=lambda anchor: {
            "name":anchor["name"][0].strip(),
            "number":anchor["number"][0]
            }  # anchor["name"] 是findall返回的列表，里面只有一个元素，所以索引是0
        return map(l,anchors) # 是一个对象，后面要使用list转换成列表

    def __sort(self,anchors):
        anchors=sorted(anchors,key=self.__sort_seed,reverse=True)   # 调用函数__sort_seed居然没有带括号和一个必要参数？？？？？？？？？？？？？？
        return anchors

    def __sort_seed(self,anchor):
        # 提取数字，去掉里面的单位，如“人”
        r = re.findall("\d*",anchor["number"])  #  \d  在正则里面是 数字
        number = float(r[0])
        if "万" in anchor["number"]:
            number *= 10000
        return number

    def __show(self,anchors):
#        for anchor in anchors:
        for rank in range(0,len(anchors)):     # 打印排名序号
            print("rank " + str(rank+1)
                  + ":  " + anchors[rank]["name"]
                  + "   "+ anchors[rank]["number"])

    def go(self):
        htmls=self.__fetch_content()
        anchors=self.__analysis(htmls)
        anchors=list(self.__refine(anchors))
        anchors=self.__sort(anchors)
        self.__show(anchors)

spider=Spider()
spider.go()

