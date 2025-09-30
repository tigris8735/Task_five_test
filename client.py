# client.py
import tkinter as tk
from tkinter import scrolledtext
import requests
import json

class ChatClient:
    def __init__(self, master):
        self.master = master
        master.title("RSP Chat Client")
        
        self.chat_history = scrolledtext.ScrolledText(master, state='disabled', width=50, height=20)
        self.chat_history.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        self.entry = tk.Entry(master, width=40)
        self.entry.grid(row=1, column=0, padx=10, pady=10)
        self.entry.bind("<Return>", self.send_message)
        
        self.send_btn = tk.Button(master, text="Отправить", command=self.send_message)
        self.send_btn.grid(row=1, column=1, padx=10, pady=10)
        
        self.server_url = "http://localhost:5000/chat"
        
    def send_message(self, event=None):
        message = self.entry.get()
        if not message:
            return
            
        self.entry.delete(0, tk.END)
        self.display_message(f"Вы: {message}")
        
        try:
            response = requests.post(
                self.server_url,
                json={'message': message},
                headers={'Content-Type': 'application/json'}
            )
            if response.status_code == 200:
                bot_response = response.json()['response']
                self.display_message(f"Бот: {bot_response}")
            else:
                self.display_message("Ошибка сервера")
        except requests.exceptions.ConnectionError:
            self.display_message("Не могу подключиться к серверу")
    
    def display_message(self, message):
        self.chat_history.configure(state='normal')
        self.chat_history.insert(tk.END, message + "\n")
        self.chat_history.configure(state='disabled')
        self.chat_history.see(tk.END)

if __name__ == '__main__':
    root = tk.Tk()
    client = ChatClient(root)
    root.mainloop()