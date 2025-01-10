import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select

from testcase.PageObjectModel import CheckBox
from testcase.log import LogGenerator


class Test_worldCup:

    def test_cup2020(self, Setup):
        self.driver = Setup
        self.log=LogGenerator()
        self.CH = CheckBox(self.driver)
        self.CH.Box()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@type='checkbox'][@checked]").click()
        Ac=ActionChains(self.driver)
        self.log.logData().info("Successfully click")
        time.sleep(5)

