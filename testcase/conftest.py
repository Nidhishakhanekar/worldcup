import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser')


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture
def Setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'edge':
        driver = webdriver.Edge()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        driver.maximize_window()
    else:
        driver = webdriver.Safari()
    driver.get("https://the-internet.herokuapp.com/")
    return driver
