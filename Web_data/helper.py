# TODO change funktion name
from Web_data.academicwork import AcademicWork
from Web_data.careersweden import Careersweden
from Web_data.randstad import Ranstad


def check_if_url_ready_to_be_used(url):
    if 'academicwork' in url:
        print("Academic Work")
        return True
    elif 'randstad' in url:
        print("Ranstad")
        return True
    elif 'careersweden' in url:
        print("Careersweden")
        return True
    else:
        return False


def open_link_in_chrome(url):
    if 'academicwork' in url:
        AcademicWork().academic_work_action(url)
        return True
    elif 'randstad' in url:
        Ranstad().ranstad_action(url)
        return True
    elif 'careersweden' in url:
        Careersweden().careersweden_action(url)
        return True
    else:
        print("No it is not ready for use")
        return False
