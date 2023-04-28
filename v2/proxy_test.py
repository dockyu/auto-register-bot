from fp.fp import FreeProxy

proxy = FreeProxy(https=True).get()

print(type(proxy))
print(proxy)