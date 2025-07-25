remove_yellow_line = [cache := dict(), fib := lambda n: [cache.update({n: n if n < 2 else (fib(n - 1) + fib(n - 2))}) if n not in cache else None, cache[n]][-1], [print(f'{x}: {fib(x)}') for x in range(20)]]




'''
Readable version:

remove_yellow_line = [
    cache := dict(),
    fib := lambda n: [
        cache.update({n: n if n < 2 else (fib(n - 1) + fib(n - 2))}) if n not in cache else None,
        cache[n]
    ][-1],
    [print(f'{x}: {fib(x)}') for x in range(20)]
]
'''