
class Empty:
    def __init__(self, solid_symbol):
        self._solid_symbol = solid_symbol

    # public methods

    def generate(self, num_rows, num_columns):
        level = []
        for row in range(0, num_rows):
            level.append([])

            for _column in range(0, num_columns):
                level[row].append(self._solid_symbol)

        return level
