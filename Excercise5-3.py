def is_triangle(a,b,c):
    if (a + b > c) or (a + c > b) or (b + c > a):
        print ('Yes')
    else:
        print('No')

is_triangle(1, 2, 3)
is_triangle(10, 20, 100)