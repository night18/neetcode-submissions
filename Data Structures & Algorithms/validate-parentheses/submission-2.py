class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque

        q = deque([])

        for c in s:
            if c in "{[(":
                q.append(c)
                continue

            if c in ")]}":
                if len(q) <= 0:
                    return False

                last = q.pop()
                

                if c == ")" and last != "(":
                    return False

                if c == "]" and last != "[":
                    return False

                if c == "}" and last != "{":
                    return False
            
        return len(q) == 0





