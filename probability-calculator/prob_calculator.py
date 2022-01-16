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
        item_num = min(item_num, len(self.contents))
#        if item_num > len(self.contents):
#            item_num = len(self.contents)
        print(item_num)
        drawn_list = []
        for item in range(0, item_num):
            picked_ball = random.sample(self.contents, 1)[0]
            self.contents.remove(picked_ball)
            drawn_list.append(picked_ball)
        return drawn_list
            
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_result = 0
    for experiment in range(0, num_experiments):
        trial_hat = copy.deepcopy(hat)
        result = trial_hat.draw(num_balls_drawn)
        colours = list(expected_balls.keys())
        print(result, colours)
    return expected_result/num_experiments

if __name__ == "__main__":
    my_hat = Hat(blue=4, red=2, purple=5, yellow=3)
    print(my_hat.contents)
#    print(sorted(my_hat.draw(4)))
#    print(sorted(my_hat.draw(10)))
    print(experiment(my_hat, {"blue": 2, "red": 1}, 6, 2))
