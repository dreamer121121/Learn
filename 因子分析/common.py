import numpy


class Math:
    def __init__(self, vec1, vec2):
        self.vec1 = vec1
        self.vec2 = vec2

    def distance(self):
        dist = numpy.sqrt(numpy.sum(numpy.square(self.vec1 - self.vec2)))
        return dist
