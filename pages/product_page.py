#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 18:44:40 2019

@author: io
"""

from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def should_be_add_to_basket_button(self):
        self.browser.find_element(*ProductPageLocators.ADDBASKET_BUTTON).click()
       
    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text   # №2 option allows not depend on the content changes

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text  #№2 option allows not depend on the content changes
    def verify_message_added_product_name_to_basket(self):
        #product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text              # №1 option
        message_pname = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_FOR_PRODUCT)
        assert self.get_product_name() == message_pname.text, "Book wasn't added to cart"  # changed to get_product_name() instead product_name

    def verify_message_product_price_to_basket(self):
        #product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text             # №1 option
        message_pprice = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_WITH_PRICE)
        assert self.get_product_price() == message_pprice.text, "Incorrect product price in cart"  # changed to get_product_price() instead product_price

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def message_should_be_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Message isn't dissapeared after adding product to basket"
