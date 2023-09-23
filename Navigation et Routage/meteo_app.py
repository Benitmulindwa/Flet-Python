import flet
from flet import *

days = ["Lun", "Mar", "Merc", "Jeu", "Ven", "Sam", "Dim"]


def main(page: flet.Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    def _expand(e):
        if e.data == "true":
            _c.content.controls[0].height = 560
            _c.content.controls[0].update()
        else:
            _c.content.controls[0].height = 660 * 0.40
            _c.content.controls[0].update()

    def _top():
        top = Container(
            # width=310,
            # height=550 * 0.40,
            expand=True,
            gradient=LinearGradient(
                begin=alignment.bottom_left,
                end=alignment.top_right,
                colors=["lightblue600", "lightblue900"],
            ),
            border_radius=35,
            animate=animation.Animation(duration=50, curve="decelerate"),
            on_hover=lambda e: _expand(e),
        )
        return top

    _c = Container(
        # width=310,
        # height=660,
        expand=True,
        border_radius=35,
        bgcolor="black",
        padding=10,
        content=Stack(expand=True, controls=[_top()]),
    )
    page.add(_c)


if __name__ == "__main__":
    flet.app(target=main, assets_dir="assets")
