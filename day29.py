c = 1                       # start the count at 1
next = s[0]                 # set the first string to the first letter
for i in range(1, len(s)):  # repeat for all the letters after the first
    if next == s[i]:        # if it's the same letter
        c += 1              # increase the count
    else:                   # if it is a different letter
        print(c, next, sep='', end='')   # print the current count and letter
        c=1                 # restart the count
        next = s[i]         # at this new letter

print(c, next, sep='')  # print the details of the final letter
