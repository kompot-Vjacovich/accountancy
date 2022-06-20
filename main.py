import pandas as pd
import PySimpleGUI as sg

from layouts import MAIN_COLUMN


class App:
    def __init__(self):
        self.layout = [[MAIN_COLUMN], [sg.Text('asdad', key='a')]]
        self.file = None

        self.window = sg.Window('My new window', self.layout)

    def open_file(self):
        filename = sg.popup_get_file(
            message='Выберите файл с товарами',
            title='Загрузка товаров',
            file_types=(('Книга Excel', '*.xlsx'),) + sg.FILE_TYPES_ALL_FILES
        )
        if not filename:
            return False
        try:
            self.file = pd.read_excel(filename, header=0, engine='openpyxl')
        except Exception as e:
            sg.popup_error('Произошла ошибка', e)
            self.file = None
            self.run()
        else:
            self.window.read(timeout=10)
            self.window['_supplier_'].update(value='1', values=['1', '2', '3'])
            return True

    def run(self):
        # work = True
        work = self.open_file()

        while work:
            event, values = self.window.read()
            if event in (sg.WIN_CLOSED, 'Exit'):
                break

        self.window.close()


if __name__ == '__main__':
    # Create the class
    app = App()
    # run the event loop
    app.run()
