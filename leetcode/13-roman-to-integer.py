# ok solution

class Solution:
    def romanToInt(self, s: str) -> int:
        rome = {'M':1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        output = 0
        for i in range(0, len(s) - 1):
            if rome[s[i]] < rome[s[i+1]]:
                output -= rome[s[i]]
            else:
                output += rome[s[i]]
        output += rome[s[-1]]
        return output

# dumb solution (first)

class Solution:
    def romanToInt(self, s: str) -> int:
        x = s
        output = 0
        while len(x) > 0:
            if x[0] == 'M':
                output += 1000
                x = x[1:]
                continue
            if  x[0] == 'D':
                output += 500
                x = x[1:]
                continue
            if  x[0] == 'L':
                output += 50
                x = x[1:]
                continue
            if  x[0] == 'V':
                output += 5
                x = x[1:]
                continue
            if x[0] == 'C':
                if len(x) > 1:
                    if x[1] == 'M':
                        output += 900
                        x = x[2:]
                        continue
                    elif  x[1] == 'D':
                        output += 400
                        x = x[2:]
                        continue
                    else:
                        output += 100
                        x = x[1:]
                        continue
                else:
                    output += 100
                    x = x[1:]
                    continue
            if x[0] == 'X':
                if len(x) > 1:
                    if x[1] == 'L':
                        output += 40
                        x = x[2:]
                        continue
                    elif  x[1] == 'C':
                        output += 90
                        x = x[2:]
                        continue
                    else:
                        output += 10
                        x = x[1:]
                        continue
                else:
                    output += 10
                    x = x[1:]
                    continue
            if x[0] == 'I':
                if len(x) > 1:
                    if x[1] == 'V':
                        output += 4
                        x = x[2:]
                        continue
                    elif  x[1] == 'X':
                        output += 9
                        x = x[2:]
                        continue
                    else:
                        output += 1
                        x = x[1:]
                        continue
                else:
                    output += 1
                    x = x[1:]
                    continue
        return output
