import flet as ft

# Define custom button class with a circular shape and click functionality
class MyButton(ft.Container):
    def __init__(self, text, is_operation=False, result=None, **kwargs):
        super().__init__(
            content=ft.ElevatedButton(
                text=text,
                bgcolor=ft.colors.ORANGE_300 if is_operation else ft.colors.BLACK,
                color=ft.colors.BLACK if is_operation else ft.colors.WHITE,
                on_click=self.button_clicked,  # Set the click event handler
                data=text,
                **kwargs
            ),
            width=80,  # Fixed width and height for consistent circular shape
            height=80,
            border_radius=40,  # Border radius for perfect circle
            bgcolor=ft.colors.TRANSPARENT,
        )
        self.result = result  # Reference to the result Text control

    def button_clicked(self, e):
        # Handle button clicks and update the result
        if e.control.data == "AC":
            self.result.value = "0"
        elif e.control.data == "=":
            try:
                self.result.value = str(eval(self.result.value))
            except:
                self.result.value = "Error"
        else:
            if self.result.value == "0" or self.result.value == "Error":
                self.result.value = e.control.data
            else:
                self.result.value += e.control.data
        self.result.update()


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
                            MyButton(text="AC", result=result),
                            MyButton(text="+/-", result=result),
                            MyButton(text="%", result=result),
                            MyButton(text="/", is_operation=True, result=result),
                        ]
                    ),
                    ft.Row(
                        spacing=5,
                        controls=[
                            MyButton(text="7", result=result),
                            MyButton(text="8", result=result),
                            MyButton(text="9", result=result),
                            MyButton(text="*", is_operation=True, result=result),
                        ]
                    ),
                    ft.Row(
                        spacing=5,
                        controls=[
                            MyButton(text="4", result=result),
                            MyButton(text="5", result=result),
                            MyButton(text="6", result=result),
                            MyButton(text="-", is_operation=True, result=result),
                        ]
                    ),
                    ft.Row(
                        spacing=5,
                        controls=[
                            MyButton(text="1", result=result),
                            MyButton(text="2", result=result),
                            MyButton(text="3", result=result),
                            MyButton(text="+", is_operation=True, result=result),
                        ]
                    ),
                    ft.Row(
                        spacing=5,
                        controls=[
                            MyButton(text="0", result=result),
                            MyButton(text=".", result=result),
                            MyButton(text="=", is_operation=True, result=result),
                        ]
                    ),
                ]
            )
        )
    )

ft.app(target=main)
