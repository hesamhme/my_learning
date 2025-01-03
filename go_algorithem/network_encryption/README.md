# The encryption rules are as follows:

## Letter Shifting and Emoticons
### Each letter or emoji in the message must be shifted forward in the alphabet by the remainder of dividing the Unicode value of that letter by 5.If the shift reaches the end of the alphabet or the range of emoticons, it continues to the beginning.
---
## Number Substitution
### Each number in the message must be replaced with its Unicode code and then multiplied by the length of the message itself.
## For example, if the number 3 is in the message and the length of the message before encryption is 10, the number 3 is replaced with its Unicode code (51) and then multiplied by 10, resulting in 510.
## The length of the message is the number of characters in it.
---
## Whitespace Conversion
### Each whitespace must be converted to the underscore _ by the number of characters in the word before it.
## For example, if there is a word with 5 letters before the space, that space will be converted to _____.
---
## Reversing the message
### The final message after applying all the above rules should be printed in reverse (except for numbers).
---
## Note: These apply to any message in the same way.
You need to write a program that takes a message as input, encrypts it according to the above rules, and prints the result.
---
# Note
### It is guaranteed that only uppercase and lowercase English letters, numbers, spaces, and emoticons are included in the expressions.
### First, you receive an integer n, which indicates the number of sentences you are going to receive from the input for encryption.
### On the next n lines of input, a sentence comes, which can contain uppercase and lowercase letters, numbers, and spaces.
---
## Output
### Print a string on each line of output that represents the final encrypted message.

# Example
## Sample Input 1
```
1
Hello World 123
```

## Sample Output 1
```
765750735_____dovpY_____poofJ
```
---

## Sample Input 2
```
4
cCT6gxy
pzZL7A2RJQiknB8BCEAz😁
OAtv wTVpq0HndG kHs1
l2JQAiGsu
```

## Sample Output 2
```
zxj378XEg
😄bAIEC1176CnmiRNT1050A1155MZbr
980sJm__________HdnJ960trWXa____yuAS
wsHiARN450o
```