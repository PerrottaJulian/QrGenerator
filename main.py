import qrcode

#Ingresar URL de donde se quiere que le QR redireccione
url = input("Ingrese una URL: ")

#Se crea el objeto QR
qr = qrcode.QRCode(
    version = 1,
    box_size=10,
    border=2.5
)

#Añado la URL al objeto QR
qr.add_data(url)
qr.make(fit=True)

#Creo la imagen
img = qr.make_image()
img.save("TuQR.png")