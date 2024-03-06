# flake8: noqa: F401
"""Record parsers for IGOR's packed experiment files."""
from igor2.record.base import Record, UnknownRecord, UnusedRecord
from igor2.record.variables import VariablesRecord
from igor2.record.history import HistoryRecord, RecreationRecord, GetHistoryRecord
from igor2.record.wave import WaveRecord
from igor2.record.procedure import ProcedureRecord
from igor2.record.packedfile import PackedFileRecord
from igor2.record.folder import FolderStartRecord, FolderEndRecord


# From PackedFile.h
RECORD_TYPE = {
    0: UnusedRecord,
    1: VariablesRecord,
    2: HistoryRecord,
    3: WaveRecord,
    4: RecreationRecord,
    5: ProcedureRecord,
    6: UnusedRecord,
    7: GetHistoryRecord,
    8: PackedFileRecord,
    9: FolderStartRecord,
    10: FolderEndRecord,
}
