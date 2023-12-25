#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2023/12/17 11:28
# @Author :wyb
import xml.etree.ElementTree as ET
tree = ET.parse('D:\git_project\LeetCode-Py\XMLTest\in\country_data.xml')
root = tree.getroot()
print(root.tag)
print(root.attrib)

for child in root:
    print(child.tag, child.attrib)

print(root[0][0].text)

for neighbor in root.iter('nerghbor'):
    print(neighbor.attrib)

for country in root.findall('country'):
    # print(country.text)
    print(country.attrib)
    print(country.find('rank').text)
    print(country.get('name'))

print(root.findall('.'))
print(root.findall('./country/neighbor'))
print(root.findall(".//year/..[@name='Singapore']"))
print(root.findall(".//*[@name='Singapore']/year"))
print(root.findall(".//neighbor[1]"))