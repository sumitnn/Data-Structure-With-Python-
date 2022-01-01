# # Check for balanced parentheses in Python
# Input: {[]{()}}
# Output: Balanced

# Input: [{}{}(]
# Output: Unbalanced
stack = []

d = {
    '(': ')',
    '{': '}',
    '[': ']'
}


def check_balanced(x):
    for s in x:
        if s in d.keys():
            stack.append(s)

        else:
            if stack:
                a = stack[-1]
                if d[a] == s:
                    stack.pop()
                else:

                    return "not balanced"

            else:

                return "not balanced"

    return "not balanced " if stack else "Balanced"


x = '[{}{}(]'
l = check_balanced(x)
print(l)
