import PyPDF2
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import pyttsx3
from tqdm import tqdm


def convert_to_mp3():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if not file_path:
        return

    save_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
    if not save_path:
        return

    pdf_reader = PyPDF2.PdfReader(open(file_path, 'rb'))
    speaker = pyttsx3.init()

    mp3_file = save_path

    total_pages = len(pdf_reader.pages)
    download_bar["maximum"] = total_pages

    for page_num in tqdm(range(total_pages), desc="Converting to MP3"):
        text = pdf_reader.pages[page_num].extract_text()  # Modified line
        clean_text = text.strip().replace('\n', ' ')
        speaker.save_to_file(clean_text, mp3_file)
        speaker.runAndWait()
        download_bar["value"] = page_num + 1
        download_bar.update()

    speaker.stop()
    status_label.config(text="Conversion complete.")


root = tk.Tk()
root.title("PDF to MP3 Converter")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

convert_button = tk.Button(frame, text="Convert PDF to MP3", command=convert_to_mp3)
convert_button.pack()

download_bar = ttk.Progressbar(frame, orient="horizontal", length=300, mode="determinate")
download_bar.pack()

status_label = tk.Label(frame, text="")
status_label.pack()

root.mainloop()
