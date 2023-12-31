# from pynput import mouse
import flet as ft


class Test:
    def __init__(self):
        ft.app(self.main)

    # Builds the page
    def main(self, page: ft.page):
        self.page = page
        self.page.padding = 0

        self.page.window_height = 360
        self.page.window_width = 640
        self.page.window_frameless = True
        self.page.window_always_on_top = True
        self.page.bgcolor = ft.colors.TRANSPARENT
        self.page.window_bgcolor = ft.colors.TRANSPARENT
        # self.page.opacity = 0.5dth

        def on_pan_update1(e: ft.DragUpdateEvent):
            box.height = min(max(0, box.height + e.delta_y), self.page.window_height)
            box.width = min(max(0, box.width + e.delta_x), self.page.window_width)
            print(box.width, box.height)
            box.update()

        gd = ft.GestureDetector(
            mouse_cursor=ft.MouseCursor.MOVE,
            drag_interval=0,
            on_pan_update=on_pan_update1,
        )

        box = ft.Container(
            content=gd, bgcolor="red", width=20, height=20, left=0, top=0
        )

        text = ft.Container(
            content=ft.Text("fdsfhufio pmnuihqnf equhfuwhfuhaohdfouashdfnu"),
            height=360,
            width=640,
        )

        self.page.add(ft.Stack([text, box]))

        # # Collect events until released
        # with mouse.Events() as events:
        #     for event in events:
        #         try:
        #             if event.button == mouse.Button.right:
        #                 print('Right button clicked!')
        #                 break
        #         except: pass
        #         finally:
        #             print('Received event {}'.format(event))


Test()
