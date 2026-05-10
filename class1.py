#indexing
value="python programming"
print(value[4])
print(value[-1])
#Slicing 
#Form 1
#syntax[start:end]
print(value[:])
print(value[4:])
print(value[:8])
print(value[0:12])
print(value[-12:-1])
#Form 2
#syntax[start:end:step]
print(value[::])
print(value[::2])
print(value[::-1])#used to reverse the string
print(value[-1::])
print(value[-1:-17:])#it prints nothing because the start value should be less then end value
#Form 3
print(value[::0])#it throws error because the step should not be zero because if step is zero there is no next iterations
