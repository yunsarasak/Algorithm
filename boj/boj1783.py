
# | 000X0
# | 0000X
# N 00X00
# | 0000X
# | 000X0
#   --M--

hight, width = list(map(int, input().split()))

move_count = 1

class Position:
    global width
    global hight
    
    def __init__(self):
        self.col = 0
        self.row = 0
        self.end_of_col = False

    def CanGoToRight(self):
        if self.col + 1 <= width:
            return True
        else:
            return False

    def CanGoToNextToRight(self):
        if self.col + 2 <= width:
            return True
        else:
            return False

    def CanGoToDown(self):
        if self.row - 1 >= 0:
            return True
        else:
            return False

    def CanGoToDownDown(self):
        if self.row - 2 >= 0:
            return True
        else:
            return False

    def CanGoToUp(self):
        if self.row + 1 <= width:
            return True
        else:
            return False

    def CanGoToUpUp(self):
        if self.row + 2 <= width:
            return True
        else:
            return False
    
    def MoveUpUp(self):
        if self.CanGoToUpUp() and self.CanGoToRight():
            self.row += 2
            self.col += 1
            self.CanMove = not self.CanGoToRight()
            return True
        else:
            return False

    def MoveUp(self):
        if self.CanGoToUp() and self.CanGoToNextToRight():
            self.row += 1
            self.col += 2
            self.CanMove = not self.CanGoToRight()
            return True
        else:
            return False

    def MoveDownDown(self):
        if self.CanGoToDownDown() and self.CanGoToRight():
            self.row -= 2
            self.col += 1
            self.CanMove = not self.CanGoToRight()
            return True
        else:
            return False

    def MoveDown(self):
        if self.CanGoToDown() and self.CanGoToNextToRight():
            self.row -= 1
            self.col += 2
            self.CanMove = not self.CanGoToRight()
            return True
        else:
            return False

    # def __repr__(self):
    #     print("(%d, %d)"%(self.row, self.col))

    def __str__(self):
        return ("(%d, %d)"%(self.row, self.col))

    def CanMove(self):
        return not self.end_of_col

# 1 whole move
#       width : 6
#       hight : 3

position_of_night = Position()
print(position_of_night)

# if hight is more than 3 and width is more than 6
# 



