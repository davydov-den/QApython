__author__ = 'Давыдов'
from yandex import Search_bar
class Page():
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)
        self._search_bar = None

    def open(self, url):
        self.driver.get(url)
        return self

    def get_title(self):
        return self.driver.title

    @property
    def search_bar(self):
        if self._search_bar is None:
            self._search_bar = Search_bar(self.driver)

        return self._search_bar


