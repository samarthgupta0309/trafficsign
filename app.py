import streamlit as st 
from PIL import Image
import classify 
import numpy as np

sign_names = {
        0: 'Speed limit (20km/h)',
        1: 'Speed limit (30km/h)',
        2: 'Speed limit (50km/h)',
        3: 'Speed limit (60km/h)',
        4: 'Speed limit (70km/h)',
        5: 'Speed limit (80km/h)',
        6: 'End of speed limit (80km/h)',
        7: 'Speed limit (100km/h)',
        8: 'Speed limit (120km/h)',
        9: 'No passing',
        10: 'No passing for vehicles over 3.5 metric tons',
        11: 'Right-of-way at the next intersection',
        12: 'Priority road',
        13: 'Yield',
        14: 'Stop',
        15: 'No vehicles',
        16: 'Vehicles over 3.5 metric tons prohibited',
        17: 'No entry',
        18: 'General caution',
        19: 'Dangerous curve to the left',
        20: 'Dangerous curve to the right',
        21: 'Double curve',
        22: 'Bumpy road',
        23: 'Slippery road',
        24: 'Road narrows on the right',
        25: 'Road work',
        26: 'Traffic signals',
        27: 'Pedestrians',
        28: 'Children crossing',
        29: 'Bicycles crossing',
        30: 'Beware of ice/snow',
        31: 'Wild animals crossing',
        32: 'End of all speed and passing limits',
        33: 'Turn right ahead',
        34: 'Turn left ahead',
        35: 'Ahead only',
        36: 'Go straight or right',
        37: 'Go straight or left',
        38: 'Keep right',
        39: 'Keep left',
        40: 'Roundabout mandatory',
        41: 'End of no passing',
        42: 'End of no passing by vehicles over 3.5 metric tons'}
st.title("ECE2010 Control systems J component")
# st.set_option('deprecation.showfileUploaderEncoding', False)
activities = ["Classification","Working","About us"]
choices = st.sidebar.selectbox("Select Activities", activities)
if choices == "Classification":
        st.header("TRAFFIC SIGN CLASSIFICATION")
        st.markdown("**_Motivation_** :")
        st.write("With the development of automotive intelligent technology,many different famous car companies like Mercedes-Benz and BMW have actively invested in ADAS (Advanced Driver Assistance System) research. Commercialized ADAS also include TSR(Traffic SignRecognition) systems to remind the drivers to pay attention to the speed and help in preventing road accidents. With the increase in demand of TSR (Traffic Sign Recognition) it is impossible for others to understand the advantages and need of thissystem")
        st.write("")
        traffic_image = 'trafficsigns.png'
        st.image(traffic_image, caption = "Let the machine do the work")
        st.text("")
        uploaded_file = st.file_uploader("Choose an image...", type=['png','jpg','jpeg'])
        st.write("Note : Currently pnh file is not working. We are working on it.")
        if uploaded_file is not None:

                image = Image.open(uploaded_file)
                st.image(image, caption='Uploaded Image', use_column_width=True)

                st.write("")

                if st.button('predict'):
                        st.write("result...")
                        label = classify.predict(uploaded_file)
#                         proba = label.argsort[0][-1]
#                         top = np.argsort(proba[0])[-1]
                        label = label.item()

                        res = sign_names.get(label)
                        st.success(res)
                st.image("workingimg.png")
                st.write("")
                st.markdown("we did comparision with different model & techniques")
                st.write("")
                st.image("comparison.jpeg")
elif choices == "Working":
        st.header("Working")
        st.text("")
        st.markdown("**This project aims to classify the traffic sign**")
        st.text("")
        st.markdown("**_About_ _DataSet_** :")
        st.write("We used the German data set to import the images into this project.The German Traffic Sign Benchmark is a multi-class, single-image classification challenge held at the International Joint Conference on Neural Networks (IJCNN) 2011.")
        st.text("")
        st.markdown("**_Working_** :")
        st.write("ARCHITECTURE:")
        st.image("architect..PNG")
        st.markdown('The starting step of this project was to load the data set, We have used the numpy library to calculate summary statistics of the traffic signs data set:The size of training set is 34799, The size of the validation set is 4410, The size of test set is 12630, The shape of a traffic sign image is (32, 32, 3), The number of unique classes/labels in the data set is 43. After that we explored,summarized and visualized the data set .Design, training and testing of the model architecture occured after we had visualized the whole data set. Then, we used the model to make predictions on new images and analyse the probabilities of the new image. Finally we test the model with a data set.And deployed the project to make an interactive web app using  streamlit.')
elif choices == "About us":
        st.header("About us :")
        st.image("image.gif", format = 'GIF')
        st.write("We are 3rd year electronics and communication students and we have done this project for Control Systems under Dr Rajesh R.")
        st.write("And we have made this project with understanding of algo of ml while incorporating deep leaning using  CNN and this is the final product which analyses different traffic signs and classifies them.")
        st.write("**_TEAM_**")
        images_on_page = ["kartik.jpeg","aryaman.jpeg","ankesh.jpeg","hritik.jpeg"]
        name_img = ["Kartik Tripathi", "Aryaman Chandra","Ankesh Patel","Hritik Jha"]
        st.image(images_on_page, width=150, caption=name_img)
