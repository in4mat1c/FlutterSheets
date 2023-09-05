import asyncio

import flet

import database

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

from search import DropDownSearchBar
from top import TopNavigationBlock
from table import Table


class MainBlock(UserControl):

    def __init__(self):
        self.search = DropDownSearchBar()
        self.top_bar = TopNavigationBlock()
        self.table = Table()
        super().__init__()

    def build(self):
        _object_ = Column()
        _object_.controls.append(self.top_bar.create())
        _object_.controls.append(self.search.drop_down_search())
        _object_.controls.append(self.table.table_container())
        return _object_


