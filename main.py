import pandas as pd
import PySimpleGUI as sg

from layouts import main_column, price_element


class App:
    def __init__(self, file=None):
        self.layout = [[main_column()], [sg.Button('Result', key='_save_')]]
        self.file = file

        self.window = sg.Window('Заполнение отчёта', self.layout)

    def open_file(self):
        # filename = sg.popup_get_file(
        #     message='Выберите файл с товарами',
        #     title='Загрузка товаров',
        #     file_types=(('Книга Excel', '*.xlsx'),) + sg.FILE_TYPES_ALL_FILES
        # )
        filename = 'D:/Projects/accountancy/test.xlsx'
        if not filename:
            return False
        try:
            self.file = pd.read_excel(filename, header=0, engine='openpyxl')
        except Exception as e:
            sg.popup_error('Произошла ошибка', e)
            self.file = None
            self.run()
        else:
            self.fill_report()
            return True

    def fill_report(self):
        self.window.read(timeout=10)
        self.window['_supplier_'].update(
            values=list(self.file['Поставщик'].unique()))

    def run(self, event, values):
        if event == '_supplier_':
            self.window['_item_'].update(
                values=list(
                    self.file['Товар'][self.file['Поставщик'] == values[
                        '_supplier_']].unique()),
                disabled=False
            )
        elif event == '_add_calendar_':
            self.window.extend_layout(
                self.window['Цена в закупке'],
                price_element('Цена в закупке', 1)
            )


if __name__ == '__main__':
    # Create the class
    app = App()
    # run the event loop
    work = app.open_file()
    while work:
        w_event, w_values = app.window.read()
        if w_event in (sg.WIN_CLOSED, 'Exit'):
            break

        if w_event in ('_next_', '_save_'):
            print(w_values)
        app.run(w_event, w_values)

    app.window.close()
