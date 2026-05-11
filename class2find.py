#find
#this method is same as the index method but index method throws the error but user dont likes errors.
#so,the working of find is to show '-1' where there is error.with out showing it is error
str1='python programming'
print(str1.find('p'))
print(str1.find('pro'))
print(str1.find('java'))

#rindex
#this methods function is same as index but it checks the string from right to left side
#its checks from from right to left but the index positions doesn't change
str1='python programming'
print(str1.rindex("m"))

#rfind
#this methods function is same as index but it checks the string from right to left side
#its checks from from right to left but the index positions doesn't change
str1='python programming'
print(str1.rfind("p"))