#Khushmeet Chandi
#Period 4
#Regular Expressions - Exercise B
import sys
idx = int(sys.argv[1])-40
myRegexLst = [r"/^[.xo]{64}$/i",
            r"/^[xo]*\.[xo]*$/i",
            r"/^(x+o*)?\.|\.(o*x+)?$/i",
            r"/^.(..)*$/s",
            r"/^(1?0|11)([01]{2})*$/",
            r"/\w*(a[eiou]|e[aiou]|i[aeou]|o[aeiu]|u[aeio])\w*/i",
            r"/^(1?0)*1*$/",
            r"/^[bc]*[abc][bc]*$/", #/^\b[bc]*a?[bc]*\b$/i   # might be wrong -- /(b|c|a[bc]*$)+$/
            r"/^(b|c|a[bc]*a)+$/", #a^([bc])*a|b|c)+$ -- same but just reversed 
            r"/^((1[02]*1|2)0*)+$/"
            ]
print(myRegexLst[idx])