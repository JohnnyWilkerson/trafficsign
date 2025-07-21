from tkinter import *
from keras.models import load_model
import numpy as np
from PIL import ImageTk, Image
from tkinter import filedialog

model = load_model("traffic_classifier.h5")
sign_list = {
    1: 'Speed limit (20km/h)',
    2: 'Speed limit (30km/h)',
    3: 'Speed limit (50km/h)',
    4: 'Speed limit (60km/h)',
    5: 'Speed limit (70km/h)',
    6: 'Speed limit (80km/h)',
    7: 'End of speed limit (80km/h)',
    8: 'Speed limit (100km/h)',
    9: 'Speed limit (120km/h)',
    10: 'No passing',
    11: 'No passing veh over 3.5 tons',
    12: 'Right-of-way at intersection',
    13: 'Priority road',
    14: 'Yield',
    15: 'Stop',
    16: 'No vehicles',
    17: 'Veh > 3.5 tons prohibited',
    18: 'No entry',
    19: 'General caution',
    20: 'Dangerous curve left',
    21: 'Dangerous curve right',
    22: 'Double curve',
    23: 'Bumpy road',
    24: 'Slippery road',
    25: 'Road narrows on the right',
    26: 'Road work',
    27: 'Traffic signals',
    28: 'Pedestrians',
    29: 'Children crossing',
    30: 'Bicycles crossing',
    31: 'Beware of ice/snow',
    32: 'Wild animals crossing',
    33: 'End speed + passing limits',
    34: 'Turn right ahead',
    35: 'Turn left ahead',
    36: 'Ahead only',
    37: 'Go straight or right',
    38: 'Go straight or left',
    39: 'Keep right',
    40: 'Keep left',
    41: 'Roundabout mandatory',
    42: 'End of no passing',
    43: 'End no passing veh > 3.5 tons'}
root = Tk()

root.geometry("800x600")
root.title("Traffic Sign Classifier")

def classifysign(path):
    img = Image.open(path).convert('RGB')
    img = img.resize((30,30))
    img = np.array(img)/255.0
    img = np.expand_dims(img, axis = 0) #adds batch size, extra dimension
    pred = model.predict(img)
    pred_class = np.argmax(pred, axis = 1)[0] + 1
    sign = sign_list[pred_class]
    print(pred_class)
    print(sign)
    result.configure(text = sign, bg = 'purple')

def button_classify(path):
    classifybtn = Button(root, text = "Classify Image", command = lambda: classifysign(path))
    classifybtn.place(x = 550, y = 300)

def upload_image():
    path = filedialog.askopenfilename()
    img = Image.open(path)
    img.thumbnail(((root.winfo_width()/2.25),(root.winfo_height()/2.25)))
    tkimg = ImageTk.PhotoImage(img)
    imgdisplay.configure(image = tkimg)
    imgdisplay.image = tkimg
    button_classify(path)


lbl = Label(root, text ="Know your traffic sign", font = ('Courier New', 30, 'bold'))
lbl.pack()

btn = Button(root, text = 'Upload Image', command= upload_image)
btn.place(x=350, y= 100)

result = Label(root)
result.place(x=300, y= 200)

imgdisplay = Label(root)
imgdisplay.place(x = 100, y = 300)

mainloop()
