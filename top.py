from flet import (CircleAvatar,
                  ClipBehavior,
                  Container,
                  Column,
                  colors,
                  CrossAxisAlignment,
                  IconButton,
                  icons,
                  MainAxisAlignment,
                  Row,
                  Text,
                  UserControl,
                  PopupMenuItem,
                  PopupMenuButton,
                  Icon,
                  )

from table import Table
from tableDesign import TableDesign

class TopNavigationBlock(UserControl):
    def __init__(self):
        self.controls_list = {}
        self.table = Table()
        super().__init__()

    def check_discount_click(self, e):
        obj = self.controls_list["top"]
        e.control.checked = not e.control.checked
        obj.content.controls[0].controls[2].content.controls[4].items[1].checked = False
        obj.content.controls[0].controls[2].content.controls[4].items[1].update()
        obj.content.controls[0].controls[2].content.controls[4].items[0].update()

    def check_balance_click(self, e):
        obj = self.controls_list["top"]
        e.control.checked = not e.control.checked
        obj.content.controls[0].controls[2].content.controls[4].items[0].checked = False
        obj.content.controls[0].controls[2].content.controls[4].items[1].update()
        obj.content.controls[0].controls[2].content.controls[4].items[0].update()

    def create(self):
        _object_ = Container(
            width=354,
            height=50,
            clip_behavior=ClipBehavior.HARD_EDGE,
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                alignment=MainAxisAlignment.CENTER,
                controls=[
                    Row(
                        spacing=10,
                        vertical_alignment=CrossAxisAlignment.CENTER,
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            CircleAvatar(
                                foreground_image_url="https://avatars.githubusercontent.com/u/132345733?v=4",
                                width=40,
                                height=40,
                                bgcolor=colors.RED_400,
                                color=colors.WHITE,
                                content=Text("ЛТ"), # Add Username Like by Symbols
                            ),
                            Container(),
                            Container(
                                bgcolor=colors.RED_400,
                                border_radius=40,
                                content=Row(
                                    spacing=0,
                                    controls=[
                                        IconButton(icons.ADD, icon_size=20, icon_color='white',
                                                   tooltip='Добавление новой строки в таблицу', on_click=self.add_string),
                                        IconButton(icons.ATTACH_FILE, icon_size=20, icon_color='white',
                                                   tooltip='Прикрепление фото'),
                                        IconButton(icons.ADDCHART_ROUNDED, icon_size=20, icon_color='white',
                                                   tooltip='Добавление новой ткани'),
                                        IconButton(icons.DELETE_ROUNDED, icon_size=20, icon_color='white',
                                                   tooltip='Удаление ткани'),
                                        PopupMenuButton(
                                            content=Icon(icons.MORE_VERT_ROUNDED, color='white'),
                                            width=40,
                                            height=40,
                                            tooltip='Добавление категории для ткани',
                                            items=[
                                                PopupMenuItem(
                                                    content=Text('Скидка', size=14),
                                                    checked=False,
                                                    on_click=lambda e: self.check_discount_click(e)
                                                ),
                                                PopupMenuItem(
                                                    content=Text('Остаток', size=14),
                                                    checked=False,
                                                    on_click=lambda e: self.check_balance_click(e)
                                                ),
                                            ]
                                        ),
                                    ]
                                )
                            )
                        ],
                    ),
                ],
            ),
        )
        self.controls_list["top"] = _object_
        return _object_

    def add_string(self, e):
        obj = Table.controls_list['table']
        _added_string_ = Row(
            spacing=0,
            alignment=MainAxisAlignment.CENTER,
            vertical_alignment=CrossAxisAlignment.CENTER,
            controls=[
                TableDesign.get_table_cell('', False),
                TableDesign.get_table_cell('', False),
                TableDesign.get_table_cell('', True),
                TableDesign.get_table_cell('', False),
                TableDesign.get_table_cell('', False),
                TableDesign.get_table_cell('', True),
            ]
        )
        obj.content.controls[3].controls.append(_added_string_)
        obj.content.controls[3].update()
