class Room:
    def __init__(self, rect, node):
        self._rect = rect
        self._node = node

    # properties

    @property
    def center(self):
        return self._rect.center()

    @property
    def top_left(self):
        return self._rect.top_left

    @property
    def bottom_right(self):
        return self._rect.bottom_right
