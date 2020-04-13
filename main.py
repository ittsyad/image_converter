from PIL import Image
import io,os,subprocess
class resizer(object):

    def __init__(self,path_to_image,size_x, size_y):
        """ Resizes image.
        ---------------------------
        Warning! Ratio between X and Y must be at least 1/3.
        ---------------------------
        :param: path_to_image: [../library/coolimg.png/gif/jpeg]
        :param: size_x: Requested height of converted image.
        :param: size_y: Requested width of converted image.
        :returns:resized copy of an image w/o saving it.
        """

        self.path_to_image = path_to_image
        self.size_x = size_x
        self.size_y = size_y
        self.xy = "{}x{}".format(str(self.size_x),str(self.size_y))
        self.original_img = Image.open(self.path_to_image)
    def __format_gif(self):
        """
        Resizing GIF image, using imagemagick.
        :return: An :py:class:`~PIL.Image.Image` object.
        """
        print(self.original_img)
        self.converted = False
        try:
            self.command = ['convert',self.path_to_image,'-coalesce','-resize',self.xy,'-deconstruct','out-deconstruct1.gif']
            self.child = subprocess.Popen(self.command, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.output, self.error = self.child.communicate()
            if self.child.returncode != 0:
                raise Exception()
            self.original_img = Image.open("out-deconstruct1.gif")
            os.remove("out-deconstruct1.gif")
        except Exception as e:
            raise Exception(e)
        else:
            self.converted = True
            return self.original_img

    def __format_thumbnail(self):
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
        with io.BytesIO() as f:
            self.original_img.save(f, "JPEG", quality=90,background = (0,255,0))
        self.original_img.show()
        return self.original_img


    def __format_resize(self):
        """
        Returns a resized copy of this image.
        :return: An :py:class:`~PIL.Image.Image` object.
        """
        self.original_img = self.original_img.convert("RGB")
        self.original_img = self.original_img.resize((self.size_x, self.size_y), Image.LANCZOS)
        #self.b = io.BytesIO()
        with io.BytesIO() as f:
            self.original_img.save(f,"JPEG", quality=90,background = (0,255,0))
        return self.original_img


    def format(self,method):
        """
        Depending on your decision, function formats img to size, entered in class declaration.
        :param method: [THUMBNAIL,RESIZE]{lowercase} - resize method.
        :return: An :py:class:`~PIL.Image.Image` object.
        """
        self.method = method
        if method not in ("thumbnail","resize"):
            raise AttributeError("Incorrect method.")
        if self.original_img.mode in ["GIF","P"]:
            self.original_img = self.original_img.convert("RGBA")
            return self.__format_gif()
        elif method in "thumbnail":
            return self.__format_thumbnail()
        elif method in "resize":
            return self.__format_resize()


r = resizer("7VE.gif",500,500)
r.format(method="thumbnail")