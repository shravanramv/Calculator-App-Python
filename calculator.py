import flet as ft

def main(page: ft.Page):
    page.title = "Calculator App"
    page.window.resizable = True  # Allow the window to be resizable
    page.window.width = 400
    page.window.height = 600

    result = ft.Text(value="0", size=32, text_align="right", expand=True, weight="bold")

    page.add(
        ft.Container(
            expand=True,  # Make the container fill the available space
            padding=20,
            content=ft.Column(
                expand=True,  # Make the column fill the available space
                controls=[
                    ft.Row(controls=[result], alignment="end"),
                    ft.Row(
                        expand=True,
                        controls=[
                            ft.ElevatedButton(text="AC", expand=True),
                            ft.ElevatedButton(text="+/-", expand=True),
                            ft.ElevatedButton(text="%", expand=True),
                            ft.ElevatedButton(text="/", expand=True),
                        ]
                    ),
                    ft.Row(
                        expand=True,
                        controls=[
                            ft.ElevatedButton(text="7", expand=True),
                            ft.ElevatedButton(text="8", expand=True),
                            ft.ElevatedButton(text="9", expand=True),
                            ft.ElevatedButton(text="*", expand=True),
                        ]
                    ),
                    ft.Row(
                        expand=True,
                        controls=[
                            ft.ElevatedButton(text="4", expand=True),
                            ft.ElevatedButton(text="5", expand=True),
                            ft.ElevatedButton(text="6", expand=True),
                            ft.ElevatedButton(text="-", expand=True),
                        ]
                    ),
                    ft.Row(
                        expand=True,
                        controls=[
                            ft.ElevatedButton(text="1", expand=True),
                            ft.ElevatedButton(text="2", expand=True),
                            ft.ElevatedButton(text="3", expand=True),
                            ft.ElevatedButton(text="+", expand=True),
                        ]
                    ),
                    ft.Row(
                        expand=True,
                        controls=[
                            ft.ElevatedButton(text="0", expand=True),
                            ft.ElevatedButton(text=".", expand=True),
                            ft.ElevatedButton(text="=", expand=True),
                        ]
                    ),
                ]
            )
        )
    )

ft.app(target=main)
