class AnimalShelf:

    def __init__(self):
        self.dog_queue = []
        self.cat_queue = []
        self.any_queue = []

    def enqueue(self, animal: [int]) -> None:
        num, kind = animal
        if (len(self.dog_queue) + len(self.cat_queue)) <= 20000:
            if kind == 0:
                self.cat_queue.append(animal)
            else:
                self.dog_queue.append(animal)
            self.any_queue.append(animal)

    def dequeueAny(self) -> [int]:
        if self.any_queue:
            num, kind = self.any_queue.pop(0)
            if kind == 0:
                self.cat_queue.pop(0)
            else:
                self.dog_queue.pop(0)
            return num, kind
        else:
            return -1, -1

    def dequeueDog(self) -> [int]:
        if self.dog_queue:
            data = self.dog_queue.pop(0)
            self.any_queue.remove(data)
            return data
        else:
            return -1, -1

    def dequeueCat(self) -> [int]:
        if self.cat_queue:
            data = self.cat_queue.pop(0)
            self.any_queue.remove(data)
            return data
        else:
            return -1, -1


class AnimalShelf2:

    def __init__(self):
        self.animal_queue = []

    def enqueue(self, animal: [int]) -> None:
        if len(self.animal_queue) <= 20000:
            self.animal_queue.append(animal)

    def dequeueAny(self) -> [int]:
        if self.animal_queue:
            return self.animal_queue.pop(0)
        else:
            return -1, -1

    def dequeueDog(self) -> [int]:
        for index, item in enumerate(self.animal_queue):
            print(item[1])
            if item[1] == 1:
                return self.animal_queue.pop(index)
        return -1, -1

    def dequeueCat(self) -> [int]:
        for index, item in enumerate(self.animal_queue):
            if item[1] == 0:
                return self.animal_queue.pop(index)
        return -1, -1


# Your AnimalShelf object will be instantiated and called as such:
if __name__ == '__main__':
    obj = AnimalShelf()
    obj.enqueue((0, 0))
    obj.enqueue((1, 0))
    print(obj.dequeueCat())
    print(obj.dequeueCat())