#A collection of items without duplicates
#Sets are contained in {} curly braces.
nums = [1,1,1,2,2,2,3,3,3,4,4,5,6,7,8,9,10]
my_set = { n for n in nums}
print (my_set)

#Sets using for loop
my_set = set()
for n in nums:
     my_set.add(n)
print (my_set) # all duplicates removed
print (nums)
