def stdin_generator():
    while True:
        yield input()


def f():
    for x in stdin_generator():
        print(x)
        if(x == 'q'): return

f()