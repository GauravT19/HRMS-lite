from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import date

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    department = Column(String, nullable=False)
    
    # Relationship: One Employee has Many Attendance records
    attendance = relationship("Attendance", back_populates="employee", cascade="all, delete")

class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    date = Column(Date, default=date.today)
    status = Column(String, nullable=False) # e.g., "Present", "Absent"

    # Relationship: Many Attendance records belong to One Employee
    employee = relationship("Employee", back_populates="attendance")