from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from Data.profile import Profile


class Browser:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.profile = Profile(1)


if __name__ == '__main__':
    pass
