import qrcode

qr = qrcode.QRCode(
    version=4,  
    error_correction=qrcode.constants.ERROR_CORRECT_L,  
    box_size=10,  
    border=1  
)

data = "https://www.linkedin.com/in/jitender-kumar-30a1111b6/"

qr.add_data(data)

qr.make(fit=True)

img = qr.make_image(fill_color=(255,217,4), back_color=(0,0,0))
img.save("Jitender_linkedin.png")
