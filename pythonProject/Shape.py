class Shape:
    size = 0
    shape_type = ""

    # shape_number in range(0,8)
    def __init__(self, shape_number):
        if shape_number == 0:
            self.size = 1
            self.shape_type = "o"
        elif shape_number == 1:
            self.size = 4
            self.shape_type = "O"
        elif shape_number == 2:
            self.size = 2
            self.shape_type = "i"
        elif shape_number == 3:
            self.size = 4
            self.shape_type = "l"
        elif shape_number == 4:
            self.size = 4
            self.shape_type = "S"
        elif shape_number == 5:
            self.size = 5
            self.shape_type = "L"
        elif shape_number == 6:
            self.size = 4
            self.shape_type = "I"
        elif shape_number == 7:
            self.size = 4
            self.shape_type = "T"
        elif shape_number == 8:
            self.size = 4
            self.shape_type = "J"
        elif shape_number == 9:
            self.size = 4
            self.shape_type = "Z"
        elif shape_number == 10:
            self.size = 2
            self.shape_type = "-"

    def get_shape_type(self):
        return self.shape_type
