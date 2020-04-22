from PIL import Image
from io import BytesIO
import os
import subprocess
from random import randint
import threading
class Resizer(object):

    def __init__(self, path_to_image, size_x, size_y):
        """ Resizes image.
        ------------------
        Warning! Ratio between X and Y must be at least 1/3.
        ------------------
        :param path_to_image: [../library/coolimg.png/gif/jpeg]
        :param size_x: Requested height of converted image.
        :param size_y: Requested width of converted image.
        :returns: resized copy of an image w/o saving it.
        """
        self.path_to_image = path_to_image
        self.size_x = size_x
        self.size_y = size_y
        self.xy = "{}x{}".format(str(self.size_x), str(self.size_y))
        self.original_img = Image.open(self.path_to_image)
    def _format_gif(self):
        """
        Resizing GIF image, using imagemagick.
        :return: An :py:class:`~PIL.Image.Image` object.
        """


        try:
            img_name = randint(1,10e10)
            if  self.method == "thumbnail":
                self.magick_method = "-thumbnail"
            else:
                self.magick_method = "-resize"
            self.command = ['convert',self.path_to_image,'-coalesce',self.magick_method, self.xy +
                            '!','GIF:{}'.format(str(img_name))]
            self.child = subprocess.Popen(self.command, universal_newlines=True, stdout=subprocess.PIPE,
                                          stderr=subprocess.PIPE)
            self.out,self.err = self.child.communicate()
            if self.child.returncode != 0:
                raise Exception()
            self.child.kill()
            self.original_img = Image.open(str(img_name))
            print("now")
            print(str(img_name))
            os.remove(str(img_name))
        except Exception as e:
            print(e)
        else:
            return self.original_img

    def _format_thumbnail(self):
        """
        Makes this image into a thumbnail.  This method modifies the
        image to contain a thumbnail version of itself, no larger than
        the given size.  This method calculates an appropriate thumbnail
        size to preserve the aspect of the image, calls the
        :py:meth:`~PIL.Image.Image.draft` method to configure the file reader
        (where applicable), and finally resizes the image.

        Note that this function modifies the :py:class:`~PIL.Image.Image`
        object in place.  If you need to use the full resolution image as well,
        apply this method to a :py:meth:`~PIL.Image.Image.copy` of the original
        image.

        :return: An :py:class:`~PIL.Image.Image` object.
        """
        self.original_img = self.original_img.convert("RGB")
        self.original_img.thumbnail((self.size_x, self.size_y), Image.LANCZOS)
        with BytesIO() as f:
            self.original_img.save(f, "JPEG", quality=90, background=(0, 255, 0))
        return self.original_img

    def _format_resize(self):
        """
        Returns a resized copy of this image.
        :return: An :py:class:`~PIL.Image.Image` object.
        """
        self.original_img = self.original_img.convert("RGB")
        self.original_img = self.original_img.resize((self.size_x, self.size_y), Image.LANCZOS)
        with BytesIO() as f:
            self.original_img.save(f, "JPEG", quality=90, background=(0, 255, 0))
        return self.original_img

    def format(self, method):
        """
        Depending on your decision, function formats img to size, entered in class declaration.
        :param method: [THUMBNAIL,RESIZE]{lowercase} - resize method.
        :return: An :py:class:`~PIL.Image.Image` object.
        """
        self.method = method
        if method not in ("thumbnail", "resize"):
            raise AttributeError("Incorrect method.")
        if self.original_img.mode in ["GIF", "P"]:
            self.original_img = self.original_img.convert("RGBA")
            return self._format_gif()
        elif method in "thumbnail":
            return self._format_thumbnail()
        elif method in "resize":
            return self._format_resize()


r = Resizer("out-deconstruct.gif", 64,64)
r.format(method="thumbnail")
