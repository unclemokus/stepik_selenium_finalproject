#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 22:12:56 2019

@author: io
"""

from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET = (By.XPATH, "//a[text()='View basket']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.NAME, "registration-email")
    PASSWORD = (By.NAME, "registration-password1")
    PASSWORD_REPEAT = (By.NAME, "registration-password2")
    SUBMIT = (By.NAME, "registration_submit")


class ProductPageLocators():
    ADDBASKET_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE_FOR_PRODUCT = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) strong")
    SUCCESS_MESSAGE_WITH_PRICE = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert:nth-child(1)")

class BasketPageLocators():
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items")
    BASKET_MESSAGE = (By.XPATH, "//p[contains(text(), 'Your basket is empty.')]")