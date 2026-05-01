class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        ops = {
            "+": (lambda x,y : x+y),
            "-": (lambda x,y : x-y),
            "*": (lambda x,y : x*y),
            "/": (lambda x,y : int(x/y)),
        }

        for t in tokens:
            if t in "+-*/":
                op = ops[t](stack[-2], stack[-1])
                stack.pop()
                stack.pop()
                stack.append(op)
            else:
                stack.append(int(t))
            print("t: ", t, "stack: ", stack)
        return stack[0]