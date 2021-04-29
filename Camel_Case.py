# Alice wrote a sequence of words in CamelCase as a string of letters, 's' , having the following properties:

# It is a concatenation of one or more words consisting of English letters.
# All letters in the first word are lowercase.
# For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.
# Given 's' , print the number of words in 's' on a new line.


def camelcase(s):
    caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    count = 1
    for i in range(len(s)):
        if s[i] in caps:
            count += 1
    return count


print(camelcase("saveChangesInTheEditor"))
print(camelcase("abCd"))
print(camelcase("ab"))

