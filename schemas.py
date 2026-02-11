from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import date
from typing import List, Optional

# --- Employee Schemas ---
class EmployeeBase(BaseModel):
    name: str
    email: EmailStr
    department: str

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeOut(EmployeeBase):
    id: int
    
    # OLD: class Config: orm_mode = True
    # NEW: Pydantic V2 Syntax
    model_config = ConfigDict(from_attributes=True)

# --- Attendance Schemas ---
class AttendanceBase(BaseModel):
    employee_id: int
    date: date
    status: str

class AttendanceCreate(AttendanceBase):
    pass

class AttendanceOut(AttendanceBase):
    id: int

    # OLD: class Config: orm_mode = True
    # NEW: Pydantic V2 Syntax
    model_config = ConfigDict(from_attributes=True)