#爬取http://newrank.cn/public/info/list.html?period=day&type=data网址，获取表单网页代码
#coding:utf-8
import requests
import json
s = requests.session()
url='http://www.newrank.cn/xdnphb/list/day/rank'
da={  'end':'2016-04-19',
      'rank_name':'时事',
      'rank_name_group':'资讯',
      'start':'2016-04-19',
      'nonce':'f29a38df2',
      'xyz':'72f2dc2a91034a7a377c066e8f33c369'
      }
headers={
      'Host': 'www.newrank.cn',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
      'Accept': 'application/json, text/javascript, */*; q=0.01',
      'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
      'Accept-Encoding': 'gzip, deflate',
      'Content-Type':' application/x-www-form-urlencoded; charset=UTF-8',
      'X-Requested-With': 'XMLHttpRequest',
      'Referer':'http://www.newrank.cn/public/info/list.html?period=day&type=data',
      'Cookie':'CNZZDATA1253878005=692730084-1459139468-%7C1461144916',
      'Connection': 'keep-alive',
      'Cache-Control': 'max-age=0'
      }
url='http://www.newrank.cn/xdnphb/list/day/rank'
r=s.post(url,data=da,headers=headers)
print h.content    #表单异步加载的代码
js=json.loads(r.content)   #使用json模块解析成字典
