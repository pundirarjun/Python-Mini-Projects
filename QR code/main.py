import qrcode
 
def generate_qr (data,filename = "custom_qr.png"):
    qr = qrcode.QRCode(version= None , box_size= 5 , border = 5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color = "black" , back_color = "white")
    img.save(filename)
    print(f"QR code saved as {filename}")

print("What type of QR code would you like to generate")
print("Options: website / wifi / contact / sms / email / location / text")
choice = input("Enter your choice: ").strip().lower()


if choice == "website":
    link = input("Enter the website link: ")
    generate_qr(link, "website_qr.png")

elif choice == "wifi":
    # name = input("Enter the name of the network: ")
    # encryption = input("Enter encryption type (WPA or leave blank for none): ")
    # password = input("Enter the password: ")
    # wifi_data = f"WIFI:S:{name};T:{encryption};P:{password}"
    # generate_qr(wifi_data, "wifi_qr.png")
    print("This is not working right now so don't try again.")
    
elif choice == "contact":
    name = input("Enter the name: ")
    phone = input("Enter the number: ")
    email = input("Enter the email: ")

    # vCard is a format of storing contact detail it just use to directly add the contact to phone just by scaning the QR code 
    contact_data = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL:{phone}
EMAIL:{email}
END:VCARD"""
    generate_qr(contact_data, "contact_qr.png")

elif choice == "sms":
    number = input("Enter the number: ")
    message = input("Enter the massage: ")
    # sms: is a URI (Uniform Resource Identifier) tell the phone to Open the SMS or messaging app
    # ?body tells the message app to put the data into the message body
    sms_data = f"sms:{number}?body = {message}"
    generate_qr(sms_data, "sms_qr.png")

elif choice == "email":
    to = input("Enter the recipient email: ")
    subject = input("Enter the subject: ")
    body = input("Enter the body: ")
    # mailto is a URL scheme that open the default email app
    email_data = f"mailto:{to}?subject= {subject}&body = {body}"
    generate_qr(email_data, "email_qr.png")

elif choice == "location":
    latitude = int(input("Enter Latitude: "))
    longitude = int(input("Enter longitude: "))
    # geo is a URI to encode the geographic location after scanning it open the location in the map app
    location_data = f"geo:{latitude}, {longitude}"
    generate_qr(location_data, "location_qr.png")

elif choice == "text":
    text = input("Enter the text you want in the QR code: ")
    generate_qr(text, "text_qr.png")


else:
    print("Invalid choice. Please try again.")