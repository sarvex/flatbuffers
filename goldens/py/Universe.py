# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Universe(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Universe()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUniverse(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Universe
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Universe
    def Age(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float64Flags, o + self._tab.Pos)
        return 0.0

    # Universe
    def Galaxies(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .Galaxy import Galaxy
            obj = Galaxy()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Universe
    def GalaxiesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return self._tab.VectorLen(o) if o != 0 else 0

    # Universe
    def GalaxiesIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

def UniverseStart(builder):
    builder.StartObject(2)

def Start(builder):
    UniverseStart(builder)

def UniverseAddAge(builder, age):
    builder.PrependFloat64Slot(0, age, 0.0)

def AddAge(builder: flatbuffers.Builder, age: float):
    UniverseAddAge(builder, age)

def UniverseAddGalaxies(builder, galaxies):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(galaxies), 0)

def AddGalaxies(builder: flatbuffers.Builder, galaxies: int):
    UniverseAddGalaxies(builder, galaxies)

def UniverseStartGalaxiesVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartGalaxiesVector(builder, numElems: int) -> int:
    return UniverseStartGalaxiesVector(builder, numElems)

def UniverseEnd(builder):
    return builder.EndObject()

def End(builder):
    return UniverseEnd(builder)
