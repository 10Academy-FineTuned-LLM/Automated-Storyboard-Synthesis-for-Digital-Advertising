from typing import List

from PIL import Image

class StoryBoard:

    @staticmethod
    def combine_images_horizontally(images, separation_space=100, vertical_padding=200, background_color=(255, 255, 255)):
        """
        Combines multiple images into a new image, displayed horizontally on a larger background.
        Images are centered horizontally within the background and have vertical padding.

        :param images: loaded pillow images.
        :param separation_space: Space between images in pixels.
        :param vertical_padding: Vertical padding for the top and bottom of the images.
        :param background_color: Background color of the new image as an RGB tuple.
        :return: Combined image.
        """
        # images = [Image.open(path) for path in image_paths]
        widths, heights = zip(*(i.size for i in images))

        # Calculate total width and max height for the images, considering separation space
        total_images_width = sum(widths) + separation_space * (len(images) - 1)
        max_height = max(heights) + vertical_padding * 2

        # Calculate the background size
        background_width = total_images_width + vertical_padding * 2  # Padding on left and right for uniformity
        background_height = max_height

        # Create the background image
        background = Image.new('RGB', (background_width, background_height), color=background_color)

        # Calculate the starting x coordinate to center the images horizontally
        x_offset = (background_width - total_images_width) // 2

        # Paste each image, centered vertically
        for img in images:
            y_offset = (background_height - img.height) // 2
            background.paste(img, (x_offset, y_offset))
            x_offset += img.width + separation_space

        return background
    
if __name__ == "__main__":
    image = StoryBoard.combine_images_horizontally(['./images/01d8fa51-ca7b-499d-9938-c13f3b496439.png',
                                            'images/48e6f2e6-b292-4cae-81aa-b0362cc803f1.png',
                                            'images/d7c83396-f43f-4d61-bdf4-76db405bf2ef.png'])
    image.show()