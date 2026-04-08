# SauceDemo UI 自动化测试项目

## 项目简介

本项目基于 SauceDemo 电商网站，使用 Python + pytest 实现 UI 自动化测试，覆盖登录、商品浏览、购物车及下单等核心业务流程。

通过自动化测试提高回归测试效率，减少人工重复操作。

---

## 技术栈

* 编程语言：Python
* 自动化框架：pytest
* UI 自动化工具：Selenium
* 设计模式：Page Object Model（POM）

---

## 项目结构

03-ui-automation-saucedemo/
├── pages/              # 页面对象封装
├── tests/              # 测试用例
├── conftest.py         # 全局配置（浏览器初始化等）
├── utils/              # 工具类（可选）
├── pytest.ini          # pytest配置
├── requirements.txt
├── README.md

---

## 自动化测试内容

### 1. 登录模块

* 正确登录
* 错误登录提示校验

### 2. 商品模块

* 商品列表加载验证
* 商品添加购物车

### 3. 下单结账模块

* 查看购物车
* 删除商品
* 填写用户信息
* 完成下单流程

---

## 关键实现

### ✔ pytest管理测试

* 使用 fixture 进行测试前置处理（如浏览器初始化）
* 支持批量执行测试用例

---

## 如何运行

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 运行测试

```bash
pytest
```

### 3. 生成报告

---

##  测试结果

自动化测试覆盖核心业务流程，执行稳定，可用于回归测试。

---

## 项目收获

* 掌握 自动化测试流程
* 理解 设计模式
* 熟悉 pytest 自动化测试框架
* 提升测试代码结构设计能力

