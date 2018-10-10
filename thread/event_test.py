from multiprocessing import Event

e = Event()

print(e.is_set())

e.set()

e.wait(3)
print("wait...")

e.clear()

e.wait(3)

print("wait...")
