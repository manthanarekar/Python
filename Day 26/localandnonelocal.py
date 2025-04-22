a = 10


def outer():
    a = 5
    print("outer  a =", a)

    def done():
        a = 20

        def inner():
            nonlocal a
            a = 15
            print("inner a = ", a)

        inner()
        print("Done a = ", a)

    done()
    print("outside inner a = ", a)


outer()
print("Outside outer a =", a)
