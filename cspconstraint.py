# cspconstraint.py
# Author: Sébastien Combéfis
# Version: April 12, 2020

from cspmodel import Constraint

class Diff(Constraint):
    '''Class representing a binary diff constraint between two variables.'''

    def __init__(self, a, b):
        super().__init__([a, b])

    def is_satisfied(self):
        if any(not v.is_assigned() for v in self.variables):
            return True
        return self.variables[0].value != self.variables[1].value

    def __repr__(self):
        return '{} ≠ {}'.format(*(self.variables[i].name for i in range(2)))


class AllDiff(Constraint):
    '''Class representing an alldiff constraint between a set of variables.'''

    def __init__(self, variables):
        super().__init__(variables)

    def is_satisfied(self):
        variables = self.variables.copy()
        diff_constraints = list()
        for variable in self.variables:
            for v in variables:
                if variable != v:
                    diff_constraints.append(Diff(variable, v))
            
            variables.remove(variable)
                    
        return all(c.is_satisfied() for c in diff_constraints)


    def __repr__(self):
        return 'AllDiff({})'.format([v.name for v in self.variables])


class LinEq(Constraint):
    '''Class representing a linear equation constraint between a set of variables with given coefficients.'''

    def __init__(self, variables, coeff):
        super().__init__(variables)
        self.coeff = coeff

    def is_satisfied(self):
        if any(not v.is_assigned() for v in self.variables):
            return True
        result = 0
        for coeff, variable in zip(self.coeff, self.variables):
            result += coeff * variable.value
        return result == self.coeff[-1]

    def __repr__(self):
        lhs = ''.join(['{}{}{}'.format(('+' if x[0] > 0 else ''), (x[0] if x[0] != 1 else ''), x[1].name) for x in zip(self.coeff, self.variables)])
        if lhs[0] == '+':
            lhs = lhs[1:]
        return '{}={}'.format(lhs, self.coeff[-1])