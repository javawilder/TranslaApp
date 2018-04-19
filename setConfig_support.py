#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.12
# In conjunction with Tcl version 8.6
#    Apr 08, 2018 03:01:34 PM


import sys
import json
import tkinter.messagebox as meg
import CrawlWeb
import sitexpathconfigset

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
def set_Tk_var():
    global sendMail
    sendMail = BooleanVar()
    global Translate
    Translate = BooleanVar()
    global Seen
    Seen = BooleanVar()
    global email
    email = StringVar()
    global MD
    MD = BooleanVar()
    global HTML
    HTML = BooleanVar()
    global DOC
    DOC = BooleanVar()
    global sitename
    sitename = StringVar()
    global starturl
    starturl = StringVar()
    global listXpath
    listXpath = StringVar()
    global OriginalUrl
    OriginalUrl = StringVar()
    global titleXpath
    titleXpath = StringVar()
    global timeXpath
    timeXpath = StringVar()
    global contentXpath
    contentXpath = StringVar()
    global aurthorXpath
    aurthorXpath = StringVar()

def Saveconfig():
    print('setConfig_support.Saveconfig')
    appConfig[0]['SENDMAIL'] = sendMail.get()
    appConfig[0]['TRANSLATE'] = Translate.get()
    appConfig[0]['SEEN'] = Seen.get()
    appConfig[0]['MD'] = MD.get()
    appConfig[0]['HTML'] = HTML.get()
    appConfig[0]['DOC'] = DOC.get()
    with open("appConfig.json",'w') as c:
        json.dump(appConfig,c)


def isDOC():
    print('setConfig_support.isDOC')


def isHTML():
    print('setConfig_support.isHTML')


def isMd():
    print('setConfig_support.isMd')


def isSeen():
    print('setConfig_support.isSeen')


def isSendMail():
    print('setConfig_support.isSendMail')


def isTranslate():
    print('setConfig_support.isTranslate')


def setEmail():
    appConfig[0]['MAIL'] = email.get()
    with open("appConfig.json",'w') as c:
        json.dump(appConfig,c)
    print('setConfig_support.setEmail')


def setXpath():
    d ={"sitename": sitename.get(),
        "starturl": starturl.get(),
        "authorXpath": aurthorXpath.get(),
        "OriginalUrl": OriginalUrl.get(),
        "timeXpath": timeXpath.get(),
        "titleXpath": titleXpath.get(),
        "listXpath": listXpath.get(),
        "contentXpath": contentXpath.get()}
    for i in range(len(siteconfigjson)):
        if d['starturl'] == '':
            meg.showinfo("信息","起始网址不能为空")
            return
        elif d['contentXpath'] == '':
            meg.showinfo("信息", "内容Xpath不能为空")
            return

        if d['starturl'] in siteconfigjson[i]["starturl"]:
            meg.showinfo("信息","本网页抓取规则已收录"+ str(i))
            return
    try:
        links = CrawlWeb.getLinkList(d)
        for link in links:
            link = d['OriginalUrl'] + link
            CrawlWeb.getHTMLText(link)
    except:
        meg.showinfo('错误提示', 'Xpath 表达式错误，请重新输入')
        return
    siteconfigjson.append(d)
    with open("siteconfig.json",'w') as c:
        json.dump(siteconfigjson,c)
    print('setConfig_support.setXpath')
    meg.showinfo("提示","已成功加入"+d['sitename']+"的抓取规则")

def xhelp():
    sitexpathconfigset.vp_start_gui(root)
    # newtop = Toplevel(root)
    #
    # listSite1 = Listbox(newtop)
    # listSite2 = Listbox(newtop)
    # buttonDel = Button(newtop)
    #

    # listSite1.pack()
    # listSite2.pack()
    # buttonDel.pack()
    #
    # newtop.mainloop()
    print('setConfig_support.xhelp')



def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    with open("appConfig.json") as appconfig:
        global appConfig
        appConfig = json.load(appconfig)
    if appConfig[0]['SENDMAIL']:
        w.Checkbutton1.select()
    else:
        w.Checkbutton1.deselect()
    if appConfig[0]['TRANSLATE']:
        w.Checkbutton2.select()
    else:
        w.Checkbutton2.deselect()
    if appConfig[0]['SEEN']:
        w.Checkbutton3.select()
    else:
        w.Checkbutton3.deselect()
    w.Entry1.insert(0,str(appConfig[0]['MAIL']))
    w.Entry1.update()
    if appConfig[0]['MD']:
        w.Checkbutton4.select()
    else:
        w.Checkbutton4.deselect()
    if appConfig[0]['DOC']:
        w.Checkbutton6.select()
    else:
        w.Checkbutton6.deselect()
    if appConfig[0]['HTML']:
        w.Checkbutton5.select()
    else:
        w.Checkbutton5.deselect()
    with open("siteconfig.json") as sconfig:
        global siteconfigjson
        siteconfigjson = json.load(sconfig)


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import setConfig
    setConfig.vp_start_gui()
