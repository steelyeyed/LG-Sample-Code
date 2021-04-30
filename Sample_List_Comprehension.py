# list comprehension example
# I want 'n' for each 'n' in nums
nums = [ 1,2,3,4,5,6,7,8,9,10] # simple list
my_list = [n for n in nums]
print (my_list)

# Using for loop to achieve the same results
My_list = []  # empty list
for n in nums:
   my_list.append(n)
print (my_list)
