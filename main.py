from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy.orm import Session
from typing import List

# Import our new modules
import models
import schemas
from database import engine, get_db

# Create Tables automatically
models.Base.metadata.create_all(bind=engine)

# App Configuration
description = """
## 🚀 HRMS Lite Admin Panel

This is a modular backend API for HR management.
Use the interactive docs below to manage the system.
"""

app = FastAPI(
    title="HRMS Lite System",
    description=description,
    version="1.0.0",
    docs_url="/" # Serves Swagger UI at root
)

# --- ROUTES ---

@app.get("/health", tags=["System"])
def health_check():
    return {"status": "ok", "message": "System is running"}

# 1. Add Employee
@app.post("/employees", response_model=schemas.EmployeeOut, tags=["Employee Management"], status_code=201)
def create_employee(emp: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    # Check duplicate
    if db.query(models.Employee).filter(models.Employee.email == emp.email).first():
        raise HTTPException(status_code=400, detail="Email already exists.")
    
    new_emp = models.Employee(**emp.dict())
    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)
    return new_emp

# 2. List Employees
@app.get("/employees", response_model=List[schemas.EmployeeOut], tags=["Employee Management"])
def get_employees(db: Session = Depends(get_db)):
    return db.query(models.Employee).all()

# 3. Delete Employee
@app.delete("/employees/{employee_id}", tags=["Employee Management"])
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    emp = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    db.delete(emp)
    db.commit()
    return {"message": "Employee deleted"}

# 4. Mark Attendance
@app.post("/attendance", tags=["Attendance Tracking"])
def mark_attendance(att: schemas.AttendanceCreate, db: Session = Depends(get_db)):
    # Check if record exists for this date/employee
    existing = db.query(models.Attendance).filter(
        models.Attendance.employee_id == att.employee_id,
        models.Attendance.date == att.date
    ).first()

    if existing:
        existing.status = att.status
        db.commit()
        return {"message": "Attendance updated"}
    
    new_record = models.Attendance(**att.dict())
    db.add(new_record)
    db.commit()
    return {"message": "Attendance marked"}

# 5. View History
@app.get("/attendance/{employee_id}", response_model=List[schemas.AttendanceOut], tags=["Attendance Tracking"])
def get_attendance_history(employee_id: int, db: Session = Depends(get_db)):
    return db.query(models.Attendance).filter(models.Attendance.employee_id == employee_id).all()