from time import sleep

import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Web_data.chrome import Browser


class Wise(Browser):
    def wise_action(self, url):
        self.driver.get(url)
        try:
            _ = WebDriverWait(self.driver, self.delay).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'hero')))
            hero = self.driver.find_elements(By.ID, 'hero')[0]
            hero.find_elements(By.TAG_NAME, 'a')[0].click()
            sleep(3)
            ###########################################################################################################
            self.driver.switch_to.window(self.driver.window_handles[1])
            _ = WebDriverWait(self.driver, self.delay).until(
                EC.presence_of_element_located((By.ID, 'tt-cookie-alert__accept-all')))
            sleep(2)
            self.driver.find_element(By.ID, 'tt-cookie-alert__accept-all').click()
            self.driver.find_element(By.ID, 'candidate_first_name').send_keys(self.profile.get_f_name())
            self.driver.find_element(By.ID, 'candidate_last_name').send_keys(self.profile.get_l_name())
            self.driver.find_element(By.ID, 'candidate_email').send_keys(self.profile.get_email())
            self.driver.find_element(By.ID, 'candidate_phone').send_keys(self.profile.get_telefon())
            # TODO: fixa CV och person brev  upp laddning
            # dz_message = self.driver.find_elements(By.CLASS_NAME, 'dz-message')
            # dz_message[0].find_elements(By.XPATH, '//span[@data-forms--inputs--upload-target="desktopText"]')[0].click()
            # self.driver.find_element(By.ID, 'candidate_resume_remote_url').click()
            _ = input("Välj din CV fil and press ENTER")
            # self.driver.find_element(By.ID, 'candidate_file_remote_url').click()
            _ = input("Välj din CV fil and press ENTER")
            self.driver.find_element(By.ID, 'candidate_consent_given').click()
            _ = input("Välj din CV fil and press ENTER")
            self.driver.find_element(By.XPATH, '//input[@type="submit"]').click()
            print('Tack för din ansökan!')
            self.driver.quit()
        except selenium.common.exceptions.NoSuchElementException or selenium.common.exceptions.TimeoutException:
            self.driver.quit()


if __name__ == '__main__':
    pass
