from Web_data.chrome import Browser
from functions import delay_print
from time import sleep
from columnar import columnar


def tab_info(experience_list_item_container, headers):
    educations_information = []
    for card in experience_list_item_container:
        educations_information.append([card.find_elements_by_class_name('title')[0].text,
                                       card.find_elements_by_class_name('interval')[0].text,
                                       card.find_elements_by_class_name('type')[0].text])
    educations_table = columnar(educations_information,
                                headers,
                                justify='c',
                                no_borders=False,
                                terminal_width=500,
                                min_column_width=35,
                                max_column_width=35)
    delay_print('', educations_table, t=0)


def section_title(title):
    print(
        '||')
    print(title)


def skill_info(languages_module):
    skill_string = ''
    for skill_title in languages_module.find_elements_by_class_name('name'):
        skill_string = skill_string + "| " + skill_title.text
    delay_print('', skill_string)


class AcademicWork(Browser):
    def academic_work_action(self, url):
        self.driver.get(url)
        sleep(5)
        self.driver.find_element_by_id('onetrust-accept-btn-handler').click()
        sleep(1)
        self.driver.find_elements_by_class_name('aw-block-button')[1].click()
        print(
            '|')
        print('|Login to Academic WorK')
        delay_print('|E-post', self.profile.get_email(), 0)
        self.driver.find_element_by_id('username').send_keys(self.profile.get_email())
        delay_print('|Password', self.profile.get_password())
        self.driver.find_element_by_id('password').send_keys(self.profile.get_password())
        self.driver.find_element_by_id('login-btn').click()
        sleep(5)
        #
        section_title('|Kontaktinformation : ')
        delay_print('|Namn', self.driver.find_elements_by_class_name('information-item-info')[0].text)
        delay_print('|E-post', self.driver.find_elements_by_class_name('information-item-info')[1].text)
        delay_print('|Telefon', self.driver.find_elements_by_class_name('information-item-info')[2].text)
        #
        section_title('|Utbildning: ')
        education_module = self.driver.find_elements_by_class_name('section')[1]
        experience_list_item_container = education_module.find_elements_by_class_name('experience-list-item-container')
        tab_info(experience_list_item_container, ['Skola', 'Datum', 'Utbildning'])

        #
        section_title('|Arbetslivserfarenhet:  ')
        work_history_module = self.driver.find_elements_by_class_name('section')[2]
        work_history_container = work_history_module.find_elements_by_class_name('experience-list-item-container')
        tab_info(work_history_container, ['Företag', 'Datum', 'Jobb'])

        #
        section_title('|Språk: ')
        skill_info(self.driver.find_elements_by_class_name('section')[3])
        #
        section_title('|Kompetenser: ')
        skill_info(self.driver.find_elements_by_class_name('section')[4])
        #
        section_title('|Övriga kompetenser: ')
        second_skill = self.driver.find_elements_by_class_name('section')[5]
        print('| ' + second_skill.find_elements_by_tag_name('p')[0].text)
        #
        section_title('|Körkort: ')
        driving_licences = self.driver.find_elements_by_class_name('section')[6]
        for driving_license in driving_licences.find_elements_by_class_name('driving-licenses')[0] \
                .find_elements_by_class_name('driving-license'):
            if driving_license.find_elements_by_tag_name('input')[0].is_selected():
                print('|' + driving_license.find_elements_by_tag_name('span')[0].text + ": Ja")
            else:
                print('|' + driving_license.find_elements_by_tag_name('span')[0].text + ": Nej")
        #
        section_title('|Lägg till ett CV i din ansökan:')
        delay_print('', self.profile.get_cv_file_location())
        aw_default_button_for_cv = self.driver.find_elements_by_class_name('aw-default-button')[3]
        aw_default_button_for_cv.find_element_by_name('UploadCv').send_keys(self.profile.get_cv_file_location())
        self.driver.find_elements_by_class_name('aw-button-application')[3].click()
        sleep(5)
        self.driver.find_elements_by_class_name('aw-button-application')[0].click()
        sleep(5)
        self.driver.find_elements_by_class_name('aw-button-application')[0].click()
        sleep(5)
        print('Tack för din ansökan!')
        self.driver.quit()
