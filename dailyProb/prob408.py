# Given a non-empty string s and an abbreviation abbr, return whether the string matches with the given abbreviation.

# A string such as "word" contains only the following valid abbreviations:

# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
# Notice that only the above abbreviations are valid abbreviations of the string "word". Any other string is not a valid abbreviation of "word".

# Note:
# Assume s contains only lowercase letters and abbr contains only lowercase letters and digits.

# Example 1:
# Given s = "internationalization", abbr = "i12iz4n":

# Return true.
# Example 2:
# Given s = "apple", abbr = "a2e":

# Return false.

class Solution:
    """
    @param word: a non-empty string
    @param abbr: an abbreviation
    @return: true if string matches with the given abbr or false
    """
    def validWordAbbreviation(self, word, abbr):
        # write your code here
        i, j =0, 0
        while i < len(word) and j < len(abbr):
            if abbr[j].isalpha() and word[i] == abbr[j]:
                j += 1 
                i += 1 
            elif abbr[j].isdigit() and abbr[j] != '0':
                start = j 
                while start< len(abbr) and abbr[start].isdigit():
                    start += 1
                i += int(abbr[j:start])
                j = start
            else:
                return False
        return i == len(word)  
