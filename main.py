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
    # return fakedb
    if fakedb:
        return fakedb
    else:
        return [{"Msg":"No Courses Found"}]

# READ - Single Course
@app.get('/courses/{course_id}')
def get_a_course(course_id : int):
    for course in fakedb:
        if course['id'] == course_id:
            return course
    
    return {"msg":"No Course found with id"}

# CREATE/UPDATE
@app.post('/courses')
def add_course(course: Course):
    fakedb.append(course.dict())
    return fakedb[-1] 

# DELETE
@app.delete('/courses/{course_id}')
def delete_course(course_id : int):
    for i,course in enumerate(fakedb):
        if course['id'] == course_id:
            fakedb.pop(i)
            return {"task":"deletion success for id"+str(course_id)}
    return {"task":"Id not found/Deletion Failed for id "+str(course_id)}


