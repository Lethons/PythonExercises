def print_spam():
    print('spm')

def do_twice(f):
    f()
    f()

do_twice(print_spam)