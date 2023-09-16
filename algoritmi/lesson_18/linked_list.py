
# Связанный список
class LinkedList:
    def __init__(self):
        self._begin = None

    def pop(self):
        assert self._begin is not None, "list is empty"
        value = self._begin[0]
        self._begin = self._begin[1]
        return value

    def insert(self, value):
        self._begin = [value, self._begin]

    def __str__(self):
        result = ""
        index = self._begin
        while index is not None:
            result += f"{index[0]}"
            index = index[1]
            if index:
                result += ", "
        return result


lst = LinkedList()
lst.insert(5)
lst.insert(6)
lst.insert(10)
print(lst)

for i in range(4):
    value = lst.pop()
    print(value)
