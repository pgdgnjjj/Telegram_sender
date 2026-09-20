from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import asyncio
from telegram import Bot

class BotApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.layout.add_widget(Label(text="نام ربات:"))
        self.name_input = TextInput(multiline=False)
        self.layout.add_widget(self.name_input)

        self.layout.add_widget(Label(text="توکن ربات:"))
        self.token_input = TextInput(multiline=False, password=True)
        self.layout.add_widget(self.token_input)

        self.layout.add_widget(Label(text="آیدی گروه:"))
        self.chat_input = TextInput(multiline=False)
        self.layout.add_widget(self.chat_input)

        self.layout.add_widget(Label(text="متن پیام:"))
        self.msg_input = TextInput(multiline=True)
        self.layout.add_widget(self.msg_input)

        btn = Button(text="ارسال پیام", size_hint=(1, 0.2))
        btn.bind(on_press=self.send)
        self.layout.add_widget(btn)

        self.status = Label(text="")
        self.layout.add_widget(self.status)

        return self.layout

    def send(self, instance):
        token = self.token_input.text.strip()
        chat_id = self.chat_input.text.strip()
        text = self.msg_input.text.strip()

        if not token or not chat_id or not text:
            self.status.text = "همه فیلدها رو پر کن!"
            return

        try:
            asyncio.run(self._send(token, chat_id, text))
            self.status.text = "پیام ارسال شد!"
        except Exception as e:
            self.status.text = f"خطا: {e}"

    async def _send(self, token, chat_id, text):
        bot = Bot(token=token)
        await bot.send_message(chat_id=int(chat_id), text=text)

if __name__ == "__main__":
    BotApp().run()
