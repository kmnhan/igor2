class Record (object):
    def __init__(self, header, data, byte_order=None):
        self.header = header
        self.data = data
        self.byte_order = byte_order

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return '<{} {}>'.format(self.__class__.__name__, id(self))


class UnknownRecord (Record):
    def __repr__(self):
        return '<{}-{} {}>'.format(
            self.__class__.__name__, self.header['recordType'], id(self))


class UnusedRecord (Record):
    pass


class TextRecord (Record):
    def __init__(self, *args, **kwargs):
        super(TextRecord, self).__init__(*args, **kwargs)
        self.text = bytes(self.data).replace(
            b'\r\n', b'\n').replace(b'\r', b'\n')
        self.null_terminated_text = self.text.split(b'\x00', 1)[0]
