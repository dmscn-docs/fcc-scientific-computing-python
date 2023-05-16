import copy
import random


class Hat:
    def __init__(self, **args):
        self.contents = list()

        for hat in args:
            for _ in range(args[hat]):
                self.contents.append(hat)

    def draw(self, balls):
        if balls >= len(self.contents):
            return self.contents

        random_balls = random.sample(self.contents, balls)

        for ball in random_balls:
            self.contents.remove(ball)

        return random_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_successful_experiments = 0

    for experiment in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)
        success = True

        for ball, count in expected_balls.items():
            if balls_drawn.count(ball) < count:
                success = False
                break

        if success:
            num_successful_experiments += 1

    probability = num_successful_experiments / num_experiments

    return probability
