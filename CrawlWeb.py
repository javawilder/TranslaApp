#此代码主要是从给定腾讯新闻网页中爬取新闻的题目，时间，正文，作者
from requests import *
import requests
import GoogleTransla
import json
from lxml import etree
import datetime
import SendEmail
import mainApp
import tkinter
import pypandoc
import lxml.etree
from lxml.etree import *
import queue


def getHTMLText(url):
    try:
        r = requests.get(url,verify='cacert.pem',timeout = 10)
        return r.text
    except requests.exceptions.ConnectTimeout:
        return ""


def getLinkList(dic):
    url = dic['starturl']
    html = getHTMLText(url)
    selector = etree.HTML(html)
    links = selector.xpath(dic['listXpath'])
    return links

def getContent(dic,articles,w,isSeen):
    links = getLinkList(dic)
    if isSeen:
        with open("seen.json") as seen:
            seenLink = json.load(seen)
    else:
        seenLink = []
    for link in links:
        link = dic['OriginalUrl'] + link
        if link in seenLink:
            w.Scrolledtext1.insert(tkinter.END,"跳过已抓取" + link + "\n")
            w.Scrolledtext1.update()
            continue
        else:
            seenLink.append(link)
            html = getHTMLText(link)
            selector = etree.HTML(html)
            title = selector.xpath(dic['titleXpath'])
            if title:
                w.Scrolledtext1.insert(tkinter.END,"正在抓取：" + title[0] + "\n")
                w.Scrolledtext1.update()
            else:
                title = '无标题'
            time = selector.xpath(dic['timeXpath'])
            author = dic['sitename']
            paras = selector.xpath(dic['contentXpath'])
    #将爬取到的文章用字典格式来存
        article = {
         'Title' : str(title).replace("'"," ").replace('"'," ").replace("xa0"," "),
         'Link' : str(link),
         'Time' : str(time).replace("'"," ").replace('"'," "),
         'Paragraph' : str(paras).replace("'"," ").replace('"'," ").replace("\\"," ").replace("xa0"," "),
         'Author' : str(author).replace("'"," ").replace('"'," ")
       }
        if len(article['Paragraph']) > 10: #内容大于10个字符才进入搜索
            articles.append(article)
    with open("seen.json",'w') as seen:
        json.dump(seenLink,seen)
    return articles

def IOarticle(articles,w, isTransla):
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    filename = "result\\" + nowTime + ".md"
    fo = open(filename, "w+", encoding="utf-8")
    for article in articles:
        fo.writelines("# "+ article['Title'] + "\r\n")
        if isTransla:
            t = GoogleTransla.translateGoogle(article['Title'])
            fo.writelines("**参考译文：**" + t + "\r\n")
            w.Scrolledtext1.insert(tkinter.END, "正在翻译" + t + "\r\n")
            w.Scrolledtext1.update()
        fo.writelines("**来源：**" + article['Link'] + "\r\n")
        fo.writelines(article['Time'].strip() + "\r\n")
        if isTransla:
            fo.writelines(GoogleTransla.translateGoogle(article['Time'].strip().replace("'"," ").replace('"'," "))+ "\r\n")
        fo.writelines("**正文：**" + article['Paragraph'] + "\r\n")
        if isTransla:
            try:
                fo.writelines("**参考译文：**" + GoogleTransla.translateGoogle(article['Paragraph'].replace("'"," ").replace('"'," ") + "\n"))
            except:
                fo.writelines("文本太长，暂时只提供前2000字符的翻译\r\n")
                fo.writelines("**参考译文：**" + GoogleTransla.translateGoogle(
                    article['Paragraph'][:10000].replace("'", " ").replace('"', " ") + "\r\n"))
        fo.writelines("\n **来源网站：**" + article['Author'] + "\r\n")
        fo.writelines("\r\n\n\n")
    fo.writelines("以上文件生成于" + datetime.datetime.now().strftime('%Y%m%d %H:%M:%S') )
    fo.close()
    w.Scrolledtext1.insert(tkinter.END, "抓取文件已生成，在result目录下查找\r\n")
    w.Scrolledtext1.update()
    with open("text.json","w") as text:
        json.dump(articles,text)
    return filename

def mdTohtmldoc(filename,isDOC,isHTML):
    if isDOC:
        output = pypandoc.convert_file(filename,'docx',format='md',outputfile=filename[:-3]+".docx")
    if isHTML:
        output = pypandoc.convert_file(filename,'html',format='md',outputfile=filename[:-3]+".html",extra_args=["--ascii"])

def main(w):
    articles = []
    with open("siteconfig.json") as site:
        webs = json.load(site)
    for web in webs:
        articles = getContent(web,articles,w);
    filename = IOarticle(articles,w)
    SendEmail.send_mail(filename,filename,w)
    # getWHList(keyWord="china")

