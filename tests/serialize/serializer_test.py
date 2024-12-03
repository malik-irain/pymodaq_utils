import numpy as np
import pytest

from pymodaq_utils.serialize.factory import SerializableFactory
from pymodaq_utils.serialize.serializer import (StringSerializeDeserialize as SSD,
                                                BytesSerializeDeserialize as BSD,
                                                ScalarSerializeDeserialize as ScSD,
                                                NdArraySerializeDeserialize as NdSD,
                                                ListSerializeDeserialize as LSD,)

ser_factory = SerializableFactory()


LABEL = 'A Label'
UNITS = 'mm'
OFFSET = -20.4
SCALING = 0.22
SIZE = 20
DATA = OFFSET + SCALING * np.linspace(0, SIZE-1, SIZE)

DATA0D = np.array([2.7])
DATA1D = np.arange(0, 10)
DATA2D = np.arange(0, 5*6).reshape((5, 6))
DATAND = np.arange(0, 5 * 6 * 3).reshape((5, 6, 3))
Nn0 = 10
Nn1 = 5


def test_string_serialization():
    s = 'ert'
    obj_type = 'str'

    assert SSD.serialize(s) == b'\x00\x00\x00' + chr(len(s)).encode() + s.encode()

    assert ser_factory.get_serializer(type(s))(s) == \
           b'\x00\x00\x00' + chr(len(obj_type)).encode() + obj_type.encode() + SSD.serialize(s)

    assert ser_factory.get_serializer(type(s))(s) == \
           ser_factory.get_apply_serializer(s)

    assert SSD.deserialize(SSD.serialize(s)) == (s, b'')

    assert (ser_factory.get_apply_deserializer(ser_factory.get_apply_serializer(s))
            == s)


def test_bytes_serialization():
    b = b'kjlksjdf'
    obj_type = 'bytes'
    assert BSD.serialize(b) == b'\x00\x00\x00' + chr(len(b)).encode() + b
    assert (ser_factory.get_serializer(type(b))(b) ==
           b'\x00\x00\x00' + chr(len(obj_type)).encode() + obj_type.encode() +
            BSD.serialize(b))
    assert ser_factory.get_serializer(type(b))(b) == \
           ser_factory.get_apply_serializer(b)

    assert BSD.deserialize(BSD.serialize(b)) == (b, b'')

    assert (ser_factory.get_apply_deserializer(ser_factory.get_apply_serializer(b))
            == b)


def test_scalar_serialization():
    s = 23
    obj_type = 'int'
    assert (ser_factory.get_serializer(type(s))(s) ==
           b'\x00\x00\x00' + chr(len(obj_type)).encode() + obj_type.encode() +
            ScSD.serialize(s))
    assert (ser_factory.get_serializer(type(s))(s) ==
            ser_factory.get_apply_serializer(s))

    assert ScSD.deserialize(ScSD.serialize(s)) == (s, b'')

    assert (ser_factory.get_apply_deserializer(ser_factory.get_apply_serializer(s))
            == s)

    s = -3.8
    obj_type = 'float'
    assert (ser_factory.get_serializer(type(s))(s) ==
           b'\x00\x00\x00' + chr(len(obj_type)).encode() + obj_type.encode() +
            ScSD.serialize(s))
    assert (ser_factory.get_serializer(type(s))(s) ==
            ser_factory.get_apply_serializer(s))

    assert ScSD.deserialize(ScSD.serialize(s)) == (s, b'')

    assert (ser_factory.get_apply_deserializer(ser_factory.get_apply_serializer(s))
            == s)

    s = 4 - 2.5j
    obj_type = 'complex'
    assert (ser_factory.get_serializer(type(s))(s) ==
           b'\x00\x00\x00' + chr(len(obj_type)).encode() + obj_type.encode() +
            ScSD.serialize(s))
    assert (ser_factory.get_serializer(type(s))(s) ==
            ser_factory.get_apply_serializer(s))

    assert ScSD.deserialize(ScSD.serialize(s)) == (s, b'')

    assert (ser_factory.get_apply_deserializer(ser_factory.get_apply_serializer(s))
            == s)


def test_bool_serialization():
    s = True
    obj_type = 'bool'
    assert (ser_factory.get_serializer(type(s))(s) ==
           b'\x00\x00\x00' + chr(len(obj_type)).encode() + obj_type.encode() +
            ScSD.serialize(s))
    assert (ser_factory.get_serializer(type(s))(s) ==
            ser_factory.get_apply_serializer(s))

    assert ScSD.deserialize(ScSD.serialize(s)) == (s, b'')

    assert (ser_factory.get_apply_deserializer(ser_factory.get_apply_serializer(s))
            == s)

    s = False
    obj_type = 'bool'
    assert (ser_factory.get_serializer(type(s))(s) ==
           b'\x00\x00\x00' + chr(len(obj_type)).encode() + obj_type.encode() +
            ScSD.serialize(s))
    assert (ser_factory.get_serializer(type(s))(s) ==
            ser_factory.get_apply_serializer(s))
    assert ScSD.deserialize(ScSD.serialize(s)) == (s, b'')

    assert (ser_factory.get_apply_deserializer(ser_factory.get_apply_serializer(s))
            == s)


def test_ndarray_serialization_deserialization():

    ndarrays = [np.array([12, 56, 78,]),
                np.array([-12.8, 56, 78, ]),
                np.array([12]),
                np.array([True, False]),
                np.array([[12+6j, 56, 78, ],
                          [12, 56, 78, ],
                          [12, 56, 78, ]])]

    for ndarray in ndarrays:
        ser = NdSD.serialize(ndarray)
        assert isinstance(ser, bytes)
        assert np.allclose(NdSD.deserialize(NdSD.serialize(ndarray))[0], ndarray)

        assert np.allclose(
            ser_factory.get_apply_deserializer(
                ser_factory.get_apply_serializer(ndarray)), ndarray)


@pytest.mark.parametrize('obj_list', (['hjk', 'jkgjg', 'lkhlkhl'],  # homogeneous string
                                      [21, 34, -56, 56.7, 1+1j*99],  # homogeneous numbers
                                      [np.array([45, 67, 87654]),
                                       np.array([[45, 67, 87654], [-45, -67, -87654]])],  # homogeneous ndarrays
                                      ['hjk', 23, 34.7, np.array([1, 2, 3])],  # inhomogeneous list
                                   ))
def test_list_serialization_deserialization(obj_list):
    ser = LSD.serialize(obj_list)
    assert isinstance(ser, bytes)

    list_back = LSD.deserialize(ser)[0]
    assert isinstance(list_back, list)
    for ind in range(len(obj_list)):
        if isinstance(obj_list[ind], np.ndarray):
            assert np.allclose(obj_list[ind], list_back[ind])
        else:
            assert obj_list[ind] == list_back[ind]

    for ind, obj in enumerate(
            ser_factory.get_apply_deserializer(ser_factory.get_apply_serializer(obj_list))):
        if isinstance(obj, np.ndarray):
            assert np.allclose(obj_list[ind], obj)
        else:
            assert obj_list[ind] == obj

