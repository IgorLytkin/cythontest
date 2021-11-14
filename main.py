# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# import run_python
# import run_cython
# import time

def test(x):
    y = 1
    for i in range(1, x+1):
        y *= i
    return y

cpdef int test(int x):
    cdef int y = 1
    cdef int i
    for i in range(1, x+1):
        y *= i
    return y


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def approximate_pi(n):
   step = 1.0 / n
   result = 0
   for i in range(n):
   		x = (i + 0.5) * step
   		result += 4.0 / (1.0 + x * x)
   return step * result

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


number = 10

start = time.time()
run_python.test(number)
end =  time.time()

py_time = end - start
print("Python time = {}".format(py_time))

start = time.time()
run_cython.test(number)
end =  time.time()

cy_time = end - start
print("Cython time = {}".format(cy_time))

print("Speedup = {}".format(py_time / cy_time))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
