"""
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000"""



s = "MCMXCIV"
romansDict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
number = 0
romanSplit = [s.split()]
for i in range(len(s)):
    number += romansDict[s[i]]
print(number)
