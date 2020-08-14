# https://leetcode.com/problems/satisfiability-of-equality-equations/

# Given an array equations of strings that represent relationships 
# between variables, each string equations[i] has length 4 and 
# takes one of two different forms: "a==b" or "a!=b".  
# Here, a and b are lowercase letters (not necessarily different) 
# that represent one-letter variable names.
# Return true if and only if it is possible to assign integers to variable names so as to satisfy all the given equations.

class Solution:
    def equationsPossible(self, equations: [str]) -> bool:
        variables, possible = {}, {}
        arg_1_idx = 0
        arg_2_idx = 3

        # preprocess, see all variables
        for equation in equations:
            arg_1 = equation[arg_1_idx]
            arg_2 = equation[arg_2_idx]
            variables[arg_1] = True
            variables[arg_2] = True
            
        # assume everything is possible
        for variable in variables:
            possible[variable] = [x for x in variables if x != variable]
        
        return True

    # def comparison(equation: str) -> str:
    #     string_comparison = equation[1:3]
        