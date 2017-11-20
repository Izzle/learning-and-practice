# Exercise 61, 62
# eval and exec

list_str = '[5, 6, 7, 3, 77, 2]'

list_str = eval(list_str)

print(list_str)
print(list_str[2])

'''eval will compile your code and evalute a string expression.
   If you input "hi" into x in IDLE you just assign the value
   of the input and nothing else happens. If you input "hi" into
   check_this_out not only will it assign the value, but it will
   print the string into IDLE! You cannot evaluate a definition
   like x=5 but you can evalute an expression like 5 < 10 (True)

   Also, if you input a letter like 'd' in both, it will work for
   x but not in check_this_out (unless 'd' was already defined).

   Ex.
   >>>code: 500    # puts value into 'x'
   >>>code: x      # eval(x)
   500
'''
x = input('code:')

check_this_out = eval(input('code:'))
print(check_this_out)

'''exec will compile AND evalutes what you pass through it in string form!
   Its a compiler in a compiler! Python in Python! This is one of the most
   dangerous functions you can run on a VPS or Web Server - anything passing
   through dynamic data.


'''

exec("print('so this works like eval')")

list_str1 = '[5, 6, 7, 3, 77, 2]'
list_str1 = exec(list_str1)

print(list_str1)  # None. This is because its like the action: 'list_str = list_str'

# Although list_str2 is never defined in our code this works. It prints out!
# This is kind of hacky
exec("list_str2 = [5, 3, 2, 6, 8, 8, 7]")
print(list_str2)

exec("def test(): print('o sniiiip snapp!!!')")
test()


exec("""
def test2():
    print('lets see if multi-line works too.....')
    """)
test2()  # Works
