import turtle
PI = 3.14


def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360//n)


def circle(t, r):
    n = 36
    length = 2 * r * PI / n
    polygon(t, length, n)


if __name__ == '__main__':
    bob = turtle.Turtle()
    circle(bob, 100)
    
