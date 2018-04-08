def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = "the Great " + magicians[i].title()
    return magicians


def show_magicians(magicians):
    for magician in magicians:
        print(magician)


magicians = ['leo', 'jack', 'mark', 'tom']
ret = make_great(magicians[:])
show_magicians(ret)
show_magicians(magicians)
