# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 14:20:27 2016

@author: Venkata Jagannath
PROJECT IN PROGRESS

"""


from selenium import webdriver
import random,time


path='C:/Users/Venkata Jagannath/Desktop/Python/chromedriver_win32/chromedriver.exe'
browser = webdriver.Chrome(executable_path=path)

url='https://www.reddit.com/r/india'
browser.get(url)

text=[]
link=[]

links=browser.find_elements_by_class_name('title may-blank')

for a in links:
    print(a.get_attribute('text'))
    time.sleep(random.uniform(3.5,6.9))



for a in browser.find_elements_by_xpath('//*[@id="thing_t3_42x3jz"]/div[2]/p[1]/a'):
    print(a.get_attribute('text'))