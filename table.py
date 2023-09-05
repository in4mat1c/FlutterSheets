from flet import *
from database import Database
from tableDesign import TableDesign

class Table(UserControl):
    controls_list = {}

    def __init__(self):
        self.database = Database('database')
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
                TableDesign.get_table_cell(res_x, True),
                TableDesign.get_table_cell(value[2], disabled),
                TableDesign.get_table_cell(value[3], disabled),
                TableDesign.get_table_cell(res_y, True),
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

    def get_table_values(self, table_name):
        data = self.database.get_data(table_name)
        obj = self.controls_list['table']
        price = self.database.get_price(table_name)
        obj.content = TableDesign.top_table(table_name.replace('_', ' '), price)
        amount = 0
        for value in data:
            x = self.__validate_int(value[0])
            x1 = self.__validate_int(value[1])
            y = self.__validate_int(value[2])
            y1 = self.__validate_int(value[3])
            print(value)

            if isinstance(x, float) or isinstance(x1, float):
                res_x = round(x * x1, 2)
            else:
                res_x = round((x * x1) / 1000000, 2)

            res_y = round((y * y1) / 1000000, 2)

            amount += round((res_x + res_y), 2)

            # Create main table Design
            obj.content.controls[3].controls.append(self.__made_table_string(value, False, res_x, res_y))
            obj.content.controls.append(TableDesign.bottom_table_part(res_x, res_y, amount))

        obj.update()

    # Top Bar Functionality

