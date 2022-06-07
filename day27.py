# Given a string of round, curly, and square open and closing brackets, 
# return whether the brackets are balanced (well-formed).

# For example, given the string "([])[]({})", you should return true.

# Given the string "([)]" or "((()", you should return false.

# level: Easy

# Time O(n) | Space O(n)
def balancedBrackets(string):
    # Write your code here.
    opening_brackets = "({["
    closing_brackets = ")}]"
    matching_brackets = {")": "(", "}": "{", "]": "["}
    bracket_stack = []

    for char in string:
        if char in opening_brackets:
            bracket_stack.append(char)
        elif char in closing_brackets:
            if len(bracket_stack) == 0:
                return False
            if bracket_stack[-1] == matching_brackets[char]:
                bracket_stack.pop()
            else:
                return False
    return len(bracket_stack) == 0

print(balancedBrackets("([])[]({})"))
