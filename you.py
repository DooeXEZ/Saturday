import tkinter as tk
from tkinter import ttk, messagebox
import yt_dlp
import os
import threading

# =====================
# НАСТРОЙКИ
# =====================
DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# =====================
# ПРОГРЕСС
# =====================
def progress_hook(d):
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', '0%').replace('%', '')
        try:
            progress['value'] = float(percent)
            root.update_idletasks()
        except:
            pass

    elif d['status'] == 'finished':
        progress['value'] = 100


# =====================
# СКАЧИВАНИЕ
# =====================
def download():
    url = url_entry.get()
    quality = quality_box.get()
    mode = mode_box.get()

    if not url:
        messagebox.showerror("Ошибка", "Вставь ссылку")
        return

    def run():
        try:
            ydl_opts = {
    'outtmpl': f'{DOWNLOAD_DIR}/%(title)s.%(ext)s',
    'progress_hooks': [progress_hook],
    'nocheckcertificate': True,
    'ignoreerrors': True,
    'cookiefile': 'cookies.txt',

}


            if mode == "MP3":
                ydl_opts.update({
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                })
            else:
                if quality == "1080p":
                    ydl_opts['format'] = 'bestvideo[height<=1080]+bestaudio/best'
                elif quality == "720p":
                    ydl_opts['format'] = 'bestvideo[height<=720]+bestaudio/best'
                elif quality == "480p":
                    ydl_opts['format'] = 'bestvideo[height<=480]+bestaudio/best'
                else:
                    ydl_opts['format'] = 'best'

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            messagebox.showinfo("Готово", "Загрузка завершена!")

        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    threading.Thread(target=run).start()


# =====================
# GUI
# =====================
root = tk.Tk()
root.title("YouTube Downloader PRO")
root.geometry("520x320")
root.resizable(False, False)

title = tk.Label(root, text="YouTube Downloader PRO", font=("Arial", 16, "bold"))
title.pack(pady=10)

tk.Label(root, text="Ссылка на видео:").pack()
url_entry = tk.Entry(root, width=65)
url_entry.pack(pady=5)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Формат:").grid(row=0, column=0, padx=5)
mode_box = ttk.Combobox(frame, values=["MP4", "MP3"], width=10)
mode_box.set("MP4")
mode_box.grid(row=0, column=1)

tk.Label(frame, text="Качество:").grid(row=0, column=2, padx=5)
quality_box = ttk.Combobox(frame, values=["Лучшее", "1080p", "720p", "480p"], width=10)
quality_box.set("Лучшее")
quality_box.grid(row=0, column=3)

download_btn = tk.Button(
    root,
    text="⬇ Скачать",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    width=20,
    command=download
)
download_btn.pack(pady=15)

progress = ttk.Progressbar(root, length=420)
progress.pack(pady=10)

tk.Label(root, text="Файлы сохраняются в папку downloads").pack(pady=5)

root.mainloop()
