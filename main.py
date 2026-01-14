import qrcode
import os

url = input("Enter the URL: ").strip()

save_folder = input("Enter folder path where you want to save the QR code: ").strip()
if not save_folder:
    save_folder = "."  # default current folder

# Ask for a filename
filename = input("Enter filename (without extension): ").strip()
if not filename:
    filename = "qrcode"
    
os.makedirs(save_folder, exist_ok=True)

full_path = os.path.join(save_folder, filename + ".png")

# Create the QR code
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save(full_path)

print(f"QR Code was generated and saved to:\n{full_path}")
