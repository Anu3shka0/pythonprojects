import qrcode as qr

img = qr.make("www.linkedin.com/in/anushka-tiwari-016187324")
img.save("linkedin.png")
img.show()
print("QR code generated successfully")