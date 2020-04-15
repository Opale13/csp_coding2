class Tree():
    def __init__(self, variables, constraints):
        self.variables = variables
        self.constraints = constraints
        self.root = Node(dict(), self.variables, self.constraints, -1)

    def solve(self):
        self.root.take_decision()


class Node():
    def __init__(self, state, variables, constraints, layer):
        self.state = state
        self.variables = variables
        self.constraints = constraints
        self.layer = layer

        print("Layer {}".format(self.variables[self.layer+1].name))
        print("Domain {}".format(self.variables[self.layer+1].domain))


    def _check_constraints(self):
        return all(c.is_satisfied() for c in self.constraints)


    def take_decision(self):

        for dom in self.variables[self.layer+1].domain:
            self.variables[self.layer+1].value = dom
            self.variables[self.layer+1].domain.remove(dom)

            if self._check_constraints():
                print("For {}, {} work".format(self.variables[self.layer+1].name, self.variables[self.layer+1].value))
                Node(self.state, self.variables, self.constraints, self.layer+1).take_decision()
            
            else:
                print(print("For {}, {} does not work".format(self.variables[self.layer+1].name, self.variables[self.layer+1].value)))
                self.variables[self.layer+1].value = None
                self.variables[self.layer+1].domain.insert(dom, dom)