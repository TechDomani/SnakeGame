import random

class Food:
    def __init__(self, width, height, snakeSize):
       self.width = width
       self.height = height
       self.snakeSize = snakeSize
       self.updateFoodLocation()

    def updateFoodLocation(self):
        self.x = round(random.randrange(self.snakeSize, self.width - self.snakeSize*2) / self.snakeSize) * self.snakeSize
        self.y = round(random.randrange(self.snakeSize, self.height - self.snakeSize*2) /  self.snakeSize) * self.snakeSize