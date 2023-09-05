from flet import *

import search
from database import Database


class TableDesign:
    # Atributes list
    database = Database('database')

    @classmethod
    def change_table_name(cls, e):
        old_name = search.DropDownSearchBar.controls_list['table_name']
        search.DropDownSearchBar.controls_list['table_name'] = (e.control.value).replace(' ', '_')
        cls.database.alter_table_name(old_name, e.control.value)

    @classmethod
    def change_price(cls, e):
        table_name = search.DropDownSearchBar.controls_list['table_name']
        print(table_name)
        cls.database.set_price(table_name, e.control.value)

    @classmethod
    def top_table(cls, table_name, price):
        return Column(
            horizontal_alignment=CrossAxisAlignment.CENTER,
            alignment=MainAxisAlignment.START,
            spacing=0,
            controls=[
                Row(
                    spacing=0,
                    controls=[
                        Container(
                            width=300,
                            height=30,
                            border_radius=border_radius.only(top_left=6),
                            border=border.all(1, 'black'),
                            alignment=alignment.center,
                            content=TextField(
                                value=table_name,
                                border_radius=0,
                                focused_border_color='green',
                                text_align=TextAlign.CENTER,
                                height=30,
                                text_size=14,
                                content_padding=2,
                                cursor_color="black",
                                cursor_width=1,
                                on_submit=cls.change_table_name
                            )
                        ),
                        Container(
                            width=54,
                            height=30,
                            border_radius=border_radius.only(top_right=6),
                            border=border.all(1, 'black'),
                            alignment=alignment.center,
                            content=TextField(
                                value=price,
                                border_radius=0,
                                focused_border_color='green',
                                text_align=TextAlign.CENTER,
                                height=30,
                                text_size=14,
                                content_padding=2,
                                cursor_color="black",
                                cursor_width=1,
                                on_submit=cls.change_price
                            )
                        ),
                    ]
                ),
                Container(
                    width=354,
                    height=30,
                    content=Row(
                        spacing=0,
                        controls=[
                            Container(
                                alignment=alignment.center,
                                bgcolor=colors.RED_ACCENT_100,
                                width=177,
                                height=30,
                                border=border.all(1, 'black'),
                                content=Text('Бухта', size=14, weight=FontWeight.W_400),
                            ),
                            Container(
                                alignment=alignment.center,
                                bgcolor=colors.RED_ACCENT_100,
                                width=177,
                                height=30,
                                border=border.all(1, 'black'),
                                content=Text('Куски', size=14, weight=FontWeight.W_400),
                            ),
                        ]
                    ),
                ),
                Container(
                    width=354,
                    height=30,
                    content=Row(
                        spacing=0,
                        controls=[
                            Container(
                                alignment=alignment.center,
                                bgcolor=colors.RED_200,
                                width=59,
                                height=30,
                                border=border.only(left=border.BorderSide(1, 'black'),
                                                   right=border.BorderSide(1, 'black')),
                                content=Text('Высота', size=14),
                            ),
                            Container(
                                alignment=alignment.center,
                                bgcolor=colors.RED_200,
                                width=59,
                                height=30,
                                content=Text('Ширина', size=14),
                            ),
                            Container(
                                alignment=alignment.center,
                                bgcolor=colors.RED_200,
                                width=59,
                                height=30,
                                border=border.all(1, 'black'),
                                content=Text('Кв.', size=14),
                            ),
                            Container(
                                alignment=alignment.center,
                                bgcolor=colors.RED_200,
                                width=59,
                                height=30,
                                border=border.only(right=border.BorderSide(1, 'black')),
                                content=Text('Ширина', size=14),
                            ),
                            Container(
                                alignment=alignment.center,
                                bgcolor=colors.RED_200,
                                width=59,
                                height=30,
                                content=Text('Высота', size=14),
                            ),
                            Container(
                                alignment=alignment.center,
                                bgcolor=colors.RED_200,
                                width=59,
                                height=30,
                                border=border.all(1, 'black'),
                                content=Text('Кв.', size=14),
                            ),
                        ]
                    )
                ),
                Column(spacing=0),
            ],
        )

    @staticmethod
    def bottom_table_part(res_x, res_y, amount):
        return Column(
            spacing=0,
            controls=[
                Container(
                    width=354,
                    height=30,
                    content=Row(
                        spacing=0,
                        controls=[
                            Container(
                                alignment=alignment.center,
                                bgcolor=colors.BLUE_100,
                                width=177,
                                height=30,
                                border=border.all(1, 'black'),
                                content=Text(res_x, size=14, weight=FontWeight.W_400),
                            ),
                            Container(
                                alignment=alignment.center,
                                bgcolor=colors.BLUE_100,
                                width=177,
                                height=30,
                                border=border.all(1, 'black'),
                                content=Text(res_y, size=14, weight=FontWeight.W_400),
                            ),
                        ]
                    ),
                ),
                Container(
                    width=354,
                    height=30,
                    border_radius=border_radius.only(bottom_left=6, bottom_right=6),
                    border=border.all(1, 'black'),
                    alignment=alignment.center,
                    content=Text(amount, size=14, weight=FontWeight.W_600)  # Add adaptive table_name
                ),
            ]
        )

    @classmethod
    def get_table_cell(cls, value, disabled, color=None):
        _cell_ = TextField(
            value=value,
            disabled=disabled,
            bgcolor=color,
            border_color="black",
            border_radius=0,
            focused_border_color='green',
            text_align=TextAlign.CENTER,
            width=59,
            height=30,
            text_size=14,
            content_padding=2,
            cursor_color="black",
            cursor_width=1,
        )
        return _cell_
