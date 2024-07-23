import qrcode
from PIL import Image

#pip install qrcode
#pip install pillow


def generate_qr_code(link, file_name):
    qr = qrcode.QRCode(
        version=1,

error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(link)
    qr.make(fit=True)

    img = qr.mnake_image(fill='black', back_color='white')

    img.save(file_name)
    print(f"QR code generated and saved as {file_name}")

    #example usage
    if __name__ == "__main__":
        link = input("Enter the link to generate QR code: ")
        file_name = "qr_code.png"
        generate_qr_code(link, file_name)
