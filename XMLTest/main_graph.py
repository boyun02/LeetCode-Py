#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2023/12/17 16:26
# @Author :wyb
import xml.etree.ElementTree as ET

tree = ET.parse('D:\git_project\LeetCode-Py\XMLTest\in\country_data.xml')
root = tree.getroot()
node1 = tree
from graphviz import Digraph

def visualize_element(element, graph):
    # 添加节点
    graph.node(str(id(element)), element.tag)

    # 添加边
    for child in element:
        graph.edge(str(id(element)), str(id(child)))
        visualize_element(child, graph)

# 创建Digraph对象
graph = Digraph()

# 可视化XML文档的根节点
visualize_element(root, graph)

# 渲染并显示图形
graph.render('example.gv', view=True)