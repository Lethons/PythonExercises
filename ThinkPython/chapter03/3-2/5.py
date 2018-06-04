def print_spam(s):
    print(s)

def do_four(f, s):
    for i in range(4):
        f(s)

do_four(print_spam, 'spam')