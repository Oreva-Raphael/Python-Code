#This code uses the sort() method to sort the list of animals in descending order. 
#The reverse parameter is set to True to sort in descending order. 
#Finally, the print() function is used to display the sorted list of animals.

animals = ["dog", "cat", "elephant", "bee", "zebra", "fish", "dolphin"]
animals.sort(reverse=True)
print(animals)

#This code uses the sort() method to sort the list of animals in ascending order
# By default the sort() method sorts elements in ascending order, so no need to provide any additional parameters.
#Finally, the print() function is used to display the sorted list of animals, as well as a message "Animals in ascending order:" before the list.

animals = ["dog", "cat", "elephant", "bee", "zebra", "fish", "dolphin"]
animals.sort()
print('These are the animals in ascending order:')
print(animals)

