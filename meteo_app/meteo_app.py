import flet
from flet import *
from datetime import datetime
import requests

days = ["Lun", "Mar", "Merc", "Jeu", "Ven", "Sam", "Dim"]
# days = days.reverse()

api_key1 = "API_KEY"
lon = 36.81
lat = -1.28

parameters = {"lon": lon, "lat": lat, "appid": api_key1}
end_point1 = "https://api.openweathermap.org/data/2.5/weather"
response = requests.get(end_point1, params=parameters)
_current = response.json()

api_key2 = "API_KEY"
town = "Nairobi"
endpoint2 = (
    f"http://api.weatherapi.com/v1/forecast.json?key={api_key2}&q={town}&days=8&lang=fr"
)

_p = requests.get(endpoint2).json()


def main(page: flet.Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    def _expand(e):
        if e.data == "true":
            _c.content.controls[1].height = 560
            _c.content.controls[1].update()
        else:
            _c.content.controls[1].height = 660 * 0.40
            _c.content.controls[1].update()

    def _current_temp():
        _current_temp = round(_current["main"]["temp"] - 273.15, 1)
        _current_humidity = _current["main"]["humidity"]
        _current_weather = _current["weather"][0]["main"]
        _current_description = _current["weather"][0]["description"]
        _current_wind = _current["wind"]["speed"]
        _current_feels = round(_current["main"]["temp"] - 273.15, 1)

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
            [int(_current["visibility"]) / 1000, "Km", "Visibilité", "visibility.png"],
            [_current["main"]["pressure"] * 0.3, "inHg", "Pression", "barometer.png"],
            [
                datetime.fromtimestamp(_current["sys"]["sunset"]).strftime("%I:%M %p"),
                "",
                "Aube",
                "sunset.png",
            ],
            [
                datetime.fromtimestamp(_current["sys"]["sunrise"]).strftime("%I:%M %p"),
                "",
                "Crépuscule",
                "sunrise.png",
            ],
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

    def _bot_data():
        _bot_data = []
        for index in range(1, 8):
            _bot_data.append(
                Row(
                    spacing=5,
                    alignment="spaceBetween",
                    controls=[
                        Row(
                            expand=1,
                            alignment="start",
                            controls=[
                                Container(
                                    alignment=alignment.center,
                                    content=Text(
                                        days[
                                            index
                                            + 3
                                            - datetime.weekday(
                                                datetime.fromtimestamp(_current["dt"])
                                            )
                                        ]
                                    ),
                                )
                            ],
                        ),
                        Row(
                            expand=1,
                            controls=[
                                Container(
                                    content=Row(
                                        alignment="start",
                                        controls=[
                                            Container(
                                                width=20,
                                                height=20,
                                                alignment=alignment.center_left,
                                                content=Image(
                                                    src=f"{_p['forecast']['forecastday'][index]['day']['condition']['icon'][20:]}",
                                                ),
                                            ),
                                            Text(
                                                _p["forecast"]["forecastday"][index][
                                                    "day"
                                                ]["condition"]["text"],
                                                size=11,
                                                color="white54",
                                                text_align="center",
                                            ),
                                        ],
                                    )
                                )
                            ],
                        ),
                    ],
                )
            )
        return _bot_data

    def _bottom():
        _bot_column = Column(
            alignment="center",
            horizontal_alignment="center",
            spacing=25,
        )
        for data in _bot_data():
            _bot_column.controls.append(data)

        bottom = Container(
            padding=padding.only(top=280, left=20, right=20, bottom=20),
            content=_bot_column,
        )

        return bottom

    _c = Container(
        # width=310,
        # height=660,
        expand=True,
        border_radius=35,
        bgcolor="black",
        padding=10,
        content=Stack(expand=True, controls=[_bottom(), _top()]),
    )
    page.add(_c)


if __name__ == "__main__":
    flet.app(target=main, assets_dir="assets")
