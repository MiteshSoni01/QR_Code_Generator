import streamlit as st
import qrcode

st.title('Your Personal QR!')
st.text('Your Personally defined QR Code in seconds!')
st.image('https://www.qrcode-monkey.com/img/default-preview-qr.svg')
st.info('Please fill in the below details to get started.')

name = st.text_input('Your Name?')
email = st.text_input('Your Email Address?')
phno = st.text_input('Your Phone Number?')
websiteurl = st.text_input("Your Website's URL?")

info = f'Name: {name}\n\nEmail: {email}\n\nContact: {phno}\n\nWebsite: {websiteurl}'

qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data(info)
qr.make(fit=True)

img = qr.make_image(fill = 'blue', back_color = 'white')
img.save(f'{name}.png')

if (name and email and phno) or (name and websiteurl):
    with open(f"{name}.png", 'rb') as file:
        st.download_button(label='Your QR Code', data=file, file_name=f'{name}.png', mime='png')

