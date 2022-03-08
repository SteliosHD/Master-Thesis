import random
from itertools import cycle



class SlidingWindowOverlap :
    """TODO:add doc"""

    def __init__(self,iterable_obj,seed=2021):
        random.seed(seed)
        self.iterable_obj = iterable_obj
        self.cycle_iterable = cycle(iterable_obj)
        self.previous_elements = []


    def sliding_window_with_overlaps(self, size, overlaps=3):

        if len(self.iterable_obj) < overlaps or size < overlaps:
            raise Exception("Overlaps or size cannot be greater than the length of the iterable ")
        win = self._sliding_window(size-overlaps)

        if self.previous_elements:
            final_window = self.previous_elements + win
        else:
            last_elements = self._sliding_window(overlaps)
            final_window = win + last_elements
        self.previous_elements = final_window[-overlaps:]
        return final_window

    def _sliding_window(self, size):
        """private_method should not be called directly"""
        win = []
        for e in range(0,size):
            win.append(next(self.cycle_iterable))
        return win


class SlidingWindow:
    """TODO:add doc"""

    def __init__(self,iterable_obj,seed=2021):
        self.cycle_iterable = cycle(iterable_obj)

    def sliding_window(self, size):
        win = []
        for e in range(0,size):
            win.append(next(self.cycle_iterable))
        return win

if __name__=="__main__":
    normal_sliding = SlidingWindow(list(range(1,10)))
    overlapping_sliding = SlidingWindowOverlap(list(range(1,20)))
    for _ in range(10):
        print(normal_sliding.sliding_window(3))
        print(overlapping_sliding.sliding_window_with_overlaps(8,overlaps=2))