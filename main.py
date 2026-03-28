from PIL import Image, ImageTk
import customtkinter as ctk
import os


class Convert:
    def convert_image(self, img_1, img_2):
        image = Image.open(img_1)

        # Convert EVERYTHING with transparency to RGBA first
        if image.mode in ("P", "RGBA", "LA"):
            image = image.convert("RGBA")

            background = Image.new("RGB", image.size, (255, 255, 255))
            background.paste(image, mask=image.getchannel("A"))  # safer than split()

            background.save(img_2, "JPEG")
        else:
            image = image.convert("RGB")
            image.save(img_2, "JPEG")
convert = Convert()
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("800x600")
app.title("Image Converter")

def set_icon():
    icon_path = "logo.png"
    if os.path.exists(icon_path):
        try:
            img = Image.open(icon_path).convert("RGBA")
            app.icon_object = ImageTk.PhotoImage(img)
            app.wm_iconphoto(False, app.icon_object)
        except Exception as e:
            print(f"Icon error: {e}")
    else:
        print(f"Icon not found: {icon_path}")

app.after(200, set_icon)


def select_file():
    # Open File Explorer on windows, Finder on macos, and whatever the files app is on linux
    filename = ctk.filedialog.askopenfilename(
        initialdir="/",
        title="Select an Image",
        filetypes=(("Portable Network Graphics (PNG)", "*.png"), ("All files", "*.*"))
    )
    if filename:
        print(f"Selected: {filename}")
# Stuff

button = ctk.CTkButton(app, text="CTkButton", command=lambda: convert.convert_image("test.png", "test.webp"))
button.pack()
button2 = ctk.CTkButton(app, text = "Open File Explora", command=lambda: select_file())
button2.pack()
app.resizable(False, False)
app.after(0, lambda: app.state("zoomed"))
app.mainloop()