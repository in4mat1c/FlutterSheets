from flet import *
from flet import (
    Column,
    UserControl
    )

from table import Table
from database import Database


class Register(UserControl):

    controls_list = {}

    def __init__(self, user, page):
        self.updater = page
        self.database = Database('users')
        self.users_data = self.database.get_data('users')
        self.user = user
        self.error_dialog = AlertDialog(
            modal=True,
            title=Text("Ошибка",
                       text_align=TextAlign.CENTER,
                       weight=FontWeight.W_600
                       ),
            content=Text("Неправильный логин или пароль",
                         text_align=TextAlign.CENTER,
                         weight=FontWeight.W_400
                         ),
            actions=[
                ElevatedButton("Закрыть",
                               bgcolor=colors.RED_300,
                               color=colors.WHITE,
                               on_click=self.close_error_dialog,
                ),
            ],
            actions_alignment=MainAxisAlignment.CENTER,
            on_dismiss=lambda e: print(''),
        )
        super().__init__()

    def show_error_dialog(self, e):
        self.updater.dialog = self.error_dialog
        self.error_dialog.open = True
        self.updater.update()

    def close_error_dialog(self, e):
        self.updater.dialog = self.error_dialog
        self.error_dialog.open = False
        self.updater.update()

    def go_to_table(self, e):
        is_routed = False
        obj = self.controls_list['register']
        for value in self.users_data:
            if obj.content.controls[1].controls[0].value == value[0] and obj.content.controls[2].controls[0].value == value[1]:
                self.user.username = value[0]
                self.user.permission = value[2]
                is_routed = True
                Table.controls_list['user'] = self.user
                # Create session for current user
                self.page.go('/table')
        if is_routed is not True:
            self.show_error_dialog(e)

    def _design_(self):
        _object_ = Container(
            width=354,
            height=244,
            border_radius=42,
            padding=0,
            clip_behavior=ClipBehavior.HARD_EDGE,
            animate=animation.Animation(400, "decelerate"),
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                alignment=MainAxisAlignment.CENTER,
                spacing=10,
                controls=[
                    Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            Image(
                                src=f"/images/register_logo.jpg",
                                width=70,
                                height=70,
                                fit=ImageFit.CONTAIN,
                            ),
                        ]
                    ),
                    Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            Dropdown(
                                width=254,
                                height=35,
                                content_padding=5,
                                border_radius=42,
                                border_width=1,
                                border_color='black',
                            )
                        ]
                    ),
                    Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            TextField(
                                border_color="black",
                                border_width=1,
                                border_radius=42,
                                focused_border_color=colors.RED_200,
                                text_align=TextAlign.CENTER,
                                width=254,
                                height=35,
                                text_size=14,
                                content_padding=2,
                                cursor_color="black",
                                cursor_width=1,
                            )
                        ]
                    ),
                    Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            ElevatedButton(
                                text='Войти',
                                width=100,
                                height=35,
                                bgcolor=colors.RED_300,
                                color=colors.WHITE,
                                on_click=self.go_to_table
                            )
                        ]
                    )
                ]
            )
        )
        return _object_

    # Create register app structure
    def build(self):
        obj = self._design_()
        for data in self.users_data:
            obj.content.controls[1].controls[0].options.append(dropdown.Option(data[0]))
        self.controls_list['register'] = obj
        return obj

