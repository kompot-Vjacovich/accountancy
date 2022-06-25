import PySimpleGUI as sg

from datetime import date
from calendar import monthrange

YEAR = date.today().year
MONTH = date.today().month

SIZE = (800, 600)


def combo_frame(title, key, disabled=True):
    return sg.Frame(
        title=title, size=(790, 50), expand_x=True,
        layout=[
            [sg.Combo([[]], key=key, expand_x=True, enable_events=True,
                      disabled=disabled)]
        ]
    )


def calendar(title, i=0, from_to='Дата начала', default_date=None):
    key = f'_calendar_{title}{i}_'
    default_date = default_date or 1
    return (
        sg.Input(key=key, size=(10, 1), readonly=True,
                 default_text=date(YEAR, MONTH, default_date).strftime(
                     '%d.%m.%Y')),
        sg.CalendarButton(
            'Выбрать', title=from_to, target=key, begin_at_sunday_plus=1,
            close_when_date_chosen=True, format='%d.%m.%Y',
            day_abbreviations='ВС.ПН.ВТ.СР.ЧТ.ПТ.СБ'.split('.'),
            month_names='ЯНВ.ФЕВ.МАР.АПР.МАЙ.ИЮН.ИЮЛ.'
                        'АВГ.СЕН.ОКТ.НОЯ.ДЕК'.split('.')
        ))


def price_element(title, j):
    return [
        [sg.Push(), sg.Input(key=f'_price_{title}{j}_', size=(20, 1)),
         sg.Push()],
        [*calendar(title, f'{j}_start'), sg.Push(),
         *calendar(title, f'{j}_end', 'Дата окончания',
                   monthrange(YEAR, MONTH)[1])],
    ]


def range_frame(title):
    return sg.Frame(
        title=title, expand_x=True, expand_y=True,
        element_justification='center',
        layout=[
            [sg.Column(key=title, layout=price_element(title, 0))],
            [sg.VPush()],
            [sg.Push(),
             sg.Button('Добавить диапазон', key='_add_calendar_'),
             sg.Push()]
        ]
    )


def main_column():
    return sg.Column(
        size=SIZE, scrollable=True, vertical_scroll_only=True,
        element_justification='center',
        layout=[
            [combo_frame('Поставщик', '_supplier_', False)],
            [combo_frame('Товар', '_item_')],
            [range_frame('Цена в закупке')]
        ]
    )
