from table import Table
from database import Database
from flet import (animation,
                  border,
                  ClipBehavior,
                  Container,
                  Column,
                  CrossAxisAlignment,
                  Icon,
                  icons,
                  MainAxisAlignment,
                  padding,
                  Row,
                  Text,
                  TextField,
                  TextSpan,
                  UserControl
                  )


class DropDownSearchBar(UserControl):
    controls_list = {}

    def __init__(self):
        self.item_number = Text(size=9, italic=True, color="black")
        self.database = Database('database')
        self.table = Table()
        super().__init__()

    def check_instance(self, e, height):
        obj = self.controls_list["search"]
        if height == 0:
            self.item_number.value = f"0 совпадений"
            self.item_number.update()
            self.leave(e)
        else:
            obj.height = 60 + (height * 20)
            obj.update()

    def leave(self, e):
        obj = self.controls_list["search"]
        obj.height = 50
        obj.update()

    def get_blind(self, e):
        obj = self.controls_list["search"]
        self.controls_list['table_name'] = e.control.text.replace(' ', '_')
        obj.content.controls[0].controls[1].value = e.control.text
        self.table.get_table_values(self.controls_list['table_name'])
        obj.height = 50
        obj.update()

    def filter_data_table(self, e):
        records = self.database.get_table_names()
        obj = self.controls_list["search"]
        for data in obj.content.controls[1].controls[:]:
            obj.content.controls[1].controls.remove(data)
            obj.content.update()
        if e.data.lower() == "":
            self.item_number.value = f"нет совпадений"
            self.item_number.update()
            self.leave(e)
        else:
            count = 0
            for names in records:
                for name in names:
                    if e.data.lower() in name.lower().replace('_', ' '):
                        obj.content.controls[1].controls.append(
                            Row(
                                visible=True,
                                alignment=MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    Text(size=14, spans=[
                                        TextSpan(
                                            name.replace('_', ' '),
                                            on_click=lambda e: self.get_blind(e)
                                        )
                                    ]),
                                    Text("name", italic=True, size=10, color="black"),
                                ],
                            )
                        )
                        count += 1
                    self.item_number.value = f"{count} совпадений"
                    self.item_number.update()
                    self.check_instance(e, count)

    def drop_down_search(self):
        _object_ = Container(
            width=354,
            height=50,
            bgcolor="white10",
            border=border.all(1, 'black'),
            border_radius=6,
            padding=padding.only(top=15, left=21, right=21, bottom=15),
            clip_behavior=ClipBehavior.HARD_EDGE,
            animate=animation.Animation(400, "decelerate"),
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                alignment=MainAxisAlignment.START,
                controls=[
                    Row(
                        spacing=10,
                        vertical_alignment=CrossAxisAlignment.CENTER,
                        controls=[
                            Icon(
                                name=icons.SEARCH_ROUNDED,
                                size=15,
                                opacity=0.90,
                            ),
                            TextField(
                                border_color="transparent",
                                height=20,
                                text_size=14,
                                content_padding=2,
                                cursor_color="black",
                                cursor_width=1,
                                hint_text="Поиск...",
                                on_change=lambda e: self.filter_data_table(e)
                            ),
                            self.item_number,
                        ],
                    ),
                    Column(
                        scroll="auto",
                        expand=True,
                    ),
                ],
            ),
        )
        self.controls_list["search"] = _object_
        return _object_

