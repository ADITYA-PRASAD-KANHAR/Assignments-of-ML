# 8. Write a function to return the Fibonacci sequence up to n terms.

def return_Fibonacci(term):
    fibonacci_series = [0,1]
    for i in range(2,term):
        fibonacci_series.append(fibonacci_series[i-1]+fibonacci_series[i-2])
    return fibonacci_series

print(return_Fibonacci(5))

    