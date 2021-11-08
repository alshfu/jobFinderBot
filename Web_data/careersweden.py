import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

from Web_data.chrome import Browser


class Careersweden(Browser):

    def careersweden_action(self, url):
        self.driver.get(url)
        try:
            _ = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.ID, 'tt-cookie-alert__accept-all')))
            self.driver.find_element(By.ID, 'tt-cookie-alert__accept-all').click()
            self.driver.find_elements(By.CLASS_NAME, 'btn-apply')[0].click()
            sleep(3)
            ###########################################################################################################
            _ = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.ID, 'candidate_first_name')))
            self.driver.find_element(By.ID, 'candidate_first_name').send_keys(self.profile.get_f_name())
            self.driver.find_element(By.ID, 'candidate_last_name').send_keys(self.profile.get_l_name())
            self.driver.find_element(By.ID, 'candidate_email').send_keys(self.profile.get_email())
            self.driver.find_element(By.ID, 'candidate_phone').send_keys(self.profile.get_telefon())
            self.driver.find_element(By.ID, 'candidate_resume_remote_url').send_keys(self.profile.get_cv_file_location())
            self.driver.find_element(By.ID, 'candidate_job_applications_attributes_0_cover_letter').send_keys(self.profile.get_p_brev())
            self.driver.find_element(By.XPATH, '//input[@type="submit"]').click()
            print('Tack för din ansökan!')
            self.driver.quit()
        except selenium.common.exceptions.NoSuchElementException or selenium.common.exceptions.TimeoutException:
            self.driver.quit()


if __name__ == '__main__':
    pass

