def do_twice(f,x):
    f(x)
    f(x)

def print_spam(y):
    print(y)

do_twice(print_spam, 'spam')

def do_four(f,x):
    do_twice(f,x)
    do_twice(f,x)

do_four(print_spam, 'spam')