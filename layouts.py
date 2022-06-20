import PySimpleGUI as sg


def combo_frame(title, key):
    return sg.Frame(
        title=title, element_justification='center',
        layout=[
            [sg.Combo(['1'], key=key, enable_events=True)]
        ]
    )


MAIN_COLUMN = sg.Column(
    size=(800, 600), scrollable=True, vertical_scroll_only=True,
    layout=[
        [combo_frame('Поставщик', '_supplier_')],
        [combo_frame('Товар', '_item_')],
    ]
)
