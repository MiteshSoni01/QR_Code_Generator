#Importing Necessary Libraries
import streamlit as st
import qrcode

#Designing the Web App
st.title('Your Personal QR!') #Title
st.text('Your Personally defined QR Code in seconds!') #Normal Text
st.image('https://www.qrcode-monkey.com/img/default-preview-qr.svg') #Image
st.info('Please fill in the below details to get started.') #Informative Text Areain

#User's Input
name = st.text_input('Your Name?')
email = st.text_input('Your Email Address?')
phno = st.text_input('Your Phone Number? ')
websiteurl = st.text_input("Your Website's URL?")

#Variable to allocate to the QR-Code's Memory
info = f'Name: {name}\n\nEmail: {email}\n\nContact: {phno}\n\nWebsite: {websiteurl}'

#Initializing the QR-Code
qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data(info) #Fitting the data.
qr.make(fit=True)

#QR Code Creation
img = qr.make_image(fill = 'blue', back_color = 'white')
img.save(f'{name}.png') #Saving of Image

#Downloading Image.
if (name and email and phno) or (name and websiteurl):
    with open(f"{name}.png", 'rb') as file:
        st.download_button(label='Your QR Code', data=file, file_name=f'{name}.png', mime='png')

