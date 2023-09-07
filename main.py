from flet import *
from app_structure import App
from flet import (app,
                  Column,
                  Page,
                  ThemeMode,
                  View
                  )
from register_app import Register
from user import User


def main(page: Page):

    # Check client storage keys. If keys exist, add user and route to table

    page.theme_mode = ThemeMode.LIGHT
    current_user = User()

    def route_change(route):
        page.views.clear()
        page.views.append(
            View(
                "/",
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[Register(current_user, page)]
            )
        )
        if page.route == "/table":
            page.views.append(
                View(
                    "/table",
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    controls=[App()]
                    )
                )
        page.update()

    page.window_min_width = 390
    page.window_min_height = 600
    page.bgcolor = colors.WHITE54
    page.on_route_change = route_change
    page.go(page.route)


if __name__ == "__main__":
    app(target=main)