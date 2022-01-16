import copy
import random
# Consider using the modules imported above.
import collections

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for colour, num in balls.items():
            for ball in range(num):
                self.contents.append(str(colour))
    def draw(self, item_num):
#       Using min() as more elegant substitute of if construct
        item_num = min(item_num, len(self.contents))
#        if item_num > len(self.contents):
#            item_num = len(self.contents)
        drawn_list = []
        for item in range(item_num):
            picked_ball = random.sample(self.contents, 1)[0]
            self.contents.remove(picked_ball)
            drawn_list.append(picked_ball)
        return drawn_list
            
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_result = 0
    for experiment in range(num_experiments):
        trial_hat = copy.deepcopy(hat)
        result = collections.Counter(trial_hat.draw(num_balls_drawn))
        expected = collections.Counter(expected_balls)
        # If expected is in the result, taking result
        # away from expected will return nothing.
        # However, nothing is considered False, so
        # we needto negate that to produce True
        if not expected - result:
            expected_result += 1
    return expected_result/num_experiments

if __name__ == "__main__":
    my_hat = Hat(blue=4, red=2, purple=5, yellow=3)
    print(my_hat.contents)
#    print(sorted(my_hat.draw(4)))
#    print(sorted(my_hat.draw(10)))
    print(experiment(my_hat, {"blue": 2, "red": 1}, 6, 2))
