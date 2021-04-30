# Generators snippet
nums = [1,2,3,4,5,6,7,8,9,10] # simple list
def square_numbers(nums):
   for i in nums:
       yield (i*i)
# interate over a generator object
my_nums = square_numbers(nums)
for num in my_nums:
    
    print (num)

# Another way to create square numbers generator...
# looks much like a list comprehension
my_nums = ( x*x for x in [nums])
print (my_nums) # print statement will generate a generator object error
                # this is done intentionally to demonstrate that a generator
                # can't be directly printed.

# square function does the same as the generator code
# above but returns the results in a list
def square_numbers(nums):
   result = []
   for i in nums:
        result.append(i*i)
   return result
my_nums = square_numbers(nums)
print (my_nums)


