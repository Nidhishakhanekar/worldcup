from selenium.webdriver.common.by import By


class CheckBox():

    def __init__(self, driver):
        self.driver = driver

    def Box(self):
        self.driver.find_element(By.XPATH, "//a[text()='Checkboxes']").click()


