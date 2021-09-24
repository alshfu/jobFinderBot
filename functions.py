import sys
import time

import click


def delay_print(title='', string='', t=0, color=''):
    string = color + string
    if title != '':
        sys.stdout.write(title + ": ")
    if title == '|Password':
        for c in string:
            sys.stdout.write('*')
            sys.stdout.flush()
            time.sleep(0.25)
    else:
        for c in string:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(t)
    print('')


def status(status_id):
    if status_id == 0:
        return 'Inte med i lista'
    # Det fins något fel måste kontrolleras
    if status_id == 1:
        return 'Det fins något fel måste kontrolleras'
    # Redan sökt inga problem
    elif status_id == 2:
        return 'Redan sökt redo för rapportering'
    # Redo till ansökan
    elif status_id == 3:
        return ' Redo till ansökan'
    # anons sida inte med lista
    elif status_id == 4:
        return 'Anons sida inte med regel lista'
    elif status_id == 5:
        return 'Ansökt och raporterad'
    else:
        return 'Inte med i lista'


def status_style(status_id, string):
    if status_id == 0 or None:
        return click.style(string, fg='white')
    if status_id == 1:
        # Det fins något fel måste kontrolleras
        return click.style(string, fg='red')
    elif status_id == 2:
        # Redan sökt inga problem
        return click.style(string, fg='green')
    elif status_id == 3:
        # Redo till ansökan
        return click.style(string, fg='yellow')
    elif status_id == 4:
        # anons sida inte med lista
        return click.style(string, fg='cyan')
    else:
        return click.style(string, fg='white')


def wait_timer(t):
    while t:
        sys.stdout.write(str(t) + " ")
        time.sleep(1)
        t -= 1
    print('')


def yes_or_no(string):
    answer = input(string + "Ja/Nej: ")
    print(answer)
    if answer == 'Ja' or \
            answer == 'J' or \
            answer == 'ja' or \
            answer == 'j' or \
            answer == 'J' or \
            answer == 'YES' or \
            answer == 'Y' or \
            answer == 'y':
        return True
    else:
        return False


if __name__ == '__main__':
    print(status_style(0, 'Demo Test'))
    print(status_style(1, 'Demo Test'))
    print(status_style(2, 'Demo Test'))
    print(status_style(3, 'Demo Test'))
    print(status_style(4, 'Demo Test'))
