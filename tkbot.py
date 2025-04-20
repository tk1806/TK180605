import flet as ft
import google.generativeai as genai
GENAI_API_KEY = "AI linking api key"
genai.configure(api_key=GENAI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=[])
def get_bot_response(prompt):
    try:
        response = chat.send_message(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"
def main(page: ft.Page):
    page.title = "Tk1806"
    page.bgcolor = ft.colors.WHITE
    page.scroll = "auto"

    chat_display = ft.Column(expand=True, spacing=10)

    user_input = ft.TextField(label="Ask something", expand=True, border_color="GRAY")

    def send_message(e):
        user_msg = user_input.value.strip()
        if not user_msg:
            return
        
        chat_display.controls.append(
            ft.Text(f"You: {user_msg}", color=ft.colors.BLUE, size=16)
        )
        page.update()

        bot_reply = get_bot_response(user_msg)
        chat_display.controls.append(
            ft.Text(f"Tk1806: {bot_reply}", color=ft.colors.RED, size=16)
        )
        user_input.value = ""
        page.update()

    send_button = ft.ElevatedButton("Send", color="BLACK", bgcolor="GRAY", on_click=send_message)

    page.add(
        chat_display,
        ft.Row([user_input, send_button])
    )

ft.app(target=main)