__author__ = 'Давыдов'

from unittest import TestCase
from selenium import webdriver
from page import Page
import unittest


class SeleniumTest(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.page = Page(self.driver)
        self.page.open("http://www.yandex.ru")

    def testEntering(self):
        tag = self.page.search_bar.get_attribute()
        self.page.open(tag)
        self.assertEqual(self.driver.current_url,tag,"Неправильный переход")

    def testTitle(self):
        self.page.search_bar.entering("Тестирование")
        self.assertIn('Тестирование', self.page.get_title(), "Неверное значение")

    def testTitle2(self):
        self.page.search_bar.entering("")
        self.assertEqual("Яндекс: задан пустой поисковый запрос",self.page.get_title(), "Неверное значение")



    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
