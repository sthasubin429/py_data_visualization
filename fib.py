from matplotlib import pyplot as plt
x = []
y = []
def fibonacci(num):

    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

def fib(n, computed={0: 0, 1: 1}):
    if n not in computed:
        computed[n] = fib(n - 1, computed) + fib(n - 2, computed)
    return computed[n]

for i in range(50):
    x.append(i)
    y.append(fib(i))
    #print("fib({}):{}".format(i,fib(i)))


plt.plot(x, y)
plt.xlabel('n term')
plt.ylabel('Fibanachi number')
plt.title('Fibanachi')
plt.show()
