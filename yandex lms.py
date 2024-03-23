class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def intersection(self, rect2):
        x1_2 = rect2.x
        x2_2 = rect2.x + rect2.w
        x2 = self.x + self.w
        y1_2 = rect2.y
        y2_2 = rect2.y + rect2.h
        y2 = self.y + self.h
        if min(x2_2, x2) > max(x1_2, self.x) and min(y2_2, y2) > max(self.y, y1_2):
            x = max(x1_2, self.x)
            y = max(self.y, y1_2)
            w = min(x2_2, x2) - x
            h = min(y2_2, y2) - y
            return Rectangle(x, y, w, h)
        return None

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_h(self):
        return self.h

    def get_w(self):
        return self.w

rect1 = Rectangle(3, 5, 2, 1)
rect2 = Rectangle(1, 2, 10, 10)
rect3 = rect1.intersection(rect2)

if rect3 is None:
    print('No intersection')
else:
    print(rect3.get_x(), rect3.get_y(), rect3.get_w(), rect3.get_h())
    
        
