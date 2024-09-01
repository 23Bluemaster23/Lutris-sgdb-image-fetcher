import io
import requests

from PIL import Image, ImageOps, ImageTk

from utils.Constants import ImageRes


class WebImage:
    def __init__(self, url):
        try:
            request = requests.get(url, stream=True)
            raw_data = request.content
            request.close()
        except requests.exceptions.HTTPError as errh:
            print("Http Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
        except requests.exceptions.RequestException as err:
            print("OOps: Something Else", err)
        self.image = Image.open(io.BytesIO(raw_data))

        self.image = ImageOps.contain(self.image, [200, 300])
        self.imageWidget = ImageTk.PhotoImage(self.image)

    def get_image(self):

        return self.imageWidget

    def save_image(self, type: str, file_name: str = "default.png"):
        match (type):
            case "coverart":
                save_image = self.image.convert(mode="RGB").resize(
                    ImageRes.COVERART.value
                )

            case "banner":
                save_image = self.image.convert(mode="RGB").resize(
                    ImageRes.BANNER.value
                )

            case "icon":
                save_image = self.image.resize(ImageRes.ICON.value)

            case _:
                save_image = self.image

        save_image.save(
            file_name,
            quality=100,
            subsampling=0,
        )
