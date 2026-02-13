

class Event():
    def __init__(self):
        self._listeners = {}
        self._count = 0

    def Subscribe(self, methode):
        self._listeners[self._count] = methode
        self._count += 1
        return self._count - 1 # returns ID

    def Unsubscribe(self, ID):
        del self._listeners[ID]

    def Trigger(self, args):
        for listener in self._listeners.values():
            listener(args)
        print(f"ran trigger. triggered {len(self._listeners)} listeners")