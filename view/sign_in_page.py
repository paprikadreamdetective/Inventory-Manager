import flet as ft

body_sign_in = ft.Container(
    ft.Row([
        ft.Container(
            ft.Column(controls=[
                ft.Text(
                    'Iniciar Sesión',
                    width=360,
                    size=30,
                    weight ='900',
                    text_align = 'center'
                ),
                ft.Container(
                    ft.TextField(
                        width=280,
                        height=40,
                        hint_text= 'Correo electronico',
                        border ='underline',
                        color ='black',
                        prefix_icon = ft.icons.EMAIL,
                    ), padding = ft.padding.only(20,10)
                ),
                ft.Container(
                    ft.TextField(
                        width=280,
                        height=40,
                        hint_text= 'Contraseña',
                        border ='underline',
                        color ='black',
                        prefix_icon = ft.icons.LOCK,
                        password = True,
                    ), padding = ft.padding.only(20,10)
                ),
                ft.Container(
                    ft.ElevatedButton(
                        content = ft.Text(
                            'Iniciar Sesion',
                            color = 'black',
                            weight ='w500',
                        ), 
                        width =280,
                        bgcolor = 'white',
                    ), padding = ft.padding.only(20,10)
                )
            ])
        ),
    ], alignment = ft.MainAxisAlignment.SPACE_EVENLY), padding= 10
)

def sign_in_gui(page: ft.Page):
    page.window_width=500
    page.window_height = 500
    page.padding = 0
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    #page.add(body_sign_in)

    def route_change(e: ft.RouteChangeEvent):
        page.views.clear()
        page.views.append(
            ft.View(
                route = '/',
                controls = [
                    ft.AppBar(
                        title=ft.Text('Home'),
                        bgcolor='blue',  
                    ),
                    ft.Text(
                        value='Home', 
                        size=30
                    ),
                    ft.ElevatedButton(
                        text='Go to Stock',
                        on_click=lambda _: page.go('/stock')
                    )
                ],
                vertical_alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=26
            )
        )
        # Stock
        if page.route == '/stock':
            page.views.append(
                ft.View(
                    route = '/stock',
                    controls = [
                        ft.AppBar(
                            title=ft.Text('Stock'),
                            bgcolor='blue',  
                        ),
                        ft.Text(
                            value='Stock', 
                            size=30
                        ),
                        ft.ElevatedButton(
                            text='Go back',
                            on_click=lambda _: page.go('/home')
                        )
                    ],
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=26
                )
            )
        page.update()
    def view_pop(e: ft.ViewPopEvent):
        page.views.pop()
        top_view: ft.View = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(target=sign_in_gui)