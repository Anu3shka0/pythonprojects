
import qrcode 
from PIL import Image

qr = qrcode.QRCode(version = 2, error_correction = qrcode.constants.ERROR_CORRECT_H, box_size = 5, border = 12 )
qr.add_data("www.linkedin.com/in/anushka-tiwari-016187324")
qr.make(fit = True)
img = qr.make_image(fill_color = "red", back_color = "black")
img.save("linkedin1.png")
img.show()
print("QR code generated successfully")