COUNT = 0

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

    
    def _get_degree(self):
        var = dict()

        for variable in self.variables:
            if variable.value == None:
                var[variable.name] = 0
                for constraint in self.constraints:
                    if variable in constraint.variables:
                        var[variable.name] += 1
                        
        return var


    def _find_variable_with_high_degree(self):
        var = self._get_degree()
        return max(var, key=var.get)

    
    def _find_variable_with_less_degree(self):
        var = self._get_degree()        
        return min(var, key=var.get)


    def take_decision(self):        
        global COUNT

        if self.layer < len(self.variables) and self._check_constraints():
            #first variable
            variable = self.variables[self.layer]

            #high degree
            # var = self._find_variable_with_high_degree()

            #less degree
            # var = self._find_variable_with_less_degree()

            # variable = None
            # for v in self.variables:
            #     if v.name == var:
            #         variable = v

            for dom in variable.domain:
                variable.value = dom
                variable.domain.remove(dom)
                COUNT += 1
                next_node = Node(self.variables, self.constraints, self.layer+1)

                if next_node.take_decision():
                    return True
                
                else:
                    variable.value = None
                    variable.domain.insert(dom, dom)
            
            return False
                
        elif not self._check_constraints():
            return False
        
        elif self.layer == len(self.variables):
            print("Node: {}".format(COUNT))
            return self._is_solved()