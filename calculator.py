import flet as ft

# Function to handle button clicks
def button_clicked(e):
    result = e.page.controls[0].controls[0].content.controls[1].controls[0].text
    if e.control.data == "AC":
        result.value = "0"
    elif e.control.data == "=":
        try:
            result.value = str(eval(result.value))
        except:
            result.value = "Error"
    else:
        if result.value == "0" or result.value == "Error":
            result.value = e.control.data
        else:
            result.value += e.control.data
    result.update()

def main(page: ft.Page):
    page.title = "Calculator App"
    page.window.resizable = True
    page.window.width = 350
    page.window.height = 550
    page.window.minimum_width = 350
    page.window.minimum_height = 550

    theme = "light"

    # Function to update theme
    def toggle_theme(e):
        nonlocal theme
        theme = "dark" if theme == "light" else "light"
        page.bgcolor = ft.colors.BLACK87 if theme == "dark" else ft.colors.WHITE
        result.color = ft.colors.WHITE if theme == "dark" else ft.colors.BLACK
        result.update()
        for row in button_rows:
            for btn in row.controls:
                btn.bgcolor = ft.colors.ORANGE_300 if btn.data in "/*-+=" else (ft.colors.BLACK if theme == "dark" else ft.colors.WHITE)
                btn.color = ft.colors.BLACK if btn.bgcolor == ft.colors.ORANGE_300 or theme == "light" else ft.colors.WHITE
                btn.update()

    # Display for the calculator
    result = ft.Text(value="0", size=32, text_align="right", expand=True, weight="bold")

    # Theme toggle button
    theme_toggle_btn = ft.IconButton(
        icon=ft.icons.BRIGHTNESS_6,
        on_click=toggle_theme,
        icon_color=ft.colors.YELLOW_600,
        icon_size=30,
    )

    # Button layout
    button_texts = [
        ["AC", "+/-", "%", "/"],
        ["7", "8", "9", "*"],
        ["4", "5", "6", "-"],
        ["1", "2", "3", "+"],
        ["0", ".", "="]
    ]

    button_rows = []
    for row in button_texts:
        buttons = []
        for text in row:
            buttons.append(
                ft.ElevatedButton(
                    text=text,
                    bgcolor=ft.colors.ORANGE_300 if text in "/*-+=" else (ft.colors.BLACK if theme == "dark" else ft.colors.WHITE),
                    color=ft.colors.BLACK if text in "/*-+=" or theme == "light" else ft.colors.WHITE,
                    on_click=button_clicked,
                    data=text,
                    expand=True,
                    height=80
                )
            )
        button_rows.append(ft.Row(controls=buttons, spacing=5))

    # Adding all controls to the page
    page.bgcolor = ft.colors.WHITE
    page.add(
        ft.Column(
            controls=[
                ft.Row(controls=[theme_toggle_btn, result], alignment="end"),
                *button_rows
            ],
            spacing=5,
            expand=True
        )
    )

ft.app(target=main)
