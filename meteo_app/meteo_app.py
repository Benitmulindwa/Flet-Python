import flet
from flet import *
from datetime import datetime

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

    def _current_temp():
        _current_temp = 28
        _current_humidity = 3
        _current_weather = "Nuages"
        _current_description = "Le ciel est d'un bleu pur et sans nuages aujourd'hui. Le soleil rayonne, réchauffant l'atmosphère d'une douce chaleur. Une brise légère souffle de temps en temps, apportant un soulagement bienvenu. Les températures sont agréables, invitant à profiter du temps en plein air. En soirée, le ciel se teinte de nuances chaudes au coucher du soleil, créant une atmosphère paisible. Les étoiles commencent à scintiller dans la nuit, promettant une soirée étoilée. Un temps idéal pour profiter de la journée et de la soirée en toute simplicité."
        _current_wind = 220
        _current_feels = "good"

        return [
            _current_temp,
            _current_weather,
            _current_description,
            _current_wind,
            _current_humidity,
            _current_feels,
        ]

    def _current_extra():
        _extra_info = []

        _extra = [
            [0.80, "Km", "Visibilité", "visibility.png"],
            [6500, "inHg", "Pression", "barometer.png"],
            [datetime.now().time(), "", "Aube", "sunset.png"],
            [datetime.now().time(), "", "Crépuscule", "sunrise.png"],
        ]

        for data in _extra:
            _extra_info.append(
                Container(
                    bgcolor="white10",
                    border_radius=12,
                    alignment=alignment.center,
                    content=Column(
                        alignment="center",
                        horizontal_alignment="center",
                        spacing=25,
                        controls=[
                            Container(
                                alignment=alignment.center,
                                content=Image(
                                    src=data[3],
                                    color="white",
                                ),
                                width=32,
                                height=32,
                            ),
                            Container(
                                content=Column(
                                    alignment="center",
                                    horizontal_alignment="center",
                                    spacing=0,
                                    controls=[
                                        Text(
                                            str(data[0]) + " " + data[1],
                                            size=14,
                                        ),
                                        Text(data[2], size=11, color="white54"),
                                    ],
                                )
                            ),
                        ],
                    ),
                )
            )

        return _extra_info

    def _top():
        _today = _current_temp()

        _today_extra = GridView(
            max_extent=150,
            expand=1,
            run_spacing=5,
            spacing=5,
        )
        for info in _current_extra():
            _today_extra.controls.append(info)

        top = Container(
            height=660 * 0.40,
            gradient=LinearGradient(
                begin=alignment.bottom_left,
                end=alignment.top_right,
                colors=["lightblue600", "lightblue900"],
            ),
            border_radius=35,
            animate=animation.Animation(duration=50, curve="decelerate"),
            on_hover=lambda e: _expand(e),
            padding=15,
            content=Column(
                alignment="start",
                spacing=10,
                controls=[
                    Row(
                        alignment="center",
                        controls=[
                            Text(
                                "Nairobi, KE",
                                size=16,
                                weight="w500",
                            )
                        ],
                    ),
                    Container(padding=padding.only(bottom=5)),
                    Row(
                        alignment="center",
                        spacing=30,
                        controls=[
                            Column(
                                controls=[
                                    Container(
                                        width=90,
                                        height=90,
                                        image_src="cloudy1.png",
                                    ),
                                ]
                            ),
                            Column(
                                spacing=5,
                                horizontal_alignment="center",
                                controls=[
                                    Text("Today", size=12, text_align="center"),
                                    Row(
                                        vertical_alignment="start",
                                        spacing=0,
                                        controls=[
                                            Container(
                                                content=Text(
                                                    _today[0],
                                                    size=52,
                                                ),
                                            ),
                                            Container(
                                                content=Text(
                                                    "°",
                                                    size=28,
                                                    text_align="center",
                                                )
                                            ),
                                        ],
                                    ),
                                    Text(
                                        _today[1] + "-Couvert",
                                        size=10,
                                        color="white54",
                                        text_align="center",
                                    ),
                                ],
                            ),
                        ],
                    ),
                    Divider(height=8, thickness=1, color="white10"),
                    Row(
                        alignment="spaceAround",
                        controls=[
                            Container(
                                content=Column(
                                    horizontal_alignment="center",
                                    spacing=2,
                                    controls=[
                                        Container(
                                            alignment=alignment.center,
                                            content=Image(
                                                src="wind.png",
                                                color="white",
                                            ),
                                            width=20,
                                            height=20,
                                        ),
                                        Text(
                                            str(_today[3]) + "km/h",
                                            size=11,
                                        ),
                                        Text(
                                            "Vent",
                                            size=9,
                                            color="white54",
                                        ),
                                    ],
                                )
                            ),
                            Container(
                                content=Column(
                                    horizontal_alignment="center",
                                    spacing=2,
                                    controls=[
                                        Container(
                                            alignment=alignment.center,
                                            content=Image(
                                                src="humidity.png",
                                                color="white",
                                            ),
                                            width=20,
                                            height=20,
                                        ),
                                        Text(
                                            str(_today[4]) + "%",
                                            size=11,
                                        ),
                                        Text(
                                            "Humidité",
                                            size=9,
                                            color="white54",
                                        ),
                                    ],
                                )
                            ),
                            Container(
                                content=Column(
                                    horizontal_alignment="center",
                                    spacing=2,
                                    controls=[
                                        Container(
                                            alignment=alignment.center,
                                            content=Image(
                                                src="temperature.png",
                                                color="white",
                                            ),
                                            width=20,
                                            height=20,
                                        ),
                                        Text(
                                            str(_today[0]) + "°",
                                            size=11,
                                        ),
                                        Text(
                                            "Temps",
                                            size=9,
                                            color="white54",
                                        ),
                                    ],
                                )
                            ),
                        ],
                    ),
                    _today_extra,
                ],
            ),
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
