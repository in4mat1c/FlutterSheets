from testingSpace import MainBlock
from flet import (app,
                  Page,
                  ThemeMode
                  )


def main(page: Page):

    page.horizontal_alignment = "center"
    page.vertical_alignment = "start"
    page.theme_mode = ThemeMode.LIGHT
    page.window_min_width = 390
    page.window_min_height = 600

    page.add(
        MainBlock()
        # TopNavigationBlock(),
        # DropDownSearchBar(),
        # Table(),
    )
    page.update()


if __name__ == "__main__":
    app(target=main)