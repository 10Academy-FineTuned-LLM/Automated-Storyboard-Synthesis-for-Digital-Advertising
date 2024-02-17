from typing import Literal, Optional, Tuple
import logging
import base64
from io import BytesIO
import os

import replicate
from PIL import Image
import requests
from pydantic import HttpUrl

# Configurations
os.environ["REPLICATE_API_TOKEN"] = "r8_3XvmmORx5HCfHYlbeVEFAJJIO7xjkUV1Xq35K"
logging.basicConfig(level=logging.INFO)

class ImageGenerater:
    def __init__(self, asset_suggestions: dict) -> None:
        self.asset_suggestions = asset_suggestions

    def generate_images(self, store_location: str ='./images') -> dict:
        generated_images = {}
        for frame, elements in self.asset_suggestions.items():
            if frame.startswith('frame'):
                generated_images[frame] = []
                for type, description in elements.items():
                    print(type)
                    downloaded_image = ImageGenerater.download_image(ImageGenerater.generate_image(prompt=description)[0], store_location)
                    generated_images[frame].append((type, *downloaded_image))

        return generated_images


    @staticmethod
    def generate_image(prompt: str, performance_selection: Literal['Speed', 'Quality', 'Extreme Speed'] = "Extreme Speed", 
                       aspect_ratios_selection: str = "1024*1024", image_seed: int = 1234, sharpness: int = 2) -> Optional[dict]:
        """
        Generates an image based on the given prompt and settings.

        :param prompt: Textual description of the image to generate.
        :param performance_selection: Choice of performance level affecting generation speed and quality.
        :param aspect_ratio: The desired aspect ratio of the generated image.
        :param image_seed: Seed for the image generation process for reproducibility.
        :param sharpness: The sharpness level of the generated image.
        :return: The generated image or None if an error occurred.
        """
        try:
            output = replicate.run(
                "konieshadow/fooocus-api-anime:a750658f54c4f8bec1c8b0e352ce2666c22f2f919d391688ff4fc16e48b3a28f",
                input={
                    "prompt": prompt,
                    "performance_selection": performance_selection,
                    "aspect_ratios_selection": aspect_ratios_selection,
                    "image_seed": image_seed,
                    "sharpness": sharpness
                }
            )
            logging.info("Image generated successfully.")
            return output
        except Exception as e:
            logging.error(f"Failed to generate image: {e}")
            return None
        
    @staticmethod
    def decode_image(base64_data: str) -> Optional[Image.Image]:
        """
        Converts a base64 image into pillow iamge object.

        :param base64_data: Textual base64 image data.
        :return: Converted pillow image.
        """
        image_data = base64.b64decode(base64_data)
        image_stream = BytesIO(image_data)
        return(Image.open(image_stream))
    
    @staticmethod
    def download_image(url: HttpUrl, save_path: str) -> Tuple[str, str]:
        """
        Downloads provided url data to given location.

        :param url: HTTP Url of the file.
        :param save_path: Folder location to save the data.
        :return: Tuple of the url and save location.
        """

        try:
            response = requests.get(url)
            
            if response.status_code == 200:
                save_path = os.path.join(save_path, os.path.basename(url))
                image = Image.open(BytesIO(response.content))
                image.save(save_path)
                logging.info(f"Image saved to {save_path}")
                return (url, save_path)
            else:
                raise RuntimeError(f"Failed to download image. Status code: {response.status_code}") from None
        except Exception as e:
            raise RuntimeError(f"An error occurred: {e}") from e
        
        
if __name__ == "__main__":
    # output = ImageGenerater.generate_image("a big star being born")
    # print(output)
    # image = ImageGenerater.download_image('https://replicate.delivery/pbxt/a4uwoBueQhS5cCdF6VeUJfpvuslvXQBA9NRQcE3dFRR6D5skA/d7c83396-f43f-4d61-bdf4-76db405bf2ef.png', './images')
    # image.show()
    a = {
    "frame_1": {
        "Animated Element": "A high-resolution 3D Coca-Cola bottle center-screen, bubbles rising to the top, transitioning into a sleek DJ turntable with a vinyl record that has the Coke Studio logo.",
    },
    "frame_2": {
        "CTA Text": "'Mix Your Beat' in bold, playful font pulsating to the rhythm of a subtle background beat, positioned at the bottom of the screen."
    },
    "explanation": "This variation emphasizes the joy and interactivity of music mixing, with each frame building on the last to create a crescendo of engagement. The 3D bottle-to-turntable animation captures attention, the interactive beat mixer sustains engagement, and the vibrant animations encourage sharing, aligning with the campaign's objectives of engagement and message recall."
    }
    test = ImageGenerater(a)

    test.generate_images()
    