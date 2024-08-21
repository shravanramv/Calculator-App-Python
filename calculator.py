import flet as ft

# Define custom button class with a circular shape
class MyButton(ft.Container):
    def __init__(self, text, is_operation=False, **kwargs):
        super().__init__(
            content=ft.ElevatedButton(
                text=text,
                bgcolor=ft.colors.ORANGE_300 if is_operation else ft.colors.BLACK,
                color=ft.colors.BLACK if is_operation else ft.colors.WHITE,
                **kwargs
            ),
            width=80,  # Set fixed width and height for consistent circular shape
            height=80,
            border_radius=40,  # Border radius for perfect circle
            bgcolor=ft.colors.TRANSPARENT,
        )

def main(page: ft.Page):
    page.title = "Calculator App"
    page.window.resizable = True
    page.window.width = 350
    page.window.height = 550
    page.window.minimum_width = 350  # Set minimum width
    page.window.minimum_height = 550  # Set minimum height

    result = ft.Text(value="0", size=32, text_align="right", expand=True, weight="bold")

    page.add(
        ft.Container(
            expand=True,
            padding=10,
            content=ft.Column(
                expand=True,
                spacing=5,  # Spacing between rows
                controls=[
                    ft.Row(controls=[result], alignment="end"),
                    ft.Row(
                        spacing=5,
                        controls=[
                            MyButton(text="AC"),
                            MyButton(text="+/-"),
                            MyButton(text="%"),
                            MyButton(text="/", is_operation=True),
                        ]
                    ),
                    ft.Row(
                        spacing=5,
                        controls=[
                            MyButton(text="7"),
                            MyButton(text="8"),
                            MyButton(text="9"),
                            MyButton(text="*", is_operation=True),
                        ]
                    ),
                    ft.Row(
                        spacing=5,
                        controls=[
                            MyButton(text="4"),
                            MyButton(text="5"),
                            MyButton(text="6"),
                            MyButton(text="-", is_operation=True),
                        ]
                    ),
                    ft.Row(
                        spacing=5,
                        controls=[
                            MyButton(text="1"),
                            MyButton(text="2"),
                            MyButton(text="3"),
                            MyButton(text="+", is_operation=True),
                        ]
                    ),
                    ft.Row(
                        spacing=5,
                        controls=[
                            MyButton(text="0"),
                            MyButton(text="."),
                            MyButton(text="=", is_operation=True),
                        ]
                    ),
                ]
            )
        )
    )

ft.app(target=main)
