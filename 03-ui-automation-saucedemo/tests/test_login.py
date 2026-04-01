
from selenium.webdriver.common.by import By

class TestLogin:

    def test_login_success(self, driver):
        """正常登录：输入正确用户名密码，应跳转到商品列表页"""
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        assert "inventory.html" in driver.current_url

    def test_login_wrong_password(self, driver):
        """错误密码：应显示错误提示"""
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("wrong")
        driver.find_element(By.ID, "login-button").click()
        error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
        assert "Username and password do not match" in error.text

