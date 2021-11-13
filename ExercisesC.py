#Khushmeet Chandi
#Period 4
#Regular Expressions - Exercises C
import sys
idx = int(sys.argv[1])-50
myRegexLst = [r"/(\w)+\w*\1\w*/i",
            r"/(\w)+(\w*\1){3}\w*/i",
            r"/^((0|1)[01]*\2|1?|0)$/",
            r"/\b(?=\w*cat)\w{6}\b/i",
            r"/\b(?=\w*ing)(?=\w*bri)\w{5,9}\b/i",
            r"/\b((?!cat)\w){6}\b/i",
            r"/\b((\w)(?!\w*\2))+\b/i",
            r"/(?!.*10011)^[01]*$/",
            r"/\w*(([aeiou])(?!\2)){2}\w*/i",
            r"/(?!.*1.1)^[01]*$/"]
print(myRegexLst[idx])