"""
Title     : XML2 - Find the Maximum Depth
Subdomain : XML
Domain    : Python
Author    : Pavankumar Hegde
Problem   : https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth/problem
"""


# Solution


import xml.etree.ElementTree as etree

maxdepth = 0


def depth(elem, level):
    global maxdepth
    level = level + 1
    maxdepth = max(maxdepth, level)
    for child in elem:
        depth(child, level)


if __name__ == "__main__":
    n = int(input())
    xml = ""
    for i in range(n):
        xml = xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)