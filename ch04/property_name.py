class Connection:
    _connected = []

    def connect(self, user):
        self._connected.append(user)

    @property
    def connected_people(self):
        return ', '.join(self._connected)