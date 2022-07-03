import os
import sys
from PIL import Image, ImageFilter


class ImageEditor:
    def __init__(self):
        pass

    @staticmethod
    def open_image(image):
        image = Image.open(f'{image}')
        return image

    @staticmethod
    def save_image(image, im_format):
        image.save(f'{im_format}')
        return 'Image has been saved'

    @staticmethod
    def convert_to_jpeg(image, im_format):
        for infile in sys.argv[1:]:
            f, e = os.path.splitext(infile)
            outfile = f + f'{im_format}'
            if infile != outfile:
                try:
                    with Image.open(infile) as im:
                        im.save(outfile)
                except OSError:
                    print('cannot convert', infile)

    @staticmethod
    def sub_copy(image, left, upper, right, lower):
        box = (left, upper, right, lower)
        region = image.crop(box)
        return region

    @staticmethod
    def roll(image, delta):
        """Roll an image sideways."""
        xsize, ysize = image.size

        delta = delta % xsize
        if delta == 0:
            return image

        part1 = image.crop((0, 0, delta, ysize))
        part2 = image.crop((delta, 0, xsize, ysize))
        image.paste(part1, (xsize - delta, 0, xsize, ysize))
        image.paste(part2, (0, 0, xsize - delta, ysize))

        return image

    @staticmethod
    def merge(image1, image2):
        w = image1.size[0] + image2.size[0]
        h = max(image1.size[1], image2.size[1])
        image = Image.new('RGBA', (w, h))

        image.paste(image1)
        image.paste(image2, (image1.size[0], 0))
        return image

    @staticmethod
    def make_shadow(image, iterations, border, offset, background_colour, shadow_colour):
        # image: base image to give a drop shadow
        # iterations: number of times to apply the blur filter to the shadow
        # border: border to give the image to leave space for the shadow
        # offset: offset of the shadow as [x,y]
        # backgroundColour: colour of the background
        # shadowColour: colour of the drop shadow

        # Calculate the size of the shadow's image
        full_width = image.size[0] + abs(offset[0]) + 2 * border
        full_height = image.size[1] + abs(offset[1]) + 2 * border

        # Create the shadow's image. Match the parent image's mode.
        shadow = Image.new(image.mode, (full_width, full_height), background_colour)

        # Place the shadow, with the required to be offset
        shadow_left = border + max(offset[0], 0)  # if <0, push the rest of the image right
        shadow_top = border + max(offset[1], 0)  # if <0, push the rest of the image down
        # Paste in the constant colour
        shadow.paste(shadow_colour,
                     (shadow_left,
                      shadow_top,
                      shadow_left + image.size[0],
                      shadow_top + image.size[1]))

        # Apply the BLUR filter repeatedly
        for i in range(iterations):
            shadow = shadow.filter(ImageFilter.BLUR)

        # Paste the original image on top of the shadow
        imgLeft = border - min(offset[0], 0)  # if the shadow offset was <0, push right
        imgTop = border - min(offset[1], 0)  # if the shadow offset was <0, push down
        shadow.paste(image, (imgLeft, imgTop))

        return shadow
