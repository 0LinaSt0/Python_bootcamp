from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

Ally: Alignment
Carrier: Class
Corvette: Class
Cruiser: Class
DESCRIPTOR: _descriptor.FileDescriptor
Destroye: Class
Dreadno: Class
Enemy: Alignment
Frigate: Class

class Officer(_message.Message):
    __slots__ = ["first_name", "last_name", "rank"]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    first_name: str
    last_name: str
    rank: str
    def __init__(self, first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., rank: _Optional[str] = ...) -> None: ...

class Spaceship(_message.Message):
    __slots__ = ["alignment", "armed", "crew_size", "length", "name", "officers", "ship_class"]
    ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
    ARMED_FIELD_NUMBER: _ClassVar[int]
    CREW_SIZE_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OFFICERS_FIELD_NUMBER: _ClassVar[int]
    SHIP_CLASS_FIELD_NUMBER: _ClassVar[int]
    alignment: Alignment
    armed: bool
    crew_size: int
    length: float
    name: str
    officers: _containers.RepeatedCompositeFieldContainer[Officer]
    ship_class: Class
    def __init__(self, alignment: _Optional[_Union[Alignment, str]] = ..., name: _Optional[str] = ..., ship_class: _Optional[_Union[Class, str]] = ..., length: _Optional[float] = ..., crew_size: _Optional[int] = ..., armed: bool = ..., officers: _Optional[_Iterable[_Union[Officer, _Mapping]]] = ...) -> None: ...

class SpaceshipRequest(_message.Message):
    __slots__ = ["coordinates"]
    COORDINATES_FIELD_NUMBER: _ClassVar[int]
    coordinates: str
    def __init__(self, coordinates: _Optional[str] = ...) -> None: ...

class SpaceshipResponse(_message.Message):
    __slots__ = ["respons_ships"]
    RESPONS_SHIPS_FIELD_NUMBER: _ClassVar[int]
    respons_ships: Spaceship
    def __init__(self, respons_ships: _Optional[_Union[Spaceship, _Mapping]] = ...) -> None: ...

class Alignment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class Class(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
