# -*- coding: utf-8 -*-

__author__ = 'zyh'


import requests
import re
import json


citys = {
	'石家庄'   : '565',
	'唐山'    : '566',
	'邯郸'    : '568',
	'保定'    : '570',
	'沧州'    : '573',
	'邢台'    : '569',
	'廊坊'    : '574',
	'承德'    : '572',
	'张家口'   : '571',
	'衡水'    : '575' ,
	'秦皇岛'   : '567' ,
	'青海'    :'558' 
}



def get_company(city):
    pass
    url = "https://sou.zhaopin.com/p=%d?jl=" + city
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'}

    for i in range(pages):
        try:
            r = requests.get(url, headers = headers)
        except:
            break

def get_more_info(company):
    url = "https://www.qichacha.com/g_HB_%d.html"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
        'cookie': 'QCCSESSID=90jfvpflipo29bsisbr6q51u13; UM_distinctid=168116deb8f589-06c0d1461d1bd1-414f0120-13c680-168116deb90494; hasShow=1; _uab_collina=154648064341095701682524; saveFpTip=true; acw_tc=7cefef9b15464806345281311ee191640651953bafc73b46548d6de772; zg_did=%7B%22did%22%3A%20%22168116deb9e337-043f372d829622-414f0120-13c680-168116deba03f%22%7D; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201546480642979%2C%22updated%22%3A%201546481131442%2C%22info%22%3A%201546480642982%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.sogou.com%22%7D; CNZZDATA1254842228=254713797-1546479017-https%253A%252F%252Fwww.sogou.com%252F%7C1546479017; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1546480643; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1546481132'
        }
    
    r = requests.get(url%1, headers = headers)

    name = re.findall("<span class=\"name\">(.*?)</span>", r.text, re.S)
    local = re.findall("<i class=\"i i-local\"></i>(.*?)</small> </span>", r.text, re.S)

if __name__ == "__main__":

    url = "https://fe-api.zhaopin.com/c/i/sou?start=90&pageSize=90&cjs=ityId=565&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kt=3&_v=0.69283231&x-zp-page-request-id=fdebd73355714fa690877faa90b0567a-1546486575033-639894"

    r = requests.get(url)
    with open('sth.txt', 'w', encoding = 'utf-8') as f:
        f.write(str(r.content, 'utf-8'))


    
    
    
