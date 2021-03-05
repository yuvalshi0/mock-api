import threading


class AtomicCounterList:
    """Atomic safe counter, holds list of finished id's and running id's"""

    def __init__(self, initial=0):
        self.value = initial
        self.list = []
        self.finished_list = []
        self._lock = threading.Lock()

    def increment(self):
        with self._lock:
            if(self.value == 10):
                self.restart()
            self.value += 1
            self.list.append(self.value)
            return self.value

    def decrement(self, id):
        with self._lock:
            self.list.remove(id)
            self.finished_list.append(id)

    def restart(self):
        self.value = 0
        self.list.clear()
        self.finished_list.clear()

    def __len__(self):
        with self._lock:
            return len(self.list)
