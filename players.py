from string import digits
from random import choice


class Piece:
  def __init__(self, color, square):
    assert color in ['black', 'white']
    self.color = color
    self.square = square

  def moveTo(self, square):
    #if isinstance(self.piece, Pawn):
    #  print(self.square.name, "-", square.name)
    #else:
    print(self, self.square.name, "-", square.name)
    self.square.clear()
    self.square = square
    self.square.setPiece(self)

  def wakeUp(self):
    # Roll-call
    # print("The", self.color, type(self).__name__, "wakes up");
    # feel/listen: sense what squares are a no-go
    options = self.square.exploreRange(self)

    r = [o for o in options if o.piece and o.piece.color != self.color]
    if r:
      #print("value of self: " + str(self.value) + " (" + type(self).__name__ + ")")
      c = max(r, key=lambda s: s.piece.value)
      print("bid by " + type(self).__name__ + " on " + self.square.name + ": " + str(1 + c.piece.value / self.value))
      return [1 + c.piece.value / self.value, self, c]
    else:
      r = [o for o in options if not o.piece or o.piece.color != self.color]
      if r:
        return [1, self, choice(r)]
      else:
        return [0, self, None]


class King(Piece):
  def __init__(self, color, square):
    Piece.__init__(self, color, square)
    self.options = []
    self.value = 100

  def __str__(self):
    if self.color == 'white':
      return 'K'
    else:
      return 'k'

  def announcePresence(self):
    pass


class Queen(Piece):
  def __init__(self, color, square):
    Piece.__init__(self, color, square)
    self.value = 9

  def __str__(self):
    if self.color == 'white':
      return 'Q'
    else:
      return 'q'


class Knight(Piece):
  def __init__(self, color, square):
    Piece.__init__(self, color, square)
    self.value = 3

  def __str__(self):
    if self.color == 'white':
      return 'N'
    else:
      return 'n'


class Bishop(Piece):
  def __init__(self, color, square):
    Piece.__init__(self, color, square)
    self.value = 3

  def __str__(self):
    if self.color == 'white':
      return 'B'
    else:
      return 'b'

class Rook(Piece):
  def __init__(self, color, square):
    Piece.__init__(self, color, square)
    self.value = 5

  def __str__(self):
    if self.color == 'white':
      return 'R'
    else:
      return 'r'

class Pawn(Piece):
  def __init__(self, color, square):
    Piece.__init__(self, color, square)
    self.value = 1

  def __str__(self):
    if self.color == 'white':
      return 'P'
    else:
      return 'p'
