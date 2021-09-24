import sqlite3
import os

DB_DIR = os.path.dirname(os.path.realpath(__file__))
db = os.path.abspath(DB_DIR+'//pd.db')


def create_ad_list_table():
    conn = sqlite3.connect(db)
    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    sql = '''CREATE TABLE IF NOT EXISTS AD_LIST(
       id integer PRIMARY KEY,
       ad_id int NOT NULL UNIQUE,
       title char(120),
       city char(68),
       ad_date char(10),
       employer_name char(120),
       status INT
    )'''
    cursor.execute(sql)
    conn.commit()
    conn.close()


def create_profiles_table():
    conn = sqlite3.connect(db)
    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    sql = ('CREATE TABLE IF NOT EXISTS USER_PROFILE(\n'
           '       id integer PRIMARY KEY,\n'
           '       email char(120),\n'
           '       password char(120),\n'
           '       password_secondary char(120),\n'
           '       cv_file_location char(120),\n'
           '       cover_later_file_location char(120),\n'
           '       f_name char(120),\n'
           '       l_name char(120),\n'
           '       telefon char(120),\n'
           '       b_date char(120),\n'
           '       street char(120),\n'
           '       street_number char(120),\n'
           '       zip_code char(120),\n'
           '       town char(120),\n'
           '       ssn char(120),\n'
           '       status INT\n'
           '    )')
    cursor.execute(sql)
    conn.commit()
    conn.close()


def add_user_to_database(user_data):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute("insert into USER_PROFILE ("
                   "email,"
                   "password,"
                   "password_secondary,"
                   "cv_file_location,"
                   "cover_later_file_location,"
                   "f_name,"
                   "l_name,"
                   "telefon,"
                   "b_date,"
                   "street,"
                   "street_number,"
                   "zip_code,"
                   "town,"
                   "ssn)"
                   "values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                   (user_data[0],  # email
                    user_data[1],  # password
                    user_data[2],  # password_secondary
                    user_data[3],  # cv_file_location
                    user_data[4],  # cover_later_file_location
                    user_data[5],  # f_name
                    user_data[6],  # l_name
                    user_data[7],  # telefon
                    user_data[8],  # b_date
                    user_data[9],  # street
                    user_data[10],  # street_number
                    user_data[11],  # zip_code
                    user_data[12],  # town
                    user_data[13],  # ssn
                    ))
    conn.commit()
    conn.close()


def get_profile(user_id):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM USER_PROFILE WHERE id = ?", (user_id,))
    data = cursor.fetchall()
    conn.commit()
    conn.close()
    return data


def add_ad_to_database(ad_data):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute("insert into AD_LIST (ad_id,"
                   "title,"
                   "city,"
                   "ad_date,"
                   "employer_name,"
                   "status) values(?,?,?,?,?,?)",
                   (ad_data[0], ad_data[1], ad_data[2], ad_data[3], ad_data[4], ad_data[5]))
    conn.commit()
    # Closing the connection
    conn.close()


def get_ad_data_from_db(ad_id):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM AD_LIST WHERE ad_id = ?", (ad_id,))
    data = cursor.fetchall()
    conn.commit()
    conn.close()
    return data


def get_all_information():
    # Connecting to sqlite
    conn = sqlite3.connect(db)
    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM AD_LIST")
    data = cursor.fetchall()
    conn.commit()
    conn.close()
    return data


def check_ad_status(ad_id):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute("SELECT status FROM AD_LIST WHERE ad_id = ?", (ad_id,))
    data = cursor.fetchall()
    conn.commit()
    conn.close()
    if len(data) == 0:
        return None
    else:
        return data[0][0]


def update_ad_status_id(ad_id, status_id):
    # print("Update data for ad_id: " + str(ad_id) + "For status " + status_id)
    conn = sqlite3.connect(db)
    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    cursor.execute("UPDATE AD_LIST  SET status = ?  WHERE ad_id = ?", (status_id, ad_id))
    conn.commit()
    cursor.close()


if __name__ == '__main__':
    create_ad_list_table()
