__author__ = 'Давыдов'

# coding: utf-8
from selenium import webdriver
from unittest import TestCase
import unittest

class Test_Yandex(TestCase):

    def test_search(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.get("http://www.yandex.ru")
        element = driver.find_element_by_name('text')
        input_text ='тестирование'
        element.send_keys(input_text)
        element = driver.find_element_by_xpath("//button[@type='submit']")
        element.click()
        title_value = driver.title

        try:
            self.assertIn(input_text,title_value, "Неверное значение")
        finally:
            driver.close()

    def test_search2(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.get("http://www.yandex.ru")
        element = driver.find_element_by_name('text')
        input_text =''
        element.send_keys(input_text)
        element = driver.find_element_by_xpath("//button[@type='submit']")
        element.click()
        title_value = driver.title

        try:
            self.assertEqual("Яндекс: задан пустой поисковый запрос", title_value, "Неверное значение")
        finally:
            driver.close()
            
    def test_search3(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.get("http://www.yandex.ru")
        driver.find_element_by_xpath("//div[10]/div/a/span").click()
        tag = driver.find_element_by_id("tab-rasp").get_attribute('href')
        driver.get(tag)
        try:
            self.assertEqual(driver.current_url,tag,"Неправильный переход")

        finally:
            driver.close()

if __name__ == '__main__':
    unittest.main()
