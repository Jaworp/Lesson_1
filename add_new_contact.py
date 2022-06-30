# -*- coding: utf-8 -*-
from selenium import webdriver
#from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from parameters import parameters

import unittest

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_untitled_test_case(self):
        wd = self.wd
        self.open_pages(wd)
        self.login(wd, username="admin", password="secret")
        self.add_new_contact(wd)
        self.fill_form(wd, parameters(f_name="Piter", l_name="Nazwiskowy", nick="Jawi", title="tester",
                  address="Wyspa, ul. Zjawiskowa 20", home_number="54-567-890", mobile_number="400-565-678",
                  email="adres@email.com", day_b="3", month_b="February", year_b="1980", group="Domowa"))
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def fill_form(self, wd, parameter):
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(parameter.f_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(parameter.l_name)
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(parameter.nick)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(parameter.title)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(parameter.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(parameter.home_number)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(parameter.mobile_number)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(parameter.email)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(parameter.day_b)
        wd.find_element_by_xpath("//option[@value='4']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(parameter.month_b)
        wd.find_element_by_xpath("//option[@value='February']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(parameter.year_b)
        wd.find_element_by_name("new_group").click()
        Select(wd.find_element_by_name("new_group")).select_by_visible_text(parameter.group)
        wd.find_element_by_xpath("//div[@id='content']/form/select[5]/option[6]").click()
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("To są notatki2")
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def add_new_contact(self, wd):
        wd.find_element_by_link_text("add new").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value=\"<?= ucfmsg('LOGIN'); ?>\"]").click()

    def open_pages(self, wd):
        wd.get("http://127.0.0.1/addressbook/")

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
