
class Color_optimiser():
    def __init__(self):
        self.rgb_diapason = {'min':0, 'max':255}
        self.diapason_dicionary = {}
        self.absolute_min = self.rgb_diapason["min"]
        self.absolute_max = self.rgb_diapason["max"]

    def get_optimised_colors(self, window_width=10):
        window_diapason_optimiser = window_width
        nr_of_windows = int((self.rgb_diapason["max"] + 1) / window_diapason_optimiser)
        min = None
        max = None
        for x in range(nr_of_windows+1):
            if min == None:
                min = self.rgb_diapason["min"]
                max = min+window_diapason_optimiser
                self.diapason_dicionary[x] = {"min":min,
                                          "med":min+((max-min)/2),
                                          "max":max,
                                          }
                min = max+1
            elif min+window_diapason_optimiser <= self.rgb_diapason["max"]:
                max = min + window_diapason_optimiser
                self.diapason_dicionary[x] = {"min": min,
                                         "med": min + ((max - min) / 2),
                                         "max": max,
                                         }
                min = max + 1
            elif max == 255:
                pass
            else:
                max = self.rgb_diapason["max"]
                self.diapason_dicionary[x] = {"min": min,
                                         "med": min + ((max - min) / 2),
                                         "max": max,
                                         }
                min = max + 1

#
#
#
#
#
#
#
# # class Color_optimisation():
# nr_of_rgb_diapason = 256
# diapason_abatere = 3
# total_diapason = diapason_abatere*2
# nr_of_integer_diapasons = int(nr_of_rgb_diapason/total_diapason)
# last_diapason = nr_of_rgb_diapason - (nr_of_integer_diapasons*total_diapason)
# total_a= last_diapason+nr_of_integer_diapasons*total_diapason
#
# # print(nr_of_integer_diapasons)
# # print (last_diapason)
# # print(total_a)
#
# min = 0
# diapasons_dict = {}
#
# for x in range (nr_of_integer_diapasons):
#     max = min + total_diapason-1
#     diapasons_dict[x] = {'min': min,
#                          "med": max - diapason_abatere,
#                          "max": max,
#                          }
#     min = max+1
#
# print(diapasons_dict)