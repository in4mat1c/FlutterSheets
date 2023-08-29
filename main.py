""" Flet Search Bar """
# modules
import flet
from flet import *
import asyncio
import aiosqlite
import search

def main(page: Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "start"
    page.padding = padding.only(top=200)
    page.theme_mode = ThemeMode.LIGHT

    page.add(
        search.DropDownSearchBar(),
    )
    page.update()


if __name__ == "__main__":
    flet.app(target=main)