# Sample Functions
# it is a good idea to create numerous useful functions and use them in
# your code as needed.  Create once, use many

def samplefunction():
    print ('this is a test')
samplefunction() # should result in printing 'this is a test'

nums = [2,4,6,8]
def square_numbers(nums): # can be a number or list of numbers
   result = [] # empty list
   for i in nums:
        result.append(i*i)
   return result
square = square_numbers(nums)   # set the variable square to the
                                #value(s) returned by the function
print (square)
