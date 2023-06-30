import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from colors_optimisation import Color_optimiser


class Image_processor():
    def __init__(self):
        self.file_path = None
        self.img_op = None
        self.img_arr = None
        self.diapason_of_colors = None
        self.list_of_unique_pixels = []
        self.all_pixels = []
        self.sorted_dictionary = {}
        self.dictionary_of_all_colors = {}
        self.nr_of_top = None

    def change_image_to_process(self, image_path=None):
        self.file_path = image_path
        self.img_op = Image.open(self.file_path)
        if self.img_op.size[0] > 250:
            ratio = round(self.img_op.size[0] / 300, 2)
        elif self.img_op.size[1] > 250:
            ratio = round(self.img_op.size[1] / 300, 2)
        else:
            ratio=1
        self.img_op.thumbnail((int(self.img_op.size[0]/ratio), int(self.img_op.size[1]/ratio)))
        self.img_arr = np.array(self.img_op)

    def change_window_for_color_optimiser(self, window_width:int):
        self.diapason_of_colors.get_optimised_colors(window_width=window_width)

    def get_optimized_color_picture(self):
        for each in self.diapason_of_colors.diapason_dicionary:
            self.img_arr[(self.img_arr <= self.diapason_of_colors.diapason_dicionary[each]["max"]) & (
                        self.img_arr >= self.diapason_of_colors.diapason_dicionary[each]["min"])] = \
                self.diapason_of_colors.diapason_dicionary[each]["med"]

    def count_nr_of_same_pixels(self, pixel, list_of_pixels:list):
        nr_of_repeats = 0
        for el in list_of_pixels:
            if pixel==el:
                nr_of_repeats += 1
        return nr_of_repeats

    def get_lists_of_colors(self):
        self.list_of_unique_pixels = []
        self.all_pixels = []
        for row in self.img_arr:
            for pixel in row:
                color1 = pixel[0]
                color2 = pixel[1]
                color3 = pixel[2]
                color = (color1, color2, color3)
                self.all_pixels.append(color)
        for color in self.all_pixels:
            if color not in self.list_of_unique_pixels:
                self.list_of_unique_pixels.append(color)


    def get_final_dictionary_of_all_colors(self):
        self.dictionary_of_all_colors = {}
        order_nr = 0
        for pixel in self.list_of_unique_pixels:
            nr_of_pixels = self.count_nr_of_same_pixels(pixel=pixel, list_of_pixels=self.all_pixels)
            self.dictionary_of_all_colors[order_nr] = {
                'color_RGB': pixel,
                'nr_of_pixels': nr_of_pixels}
            order_nr += 1

    def change_nr_of_top(self, nr_of_top):
        self.nr_of_top = nr_of_top

    def get_top_dictionary_colors(self,):
        list_of_nr_of_pixel = []
        self.sorted_dictionary = {}
        for each in self.dictionary_of_all_colors:
            list_of_nr_of_pixel.append(self.dictionary_of_all_colors[each]['nr_of_pixels'])
        list_of_nr_of_pixel.sort(reverse=True)
        for nr in range(self.nr_of_top):
            for each in self.dictionary_of_all_colors:
                if self.dictionary_of_all_colors[each]['nr_of_pixels'] == list_of_nr_of_pixel[nr]:
                    self.sorted_dictionary[nr] = self.dictionary_of_all_colors[each]
                    self.sorted_dictionary[nr]["ponderea"] = round(self.dictionary_of_all_colors[each]["nr_of_pixels"]/len(self.all_pixels)*100, 2)

    def show_processed_image(self):
        plt.imshow(self.img_arr)
        plt.show()

    def make_all_the_circle(self, image_path = None, top_nr = 10, window_color_width = 8):
        self.diapason_of_colors = Color_optimiser()
        self.diapason_of_colors.get_optimised_colors(window_width=window_color_width)
        self.nr_of_top = top_nr
        self.change_image_to_process(image_path)
        print("1")
        self.get_optimized_color_picture()
        print("2")
        self.get_lists_of_colors()
        print("3")
        self.get_final_dictionary_of_all_colors()
        print("4")
        self.get_top_dictionary_colors()
        print(f'Nr of unique colors = {len(self.list_of_unique_pixels)}')
        print(f'Nr of all pixels = {len(self.all_pixels)}')
        print(f'Dict all colors = {self.dictionary_of_all_colors}')
        print(f'Dict top {self.nr_of_top} colors = {self.sorted_dictionary}')
