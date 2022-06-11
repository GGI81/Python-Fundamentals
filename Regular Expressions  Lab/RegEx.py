"""

A regular expression or regex is a sequence of characters that
define a search pattern

Usually, such patterns are used by string searching algorithms for
"find" or "find and replace" operations on strings

Regular expressions are used in search engines search and replace dialogs
of word processors and text editors etc

"""

# IMPORT RE

# SYNTAX
# \d -> Find everything which is a number||| \d+ takes whole numbers
# \D -> Finds everything which is NOT a number||| \D+ takes whole strings between numbers
# \b -> Returns a match where the specified characters are at the beginning
# or at the end of a word
# \s -> Returns a match where the string contains a white space character
# \S -> Returns a match where the string DOES NOT contain a white space character
# \w -> !!! Returns a match where the string contains any word characters
# (characters from a to Z, digits from 0 - 9, and the underscore _ character
# \W -> Returns a match where the string DOES NOT contain any word character

# METACHARACTERS
# \ -> Signals a special sequence (can also be used to escape special characters)
# . -> Any character (except newline character)
# + -> One or more occurrences
# * -> Zero or more occurrences  Ex. 1*[0-9]
# | -> Either or                 Ex. a|x  (match "a" or "x")
# () -> Capture and group
# {} -> Exactly the specified number of occurrences
# ^ -> Starts with (the line)
# $ -> Ends with (the line)

# SETS
# [arn] -> Returns a match where one of the specified characters (a, r, or n)
# are present
# [a-n] -> Returns a match for any lower-case character, alphabetically between a and n
# [^arn] -> Returns a match for any charachter EXCEPT a, r and n
# [1023] -> Returns a match where any of the specified digits (0, 1, 2, or 3)
# [0-9] -> Returns a match for any digit between 0 and 9
# [0-5][0-9] -> Returns a match for any two-digit numbers from 00 and 59
# [a-zA-Z] -> Returns a match for any character ALPHABETICALLY between
# a and z lower cas OR upper case

# !!!
# re.finditer() -> iter<match> -> [match1, match2, match3, ...] -> match.group, ....
# re.findall() -> iter<str> -> [substr1, substr2, substr3, ...] -> string
