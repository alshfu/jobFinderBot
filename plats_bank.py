import json
import textwrap
from datetime import datetime

from stripe.http_client import requests
from columnar import columnar
from click import style
from tabulate import tabulate
from DB.data_base import check_ad_status, add_ad_to_database, update_ad_status_id
from Web_data.helper import check_if_url_ready_to_be_used, open_link_in_chrome
from functions import delay_print, status_style, yes_or_no


def go_to_ad_url(url, ad_id):
    if yes_or_no('Ansök den här tjänst'):
        try:
            open_link_in_chrome(url)
            update_ad_status_id(ad_id, 2)
        except IndexError:
            update_ad_status_id(ad_id, 1)
    else:
        pass


class PlatsBank:
    def __init__(self):
        self.job_list = []
        self.ad_url = ''
        api_key = 'YicmXHhlMFx4ZGRceDgxXHg4ZVx4ZDZpXHhjMlx4YjFceGYwXHgxZS5ceGFhXHhjNFx4OGVqXV1ceGFmXHg5OCc'
        self.headers = {'api-key': api_key, 'accept': 'application/json'}
        self.url = f"https://jobsearch.api.jobtechdev.se/"

    def ad_search_query(self, query, type_of_search, ) -> json:
        if type_of_search != 'ad':
            search_params = {'q': query}
            response = requests.get(self.url + type_of_search, headers=self.headers, params=search_params)
        else:
            response = requests.get(self.url + type_of_search + '/' + query, headers=self.headers)
        response.raise_for_status()
        json_response = json.loads(response.content.decode('utf8'))
        return json_response

    def get_complete_typeahead(self):
        tag = input("skriv din sök ord: ")
        json_response = self.ad_search_query(tag, 'complete')
        typeahead = json_response['typeahead']
        completed_typeahead_list = []
        for value in typeahead:
            value_name = value['value']
            value_type = value['type']
            completed_typeahead_list.append([value_name, value_type])
        patterns = [
            ('skill', lambda text: style(text, fg='red')),
            ('occupation', lambda text: style(text, fg='cyan')),
            ('compound', lambda text: style(text, fg='green')),
        ]
        headers = ['Typeahead value', 'Type']
        table = columnar(completed_typeahead_list, headers, no_borders=False, terminal_width=500, patterns=patterns)
        print(table)

    def get_full_ad_info(self, ad_id=''):
        if ad_id == '':
            ad_id = input('Skriv in annons-ID: ')
        elif ad_id == 'DEMO':
            delay_print('Skriv in annons-ID', '25059066', 0)
            ad_id = '25059066'
        json_response = self.ad_search_query(ad_id, 'ad')
        description = [[json_response['workplace_address']['municipality']],
                       [json_response['employer']['name']],
                       [json_response['headline']],
                       [('\n'.join(textwrap.wrap(json_response['description']['text'], 128)))],
                       [json_response['application_details']['url']]]
        output = tabulate(description, tablefmt='grid')
        delay_print('', output, 0)
        go_to_ad_url(json_response['application_details']['url'], ad_id)

    def show_job_list(self, tag=''):
        if tag == '':
            tag = input("skriv din  sök fras: ")
        elif tag == 'DEMO':
            demo_string = 'Academic Work Sweden AB python'
            delay_print('Skriv din  sök fras: ', demo_string, 0)
            tag = demo_string
        json_response = self.ad_search_query(tag, 'search')
        hits = json_response['hits']
        table_headers = ['Id', 'Titel', 'Företag', 'Ort', 'Status']
        job_list_table = []
        now = datetime.now()
        for hit in hits:
            if hit['application_details']['url'] is not None:
                status = check_ad_status(int(hit['id']))
                if status is None:
                    if check_if_url_ready_to_be_used(hit['application_details']['url']) is True:
                        status = 3
                    else:
                        status = 0
                    add_ad_to_database([int(hit['id']),  # ad_data[0] står för ad_id
                                        hit['headline'],  # ad_data[1] står för title
                                        str(hit['workplace_address']['municipality']),  # ad_data[2] står för city
                                        now.strftime("%Y-%m-%d"),  # ad_data[3] står för ad_date
                                        str(hit['employer']['name']),  # ad_data[4] står för employer_name
                                        status])  # ad_data[6] står för status
                self.job_list.append([hit['id'], status])
                job_list_table.append([
                    status_style(status, str(hit['id'])),
                    status_style(status, str(hit['headline'])),
                    status_style(status, str(hit['employer']['name'])),
                    status_style(status, str(hit['workplace_address']['municipality']))])
        table = columnar(job_list_table, table_headers, no_borders=False, terminal_width=500)
        delay_print('', table, 0)
        if yes_or_no("Ansök lediga tjänster ") is True:
            self.submit_application()

    def submit_application(self):
        print('submit_application')
        for ad in self.job_list:
            if ad[1] == 3:
                self.get_full_ad_info(ad[0])


if __name__ == '__main__':
    pass
