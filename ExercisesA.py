#Khushmeet Chandi
#Period 4
#Regular Expressions - Exercise A
import sys
idx = int(sys.argv[1])-30
myRegexLst = [r"/^0$|^10[01]$/",
            r"/^[01]*$/",
            r"/0$/",
            r"/\w*[aeiou]\w*[aeiou]\w*/i",
            r"/^0$|^1[01]*0$/",
            r"/^[01]*110[01]*$/",
            r"/^.{2,4}$/s", #/^...?.?$/s
            r"/^\d{3} *-? *\d\d *-? *\d{4}$/",
            r"/^.*?d\w*/mi",
            r"/^1[01]*1$|^0[01]*0$|^[01]?$/"]
print(myRegexLst[idx])