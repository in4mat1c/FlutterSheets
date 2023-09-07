from flet import *

import search
from database import Database
from tableDesign import TableDesign


class Table(UserControl):
    controls_list = {}
    database = Database('database')

    def __init__(self):
        super().__init__()

    @classmethod
    def __made_table_string(cls, value, disabled, res_x, res_y):
        return Row(
            spacing=0,
            alignment=MainAxisAlignment.CENTER,
            vertical_alignment=CrossAxisAlignment.CENTER,
            controls=[
                TableDesign.get_table_cell(value[0], disabled),
                TableDesign.get_table_cell(value[1], disabled),
                TableDesign.get_table_cell(res_x, True, colors.GREY_300),
                TableDesign.get_table_cell(value[2], disabled),
                TableDesign.get_table_cell(value[3], disabled),
                TableDesign.get_table_cell(res_y, True, colors.GREY_300),
            ]
        )

    def table_container(self):
        _object_ = Container(
            width=354,
            height=500,
            bgcolor="white10",
            padding=0,
            clip_behavior=ClipBehavior.HARD_EDGE,
            animate=animation.Animation(400, "decelerate"),
        )
        self.controls_list['table'] = _object_
        return _object_

    @staticmethod
    def __validate_int(value):
        try:
            return int(value)
        except:
            try:
                return float(value)
            except:
                return 0

    @classmethod
    def get_table_values(cls, table_name):
        data = cls.database.get_data(table_name)
        obj = cls.controls_list['table']
        price = cls.database.get_price(table_name)
        obj.content = TableDesign.top_table(table_name.replace('_', ' '), price)
        amount_x = 0
        amount_y = 0
        for value in data:
            x = cls.__validate_int(value[0])
            x1 = cls.__validate_int(value[1])
            y = cls.__validate_int(value[2])
            y1 = cls.__validate_int(value[3])

            if isinstance(x, float) or isinstance(x1, float):
                res_x = round(x * x1, 2)
            else:
                res_x = round((x * x1) / 1000000, 2)

            res_y = round((y * y1) / 1000000, 2)

            amount_x += res_x
            amount_y += res_y

            # Create main table Design
            obj.content.controls[3].controls.append(cls.__made_table_string(value, False, res_x, res_y))

        obj.content.controls.append(TableDesign.bottom_table_part(round(amount_x, 2), round(amount_y, 2), round(amount_x + amount_y, 2)))
        obj.update()

    @classmethod
    def get_table_values_list(cls):
        obj = cls.controls_list['table']
        main_list = []
        for rows in obj.content.controls[3].controls:
            first_list = []
            for subject in rows.controls:
                if subject.read_only != True:
                    first_list.append(subject.value)
            main_list.append(first_list + [' '])
        return main_list

    @classmethod
    def change_cell_value(cls, e):
        values = cls.get_table_values_list()
        obj = cls.controls_list['table']
        current_table = search.DropDownSearchBar.controls_list['table_name']
        cls.database.delete_data(current_table)
        for value in values:
            cls.database.insert_data(current_table, value)
        cls.get_table_values(current_table)
        # Update Error Can't update file

    # Top Bar Functionality

