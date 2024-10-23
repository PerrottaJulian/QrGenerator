import qrcode

url = input("Ingrese una URL: ")

qr = qrcode.QRCode(
    version = 1,
    box_size=10,
    border=2.5
)

qr.add_data(url)
qr.make(fit=True)

img = qr.make_image()
img.save("TuQR.png")