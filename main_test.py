import main
import unittest

class TestFuncMethod(unittest.TestCase):

    def test_resize_img_increase(self):
        self.r = main.Resizer("test_png_200x200.png", 300, 300)
        self.assertEqual(self.r.format(method="resize").size, (300, 300))


    def test_resize_img_decrease(self):
        self.r = main.Resizer("test_png_200x200.png", 64, 64)
        self.assertEqual(self.r.format(method="resize").size, (64, 64))

    def test_thumbnail_img_decrease(self):
        self.r = main.Resizer("test_png_200x200.png", 100, 100)
        self.assertEqual(self.r.format(method="thumbnail").size, (100, 100))

    def test_gif_resize_increase(self):
        self.r = main.Resizer("out-deconstruct.gif", 300, 600)
        self.assertEqual(self.r.format(method="resize").size, (300, 600))

    def test_gif_resize_decrease(self):
        self.r = main.Resizer("out-deconstruct.gif", 100, 50)
        self.assertEqual(self.r.format(method="resize").size, (100,50))

    def test_gif_thumbnail_increase(self):
        self.r = main.Resizer("out-deconstruct.gif", 300, 600)
        self.assertEqual(self.r.format(method="thumbnail").size, (300, 600))

    def test_gif_thumbnail_decrease(self):
        self.r = main.Resizer("out-deconstruct.gif", 100, 50)
        self.assertEqual(self.r.format(method="thumbnail").size, (100,50))


if __name__ == '__main__':
    unittest.main()
