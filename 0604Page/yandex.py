__author__ = 'Давыдов'
from base_component import BaseComponent

class Search_bar(BaseComponent):
    data ={
        'text': 'text',
        'input_text': 'input',
        'submit':"//button[@type='submit']",
        'button':"//div[10]/div/a/span",
    }

    def entering(self,text):
        self.driver.find_element_by_id(self.data['text']).send_keys(text)
        self.driver.find_element_by_xpath(self.data['submit']).click()

    def get_attribute(self):
        self.driver.find_element_by_xpath("button").click()
        return self.driver.find_element_by_id("tab-rasp").get_attribute('href')
