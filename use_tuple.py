# when make const, use tuple (more speedy than list)

# functions
def run():
    t = ('a', 'b', 'c')
    print('t :', t)

    print('len(t) :', len(t))

    print('t[1] :', t[1])

    print('t[0:2] :', t[0:2])

# implementation
if __name__ == '__main__':
    run()