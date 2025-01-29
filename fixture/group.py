import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        # if not wd.current_url.endswith("/group.php") and len(wd.find_elements(By.NAME, "new")) > 0:
        #     self.app.wd.find_element(By.LINK_TEXT, "groups").click()
        elements = len(wd.find_elements(By.NAME, "new"))
        print(elements)
        if not wd.current_url.endswith("/group.php"):
            self.app.wd.find_element(By.LINK_TEXT, "groups").click()

    def create(self, group):
        print("Создание группы")
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        try:
            wd.find_element(By.NAME, "new").click()
        except NoSuchElementException:
            time.sleep(2)
            wd.find_element(By.XPATH, "(//input[@value='New group'])[1]").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()
        self.group_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def fill_group_form(self, group):
        # fill group form
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        wd.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def select_first_group(self):
        # select first group
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()

    def select_group_by_index(self, index):
        # select first group
        wd = self.app.wd
        wd.find_elements(By.NAME, "selected[]")[index].click()

    def modify_first_group(self):
        self.modify_group_by_index(0)

    def modify_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # open modification form
        wd.find_element(By.NAME, "edit").click()
        # fill group from
        self.fill_group_form(new_group_data)
        # submit modification
        wd.find_element(By.NAME, "update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def return_to_groups_page(self):
        # return to groups page
        self.app.wd.find_element(By.LINK_TEXT, "group page").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        count_elements = len(wd.find_elements(By.NAME, "selected[]"))
        print("Всего групп:", count_elements)
        return count_elements

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements(By.CSS_SELECTOR, "span.group"):
                text = element.text
                id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)

