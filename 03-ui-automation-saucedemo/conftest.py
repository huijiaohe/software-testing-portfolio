import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
@pytest.fixture(scope="function")
def driver():
    """每个测试函数启动一个浏览器，结束后自动关闭"""
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(5)   # 隐式等待5秒，找不到元素时自动重试
    yield driver
    driver.quit()

