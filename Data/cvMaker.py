import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class Person:
    def __init__(self, login_name=None, pwd=None, url=None):
        self.url = url
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.get_person_page()
        self.login = login_name
        self.password = pwd

    def get_person_page(self):
        self.driver.get(self.url)

    def do_login(self):
        sleep(5)
        try:
            self.driver.find_element_by_xpath('//*[@class="authwall-join-form__form-toggle form-toggle"]').click()
            self.driver.find_element_by_id('session_key').send_keys(self.login)
            self.driver.find_element_by_id('session_password').send_keys(self.password)
            self.driver.find_elements_by_class_name('sign-in-form__submit-button')[0].click()
        except selenium.common.exceptions.NoSuchElementException:
            self.driver.find_elements_by_class_name('form-toggle')[1].click()
            self.driver.find_element_by_id('login-email').send_keys(self.login)
            self.driver.find_element_by_id('login-password').send_keys(self.password)
            self.driver.find_element_by_id('login-submit').click()
        sleep(5)
        edit_public = self.driver.find_element_by_xpath('//*[@class="relative display-flex justify-space-between"]')
        url = edit_public.find_elements_by_tag_name('a')[0].get_attribute('href')
        self.url = url
        self.get_person_page()

    def get_name(self) -> str:
        try:
            name = self.driver.find_elements_by_class_name('top-card-layout__title')[0].text
            print('name: ' + name)
            return name
        except IndexError:
            self.do_login()
            sleep(5)
            name = self.driver.find_elements_by_class_name('top-card-layout__title')[0].text
            print('name: ' + name)
            return name

    def get_headline(self) -> str:
        headline = self.driver.find_elements_by_class_name('top-card-layout__headline')[0].text
        print('headline: ' + headline)
        return headline

    def get_about_info(self) -> str:
        # core-section-container__content
        about = self.driver.find_elements_by_class_name('core-section-container__content')[0].text
        print('about: ' + about)
        return about

    def get_experiences(self) -> []:
        experiences_data = []
        experience__list = self.driver.find_element_by_class_name('experience__list')
        experiences_items = experience__list.find_elements_by_class_name('experience-item')
        for experiences_item in experiences_items:
            organisations_name = experiences_item.find_element_by_class_name('profile-section-card__subtitle').text
            title = experiences_item.find_element_by_class_name('profile-section-card__title').text
            date_range = experiences_item.find_element_by_class_name('date-range').text
            location = experiences_item.find_element_by_class_name('experience-item__location').text
            experiences_data.append({
                'organisations_name': organisations_name,
                'title': title,
                'date range': date_range,
                'location': location})
        return experiences_data

    def get_education(self) -> []:
        education_data = []
        education_list = self.driver.find_elements_by_class_name('education__list')[0]
        education_list_items = education_list.find_elements_by_class_name('education__list-item')
        for education_list_item in education_list_items:
            school_name = education_list_item.find_elements_by_class_name('screen-reader-text')[0].text
            education_title = education_list_item.find_elements_by_class_name('education__item--degree-info')[1].text
            date_range = education_list_item.find_elements_by_class_name('date-range')[0].text
            education_data.append({
                'school_name': school_name,
                'education_title': education_title,
                'date_range': date_range
            })
        return education_data

    def get_certifications(self) -> []:
        certifications_data = []
        certifications_list = self.driver.find_elements_by_class_name('certifications__list')[0]
        certifications_list_items = certifications_list.find_elements_by_class_name('profile-section-card ')
        for certifications_list_item in certifications_list_items:
            title = certifications_list_item.find_elements_by_class_name('profile-section-card__title')[0].text
            subtitle = certifications_list_item.find_elements_by_class_name('profile-section-card__subtitle')[0].text
            date_range = certifications_list_item.find_elements_by_class_name('certifications__date-range')[0].text
            certifications_data.append({
                'title': title,
                'subtitle': subtitle,
                'date_range': date_range
            })
        return certifications_data

    def get_courses(self) -> []:
        courses_data = []
        courses_list = self.driver.find_elements_by_class_name('courses__list')[0]
        courses_list_items = courses_list.find_elements_by_class_name('profile-section-card')
        for courses_list_item in courses_list_items:
            titel = courses_list_item.find_elements_by_class_name('profile-section-card__title')[0].text
            subtitle = courses_list_item.find_elements_by_class_name('profile-section-card__subtitle')[0].text
            courses_data.append({
                'titel': titel,
                'subtitle': subtitle
            })
        return courses_data

    def get_projects(self) -> []:
        projects_data = []
        projects__list = self.driver.find_elements_by_class_name('projects__list')[0]
        projects__list_items = projects__list.find_elements_by_class_name('personal-project')
        for projects__list_item in projects__list_items:
            title = projects__list_item.find_elements_by_class_name('profile-section-card__title')[0].text
            subtitle = projects__list_item.find_elements_by_class_name('profile-section-card__subtitle')[0].text
            info = projects__list_item.find_elements_by_class_name('profile-section-card__meta')[0].text
            projects_data.append({
                'title': title,
                'subtitle': subtitle,
                'info': info
            })
        return projects_data

    def get_languages(self) -> []:
        languages_data = []
        languages_list = self.driver.find_elements_by_class_name('languages__list')[0]
        languages_list_items = languages_list.find_elements_by_class_name('profile-section-card ')
        for languages_list_item in languages_list_items:
            title = languages_list_item.find_elements_by_class_name('profile-section-card__title')[0].text
            subtitle = languages_list_item.find_elements_by_class_name('profile-section-card__subtitle')[0].text
            languages_data.append({
                'title': title,
                'subtitle': subtitle
            })
        return languages_data


if __name__ == '__main__':
    login = ''
    password = ''
    url_page = ''
    person = Person(login_name=login, pwd=password, url=url_page)
    person.get_name()
    person.get_headline()
    person.get_about_info()
    experiences = person.get_experiences()
    educations = person.get_education()
    certifications = person.get_certifications()
    languages = person.get_languages()
    courses = person.get_courses()
    projects = person.get_projects()
    print(projects)
    print(courses)
    print(languages)
    print(certifications)
    print(educations)



