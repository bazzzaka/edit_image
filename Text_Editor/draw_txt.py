import requests
from io import BytesIO
from PIL import Image, ImageFont, ImageDraw


class DrawTxt:

    @staticmethod
    def draw_txt(image, position, text, size_txt, fill, font):
        print('work def draw_txt')
        im = Image.open(BytesIO(image))
        draw = ImageDraw.Draw(im, mode='RGBA')
        get_font = ImageFont.truetype(font, size_txt)
        draw.text(position, text, fill, get_font)
        print('return image with text')
        return draw

    @staticmethod
    def image_text(image_path, image_url, position, text, size_txt, fill, font):
        """

        :param fill:
        :param size_txt:
        :param image_path: the image that is on the computer
        :param image_url: link to the image to be downloaded
        :param position: text position
        :param text: text to insert into the image
        :param font: text font
        :param align: edge alignment
        :return: image with text
        """
        print('work def image_text')

        if image_path is None:
            im = requests.get(image_url).content
            print('image to be download')
        else:
            im = Image.open(r'{}'.format(image_path))

        print('image put in draw_txt')
        result = DrawTxt.draw_txt(im, position, text, size_txt, fill, font)
        return result


if __name__ == '__main__':
    result_im = DrawTxt.image_text(
        image_path=None,
        image_url='https://www.imgonline.com.ua/examples/bee-on-daisy.jpg',
        position=(20, 20),
        text='some_txt',
        size_txt=20,
        fill='black',
        font='D:\Fonts SUA\Pangolin-Regular.ttf',
    )
    result_im.save('test_image.png')

