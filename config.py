import json

#本文档用于生成siteconfig.json文件。

config = [{
    'sitename':'美国白宫官网',
    'starturl':'https://www.whitehouse.gov/issues/economy-jobs/',
    'listXpath':r'//article//h2/a/@href',
    'OriginalUrl':"",
    'titleXpath':r'//*[@id="main-content"]/div/div/h1/text()',
    'timeXpath':r'//*[@id="main-content"]/div[1]/div/div/p/time/text()',
    'contentXpath':r'//*[@id="main-content"]/div[2]/div/div/p/text()',
    'authorXpath':r'//*[@id="main-content"]/div[1]/div/p/text()'
},
    {
        'sitename': '美国财政部官网',
        'starturl': 'https://home.treasury.gov/news/press-releases/',
        'listXpath': r'//*[@id="block-hamilton-content"]//h2/a/@href',
        'OriginalUrl':"https://home.treasury.gov",
        'titleXpath': r'//*[@id="block-hamilton-page-title"]/h1/span/text()',
        'timeXpath': r'//*[@id="block-hamilton-content"]/article/div//time/text()',
        'contentXpath': r'//*[@id="block-hamilton-content"]/article/div//p/text()',
        'authorXpath': r''
    },
    {
        'sitename': '美国国会预算办公室',
        'starturl': 'https://www.cbo.gov/most-recent',
        'listXpath': r'//*[@id="content"]/div//span/a/@href',
        'OriginalUrl': "https://www.cbo.gov",
        'titleXpath': r'//*[@id="page-title"]/text()',
        'timeXpath': r'//*[@class="date-display-single"]/text()',
        'contentXpath': r'//*[@id="content-panel"]//p/text()',
        'authorXpath': r''
    }
]
with open("siteconfig.json", "w") as text:
    json.dump(config, text)