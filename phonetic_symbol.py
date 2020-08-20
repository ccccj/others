import urllib.request
import ssl
import re
from bs4 import BeautifulSoup
from distutils.filelist import findall
import openpyxl
import pandas as pd

ssl._create_default_https_context = ssl._create_unverified_context

def getdata(word):
    url = "https://www.youdao.com/w/eng/" + word + "/#keyfrom=dict2.index"
    data = urllib.request.urlopen(url).read()
    z_data = data.decode('UTF-8')
    return z_data

def pac(word):
    try:
        contents = getdata(word)
        soup = BeautifulSoup(contents, "html.parser")
        span = soup.find_all("span", attrs={"class" :"phonetic"})[1]
        span = str(span)
        left = 0
        right = 10
        t = 0
        for i in span:
            if i == '[':
                left = t
            if i == ']':
                right = t
            t = t + 1
        return span[left : right + 1]
    except IndexError:
        return ' '

wb = openpyxl.load_workbook('/Users/Amon/Desktop/words1.xlsx')
ws = wb.active
li = []
for i in range(222, 802):
    c = ws['B' + str(i)].value
    print(c)
    if (' ' in c) == True:
        li.append(' ')
    else:
        ret = pac(c)
        print(ret)
        li.append(ret)
    if i % 20 == 0:
        print('=============================')
        print(i)
        frame = pd.DataFrame({'a':li})
        frame.to_csv('/Users/Amon/Desktop/k.xlsx', mode='a', index=False, header=False,)
        li = []





#
