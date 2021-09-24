from DB.data_base import create_profiles_table, add_user_to_database, get_profile


class Profile:

    def __init__(self, id_user=None):
        if id_user is not None:
            user_data = get_profile(id_user)[0]
            self.email = user_data[1]
            self.password = user_data[2]
            self.password_secondary = user_data[3]
            self.cv_file_location = user_data[4]
            self.cover_later_file_location = user_data[5]
            self.f_name = user_data[6]
            self.l_name = user_data[7]
            self.telefon = user_data[8]
            self.b_date = user_data[9]
            self.street = user_data[10]
            self.street_number = user_data[11]
            self.zip_code = user_data[12]
            self.town = user_data[13]
            self.ssn = user_data[14]

    @staticmethod
    def create_new_user():
        # TODO skapa ny Användare med hjälp från linkedin sida
        create_profiles_table()
        print('Ange huvud information om dig själv')
        # TODO hämta namn och adress från upplysning
        ssn = input('person nummer: ')
        f_name = input('förnamn: ')
        l_name = input('efternamn: ')
        b_date = input('födelse datum: ')
        print('Ange ditt kontakt information ')
        email = input('e-post: ')
        telefon = input('telefon nummer: ')
        print('Ange information om din adress')
        street = input('gatan: ')
        street_number = input('gata nummer: ')
        zip_code = input('post nummer')
        town = input('ort: ')
        print('Ange lösenord som du använder för att logga in på ex. AcademicWork')
        password = input('huvud lösenord: ')
        password_secondary = input('andra lösenord: ')
        print('Ange fullständig mål till cv och personlig brev filerna ')
        cv_file_location = input('mål till cv fil: ')
        cover_later_file_location = input('mål till personlig brev fil: ')

        add_user_to_database(
            [email,
             password,
             password_secondary,
             cv_file_location,
             cover_later_file_location,
             f_name,
             l_name,
             telefon,
             b_date,
             street,
             street_number,
             zip_code,
             town,
             ssn])

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def get_password_secondary(self):
        return self.password_secondary

    def get_cv_file_location(self):
        return self.cv_file_location

    def get_cover_later_file_location(self):
        return self.cover_later_file_location

    def get_f_name(self):
        return self.f_name

    def get_l_name(self):
        return self.l_name

    def get_telefon(self):
        return self.telefon

    def get_b_date(self):
        return self.b_date

    def get_street(self):
        return self.street

    def get_street_number(self):
        return self.street_number

    def get_zip_code(self):
        return self.zip_code

    def get_town(self):
        return self.town

    def get_ssn(self):
        return self.ssn

    @staticmethod
    def get_p_brev():
        return ' Jag har goda programmeringskunskaper i Python, php, java, javascript \n' \
               ' Jag har erfarenhet av Web programmering för Wordpress\n' \
               'Jag har erfarenhet av programmering i C++ och inbyggda system .'


if __name__ == '__main__':
    pass
