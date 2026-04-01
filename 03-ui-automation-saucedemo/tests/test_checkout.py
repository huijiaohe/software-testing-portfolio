import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class TestCheckout:

    @pytest.fixture(autouse=True)
    def login_and_add_item(self, driver):

        """前置条件：登录并添加一个商品到购物车"""
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
        )
        driver.find_element(By.CSS_SELECTOR, ".btn_inventory").click()

    def test_checkout_full_flow(self, driver):
        """完整结账流程"""
        # 进入购物车
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        # 点击 Checkout
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "checkout"))
        )
        driver.find_element(By.ID, "checkout").click()
        # 填写结账信息
        driver.find_element(By.ID, "first-name").send_keys("Test")
        driver.find_element(By.ID, "last-name").send_keys("User")
        driver.find_element(By.ID, "postal-code").send_keys("12345")
        driver.find_element(By.ID, "continue").click()
        # 点击 Finish
        driver.find_element(By.ID, "finish").click()
        # 验证完成
        complete_header = driver.find_element(By.CLASS_NAME, "complete-header")
        assert "Thank you for your order!" in complete_header.text
