class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # last in first out
        # Stack

        cal = []
        result = None

        for token in tokens:
            if token in "+-*/":
                B = cal.pop()
                A = cal.pop()
                if token == "+":
                    cal.append(A+B)
                elif token == "-":
                    cal.append(A-B)
                elif token == "*":
                    cal.append(A*B)
                elif token == "/":
                    # Truncate to zero
                    if A * B < 0:
                        cal.append(-1 * (-A//B))
                    else:
                        cal.append(A//B)
            else:
                cal.append(int(token))

        return cal.pop()