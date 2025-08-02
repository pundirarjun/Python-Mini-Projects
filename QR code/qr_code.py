import qrcode

website_link = input("Enter the link which you want to create QR code: ")
qr = qrcode.QRCode(version = None , box_size = 5 , border = 5 )
qr.add_data(website_link)
qr.make()
img = qr.make_image(fill_color = "black", back_color = "white")
img.save("youtube_qr.png")
