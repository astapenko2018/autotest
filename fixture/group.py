from selenium.webdriver.common.by import By


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        self.app.wd.find_element(By.LINK_TEXT, "groups").click()

    def create(self, group):
        self.open_groups_page()
        # init group creation
        self.app.wd.find_element(By.NAME, "new").click()
        self.app.wd.find_element(By.NAME, "group_name").click()
        self.app.wd.find_element(By.NAME, "group_name").send_keys(group.name)
        self.app.wd.find_element(By.NAME, "group_header").click()
        self.app.wd.find_element(By.NAME, "group_header").send_keys(group.header)
        self.app.wd.find_element(By.NAME, "group_footer").click()
        self.app.wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # submit group creation
        self.app.wd.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        # return to groups page
        self.app.wd.find_element(By.LINK_TEXT, "group page").click()
