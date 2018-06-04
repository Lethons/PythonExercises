def do_twice(f, s):
    f(s)
    f(s)

def print_twice(bruce):
    print(bruce)
    print(bruce)

do_twice(print_twice, 'spam')