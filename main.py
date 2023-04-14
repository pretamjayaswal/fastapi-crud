from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


app = FastAPI()

fakedb = []

class Course(BaseModel):
    id: int
    name: str
    price: float
    is_earlybird: Optional[bool] = None

# TEST
@app.get('/')
def read_root():
    return {"greetings":"welcome to App Root"}

# READ - All courses
@app.get('/courses')
def get_coursees() -> list:
    if not fakedb:
        return fakedb
    else:
        {"Msg":"--No Courses Found--"}

# READ - Single Course
@app.get('/courses/{course_id}')
def get_a_course(course_id : int):
    course = course_id - 1
    return fakedb[course]

# CREATE/UPDATE
@app.post('/courses')
def add_course(course: Course):
    fakedb.append(course.dict())
    return fakedb[-1] 

# DELETE
@app.delete('/courses/{course_id}')
def delete_course(course_id : int):
    fakedb.pop(course_id- 1)
    return {"task":"deletion success"}


