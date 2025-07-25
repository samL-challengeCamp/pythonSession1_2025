# import libraryname
import random

print(random.randint(3, 6))
print(random.randint(4, 700))

print(random.random())

my_campers = ['ben', 'william', 'max', 'jeffrey']

print(my_campers[random.randint(0, 3)])

print(random.choice(my_campers))


import time

# time.sleep(10)

print('10 seconds passed!')

print(time.time())


start = time.time()
for i in range(100000):
    print(i)
end = time.time()

print(end - start)

import webbrowser

webbrowser.open("https://google.com")

import selenium.webdriver

selenium.webdriver.Firefox().get("firefox:history")










