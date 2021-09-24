from consolemenu import *
from consolemenu.format import MenuBorderStyleType
from consolemenu.items import *

from Data.profile import Profile
from Web_data.arbetsförmedlingen import Arbetsformedlingen
from functions import yes_or_no
from plats_bank import PlatsBank


def menu_format() -> MenuFormatBuilder():
    m_format = MenuFormatBuilder()
    m_format.set_border_style_type(MenuBorderStyleType.HEAVY_BORDER)
    m_format.set_prompt("SELECT>")
    m_format.set_title_align('center')
    m_format.set_subtitle_align('center')
    m_format.set_left_margin(4)
    m_format.set_right_margin(4)
    m_format.show_header_bottom_border(True)
    return m_format


def palts_bank_menu() -> SelectionMenu([]):
    pb = PlatsBank()
    pb_menu = SelectionMenu([])
    pb_menu.append_item(FunctionItem("Returnera annonser som matchar din sökfras. ", pb.show_job_list))
    pb_menu.append_item(FunctionItem("Returnera vanliga ord som matchar en sökfras. ", pb.get_complete_typeahead))
    pb_menu.append_item(FunctionItem("Returnera specifik job annons efter annons-ID-nummer.", pb.get_full_ad_info))
    return pb_menu


def aktivitetsrapport():
    if yes_or_no("Vill du skapa aktivitetsrapport"):
        try:
            Arbetsformedlingen().make_reporting()
        except IndexError:
            print('Något har gåt snett')
    else:
        pass


def main_menu():
    menu = ConsoleMenu("Huvud menu", "Automatiserad jobbsökning", formatter=menu_format())
    palts_banken = SubmenuItem("Platsbanken", palts_bank_menu(), menu)
    create_new_user = FunctionItem("Skapa en ny profile", Profile().create_new_user, '')
    arbetsformedling = FunctionItem("Skapa aktivitetsrapport rapport", aktivitetsrapport, '')
    menu.append_item(palts_banken)
    menu.append_item(arbetsformedling)
    menu.append_item(create_new_user)
    menu.show()
