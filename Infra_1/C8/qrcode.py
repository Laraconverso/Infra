import qrcode

data = 'Happy Birthdae!'
img = qrcode.make(data)
img.save('YOU/ENTER/THE/ROOT/TO/THE/FOLDER/HERE/name.png')


####other option

qr = qrcode.QRCode(version = 1, box_size = 10, borde= 5)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color = 'red', back_color= 'black')
img.save('YOU/ENTER/THE/ROOT/TO/THE/FOLDER/HERE/name.png')