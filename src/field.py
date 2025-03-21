import logging

logger = logging.getLogger(__name__)

class Field:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def is_within_bounds(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return True
        else:
            return False
