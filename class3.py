#12/5/26
#count
str1='java programming language java developer python developer'
print(str1.count('java'))
print(str1.count('python'))
print(str1.count('php'))
#is alpha
str1='a'
print(str1.isalpha())
str1='1234'
print(str1.isalpha())
#isupper
str1='A'
print(str1.isupper())
str1="a"
print(str1.isupper())
#islower
str1='A'
print(str1.islower())
str1="a"
print(str1.islower())
#isdigit
str1='11'
print(str1.isdigit())
str1="1123abc"
print(str1.isdigit())
#isnumeric
str1="V"                  #it is same like isdigit but it allows roman numbers ex:i.,ii.,iii.
print(str1.isnumeric())
str1="1"
print(str1.isnumeric())
#isalnum
str1='ABC123'
print(str1.isupper())
str1="123"
print(str1.isupper())
#isspace
str1=' '
print(str1.isspace())
str1='abc'
print(str1.isspace())
#isidentifier
str1='@#$%'
print(str1.isidentifier())
str1='class'
print(str1.isidentifier())
str1='12sai'
print(str1.isidentifier())
str1='sai rishi'
print(str1.isidentifier())
str1='sai_rishi'
print(str1.isidentifier())
#istitle
str1='sai rishi'
print(str1.istitle())
str1='Sai Rishi'
print(str1.istitle())
#strip
#it is the method used to remove the unwanted spaces in first and last of the given string
str1='     sai rishi    '
print(str1,len(str1))
print(str1.strip())
print(str1,len(str1.strip()))
#lstrip
str1='     sai rishi    '
print(str1,len(str1))
print(str1.lstrip())
print(str1,len(str1.lstrip()))
#rstrip
str1='     sai rishi    '
print(str1,len(str1))
print(str1.rstrip())
print(str1,len(str1.rstrip()))
#split
value='sai rishi 1234 !@#$%^'
print(value.split())
value='sai@rishi@1234@!$#$%^'
print(value.split('@'))
#splitlines
value='sai\nrishi\n1234\n!$#$%^'
print(value)

