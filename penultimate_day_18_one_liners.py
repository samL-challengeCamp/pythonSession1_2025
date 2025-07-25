
def three():
    print('Hello')
    
    print('This')
    
    if 3 < 0:
        print('THIS SHOULD NEVER PRINT')
    
    return 3

def four():
    print('Sigma')
    return 4

def no_return():
    print('This has no return')


print(no_return())

print([no_return(), no_return()])

[x := 5, print(x)]


# def my_function(x):
#     return x * 2

[my_function := lambda x: x * 2, print(my_function(4))]

x = 3
if x > 5:
    print(5)
else:
    print(0)

# [x := 3, print(5) if x > 5 else print(0)]

print(four() if x > 5 else three())

[random := __import__('random'), print(random.randint(1, 4))]
































