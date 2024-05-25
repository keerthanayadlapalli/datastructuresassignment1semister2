class DynamicArray:
    def __init__(self, resize_factor=2):
        self.array = []
        self.size = 0
        self.resize_factor = resize_factor

    def _resize(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def insert_at_index(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        if self.size == len(self.array):
            self._resize(max(1, len(self.array) * self.resize_factor))
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = value
        self.size += 1

    def delete_at_index(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.size -= 1
        self.array[self.size] = None
        if self.size <= len(self.array) // (self.resize_factor * 2):
            self._resize(max(1, len(self.array) // self.resize_factor))

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def rotate_right(self, k):
        if self.size == 0 or k == 0:
            return
        k = k % self.size
        self.array = self.array[-k:] + self.array[:-k]

    def reverse(self):
        left, right = 0, self.size - 1
        while left < right:
            self.array[left], self.array[right] = self.array[right], self.array[left]
            left += 1
            right -= 1

    def append(self, value):
        if self.size == len(self.array):
            self._resize(max(1, len(self.array) * self.resize_factor))
        self.array[self.size] = value
        self.size += 1

    def prepend(self, value):
        self.insert_at_index(0, value)

    def merge(self, other):
        for element in other.array[:other.size]:
            self.append(element)

    def interleave(self, other):
        new_array = DynamicArray()
        i, j = 0, 0
        while i < self.size or j < other.size:
            if i < self.size:
                new_array.append(self.array[i])
                i += 1
            if j < other.size:
                new_array.append(other.array[j])
                j += 1
        return new_array

    def get_middle(self):
        if self.size == 0:
            return None
        return self.array[self.size // 2]

    def index_of(self, value):
        for i in range(self.size):
            if self.array[i] == value:
                return i
        return -1

    def split_at_index(self, index):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        first_part = DynamicArray()
        second_part = DynamicArray()
        for i in range(index):
            first_part.append(self.array[i])
        for i in range(index, self.size):
            second_part.append(self.array[i])
        return first_part, second_part
