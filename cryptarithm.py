
# cryptarithm.py
# Author: Sébastien Combéfis
# Version: April 12, 2020

from cspmodel import Problem, Variable
from cspconstraint import AllDiff, LinEq

DIGITS = [x for x in range(10)]

class Cryptarithm(Problem):
    def __init__(self):
        letters = [Variable(c, DIGITS) for c in 'TWOFUR']
        reports = [Variable('X' + str(i + 1), [0, 1]) for i in range(3)]
        constraints = [
            AllDiff(letters),
            LinEq([letters[2], letters[5], reports[0]], [2, -1, -10, 0]),
            LinEq([reports[0], letters[1], letters[4], reports[1]], [1, 2, -1, -10, 0]),
            LinEq([reports[1], letters[0], letters[2], reports[2]], [1, 2, -1, -10, 0]),
            LinEq([reports[2], letters[3]], [1, -1, 0])
        ]
        super().__init__('Cryptarithm', letters + reports, constraints)

c = Cryptarithm()
print(c)
print(c.solve())