
import tkinter as tk
import customtkinter as ctk

import torch
#import tensorflow as tf

from PIL import ImageTk
from torch import autocast

import auth_token 
from diffusers import StableDiffusionPipeline

# Creating main tkinter window
app = tk.Tk()
app.geometry("532x622")
app.title("Image Generator")

ctk.set_appearance_mode("dark")

device = 'cpu'
modelid = "CompVis/stable-diffusion-v1-4"
#revision will let as less cuda
pipe = StableDiffusionPipeline.from_pretrained(modelid, revision="fp16", tf_dtypes=torch.float16,use_auth_token=auth_token)
pipe.to(device)

def generate():
    with autocast (device):
        description = prompt.get
        image = pipe(description(),guidance_scale = 8.5)["sample"][0]

    img = ImageTk.PhotoImage(image)
    img.save("generatedimage.png")
    lmain.configure(image=img)

#def convert_image(image):


prompt = ctk.CTkEntry(app, height=40, width=512, font=("Arial", 20), text_color="black", fg_color="white")
prompt.place(x=10, y=10)

lmain = ctk.CTkLabel(app, height=512, width=512)
lmain.place(x=10,y=110)

trigger = ctk.CTkButton(app, height=40, width= 100, font=("Arial", 20), text_color="black", fg_color="blue", command = generate) 
trigger.configure(text="Generate")
trigger.place(x=210, y=60)
app.mainloop()