# https://leetcode.com/problems/satisfiability-of-equality-equations/

# Given an array equations of strings that represent relationships 
# between variables, each string equations[i] has length 4 and 
# takes one of two different forms: "a==b" or "a!=b".  
# Here, a and b are lowercase letters (not necessarily different) 
# that represent one-letter variable names.
# Return true if and only if it is possible to assign integers to variable names so as to satisfy all the given equations.

class Solution:
    def equationsPossible(self, equations: [str]) -> bool:
        not_possible_equations = []
        hashmap = {}

        arg_1_idx = 0
        arg_2_idx = 3

        for equation in equations:
            arg_1 = equation[arg_1_idx]
            arg_2 = equation[arg_2_idx]
            if equation[1:3] == '==':
                # if (arg_1 in hashmap.keys() and arg_2 not in hashmap[arg_1]):
                #     hashmap[arg_1].append(arg_2)
                # else:
                #     hashmap[arg_1] = [arg_2]
                # if (arg_2 in hashmap.keys() and arg_1 not in hashmap[arg_2]):
                #     hashmap[arg_2].append(arg_1)
                # else:
                #     hashmap[arg_2] = [arg_1]
            else:
                not_possible_equations.append(equation)
        
        for equation in not_possible_equations:
            arg_1 = equation[arg_1_idx]
            arg_2 = equation[arg_2_idx]

            if (arg_1 in hashmap.keys() and arg_2 in hashmap[arg_1]):
                return False
            
            if (arg_2 in hashmap.keys() and arg_1 in hashmap[arg_2]):
                return False

        return True