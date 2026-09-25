import winsound
import time
import os
import threading
import tkinter as tk

MEDIA_PATH = r"C:\Windows\Media"
BPM = 120
BEAT = 60.0 / BPM

def sound(name):
    path = os.path.join(MEDIA_PATH, name)
    return path if os.path.exists(path) else None

S = {
    "kick": sound("Windows Error.wav"),
    "snare": sound("Windows Ding.wav"),
    "hat": sound("Windows Notify.wav"),
    "crash": sound("Windows Critical Stop.wav"),
    "bass": sound("Windows Battery Low.wav"),
}

# Ритм + текст
melody = [
    # Вступление
    ("kick", 0.25, ""), ("kick", 0.25, ""), ("snare", 0.25, ""), ("kick", 0.25, ""),
    ("kick", 0.25, ""), ("kick", 0.25, ""), ("snare", 0.25, ""), ("kick", 0.25, ""),

    # "Тёплое место, но улицы ждут"
    ("bass", 0.5, "Тёплое место,"), ("bass", 0.5, "но улицы ждут"),
    ("snare", 0.25, ""), ("snare", 0.25, ""),

    # "Отпечатков наших ног"
    ("bass", 0.5, "Отпечатков"), ("bass", 0.5, "наших ног"),
    ("snare", 0.25, ""), ("snare", 0.25, ""),

    # "Звёздная пыль — на сапогах"
    ("hat", 0.25, "Звёздная пыль —"), ("hat", 0.25, "на сапогах"),
    ("hat", 0.25, ""), ("hat", 0.25, ""),

    # "Мягкое кресло, клетчатый плед"
    ("bass", 0.5, "Мягкое кресло,"), ("bass", 0.5, "клетчатый плед"),
    ("snare", 0.25, ""), ("snare", 0.25, ""),

    # "Не нажатый вовремя курок"
    ("bass", 0.5, "Не нажатый"), ("bass", 0.5, "вовремя курок"),
    ("snare", 0.25, ""), ("snare", 0.25, ""),

    # Припев
    ("kick", 0.25, "Группа крови —"), ("kick", 0.25, "на рукаве"),
    ("snare", 0.25, ""), ("kick", 0.25, ""),
    ("kick", 0.25, "Мой порядковый"), ("kick", 0.25, "номер — на рукаве"),
    ("snare", 0.25, ""), ("kick", 0.25, ""),

    ("bass", 0.5, "Пожелай мне"), ("bass", 0.5, "удачи в бою"),
    ("snare", 0.25, ""), ("snare", 0.25, ""),

    ("hat", 0.25, "Пожелай мне"), ("hat", 0.25, "удачи"),
    ("crash", 0.5, ""),
]

# Глобальная переменная для окна
root = None
label = None

def create_window():
    global root, label
    root = tk.Tk()
    root.title("Группа крови")
    root.geometry("600x200+500+300")
    root.configure(bg="black")
    root.attributes("-topmost", True)  # Поверх всех окон
    label = tk.Label(root, text="", font=("Arial", 28, "bold"), fg="white", bg="black")
    label.pack(expand=True)
    root.mainloop()

def update_text(text):
    if label:
        label.config(text=text)
        root.update()

def play():
    print("🎸 Кино — Группа крови (Windows Edition)")
    for drum, duration, text in melody:
        file_path = S.get(drum)
        if file_path:
            try:
                winsound.PlaySound(file_path, winsound.SND_FILENAME | winsound.SND_ASYNC)
            except Exception as e:
                print(f"Ошибка: {e}")
        if text:
            update_text(text)
        time.sleep(duration * BEAT)
        if text:
            update_text("")

if __name__ == "__main__":
    # Запускаем окно в отдельном потоке
    window_thread = threading.Thread(target=create_window, daemon=True)
    window_thread.start()
    time.sleep(1)  # Ждём, пока окно создастся
    play()
    time.sleep(2)
    if root:
        root.destroy()
