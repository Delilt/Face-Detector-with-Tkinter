import cv2
from PIL import Image, ImageTk
import numpy as np
import tkinter as tk
from tkinter import filedialog

def openFile():
    filePath = filedialog.askopenfilename()
    print(f"Seçilen dosya yolu: {filePath}")
    
    img = None  # 'img' değişkenini burada tanımlıyoruz
    try:
        pil_img = Image.open(filePath)  # Resmi PIL ile aç
        img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)  # OpenCV formatına dönüştür
    except Exception as e:
        print(f"Resim yüklenemedi: {e}")
        return
    
    if img is None:
        print("Görüntü dosyası bulunamadı veya okunamadı.")
        return
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.25, minNeighbors=5, minSize=(30,30))

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(img, 'insan', (x, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img = img.resize((600,400),Image.LANCZOS)
    img = ImageTk.PhotoImage(img)

    canvas.img = img
    canvas.create_image(0, 0, anchor=tk.NW, image=img)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# arayüz
root = tk.Tk()
root.title("yüz tanıma")

canvas = tk.Canvas(root, width=600, height=400)
canvas.pack()
openButton = tk.Button(root, text="dosya seç", command=openFile)
openButton.pack()

root.mainloop()
