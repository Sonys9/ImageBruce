from PIL import Image
from customtkinter import *
import os, tempfile, random
from tkinter import messagebox

tempdir = tempfile.gettempdir()

def resize_image(image_dir):

    if os.path.isfile(image_dir):

        all = image_dir.split('\\')
        filename = '\\'.join(all).split('.')[0].split('\\')[-1]
        fileformat = image_dir.split('.')[-1]
        path = image_dir.split('\\')
        path.pop(-1)
        path = '\\'.join(path)

        resdir = path+'\\'+filename+'-'+''.join(random.choices('qwertyuiopas0', k=16))

        res = tempdir+'\\'+filename+'-'+''.join(random.choices('qwertyu123', k=16))+'.'+fileformat
        res2 = tempdir+'\\'+filename+'-'+''.join(random.choices('qwer1234567890', k=16))+'.'+fileformat
        res3 = tempdir+'\\'+filename+'-'+''.join(random.choices('qwertyuiopas0', k=16))+'.'+fileformat

        check_horiz(image_dir, res)
        resize1(res, res2)
        resize2(res, res3)

        os.makedirs(resdir+'\\'+'1_var', exist_ok=True)
        os.makedirs(resdir+'\\'+'2_var', exist_ok=True)

        convert(res2, resdir+'\\'+'1_var'+'\\'+'boot.jpg')
        convert(res3, resdir+'\\'+'2_var'+'\\'+'boot.jpg')

        messagebox.showinfo('Image Conv', 'Успех! Результаты в '+resdir+'!')

    else: messagebox.showerror('Image Conv', 'Выберите файл!')

def check_horiz(image_dir, res_dir):

    img = Image.open(image_dir)
    if img.width < img.height:
        flip_img = img.transpose(Image.Transpose.ROTATE_90)
        flip_img.save(res_dir)
    else: img.save(res_dir)

def resize1(image_dir, res_dir):
    img = Image.open(image_dir)
    img = img.resize((240, 135), Image.Resampling.LANCZOS)
    img.save(res_dir)

def resize2(image_dir, res_dir):
    img = Image.open(image_dir)
    img = img.crop((0,0,240,135))
    img.save(res_dir)

def convert(image_dir, res_dir):

    img = Image.open(image_dir)
    img = img.convert("RGB")

    img.save(res_dir, "JPEG")

window = CTk()
window.title('Palka 2.0 Image Conventer')
window.geometry('300x200')
window.resizable(False, False)
set_appearance_mode("dark")
window.protocol("WM_DELETE_WINDOW", lambda: os._exit(0))
image = ''

def choicefile():

    global image

    file_path = filedialog.askopenfilename(filetypes=(('PNG', '*.png'), ('JPG', '*.jpg'), ('JPEG', '*.jpeg'), ('WEBP', '*.webp')))
    if file_path: 
        filename = file_path.split('/')[-1]
        format = filename.split('.')[-1]
        if format.lower() in ['png', 'jpg', 'jpeg', 'webp']:
            if len(filename) > 18:
                infoo.configure(text=filename[:20]+'...')
            else:
                infoo.configure(text=filename)
        else: messagebox.showerror('Image Conv', 'Тип файла не поддерживается!')

    image = file_path.replace('/','\\')

fg = '#008E63'
hover = '#225244'
bg = '#2B2B2B'

CTkFrame(window, width=280, height=180).place(x=10,y=10)

choiceafile = CTkButton(window, text='Выбрать фото', width=100, fg_color=fg, bg_color=bg, hover_color=hover, command=choicefile)
choiceafile.place(x=20, y=25)

infoo = CTkLabel(window, text='Не выбрано', bg_color=bg, font=('Calibri', 15))
infoo.place(x=130, y=25)

convertbtn = CTkButton(window, text='Конвертировать фото', width=100, fg_color=fg, bg_color=bg, hover_color=hover, command=lambda: resize_image(image))
convertbtn.place(x=20, y=65)

window.mainloop()