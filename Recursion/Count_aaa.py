# a. Write a recursive function which counts, the number of times “aaa”
# appears in the string. Print the value returned.

# b. Write a recursive function which counts, the number of times “aaa”
# appears in the string, but only such instances of “aaa” should be
# considered which do not overlap. Print the value returned.

# Example:
# Input:
# aaaaaa

# Output:
# 4
# 2

s = 'aaaaaa'
i = 0
count = 0
def Countaaa(s, alph='a'):

    

    cnt = Countaaa(s[i:i+3])
    count = count + cnt

    return count

cnt = Countaaa(s, i)
print(cnt)