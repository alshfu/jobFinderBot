# TODO change funktion name
from Web_data.academicwork import AcademicWork
from Web_data.randstad import Ranstad


def check_if_url_ready_to_be_used(url):
    # elif 'pnty-apply.ponty-system.se' in url:
    #     ponty_action(url)
    # elif 'www.recruto.se' in url:
    #     recruto_action(url)
    # elif 'softwareskills' in url:
    #     softwareskills_action(url)
    # elif 'semconsweden' in url:
    #     semconsweden_actoin(url)
    # elif 'altiusconsulting' in url:
    #     altiusconsulting_action(url)
    # elif 'www.infotiv.se' in url:
    #     infotiv_action(url)
    # elif 'jobb.danda.se' in url:
    #     danda_action(url)
    if 'academicwork' in url:
        print("Academic Work")
        return True
    elif 'randstad' in url:
        print("Ranstad")
    else:
        return False


def open_link_in_chrome(url):
    if 'academicwork' in url:
        AcademicWork().academic_work_action(url)
        return True
    elif 'randstad' in url:
        Ranstad().ranstad_action(url)
    else:
        print("No it is not ready for use")
        return False
