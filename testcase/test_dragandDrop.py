import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Test_Drag:

    def test_dragndrop(self, Setup):
        self.driver = Setup
        self.driver.find_element(By.XPATH, "//a[text()='Drag and Drop']").click()
        A = self.driver.find_element(By.XPATH, "//div[contains(@id,'column-a')]")
        B = self.driver.find_element(By.XPATH, "//div[contains(@id,'column-b')]")
        Ac = ActionChains(self.driver)
        Ac.drag_and_drop(A, B).perform()
        time.sleep(5)
