import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Web_data.chrome import Browser


class Ranstad(Browser):

    def ranstad_action(self, url):
        try:
            self.driver.get(url)
            self.ranstad_fill()
            print('Tack för din ansökan!')
            self.driver.quit()
        except:
            self.driver.refresh()
            self.ranstad_fill()
            print('Tack för din ansökan!')
            self.driver.quit()

    def ranstad_fill(self):
        _ = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.ID, 'content')))
        self.driver.find_element(By.ID, 'firstname').send_keys(self.profile.get_f_name())
        self.driver.find_element(By.ID, 'lastname').send_keys(self.profile.get_l_name())
        self.driver.find_element(By.ID, 'email').send_keys(self.profile.get_email())
        self.driver.find_element(By.ID, 'firstname').send_keys(Keys.PAGE_DOWN)
        self.driver.find_element(By.ID, 'accept-cookies').click()
        self.driver.find_elements(By.CLASS_NAME, 'phone_input')[0].send_keys(self.profile.get_telefon())
        self.driver.find_elements(By.XPATH, '//input[@type="file"]')[0].send_keys(self.profile.get_cv_file_location())
        self.driver.find_elements(By.XPATH, '//span[@class="rms__template__selection-control__input--2lsy0"]')[4].click()
        self.driver.find_element(By.XPATH, '//input[@type="submit"]').click()
        _ = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH, '//div[@class="hero-space hero-space--red hidden-print padding-bottom-130"]')))


if __name__ == '__main__':
    pass
    # cs = Ranstad()
    # url = "https://www.randstad.se/arbetssokande/jobb/ansok/cloud-developer-in-gothenburg-201365366/?jobsite=AMS&utm_source=AMS&utm_medium=jobboard"
    # cs.ranstad_action(url)