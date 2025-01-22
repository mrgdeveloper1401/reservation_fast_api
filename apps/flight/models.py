from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import relationship
from src.postgres_alchemy import base, engine

from .enums import FlightTypeEnum, PassengerType, TicketType

flight_type = ENUM(FlightTypeEnum, name="flight_type")
flight_type.create(engine, checkfirst=True)

ticket_type = ENUM(TicketType, name="ticket_type")
ticket_type.create(engine, checkfirst=True)

p_type = ENUM(PassengerType, name="passenger_type")
p_type.create(engine, checkfirst=True)

class DbFlightTicket(base):
    __tablename__ = "flight"
    id = Column(Integer, primary_key=True, index=True)
    flight_type = Column(flight_type, default=FlightTypeEnum.want)
    ticket_type = Column(ticket_type, default=TicketType.domestic_flight)
    origin = Column(String)
    destination = Column(String)
    departure_date = Column(Date)
    passanger_type = Column(p_type, default=PassengerType.adult)
    passanger_count = Column(Integer)
    is_deleted = Column(Boolean, default=False, nullable=True)
    deleted_at = Column(DateTime, nullable=True)

    flight_comment = relationship("DbFlightComment", back_populates="flight_comment")


class DbFlightComment(base):
    __tablename__ = "flight_comment"
    id = Column(Integer, primary_key=True, index=True)
    body = Column(String)
    is_publish = Column(Boolean, default=True)
    rate = Column(Integer, nullable=True)
    is_deleted = Column(Boolean, default=False, nullable=True)
    deleted_at = Column(DateTime, nullable=True)

    flight_id = Column(Integer, ForeignKey("flight.id"))
