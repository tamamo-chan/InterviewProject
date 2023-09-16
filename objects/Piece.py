class Piece:
    def __init__(self, id, color):
        self.id = id
        self.color = color

    # Required due to Piece being used as dict keys
    def __hash__(self):
        return hash((self.id, self.color))

    def __eq__(self, other):
        if hasattr(other, "id"):
            if hasattr(other, "color"):
                return self.id == other.id and self.color == other.color
        return False

    def __ne__(self, other):
        return not(self.__eq__(other))
