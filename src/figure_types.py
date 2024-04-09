from primitives import *
import globals


class AbstractFigure:

    label = ""
    color = ""

    def set_label(self, label):
        self.label = label


class PointGraph(AbstractFigure):
    def __init__(self, vecs=[]):
        self.vecs = vecs
        self.sz = len(vecs)
        if vecs != []:
            self.maxx = max(vec.x for vec in vecs)
            self.maxy = max(vec.y for vec in vecs)
            self.minx = min(vec.x for vec in vecs)
            self.miny = min(vec.y for vec in vecs)

    def build_from_xy(self, array_x, array_y):
        vecs = []
        for i in range(len(array_x)):
            vecs.append(Vec2d(array_x[i], array_y[i]))
        self.__init__(vecs)

    def approximate(self):  # todo
        """Finds the best function to fit this set of points"""

        pass

    def __str__(self):
        return "\n".join([str(vec) for vec in self.vecs])


class FuncGraph(AbstractFigure):
    def __init__(self, func, label):
        self.func = func
        self.label = label
        self.vecs = []

    def build(  # Calculate values of function in some points
        self,
        minx,
        maxx,
        miny,
        maxy,
        sz,
    ):

        self.vecs = []

        step = (maxx - minx) / sz
        array_x = []
        cur_x = minx
        while cur_x < maxx:
            try:
                cur_y = self.func(cur_x, globals.global_kwargs)

                if miny <= cur_y and maxy >= cur_y:  # todo: fix this
                    pass
                self.vecs.append(Vec2d(cur_x, cur_y))
            except:
                pass
            cur_x += step

        self.sz = len(self.vecs)

    def __str__(self):
        return "\n".join([str(vec) for vec in self.vecs])


class Histogram(AbstractFigure):
    def __init__(self, columns, style):
        self.columns = columns
        self.style = style

    def build_from_csv(self, path):  # todo
        pass
