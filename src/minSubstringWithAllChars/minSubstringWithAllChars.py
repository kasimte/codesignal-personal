# https://app.codesignal.com/interview-practice/task/rFeSD5rNy9RxfLcqg

# You have two strings, s and t. The string t contains only unique
# elements. Find and return the minimum consecutive substring of s
# that contains all of the elements from t.

# It's guaranteed that the answer exists. If there are several
# answers, return the one which starts from the smallest index.

# Example

# For s = "adobecodebanc" and t = "abc", the output should be
# minSubstringWithAllChars(s, t) = "banc".

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] string s

# A string consisting only of lowercase English letters.

# Guaranteed constraints:
# 0 ≤ s.length ≤ 100.

# [input] string t

# A string consisting only of unique lowercase English letters.

# Guaranteed constraints:
# 0 ≤ t.length ≤ min(26, s.length).

# [output] string

def minSubstringWithAllChars(s, t):
    # approach:
    # * keep results array of all possible substrings
    # * iterate through to find all matches
    # * return shortest match

    if t == "":
        return ""

    results = []

    for i, _ in enumerate(s):
        char = s[i]
        if char in t:
            matches = set()
            for j in range(i, len(s)):
                if s[j] in t:
                    matches.add(s[j])
                    # If the length of the set is the length of t, then we have a possible result.
                    if len(matches) == len(t):
                        results.append(s[i:j + 1])

    # We now have an array of all substring matches, so return the one of minimum length.
    return min(results, key=len)

print(minSubstringWithAllChars("adobecodebanc", "abc")) # "banc"
print(minSubstringWithAllChars("tvdsxcqsnoeccaurocnk", "acqt")) # "tvdsxcqsnoecca"
print(minSubstringWithAllChars("", "")) # ""
print(minSubstringWithAllChars("xgajymplpvftjwjqomhbnutorgysaf", "j")) # "j"
