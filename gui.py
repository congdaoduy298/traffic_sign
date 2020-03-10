from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk
from tensorflow.keras.models import load_model
import numpy as np


model = load_model('model.h5')

classes = { 1:'Speed limit (20km/h)',
            2:'Speed limit (30km/h)', 
            3:'Speed limit (50km/h)', 
            4:'Speed limit (60km/h)', 
            5:'Speed limit (70km/h)', 
            6:'Speed limit (80km/h)', 
            7:'End of speed limit (80km/h)', 
            8:'Speed limit (100km/h)', 
            9:'Speed limit (120km/h)', 
            10:'No passing', 
            11:'No passing veh over 3.5 tons', 
            12:'Right-of-way at intersection', 
            13:'Priority road', 
            14:'Yield', 
            15:'Stop', 
            16:'No vehicles', 
            17:'Veh > 3.5 tons prohibited', 
            18:'No entry', 
            19:'General caution', 
            20:'Dangerous curve left', 
            21:'Dangerous curve right', 
            22:'Double curve', 
            23:'Bumpy road', 
            24:'Slippery road', 
            25:'Road narrows on the right', 
            26:'Road work', 
            27:'Traffic signals', 
            28:'Pedestrians', 
            29:'Children crossing', 
            30:'Bicycles crossing', 
            31:'Beware of ice/snow',
            32:'Wild animals crossing', 
            33:'End speed + passing limits', 
            34:'Turn right ahead', 
            35:'Turn left ahead', 
            36:'Ahead only', 
            37:'Go straight or right', 
            38:'Go straight or left', 
            39:'Keep right', 
            40:'Keep left', 
            41:'Roundabout mandatory', 
            42:'End of no passing', 
            43:'End no passing veh > 3.5 tons' }

root = Tk()
root.geometry('800x600')
root.title('Traffic Sign Classifier')

def classify_image(file_path):
    img = Image.open(file_path)
    img = img.resize((50, 50))
    img = np.array(img)/255.0
    img = np.expand_dims(img, axis=0)
    pred = model.predict(img)
    pred_id = np.argmax(pred)
    traffic_sign_name.configure(text=classes[pred_id+1])
    traffic_sign_name.pack()

def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        img = ImageTk.PhotoImage(Image.open(file_path))
        show_img.configure(image=img)
        show_img.image = img
        classify = Button(root, text='Classify Image', command=lambda: classify_image(file_path), padx=10, pady=5)
        classify.configure(fg='white', bg='black', font=('arial', 10, 'bold'))
        classify.place(relx=0.79, rely=0.49)
    except:
        pass

label = Label(root, text='Know Your Traffic Sign', pady=10, font=('arial', 20, 'bold'))
label.pack()

traffic_sign_name = Label(root, text='', font=('arial', 10, 'bold'))

show_img = Label(root)

button = Button(root, text='Upload Image', fg='white', bg='black', font=('arial', 10, 'bold'), command=upload_image)
button.pack(side=BOTTOM, expand=True)
show_img.pack(side=BOTTOM, expand=True)
root.mainloop()