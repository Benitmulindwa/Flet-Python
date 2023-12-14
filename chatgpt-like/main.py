import openai
import flet as ft
from flet import *
import time

key = "API_KEY"

openai.api_key = key


def main_style():
    return {
        "width": 420,
        "height": 500,
        "bgcolor": "#141518",
        "border_radius": 10,
        "padding": 15,
    }


def prompt_style():
    return {
        "width": 420,
        "height": 40,
        "border_color": "white",
        "content_padding": 10,
        "cursor_color": "white",
    }


class MainContentArea(ft.Container):
    def __init__(self):
        super().__init__(**main_style())
        self.chat = ft.ListView(
            expand=True,
            height=200,
            spacing=15,
            auto_scroll=True,
        )
        self.content = self.chat


class CreateMessage(ft.Column):
    def __init__(self, name: str, message: str):
        self.name: str = name
        self.message: str = message
        self.text: str = ft.Text(self.message)
        super().__init__()
        self.controls = [ft.Text(self.name, opacity=0.6), self.text]


class Prompt(ft.TextField):
    def __init__(self, chat: ft.ListView):
        super().__init__(**prompt_style(), on_submit=self.run_prompt)
        self.chat: ListView = chat

    def animate_text(self, name: str, prompt: str):
        word_list: list = []
        msg = CreateMessage(name, "")
        self.chat.controls.append(msg)

        for word in list(prompt):
            word_list.append(word)
            msg.text.value = "".join(word_list)
            self.chat.update()
            time.sleep(0.008)

    def user_output(self, prompt):
        self.animate_text("Me", prompt)

    def gpt_output(self, prompt):
        response: any = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}]
        )
        response: any = response.choices[0].message.content.strip()
        self.animate_text(name="Atomizer", prompt=response)

    def run_prompt(self, event):
        text: any = event.control.value
        self.user_output(prompt=text)

        self.gpt_output(prompt=text)
        self.value = ""
        self.update()


def main(page: ft.Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.theme_mode = "dark"

    main = MainContentArea()
    prompt = Prompt(main.chat)

    page.add(
        Text("Atomizer Chat", size=20, weight="w800"),
        main,
        Divider(height=6, color="transparent"),
        prompt,
    )
    page.update()


if __name__ == "__main__":
    ft.app(target=main)
