#!/usr/bin/env python3
"""
Tester for Unweighted Die Problem
"""

import random


def die_tester(count):
    """Roll the Provided Die and Calculate the distribution of results

    Decorator Usage: @die_tester(80)
    """

    def wrap(func):
        def wrapped_f(*args):

            aggregate = {}

            for _ in range(count):
                res = func(*args)
                if res in aggregate.keys():
                    aggregate[res] += 1
                else:
                    aggregate[res] = 1

            for key, total in aggregate.items():
                print(key, total)

        return wrapped_f
    return wrap


@die_tester(10000)
def roll_unweighted_die(weights=None):
    """Returns the result of an unweighted die.

    This uses a fair

    Args:
        weights: (integer array) a collection of the percentage chances each
                 result of the die has. The number of sides is determined by
                 the number of provided weights, and the sum of the weights
                 must be 1.0 (100%)

    Raises:
        ValueError: Provided weights did not add up to 1 (100%)
    """
    if weights is None or sum(weights) != 1:
        raise ValueError('Weight (%s) do not add to 1.0' % (weights))

    # Roll the die
    fair_roll = random.random()

    # Which range did the selected value fall into?
    res = 0
    for weight in weights:
        res = res + 1
        if fair_roll <= weight:
            return res

        # If weights are [0.3, 0.2, 0.5], and 0.45 is rolled, removing the
        # weight from the roll allows us to compare it to that section the
        # range, compared to the previous possible values
        fair_roll -= weight

    # This can happen because of floating point inaccuracies. Just use the
    # last value if we leave the loop
    return res


def generate_unweighted_die(sides):
    """Returns a randomly generated 'unweighted die'

    Returns be an array of randomly-generated floating-point values, that
    total up to 1.0. The array will contain a number of values equal to sides

    Args:
        sides: How many sides the unweighted-die will have

    Raises:
        ValueError: Invalid number of sides provided. At least 2 must be provided

    TODO: Current approach biases the front, pick a better distribution method
    """
    if sides < 2:
        raise ValueError('Array cannot have %s sides' % (sides))

    res = []

    remaining = 1.0
    for _ in range(sides-1):
        chunk = remaining * random.random()
        res.append(chunk)
        remaining -= chunk

    res.append(1.0 - sum(res))
    return res


def main():
    sides = 5
    chances = generate_unweighted_die(sides)

    print('Range: %s' % (chances))

    roll_unweighted_die(chances)


if __name__ == '__main__':
    main()
