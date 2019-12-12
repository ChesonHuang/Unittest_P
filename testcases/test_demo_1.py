#!/usr/bin/python3
# -*-coding:utf-8-*-
import unittest
import os
import sys
import time
from selenium import webdriver
#import multiprocess

class TestDemo1(unittest.TestCase):
  def setUp(self):
    '''
    '''
    self.driver = webdriver.Chrome()
    self.driver.implicitly_wait(20)
    self._url = "https://www.baidu.com"
    print("setUp env")
  def tearDown(self):
    '''
    '''
    print("tearDown env")

  def test_demo_1():
    '''
    '''
    self.driver.get(self._url)
    search_btn = self.driver.find_element_by_id("kw")
    search_btn.clear()
    search_btn.send_keys("Hello World!")
    click_btn = self.driver.find_element_by_id("su")
    click_btn.click()
    time.sleep(3)
    title = self.driver.title
    self.assertEqual(title,u"Hello World!_")    

if __name__ == "__main__":
  unittest.main()
