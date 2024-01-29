def dunc():
    var = 1

    def f3():
        par = 2
        if 'var' not in locals():
            raise Exception
        print('var' in locals())

    f3()

    def f4():
        par = 3
        print(var)
        if 'var' not in locals():
            raise Exception

    f4()

    def f5():
        var = 4
        par = 4
        print(var)
        if 'var' not in globals():
            raise Exception

    f5()


dunc()