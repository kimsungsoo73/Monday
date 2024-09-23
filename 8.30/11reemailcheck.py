import re

def checkmail(email):
    pass

# re.findall('^시작 .[a-z]{2:} $끝' )

checkmail('kim@gmail') # .org, .com여부
checkmail('kim_gmail.net') # @포함여부
checkmail('kim')
checkmail('kim@gmail.net') #올바른 이메일

