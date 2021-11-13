#Khushmeet Chandi
#Period 4
#Regular Expressions - Exercise 4
import sys
idx = int(sys.argv[1])-60
myRegexLst = [r"/^((?!010)0|1)*$/", #passed -- 15 chars
            r"/^(?!.*(010|101))[01]*$/", #passed -- 22 chars
            r"/^(?=(0|1)+$)\1.*/i", #passed -- 16 chars
            r"/\b(?=(\w)+)(?!\w*\1\w)\w+/i", #passed -- 25 chars
            r"/(?=(\w)+\w*\1)\w*((\w*\1){4}|(?!\1)(\w)\w*\4)\w*/i", #passed -- 48 chars
            r"/\b(?=(\w)+(\w*\1){2})(\1|(\w)(?!\w*\4))+\b/i", #passed -- perfect!
            r"/\b(((?![aeiou])\w)*([aeiou])(?!\w*\3)){5}\w*/", #passed -- 44 chars -- 3 extra chars
            r"/^((?=1*(01*01*)*01*$)(0|10*1)*|11)+$/", #passed -- 36 chars
            r"/^(0|(1(01*0)*10*)+)$/", #passed -- 20 chars
            r"/^(?!(0|1(01*0)*1)+$)[01]+$/" #passed
            ]
print(myRegexLst[idx])