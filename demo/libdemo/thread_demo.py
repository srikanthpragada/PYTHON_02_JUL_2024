import threading
from threading import Thread


def print_numbers():
    for n in range(10):
        print(f"Print2 {n}")


class PrintTread(Thread):
    def run(self):
        for n in range(10):
            print(f"Print {n}")


print(threading.main_thread())
print(threading.active_count())

t = PrintTread()
t.start()

t2 = Thread(target=print_numbers)
t2.start()

for i in range(10):
    print(f"Main {i}")
