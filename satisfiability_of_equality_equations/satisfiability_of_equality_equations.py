# https://leetcode.com/problems/satisfiability-of-equality-equations/

# Given an array equations of strings that represent relationships 
# between variables, each string equations[i] has length 4 and 
# takes one of two different forms: "a==b" or "a!=b".  
# Here, a and b are lowercase letters (not necessarily different) 
# that represent one-letter variable names.
# Return true if and only if it is possible to assign integers to variable names so as to satisfy all the given equations.

class Solution:
    def equationsPossible(self, equations: [str]) -> bool:
        variables = {}

        arg_1_idx = 0
        arg_2_idx = 3
        for equation in equations:
            arg_1 = equation[arg_1_idx]
            arg_2 = equation[arg_2_idx]
            if (arg_1 not in variables.keys()):
                variables[arg_1] = []
            if (arg_2 not in variables.keys()):
                variables[arg_2] = []

        not_possible_equations = []
        for equation in equations:
            arg_1 = equation[arg_1_idx]
            arg_2 = equation[arg_2_idx]
            if equation[1:3] == '==':
                self.updateVariables(variables, arg_1, arg_2)
            else:
                not_possible_equations.append(equation)
        
        for equation in not_possible_equations:
            arg_1 = equation[arg_1_idx]
            arg_2 = equation[arg_2_idx]

            if arg_1 == arg_2:
                return False

            if (arg_2 in variables[arg_1]):
                return False
            
            if (arg_1 in variables[arg_2]):
                return False

        return True


    def updateVariables(self, variables: dict, arg_1: str, arg_2: str):
        if arg_1 == arg_2:
            return

        for i in variables[arg_1]:
            variables[i].append(arg_2)
            variables[arg_2].append(i)
        variables[arg_1].append(arg_2)

        for i in variables[arg_2]:
            variables[i].append(arg_1)
            variables[arg_1].append(i)
        variables[arg_2].append(arg_1)
