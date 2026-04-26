class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        # Pushing to stack
        for ch in s:
            n = len(stack)
            print("stack is: ",stack)
            print("char", ch)
            
            
            if n >= 1:
                stack_head = stack[n-1]
                print("stack head", stack_head)
                if stack_head == "{" and ch == "}":
                    print("{}")
                    stack.pop()
                elif stack_head == "[" and ch == "]":
                    print("[]")
                    stack.pop()
                elif stack_head == "(" and ch == ")":
                    print("()")
                    stack.pop()
                else:
                    stack.append(ch)
            else:
                stack.append(ch)
        return len(stack) == 0
            