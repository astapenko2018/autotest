from selenium import webdriver
from selenium.webdriver.common.by import By


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(60)

    def open_home_page(self):
        # open home page
        self.wd.get("http://localhost/addressbook/")

    def login(self, username, password):
        # login
        self.open_home_page()
        self.wd.find_element(By.NAME, "user").send_keys(username)
        self.wd.find_element(By.NAME, "pass").click()
        self.wd.find_element(By.NAME, "pass").send_keys(password)
        self.wd.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

    def create_group(self, group):
        self.open_groups_page()
        # init group creation
        self.wd.find_element(By.NAME, "new").click()
        self.wd.find_element(By.NAME, "group_name").click()
        self.wd.find_element(By.NAME, "group_name").send_keys(group.name)
        self.wd.find_element(By.NAME, "group_header").click()
        self.wd.find_element(By.NAME, "group_header").send_keys(group.header)
        self.wd.find_element(By.NAME, "group_footer").click()
        self.wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # submit group creation
        self.wd.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()

    def open_groups_page(self):
        self.wd.find_element(By.LINK_TEXT, "groups").click()

    def logout(self):
        # logout
        self.wd.find_element(By.LINK_TEXT, "Logout").click()

    def return_to_groups_page(self):
        # return to groups page
        self.wd.find_element(By.LINK_TEXT, "group page").click()

    # def teardown_method(self, method):
    #     self.wd.quit()

    def destroy(self):
        self.wd.quit()
