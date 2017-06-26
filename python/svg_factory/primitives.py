import os


class Circle:

    def __init__(self, cx, cy, r, fill, templates_dir):
        self.cx = cx
        self.cy = cy
        self.r = r
        self.fill = fill
        self.templates_dir = templates_dir

    def svg(self):
        tmp = self._read_circle_tmp()
        result = tmp.format(cx=self.cx, cy=self.cy, r=self.r, fill=self.fill)
        return result

    def _read_circle_tmp(self, filename='circle.svg'):
        path = os.path.join(self.templates_dir, filename)
        with open(path, 'r') as file:
            result = ''.join(file.readlines())
        return result
