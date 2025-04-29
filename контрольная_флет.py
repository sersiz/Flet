import flet as ft


def main(page: ft.Page):
    page.title = "Hamster Kombat"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Счётчик кликов
    count = ft.Ref[ft.Text]()

    # Функция обработки клика
    def button_click(e):
        try:
            current_clicks = int(count.current.value.split(': ')[1])
            count.current.value = f"Хамстеров: {current_clicks + 1}"
            page.update()
        except (IndexError, ValueError) as ex:
            page.add(ft.Text(f"Не тапается: {ex}", color=ft.colors.RED))

    # Функция сброса счётчика
    def reset_clicks(e):
        count.current.value = "Хамстеров: 0"
        page.update()

    # Функция сохранения результата
    def save_clicks(e):
        try:
            clicks = int(count.current.value.split(': ')[1])
            with open('Хамстеров.txt', 'w') as f:
                f.write(f"Всего хамстеров: {clicks}")
            # Очищаем предыдущие сообщения
            page.controls = [c for c in page.controls if not isinstance(c, ft.Text) or "Saved" not in c.value]
            page.add(ft.Text("Хамстеры засейвлины.txt!", color=ft.colors.GREEN))
            page.update()
        except (IndexError, ValueError, IOError) as ex:
            page.add(ft.Text(f"Хамстеры не засейвлены: {ex}", color=ft.colors.RED))
            page.update()

    # Элементы интерфейса
    page.add(
        ft.Text(ref=count, value="Хамстеров: 0", size=30),
        ft.Row(
            controls=[
                ft.ElevatedButton("🐹ТАПАЙ🐹", on_click=button_click),
                ft.ElevatedButton("Ресет", on_click=reset_clicks),
                ft.ElevatedButton("Сохранить", on_click=save_clicks)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )


ft.app(target=main)
