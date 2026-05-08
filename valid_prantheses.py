class Solution:
    def isValid(self, s):
        stack = []
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:
            if ch in mapping:  # closing bracket
                top = stack.pop() if stack else '#'
                if mapping[ch] != top:
                    return False
            else:
                stack.append(ch)  # opening bracket

        return len(stack) == 0
    
if __name__ == "__main__":

    sol = Solution()

    s = "([])"   # 👈 change this input to test anything

    result = sol.isValid(s)

    print("Input:", s)

    print("Output:", result)
    
