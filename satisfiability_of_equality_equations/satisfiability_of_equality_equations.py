# # https://leetcode.com/problems/satisfiability-of-equality-equations/

# # Given an array equations of strings that represent relationships 
# # between variables, each string equations[i] has length 4 and 
# # takes one of two different forms: "a==b" or "a!=b".  
# # Here, a and b are lowercase letters (not necessarily different) 
# # that represent one-letter variable names.
# # Return true if and only if it is possible to assign integers to variable names so as to satisfy all the given equations.
class Solution(object):
    def equationsPossible(self, equations):
        arg1_idx = 0
        arg2_idx = 3
        equality_idx = 1

        graph = [[] for _ in range(26)]

        not_equations = []
        for eqn in equations:
            if eqn[equality_idx] == '=':
                arg1 = ord(eqn[arg1_idx]) - ord('a')
                arg2 = ord(eqn[arg2_idx]) - ord('a')
                graph[arg1].append(arg2)
                graph[arg2].append(arg1)
            else:
                not_equations.append(eqn)

        color = [None] * 26 # array of color assignments for each argument
        t = 0               # color value
        for var in range(26):
            if color[var] is None:
                t += 1
                stack = [var]
                while stack:
                    node = stack.pop()
                    for connected_node in graph[node]:
                        if color[connected_node] is None:
                            color[connected_node] = t
                            stack.append(connected_node)

        for eqn in not_equations:
            if eqn[1] == '!':
                arg1 = ord(eqn[arg1_idx]) - ord('a')
                arg2 = ord(eqn[arg2_idx]) - ord('a')
                if arg1 == arg2: return False
                if color[arg1] is not None and color[arg1] == color[arg2]:
                    return False
        return True