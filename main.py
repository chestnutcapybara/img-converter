from PIL import Image
import customtkinter as ctk


from PIL import Image

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

# Stuff

button = ctk.CTkButton(app, text="CTkButton", command=lambda: convert.convert_image("test.png", "test.jpg"))
button.pack()

app.resizable(False, False)
app.after(0, lambda: app.state("zoomed"))
app.mainloop()