def foo(func, par):
    return func(par)

x = foo(func=lambda x:x*2, par=5)
print(x)