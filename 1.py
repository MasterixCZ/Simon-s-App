#PLUGINY
from tkinter import *
from PIL import ImageTk, Image
import playsound

#ROOT
root = Tk()
root.title("Simon's App")
root.geometry("903x707")

#DEFINICE
simon_bg = ImageTk.PhotoImage(Image.open("Simon's_App\simon.png"))#Simon's_App\simon.png
def WAYG():
    playsound.playsound("Simon's_App\\WAYG.mp3")#Simon's_App\WAYG.mp3
def YAG_QUIT():
    playsound.playsound("Simon's_App\YAG.mp3")
    root.quit()

#POZADÍ
simon_canvas = Canvas(root)
simon_canvas.place(height=707, width=903)
simon_canvas.create_image(440,350, image = simon_bg, anchor = CENTER)

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

root.mainloop()