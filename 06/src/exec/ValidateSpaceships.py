"""
								Valid parameters
-------------------------------------------------------------------------------------
| Class			|	Length		|	Crew	|	Can be armed?	|	Can be hostile?	|
-------------------------------------------------------------------------------------
| Corvette		|	80-250		|	4-10	|		Yes			|		Yes			|
| Frigate		|	300-600		|	10-15	|		Yes			|		No			|
| Cruiser		|	500-1000	|	15-30	|		Yes			|		Yes			|
| Destroyer		|	800-2000	|	50-80	|		Yes			|		No			|
| Carrier		|	1000-4000	|	120-250	|		No			|		Yes			|
| Dreadnought	|	5000-20000	|	300-500	|		Yes			|		Yes			|
-------------------------------------------------------------------------------------
"""

from enum import Enum
from pydantic import (
	BaseModel,
	root_validator,
	validator
)


VALID_DICT = {
	"Corvette": {
		"length": [80.0, 250.0],
		"crew_size": [4, 10],
		"armed": True,
		"alignment": "Enemy"
	},

	"Frigate": {
		"length": [300.0, 600.0],
		"crew_size": [10, 15],
		"armed": True,
		"alignment": "Ally"
	},

	"Cruiser": {
		"length": [500.0, 1000.0],
		"crew_size": [15, 30],
		"armed": True,
		"alignment": "Enemy"
	},

	"Destroyer": {
		"length": [800.0, 2000.0],
		"crew_size": [50, 80],
		"armed": True,
		"alignment": "Ally"
	},

	"Carrier": {
		"length": [1000.0, 4000.0],
		"crew_size": [120, 250],
		"armed": False,
		"alignment": "Enemy"
	},

	"Dreadnought": {
		"length": [5000.0, 20000.0],
		"crew_size": [300, 500],
		"armed": True,
		"alignment": "Enemy"
	}
}


class Class(str, Enum):
	COR = "Corvette"
	FRI = "Frigate"
	CRU = "Cruiser"
	DES = "Destroyer"
	CAR = "Carrier"
	DRE = "Dreadnought"
	UNK = "Unknown"


class ValidateSpaceships(BaseModel):
	alignment: str
	name: str
	length: float
	classs: str
	crew_size: int
	armed: bool
	officers: list

	@validator("classs")
	def check_name(cls, v):
		if v not in Class._value2member_map_:
			raise ValueError('Invalid ship name')
		return v

	@root_validator
	def check_valid_parameters(cls, values):
		if values["classs"] != "Unknown":
			expected_parameters = VALID_DICT[values["classs"]]
			if (expected_parameters["length"][0] > values["length"]
				or expected_parameters["length"][1] < values["length"]):
				raise ValueError("Invalid length")
			if (expected_parameters["crew_size"][0] > values["crew_size"]
				or expected_parameters["crew_size"][1] < values["crew_size"]):
				raise ValueError("Invalid crew")
			if (expected_parameters["armed"] == False
				and expected_parameters["armed"] != values["armed"]):
				raise ValueError("Invalid armed status")
			if (expected_parameters["alignment"] == "Ally"
				and expected_parameters["alignment"] != values["alignment"]):
				raise ValueError("Invalid hostile status")
		return values
