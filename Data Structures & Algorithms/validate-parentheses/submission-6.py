class Solution:
    def isValid(self, s: str) -> bool:
        par_dct = {
            ')':'(',
            ']':'[',
            '}':'{'
            }
        par_stk = []
        for item in s:
            print(item)
            # check if item is closing parantheses
            if item in par_dct:
                # if item's opposite opening matches last item in the stack
                if par_stk and par_stk[-1] == par_dct[item]:
                    # pop it
                    par_stk.pop()
                # return false if stack empty or item's don't align
                else:
                    return False
            # if it's opening parantheses
            else:
                # add it to the stack
                par_stk.append(item)

        return len(par_stk) == 0


# Solution1: use a stack to opening parentheses,
# when the right opposing closing parentheses is met, pop the opening parenthese out
# if the stack is empty at the end return true
# use a dictionary to match closing and opening parantheses in pairs
# key => closing , value => opening