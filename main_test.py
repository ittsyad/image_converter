import main
import unittest

class TestFuncMethod(unittest.TestCase):

    def test_resize_img_increase(self):
        tmp1 = main.Resizer("tmp_/test1076x1628.png", 2000, 2000)
        self.assertEqual(tmp1.format(method="resize").size, (2000, 2000))
        tmp1 = main.Resizer("tmp_/test_png_200x200.png", 500, 300)
        self.assertEqual(tmp1.format(method="resize").size, (500, 300))
        tmp1 = main.Resizer("tmp_/test500x200.png", 501, 500)
        self.assertEqual(tmp1.format(method="resize").size, (501, 500))

    def test_resize_img_decrease(self):
        tmp1 = main.Resizer("tmp_/test_png_200x200.png", 64, 64)
        self.assertEqual(tmp1.format(method="resize").size, (64, 64))
        tmp1 = main.Resizer("tmp_/test1076x1628.png", 121, 89)
        self.assertEqual(tmp1.format(method="resize").size, (121, 89))
        tmp1 = main.Resizer("tmp_/test500x200.png",199, 89)
        self.assertEqual(tmp1.format(method="resize").size, (199, 89))

    def test_thumbnail_img_decrease(self):
        tmp1 = main.Resizer("tmp_/test_png_200x200.png", 100, 33)
        self.assertEqual(tmp1.format(method="thumbnail").size, (33, 33))
        tmp1 = main.Resizer("tmp_/test1076x1628.png", 400, 200)
        self.assertEqual(tmp1.format(method="thumbnail").size, (400, 200))
        tmp1 = main.Resizer("tmp_/test500x200.png", 100, 100)
        self.assertEqual(tmp1.format(method="thumbnail").size, (100, 40))

    def test_gif_resize_increase(self):
        tmp1 = main.Resizer("tmp_/test250x243.gif", 300, 600)
        self.assertEqual(tmp1.format(method="resize").size, (300, 600))
        tmp1 = main.Resizer("tmp_/test500x200.gif", 300, 600)
        self.assertEqual(tmp1.format(method="resize").size, (300, 600))
        tmp1 = main.Resizer("tmp_/test200x500.gif", 300, 600)
        self.assertEqual(tmp1.format(method="resize").size, (300, 600))

    def test_gif_resize_decrease(self):
        tmp1 = main.Resizer("tmp_/test250x243.gif", 100, 50)
        self.assertEqual(tmp1.format(method="resize").size, (100,50))
        tmp1 = main.Resizer("tmp_/test500x200.gif", 100, 50)
        self.assertEqual(tmp1.format(method="resize").size, (100, 50))
        tmp1 = main.Resizer("tmp_/test200x500.gif", 100, 50)
        self.assertEqual(tmp1.format(method="resize").size, (100, 50))

    def test_gif_thumbnail_decrease(self):
        tmp1= main.Resizer("tmp_/test250x243.gif", 100, 150)
        self.assertEqual(tmp1.format(method="thumbnail").size, (100,150))
        tmp1 = main.Resizer("tmp_/test200x500.gif", 100, 50)
        self.assertEqual(tmp1.format(method="thumbnail").size, (100, 50))
        tmp1 = main.Resizer("tmp_/test500x200.gif", 100, 150)
        self.assertEqual(tmp1.format(method="thumbnail").size, (100, 150))
if __name__ == '__main__':
    unittest.main()
