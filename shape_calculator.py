class Rectangle:

    def __init__(self, width, height, side=0):
        self.width = width
        self.height = height
        self.side = side

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        if self.side != 0:
            self.width = width
            self.height = width
            self.side = width
        else:
            self.width = width

    def set_height(self, height):
        if self.side != 0:
            self.width = height
            self.height = height
            self.side = height
        else:
            self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        return (((self.width ** 2)+(self.height ** 2)) ** 0.5)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        pic, line = "", "*" * self.width
        for i in range(self.height):
            if i != self.height:
                pic += line + "\n"
            else:
                pic += line
        return pic

    def get_amount_inside(self, shape):
        sh = shape.get_area()
        act_sh = self.get_area()
        rt = 0
        while True:
            act_sh -= sh
            if act_sh < 0:
                break
            rt += 1
        return rt



class Square(Rectangle):
    
    def __init__(self, side):
        width, height = side, side
        Rectangle.__init__(self, width, height, side)

    def __str__(self):
        return f"Square(side={self.side})"

    def set_side(self, side):
        self.side = side 
        self.set_width(side)
