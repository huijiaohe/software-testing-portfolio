import pytest
from selenium.webdriver.common.by import By

class TestCart:

    @pytest.fixture(autouse=True)
    def login(self, driver):
        """前置条件：登录成功"""
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

    def test_add_item_to_cart(self, driver):
        """添加商品到购物车"""
        # 点击第一个商品的“Add to cart”按钮
        driver.find_element(By.CSS_SELECTOR, ".btn_inventory").click()
        # 点击购物车图标
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        # 获取购物车中的商品数量
        cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
        # 断言购物车中有 1 件商品
        assert len(cart_items) == 1

    def test_remove_item_from_cart(self, driver):
        """从购物车移除商品"""
        # 先添加商品到购物车（复用 login fixture 已登录）
        driver.find_element(By.CSS_SELECTOR, ".btn_inventory").click()
        # 进入购物车页面
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        # 点击“Remove”按钮
        driver.find_element(By.CSS_SELECTOR, ".cart_button").click()
        # 获取购物车中的商品数量
        cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
        # 断言购物车为空
        assert len(cart_items) == 0

