class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or  isinstance(capacity, bool) or capacity < 0:
            raise ValueError("Capacity must be a non negative integer")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size
       

    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError("Not enough room in jar for cookies")
        self._size += n

    def withdraw(self, n):
        if n > self._size:
            raise ValueError("Not enough cookies in jar")
        self._size -= n
       

    @property
    def capacity(self):
        return self._capacity
      

    @property
    def size(self):
        return self._size
    

jar = Jar()
jar.deposit(5)
print(jar)          # 🍪🍪🍪🍪🍪
print(jar.size)     # 5
print(jar.capacity) # 12
jar.withdraw(2)
print(jar)          # 🍪🍪🍪
print(jar.size)     # 3