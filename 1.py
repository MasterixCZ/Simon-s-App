#PLUGINY
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import playsound
import pystray
from pystray import MenuItem as item

#ROOT
root = Tk()
root.title("Simon's App")
root.geometry("903x707")
root.iconbitmap(default='RESOURCES\IKONA.ico')

#DEFINICE
current_bg = ImageTk.PhotoImage(Image.open("RESOURCES\simon.png"))

def WAYG():
    playsound.playsound("gaeFUCK.mp3")
        
def YAG_QUIT():
    playsound.playsound("RESOURCES\YAG_QUIT.mp3")
    root.quit()
    messagebox.showerror("Simon says:", "You are gay")

def quit_window(icon, item):
    icon.stop()
    root.destroy()

def show_window(icon, item):
    icon.stop()
    root.after(0, root.deiconify())

def hide_window():
    root.withdraw()
    image=Image.open("RESOURCES\IKONA.ico")
    menu=(item("Odejít", quit_window), item("Ukázat", show_window))
    icon=pystray.Icon("Simon", image, "Simon is watchin' you", menu)
    icon.run()

def verze():
    messagebox.showinfo("Verze:", "A-0.0.7")

#POZADÍ
simon_canvas = Canvas(root)
simon_canvas.place(height=707, width=903)
simon_canvas.create_image(440,350, image = current_bg, anchor = CENTER)

#ŠTÍTKY
simon_label_jmeno = Label(simon_canvas, text="Simon Kaggwa Njala", bg="#A08977")
simon_label_jmeno.place(x=430,y=180)

seznamhlasek = Label(simon_canvas, text="Seznam hlášek: ", bg="#8C4435")
seznamhlasek.place(x=20, y=10)

#TLAČÍTKA
gae_tl = Button(simon_canvas, text="Why are you gae?", command=WAYG)
gae_tl.place(x=20,y=50)
odejít = Button(simon_canvas, text="Odejít (Být gae)", command = YAG_QUIT)
odejít.place(x=800,y=670)
verze = Button(simon_canvas, text="Verze", command=verze)
verze.place(x=855, y=10)

root.protocol('WM_DELETE_WINDOW', hide_window)

root.mainloop()
