
my_str = 'sweeteew'


my_str = my_str.casefold()


rev_str = reversed(my_str)

if list(my_str) == list(rev_str):
   print("It is palindrome")
else:
   print("It is not palindrome")