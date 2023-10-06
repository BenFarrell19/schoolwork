# -----------------------------------------------------
# CSCI 127, Lab 11                                    |
# Month 11, 2021                                      |
# Ben Farrell                                         |
# -----------------------------------------------------

# Your solution goes here. ------------------------------
class Queue:
    def __init__(self, name):
        self.queue_name = name
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        pass

    def __iadd__(self, item):
        self.items.append(item)
        # fix me make the += operator work
        return self  # must return self from __iadd__

    def dequeue(self):
        name = self.items[0]
        del self.items[0]
        return name

    def is_empty(self):
        if len(self.items) == 0:
            return True

    def __str__(self):
        return "Queue: [FIRST--> " + str(self.items)[1:-1].replace("'", "") + " <--LAST]"

    def is_equal(self, queue):
        if self.items == queue.items:
            return True
        else:
            return False


# Do not change anything below. -------------------------

def main():
    presidents = Queue("Presidents")

    print("\nQueuing up G.Wash, J.Ad, T.Jeff, J.Mad, J.Mon")
    presidents.enqueue("Washington")
    presidents.enqueue("Adams")
    presidents.enqueue("Jefferson")
    presidents.enqueue("Madison")
    presidents.enqueue("Monroe")
    print(presidents)

    print("\nDequeue George -- first president in, so first one out")
    presidents.dequeue()
    print(presidents)

    print("\nDequeue everybody")
    while not presidents.is_empty():
        print("President dequeued:", presidents.dequeue())
        print(presidents)

    print("\nAdding J.Ad, A.Jack, M.Van, B.Harr, J.Ty")
    presidents.enqueue("Adams")
    presidents.enqueue("Jackson")
    presidents.enqueue("Van Buren")
    presidents.enqueue("Harrison")
    presidents.enqueue("Tyler")
    print(presidents)

    print("\nAdding J.Polk to the back of the line")
    presidents += "Polk"  # See: https://www.python-course.eu/python3_magic_methods.php
    print(presidents)

    # TODO: add some code to test two queues for equality
    queue_2 = Queue("number two")
    queue_2.enqueue("Adams")
    queue_2.enqueue("Jackson")
    queue_2.enqueue("Van Buren")
    queue_2.enqueue("Harrison")
    queue_2.enqueue("Tyler")
    queue_2.enqueue("Polk")
    print(presidents.is_equal(queue_2))

    queue_2 = Queue("number two")
    queue_2.enqueue("Jackson")
    queue_2.enqueue("Adams")
    queue_2.enqueue("Van Buren")
    queue_2.enqueue("Harrison")
    queue_2.enqueue("Tyler")
    queue_2.enqueue("Polk")
    print(presidents.is_equal(queue_2))

    queue_2 = Queue("number two")
    queue_2.enqueue("W")
    queue_2.enqueue("Ad")
    queue_2.enqueue("Jeffson")
    queue_2.enqueue("Mson")
    queue_2.enqueue("Mooe")
    print(presidents.is_equal(queue_2))


# -----------------------------------------------------

main()
