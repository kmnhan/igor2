from io import BytesIO as _BytesIO

from igor2.binarywave import load as _loadibw
from igor2.record import Record


class WaveRecord (Record):
    def __init__(self, *args, **kwargs):
        super(WaveRecord, self).__init__(*args, **kwargs)
        self.wave = _loadibw(_BytesIO(bytes(self.data)))

    def __str__(self):
        return str(self.wave)
