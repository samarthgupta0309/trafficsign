import warnings
warnings.filterwarnings("ignore")
import streamlit as st
import numpy as np
from PIL import Image, ImageEnhance
import os
import cv2
from keras.models import load_model
# from win32com.client import Dispatch

# def speak(text):
#     speak = Dispatch(("SAPI.SpVoice"))
#     speak.Speak(text)
model = load_model("Model.h5")

def preprocessing(img):
    try:
        img=img.astype('uint8')
        img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img=cv2.equalizeHist(img)
        img=img/255
    except Exception as e:
        img=img.astype('unit8')
        img=cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img=cv2.equalizeHist(img)
        img=img/255
        return img

def main():
    st.title("Traffic Sign Classification")
    # st.write("")
    st.set_option('deprecation.showfileUploaderEncoding', False)
    activites = ["Classification","About"]
    choices = st.sidebar.selectbox("Select Activities", activities)
    if choices == "Classification":
        st.subheader("Traffic sign classification")
        img_file = st.file_uploader("Upload File", type=['png','jpg','jpeg'])
        if img_file is not None:
            up_img = Image.open(img_file)
            st.image(up_img)
        if st.button("Process"):
            try:
                img=np.asarray(up_img)
                img=cv2.resize(img, (50,50))
                img=preprocessing(img)
                img=img.reshape(1, 50, 50, 1)
                prediction=model.predict(img)
                classIndex=model.predict_classes(img)
                probabilityValue = np.amax(prediction)
                if probabilityValue>0.80:
                    if classNo==0:
                        st.success('Speed Limit 20 km/h')
                        # speak('Speed Limit 20 km/h')
                    elif classNo==1:
                        st.success('Speed Limit 30 km/h')
                        # speak('Speed Limit 30 km/h')
                    elif classNo==2:
                        st.success('Speed Limit 50 km/h')
                        # speak('Speed Limit 50 km/h')
                    elif classNo==3:
                        st.success('Speed Limit 60 km/h')
                    elif classNo==4:
                        st.success('Speed Limit 70 km/h')
                    elif classNo == 5:
                        st.success('Speed Limit 80 km/h')
                    elif classNo == 6:
                        st.success('End of Speed Limit 80 km/h')
                    elif classNo == 7:
                        st.success('Speed Limit 100 km/h')
                    elif classNo == 8:
                        st.success('Speed Limit 120 km/h')
                    elif classNo == 9:
                        st.success('No passing')
                    elif classNo == 10:
                        st.success('No passing for vechiles over 3.5 metric tons')
                    elif classNo == 11:
                        st.success('Right-of-way at the next intersection')
                    elif classNo == 12:
                        st.success('Priority road')
                    elif classNo == 13:
                        st.success('Yield')
                    elif classNo == 14:
                        st.success('Stop')
                    elif classNo == 15:
                        st.success('No vechiles')
                    elif classNo == 16:
                        st.success('Vechiles over 3.5 metric tons prohibited')
                    elif classNo == 17:
                        st.success('No entry')
                    elif classNo == 18:
                        st.success('General caution')
                    elif classNo == 19:
                        st.success('Dangerous curve to the left')
                    elif classNo == 20:
                        st.success('Dangerous curve to the right')
                    elif classNo == 21:
                        st.success('Double curve')
                    elif classNo == 22:
                        st.success('Bumpy road')
                    elif classNo == 23:
                        st.success('Slippery road')
                    elif classNo == 24:
                        st.success('Road narrows on the right')
                    elif classNo == 25:
                        st.success('Road work')
                    elif classNo == 26:
                        st.success('Traffic signals')
                    elif classNo == 27:
                        st.success('Pedestrians')
                    elif classNo == 28:
                        st.success('Children crossing')
                    elif classNo == 29:
                        st.success('Bicycles crossing')
                    elif classNo == 30:
                        st.success('Beware of ice/snow')
                    elif classNo == 31:
                        st.success('Wild animals crossing')
                    elif classNo == 32:
                        st.success('End of all speed and passing limits')
                    elif classNo == 33:
                        st.success('Turn right ahead')
                    elif classNo == 34:
                        st.success('Turn left ahead')
                    elif classNo == 35:
                        st.success('Ahead only')
                    elif classNo == 36:
                        st.success('Go straight or right')
                    elif classNo == 37:
                        st.success('Go straight or left')
                    elif classNo == 38:
                        st.success('Keep right')
                    elif classNo == 39:
                        st.success('Keep left')
                    elif classNo == 40:
                        st.success('Roundabout mandatory')
                    elif classNo == 41:
                        st.success('End of no passing')
                    elif classNo == 42:
                        st.success('End of no passing by vechiles over 3.5 metric tons')

                
            except Exception as e:
                st.error("Connection problem refresh again !!")
    
    elif choices=="About":
        st.write("This application is used to classify traffic sign through Convolutional Neural Netwok and tech : Samarth Gupta ")

if __name__ == "__main__":
    main()