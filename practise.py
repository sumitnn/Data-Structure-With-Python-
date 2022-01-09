# def twoSum(s):
# Write your code here.

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         # Write your code here.
#         string = ""
#         a, b = 0, 0
#         if s == "":
#             return 0
#         if s == " ":
#             return 1
#         for value in s:

#             if value not in string:

#                 string = string+value
#                 print(string)

#             else:
#                 a = len(string)
#                 a, b = b, a
#                 string = ""
#                 string = string+value

#         if a > b:
#             return a

#         return b
def twoSum(s):

    if s == "":
        return 0
    elif s[0] == " " and len(s) == 1:
        return 1
    string = ""
    a, b = 0, 0
    for i in range(0, len(s)):
        if s[i] not in string:
            string = string+s[i]
            a = len(string)
        else:
            a = len(string)
            b, a = a, b
            string = ""
            string = string+s[i]
    if a > b:
        return a
    return b


print(twoSum("pwwkew"))
