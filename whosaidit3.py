"""
This program will input a string from the user and will see if the string is
written by Shakespeare or by Jane Austen, based on a short version of Hamlet
and Pride and Prejudice.
Foundation provided by Ms. Richardson
Edits done by Justin
Help provided by W3Schools
"""

import math
userString = str(input("Enter text: "))

# normalize
# -----
# This function takes a word and returns the same word
# with:
#   - All non-letters removed
#   - All letters converted to lowercase
def normalize(word):
    return "".join(letter for letter in word if letter.isalpha()).lower()

# getCounts
# -----
# This function takes a filename and generates a dictionary
# whose keys are the unique words in the file and whose
# values are the counts for those words.
def getCounts(filename):
    text = open(filename, "r")
    text = text.read()
    text = text.split()
    for i in range(len(text) - 1):
        text[i] = normalize(text[i])

    result_dict = {"_total": 0}
    for word in text:
        if word not in result_dict:
            result_dict[word] = 1
        elif word in result_dict:
            result_dict[word] += 1
        result_dict["_total"] += 1
    return result_dict

# Get the counts for the two shortened versions
# of the texts
shakespeareCounts = getCounts("hamlet-short.txt")
austenCounts = getCounts("pride-and-prejudice-short.txt")
del austenCounts[""]
austenCounts["_total"] -= 1

# getScore
# -----
# This function takes a word and a dictionary of
# word counts, and it generates a score that
# approximates the relevance of the word
# in the document from which the word counts
# were generated. The higher the score, the more
# relevant the word.
#
# In many cases, the score returned will be
# negative. Note that the "higher" of two
# negative scores is the one that is less
# negative, or the one that is closer to zero.
def getScore(word, counts):
    denominator = float(1 + counts["_total"])
    if word in counts:
        return math.log((1 + counts[word]) / denominator)
    else:
        return math.log(1 / denominator)

def predict(inputString, sCounts, aCounts):
    inputString = inputString.split()
    for i in range(len(inputString) - 1):
        inputString[i] = normalize(inputString[i])

    totalShakespeareScore = 0.0
    totalAustenScore = 0.0
    for i in range(len(inputString) - 1):
        shakespeareScore = getScore(inputString[i], sCounts)
        austenScore = getScore(inputString[i], aCounts)
        totalShakespeareScore += shakespeareScore
        totalAustenScore += austenScore

    if totalShakespeareScore > totalAustenScore:
        print("I think that was written by Shakespeare.")
    elif totalAustenScore > totalShakespeareScore:
        print("I think that was written by Jane Austen.")
    else:
        print("I think that could be written by either Shakespeare or Jane Austen.")

predict(userString, shakespeareCounts, austenCounts)
