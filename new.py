
from fastapi import FastAPI

app = FastAPI()

# In-memory storage (Python dictionary)
students_db = {}

# Create a Student resource
@app.post("/students/")
async def create_student(id: int, name: str, age: int, sex: str, height: float):
    if id in students_db:
        return {"error": "Student with this ID already exists"}
    student = {"id": id, "name": name, "age": age, "sex": sex, "height": height}
    students_db[id] = student
    return student

# Retrieve a single Student resource
@app.get("/students/{student_id}")
async def read_student(student_id: int):
    student = students_db.get(student_id)
    if student is None:
        return {"error": "Student not found"}
    return student

# Retrieve all Student resources
@app.get("/students/")
async def read_students():
    return students_db

# Update a Student resource
@app.put("/students/{student_id}")
async def update_student(student_id: int, name: str, age: int, sex: str, height: float):
    student = students_db.get(student_id)
    if student is None:
        return {"error": "Student not found"}
    student["name"] = name
    student["age"] = age
    student["sex"] = sex
    student["height"] = height
    return student

# Delete a Student resource
@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
    if student_id not in students_db:
        return {"error": "Student not found"}
    del students_db[student_id]
    return {"message": "Student deleted successfully"}

