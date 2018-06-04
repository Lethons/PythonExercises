def print_spam(s):
    print(s)

def do_twice(f, s):
    f(s)
    f(s)

s = 'spm'
do_twice(print_spam, s)