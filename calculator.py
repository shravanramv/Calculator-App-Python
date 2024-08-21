import flet as ft

# Define custom button class
class MyButton(ft.ElevatedButton):
    def __init__(self, text, is_operation=False, **kwargs):
        super().__init__(**kwargs)  # Pass other keyword arguments like 'expand'
        self.text = text
        if is_operation:
            self.bgcolor = ft.colors.ORANGE_300
            self.color = ft.colors.BLACK
        else:
            self.bgcolor = ft.colors.BLACK
            self.color = ft.colors.WHITE

def main(page: ft.Page):
    page.title = "Calculator App"
    page.window.resizable = True
    page.window.width = 400
    page.window.height = 600

    result = ft.Text(value="0", size=32, text_align="right", expand=True, weight="bold")

    page.add(
        ft.Container(
            expand=True,
            padding=20,
            content=ft.Column(
                expand=True,
                controls=[
                    ft.Row(controls=[result], alignment="end"),
                    ft.Row(
                        expand=True,
                        controls=[
                            MyButton(text="AC", expand=True),
                            MyButton(text="+/-", expand=True),
                            MyButton(text="%", expand=True),
                            MyButton(text="/", is_operation=True, expand=True),
                        ]
                    ),
                    ft.Row(
                        expand=True,
                        controls=[
                            MyButton(text="7", expand=True),
                            MyButton(text="8", expand=True),
                            MyButton(text="9", expand=True),
                            MyButton(text="*", is_operation=True, expand=True),
                        ]
                    ),
                    ft.Row(
                        expand=True,
                        controls=[
                            MyButton(text="4", expand=True),
                            MyButton(text="5", expand=True),
                            MyButton(text="6", expand=True),
                            MyButton(text="-", is_operation=True, expand=True),
                        ]
                    ),
                    ft.Row(
                        expand=True,
                        controls=[
                            MyButton(text="1", expand=True),
                            MyButton(text="2", expand=True),
                            MyButton(text="3", expand=True),
                            MyButton(text="+", is_operation=True, expand=True),
                        ]
                    ),
                    ft.Row(
                        expand=True,
                        controls=[
                            MyButton(text="0", expand=True),
                            MyButton(text=".", expand=True),
                            MyButton(text="=", is_operation=True, expand=True),
                        ]
                    ),
                ]
            )
        )
    )

ft.app(target=main)
