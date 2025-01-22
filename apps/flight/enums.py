from enum import Enum


# مسیر بلیط پرواز
class FlightTypeEnum(str, Enum):
    want = "want"
    back_forth = "back_forth"


# نوع مسافر
class PassengerType(str, Enum):
    baby = "baby"
    child = "child"
    adult = "adult"


# مسیر پرواز
class TicketType(str, Enum):
    domestic_flight = "domestic_flight"
    foreign_flight = "foreign_flight"
