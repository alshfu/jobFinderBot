from columnar import columnar

from DB.data_base import get_all_information, update_ad_status_id
from Web_data.chrome import Browser
from functions import wait_timer, delay_print, status
from selenium.webdriver.support.ui import Select


def tab_info(data):
    headers = ['Datum',
               'Företag',
               'Typ av jobb',
               'Ort',
               'Status']
    action_info = []
    for action in data:
        action_info.append([action[4],
                            action[5],
                            action[2],
                            action[3],
                            status(action[6])])

    action_info = columnar(action_info,
                           headers,
                           justify='c',
                           no_borders=False,
                           terminal_width=500,
                           min_column_width=35,
                           max_column_width=35)
    delay_print('', action_info, t=0)


def get_action_for_rapport():
    data = get_all_information()
    tab_info(data)
    rapport_data = []
    for action in data:
        if action[6] == 2:
            print(action)
            rapport_data.append([action[4],
                                 action[5],
                                 action[2],
                                 action[3],
                                 action[1]])
    return rapport_data


def info_string_to_display(date: str = '', job_name: str = '', employer_name: str = '') -> str:
    string = f'Den {date} ansökte du om tjänst {job_name} hos {employer_name}'
    return string


class Arbetsformedlingen(Browser):

    def make_reporting(self):
        self.af_login()
        self.rapport_page_action()

    def af_login(self):
        self.driver.get('https://arbetsformedlingen.se/loggain')
        self.driver.find_elements_by_class_name('login-mobil')[0].click()
        wait_timer(5)
        self.driver.find_elements_by_class_name('personal_number_input')[0].send_keys(self.profile.get_ssn())
        self.driver.find_element_by_id('loginButton').click()
        input("open your Mobile Bank ID and press any key when you are reddy")
        self.driver.get(
            'https://arbetsformedlingen.se/for-arbetssokande/mina-sidor/nya-aktivitetsrapporteringen#/dashboard'
            '/pagaende')
        wait_timer(5)

    def rapport_page_action(self):
        self.driver.find_element_by_id('laggTillKnapp').click()
        wait_timer(1)
        select = Select(self.driver.find_element_by_id('inputSelect'))
        select.select_by_value('soktjobb')
        select.select_by_visible_text('Sökt jobb')
        wait_timer(5)
        self.driver.find_elements_by_xpath('//input[@formcontrolname="checkbox"]')[0].click()
        i = 0
        reedy_for_rapport = get_action_for_rapport()
        for data in reedy_for_rapport:
            date = data[0]
            job_name = data[2]
            employer_name = data[1]
            city = data[3]
            self.fill_in_rapport(i=str(i),
                                 date=date,
                                 job_name=job_name,
                                 employer_name=employer_name,
                                 city=city)
            i += 1
            update_ad_status_id(data[4], 5)
        self.driver.find_elements_by_xpath('//input[@formcontrolname="checkbox"]')[0].click()

    def fill_in_rapport(self,
                        i="0",
                        date='2021-09-14',
                        employer_name='Academic Work',
                        job_name='just a Test',
                        city='Göteborg'):
        self.driver.find_element_by_id('mat-input-' + i).send_keys(date)
        self.driver.find_element_by_id('arbetsGivareText').send_keys(employer_name)
        self.driver.find_element_by_id('soktJobbText').send_keys(job_name)
        self.driver.find_element_by_id('ortText').send_keys(city)

        delay_print(string=info_string_to_display(date, job_name, employer_name), t=0.2)
        self.driver.find_element_by_id('submitButton').click()
        delay_print(string='Hämtar nästa activitet .........', t=0.2)


if __name__ == '__main__':
    pass
    # Arbetsformedlingen().make_reporting()
