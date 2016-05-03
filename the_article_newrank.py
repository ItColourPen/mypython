#对newrank下的公众号搜索的文章进行爬取，
#coding:utf-8
import requests
import json
from bs4 import BeautifulSoup
def get_url(i,article):#爬取得是热点文章还是近期文章，获取文章的网址
      url='http://www.newrank.cn/xdnphb/data/getAccountArticle'
      s=requests.session()
      data={'nonce':'7831bad1c',
            'uuid':'B06CF7ADA77947B013CAF3F9DDDB1E61',
            'xyz':'2e220fadce70d467b9e427d14464daa4'
            }
      headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'}
      source=s.post(url,data=data,headers=headers)
      js=json.loads(source.content)
      value=js['value']
      if article=='lastestArticle':
            lastestArticle=value[article]
            return lastestArticle[i]['url']
      else:
            topArticle=value[article]
            return topArticle[i]['url']
def spyder(url):#对文章进行爬取
      headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'}
      source=requests.get(url,headers=headers)
      soup=BeautifulSoup(source.text)
      c=soup.find_all('p')
      for each in c:
            print each.get_text()
if __name__ == '__main__':
      for each in ('lastestArticle','topArticle'):
            for i in range(0,10):
                  spyder(get_url(i,each))
