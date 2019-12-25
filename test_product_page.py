#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 16:28:52 2019

@author: io

WARNING!!! You need install Faker (pip install faker) for run this code
"""
import pytest
import time
import faker
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


product_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        print("\nstart open login page...")
        login_page = LoginPage(browser, link)
        login_page.open()
        print("\ncheck - login page elements")
        login_page.should_be_login_page()
        print("\nstart new_user registration ...")
        f = faker.Faker()
        email = f.email()
        password = "holyshit57"
        login_page.register_new_user(email, password)
        print("\ncheck - should be authorized_user...")
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, product_link)
        product_page.open()
        product_page.should_be_add_to_basket_button()
        time.sleep(1)
        product_page.solve_quiz_and_get_code()
        time.sleep(3)
        product_page.verify_message_added_product_name_to_basket()
        product_page.verify_message_product_price_to_basket()

    @pytest.mark.other
    def test_user_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, product_link)
        product_page.open()
        product_page.should_not_be_success_message()

@pytest.mark.need_review
@pytest.mark.parametrize('offer_number', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, offer_number):
    product_link = f"http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer{offer_number}"
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.should_be_add_to_basket_button()    # verify AddToBasket button is exist on current page
    time.sleep(1)
    product_page.solve_quiz_and_get_code()
    time.sleep(3)
    product_page.verify_message_added_product_name_to_basket()
    product_page.verify_message_product_price_to_basket()

@pytest.mark.other
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    time.sleep(3)
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_url()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_products()
    basket_page.should_be_message()


#Negative test cases:
@pytest.mark.other
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.should_be_add_to_basket_button()
    product_page.solve_quiz_and_get_code()
    product_page.should_not_be_success_message()

@pytest.mark.other
def test_quest_cant_see_success_message(browser):
    product_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.should_not_be_success_message()

@pytest.mark.other
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.should_be_add_to_basket_button()
    product_page.solve_quiz_and_get_code()
    product_page.message_should_be_disappeared_after_adding_product_to_basket() 
