# automatically generated by the FlatBuffers compiler, do not modify

# namespace: MyGame

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class InParentNamespace(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = InParentNamespace()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsInParentNamespace(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def InParentNamespaceBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x4D\x4F\x4E\x53", size_prefixed=size_prefixed)

    # InParentNamespace
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

def InParentNamespaceStart(builder):
    builder.StartObject(0)

def Start(builder):
    InParentNamespaceStart(builder)

def InParentNamespaceEnd(builder):
    return builder.EndObject()

def End(builder):
    return InParentNamespaceEnd(builder)


class InParentNamespaceT(object):

    # InParentNamespaceT
    def __init__(self):
        pass

    @classmethod
    def InitFromBuf(cls, buf, pos):
        inParentNamespace = InParentNamespace()
        inParentNamespace.Init(buf, pos)
        return cls.InitFromObj(inParentNamespace)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, inParentNamespace):
        x = InParentNamespaceT()
        x._UnPack(inParentNamespace)
        return x

    # InParentNamespaceT
    def _UnPack(self, inParentNamespace):
        if inParentNamespace is None:
            return

    # InParentNamespaceT
    def Pack(self, builder):
        InParentNamespaceStart(builder)
        return InParentNamespaceEnd(builder)
