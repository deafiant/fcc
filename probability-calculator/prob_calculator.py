import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for colour, num in balls.items():
            for ball in range(0, num):
                self.contents.append(str(colour))
    def draw(self, item_num):
# Using min() as substitute for if construct
        min(item_num, len(self.contents))
#        if item_num > len(self.contents):
#            item_num = len(self.contents)
        drawn_list = []
        for item in range(0, item_num):
            picked_ball = random.sample(self.contents, 1)[0]
            self.contents.remove(picked_ball)
            drawn_list.append(picked_ball)
        return drawn_list
            
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass

if __name__ == "__main__":
    my_hat = Hat(blue=4, red=2, purple=5, yellow=3)
    print(my_hat.contents)
    print(sorted(my_hat.draw(4)))
    print(sorted(my_hat.draw(10)))
