import time

start = time.time()
print(f'Start time:  {start}')


def countdown(n):
    if n == 0:
        print("BOOM!")
    else:
        print(n)
        countdown(n - 1)

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
#time.sleep(1)
end = time.time()
print(f'Elapsed: {end - start} seconds')