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
	validator,
	Field
)


VALID_DICT = {
	"Corvette": {
		"length": [80.0, 250.0],
		"crewSize": [4, 10],
		"armed": True,
		"alignment": "Enemy"
	},

	"Frigate": {
		"length": [300.0, 600.0],
		"crewSize": [10, 15],
		"armed": True,
		"alignment": "Ally"
	},

	"Cruiser": {
		"length": [500.0, 1000.0],
		"crewSize": [15, 30],
		"armed": True,
		"alignment": "Enemy"
	},

	"Destroyer": {
		"length": [800.0, 2000.0],
		"crewSize": [50, 80],
		"armed": True,
		"alignment": "Ally"
	},

	"Carrier": {
		"length": [1000.0, 4000.0],
		"crewSize": [120, 250],
		"armed": False,
		"alignment": "Enemy"
	},

	"Dreadnought": {
		"length": [5000.0, 20000.0],
		"crewSize": [300, 500],
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
	length: float = Field(..., ge=80.0, le=20000.0)
	shipClass: str
	crewSize: int = Field(..., ge=4, le=500)
	armed: bool
	officers: list

	@validator("name")
	def check_name(cls, v):
		if v not in Class._member_names_:
			raise ValueError('Invalid ship name')
		return v

	@root_validator
	def check_valid_parameters(cls, values):
		if values["shipClass"] != "Unknown":
			expected_parameters = VALID_DICT[values["shipClass"]]
			"""
			if ((expected_parameters["length"][0] <= values["length"]
				and expected_parameters["length"][1] >= values["length"]
				and expected_parameters["crewSize"][0] <= values["crewSize"]
				and expected_parameters["crewSize"][1] >= values["crewSize"]
				and expected_parameters["armed"] == values["armed"]
				and expected_parameters["alignment"] == values["alignment"]) is False):
				raise ValueError('Invalid fields')
			"""
			if (expected_parameters["length"][0] > values["length"]
				and expected_parameters["length"][1] < values["length"]):
				raise ValueError("Invalid length")
			if (expected_parameters["crewSize"][0] > values["crewSize"]
				and expected_parameters["crewSize"][1] < values["crewSize"]):
				raise ValueError("Invalid crew")
			if expected_parameters["armed"] != values["armed"]:
				raise ValueError("Invalid armed status")
			if expected_parameters["alignment"] != values["alignment"]:
				raise ValueError("Invalid hostile status")
		return values

