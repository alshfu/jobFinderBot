from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from Web_data.chrome import Browser


class Ranstad(Browser):

    def ranstad_action(self, url):
        self.driver.get(url)
        sleep(5)
        self.driver.implicitly_wait(5)
        sleep(2)
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))
        self.driver.execute_script('document.getElementsByTagName("input")[7].style.display = "unset"')
        self.driver.execute_script('document.getElementsByTagName("input")[9].style.display = "unset"')
        sleep(3)
        self.driver.find_elements(By.CLASS_NAME, 'form-control')[0].send_keys(self.profile.get_f_name())
        self.driver.find_elements(By.CLASS_NAME, 'form-control')[1].send_keys(self.profile.get_l_name())
        self.driver.find_elements(By.CLASS_NAME, 'form-control')[2].send_keys(self.profile.get_email())
        self.driver.find_elements(By.CLASS_NAME, 'form-control')[3].send_keys(self.profile.get_telefon())
        self.driver.find_elements(By.CLASS_NAME, 'form-control')[4].send_keys(self.profile.get_street())
        self.driver.find_elements(By.CLASS_NAME, 'form-control')[5].send_keys(self.profile.get_zip_code())
        self.driver.find_elements(By.CLASS_NAME, 'form-control')[6].send_keys(self.profile.get_town())
        self.driver.find_elements(By.CLASS_NAME, 'form-control')[6].send_keys(Keys.PAGE_DOWN)
        self.driver.find_elements(By.TAG_NAME, 'input')[8].send_keys(self.profile.get_cv_file_location())
        self.driver.find_elements(By.TAG_NAME, 'input')[11].send_keys(self.profile.get_cover_later_file_location())
        self.driver.find_elements(By.CLASS_NAME, 'custom-control-label')[2].click()
        sleep(2)
        self.driver.find_elements(By.CLASS_NAME, 'btn-outline-primary')[2].click()
        sleep(5)
        print('Tack för din ansökan!')
        self.driver.quit()
