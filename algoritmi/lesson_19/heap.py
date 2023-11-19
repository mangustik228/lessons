# Структура данных куча

# Характеризируется следующими свойствами:
#     - Пока не заполнен слой, новый не создается... (верхний слой - нулевой)
#     - Все значения слоя ниже: больше значений, верхнего слоя


class Heap:
    def __init__(self):
        self.values = []

    def add(self, value: int):
        self.values.append(value)
        self._up_element(len(self.values) - 1)

    def _up_element(self, idx: int):
        # Вычисляем индекс родителя
        parent_idx = (idx - 1) // 2
        if idx <= 0:
            return
        if self.values[idx] < self.values[parent_idx]:
            # Меняем местами
            self.values[idx], self.values[parent_idx] = \
                self.values[parent_idx], self.values[idx]
            self._up_element(parent_idx)

    def __str__(self):
        return f"size:{len(self.values) = }\n{self.values}"

    def get_min(self):
        return self.values[0]

    def find_element(self, value: int, idx: int = 0):
        if idx > len(self.values) or value < self.values[idx]:
            return -1
        if value == self.values[idx]:
            return idx
        return max(self.find_element(value, idx*2+1), self.find_element(value, idx*2+2))

    def pop(self) -> int:
        return self.values.pop()

    def get_first(self) -> int:
        result = self.values[0]
        self.values[0] = self.values.pop()
        self._down_element()
        return result

    def check_min_element(self, idx_1, idx_2):
        if idx_2 > len(self.values):
            return idx_1
        return idx_1 if self.values[idx_1] < self.values[idx_2] else idx_2

    def _down_element(self, idx=0):
        if idx*2+2 > len(self.values):
            return
        min_idx = self.check_min_element(idx*2+1, idx*2+2)
        self.values[idx], self.values[min_idx] =\
            self.values[min_idx], self.values[idx]
        self._down_element(min_idx)


heap = Heap()
heap.add(5)
heap.add(1)
heap.add(1)
heap.add(8)
heap.add(12)
heap.add(4)
heap.add(3)
heap.add(7)
heap.add(9)
heap.add(0)
print(heap)
print(heap.find_element(4))
print(heap.pop())
print(heap.get_first())
print(heap)
