from selenium.webdriver.common.by import By


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        # login
        self.app.open_home_page()
        self.app.wd.find_element(By.NAME, "user").send_keys(username)
        # self.app.wd.find_element(By.NAME, "user").clear()
        # self.app.wd.find_element(By.NAME, "pass").click()
        # self.app.wd.find_element(By.NAME, "pass").clear()
        self.app.wd.find_element(By.NAME, "pass").send_keys(password)
        self.app.wd.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

    def logout(self):
        # logout
        wd = self.app.wd
        self.app.wd.find_element(By.LINK_TEXT, "Logout").click()

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements(By.LINK_TEXT, "Logout")) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//div/div[1]/form/b").text[1:-1]

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

