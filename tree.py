class Tree():
    def __init__(self, variables, constraints):
        self.variables = variables
        self.constraints = constraints
        self.root = Node(self.variables, self.constraints, 0)


    def solve(self):
        return self.root.take_decision()


class Node():
    def __init__(self, variables, constraints, layer):
        self.variables = variables
        self.constraints = constraints
        self.layer = layer


    def _check_constraints(self):
        return all(c.is_satisfied() for c in self.constraints)


    def _is_solved(self):
        return all(v.is_assigned() for v in self.variables) and all(c.is_satisfied() for c in self.constraints)


    def take_decision(self):        
        if self.layer < len(self.variables) and self._check_constraints():
            for dom in self.variables[self.layer].domain:
                self.variables[self.layer].value = dom
                self.variables[self.layer].domain.remove(dom)
                next_node = Node(self.variables, self.constraints, self.layer+1)

                if next_node.take_decision():
                    return True
                
                else:
                    self.variables[self.layer].value = None
                    self.variables[self.layer].domain.insert(dom, dom)
            
            return False
                
        elif not self._check_constraints():
            return False
        
        elif self.layer == len(self.variables):
            return self._is_solved()