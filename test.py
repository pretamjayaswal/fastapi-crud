
    
fakedb = [
  {
    "id": 1,
    "name": "py",
    "price": 0,
    "is_earlybird": True
  },
  {
    "id": 2,
    "name": "php",
    "price": 0,
    "is_earlybird": True
  }
]
def get_a_course(course_id : int):
    for course in fakedb:
        if course["id"] == course_id:
            return course
    
    return {"msg":"No Course found with id"}

print(get_a_course(1))