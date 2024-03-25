from io import BytesIO as _BytesIO

from ..binarywave import load as _loadibw
from . import Record


class WaveRecord (Record):
    def __init__(self, *args, **kwargs):
        super(WaveRecord, self).__init__(*args, **kwargs)
        self.wave = _loadibw(_BytesIO(bytes(self.data)))

    def __str__(self):
        return str(self.wave)
