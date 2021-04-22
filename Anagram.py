# Two words are anagrams of one another if their letters can be rearranged to form the other word.
# In this challenge, you will be given a string. You must split it into two contiguous substrings, then determine the minimum number of characters to change to make the two substrings into anagrams of one another.
# For example, given the string 'abccde', you would break it into two parts: 'abc' and 'cde'. Note that all letters have been used, the substrings are contiguous and their lengths are equal. Now you can change 'a' and 'b' in the first substring to 'd' and 'e' to have 'dec' and 'cde' which are anagrams. Two changes were necessary.

def anagram(s):
    if len(s) % 2 != 0 :
        return -1
    s1 = s[:len(s) // 2]
    s2 = s[len(s) // 2 : ]
    return  sum([abs(s1.count(i) - s2.count(i)) for i in set(s1) if (s1.count(i) > s2.count(i) )])


# print(anagram("aaabbb"))
# print(anagram("xaxbbbxx"))
# print(anagram("fdhlvosfpafhalll"))
# print(anagram("mvdalvkiopaufl"))
