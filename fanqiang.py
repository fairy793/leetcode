# -*- coding: utf-8 -*-
# @Author: liangmengmeng
# @Date:   2020-05-31 15:33:42
# @Desc:

import requests
from lxml import etree

url = "https://blog.freeair999.club/v2ray%e5%85%8d%e8%b4%b9%e8%b4%a6%e5%8f%b7/"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text)

result = etree.HTML(response.text)

address_list = result.xpath("//p[contains(text(),'Address')]")

port_list = result.xpath("//p[contains(text(),'Port')]")

uuid_list = result.xpath("//p[contains(text(),'UUID')]")

alterId_list = result.xpath("//p[contains(text(),'alterId')]")


security_list = result.xpath("//p[contains(text(),'security')]")


network_list = result.xpath("//p[contains(text(),'network')]")


path_list = result.xpath("//p[contains(string(),'路径')]")


security_list = result.xpath("//p[contains(string(),'底层传输安全')]")










