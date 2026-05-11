#11/5/2026
#string concatenation
str1='sai '
str2='rishi'
str_new=str1+str2
print(str_new)
#string repetition
str1='python '
str2=5
str_new=str1*str2
print(str_new)
##string pre-defined methods
#upper
str1='python programming'
print(str1,str1.upper())
#lower
str1='PYTHON Programming'
print(str1,str1.lower())
#capitalize
str1='python programming'
print(str1,str1.capitalize())
#title
str1='python programming'
print(str1,str1.title())
#index
str1='python programming'
print(str1.index('p'))
print(str1.index('pro'))
print(str1.index('java'))  #it throws error besause java is not the sub string of the main 
#string.so,to over come this drae back we need to go to the concept find
