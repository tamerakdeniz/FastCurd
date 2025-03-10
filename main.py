from fastapi import FastAPI, Body

app = FastAPI()

courses_db = [
    {"id": 1, "instructor": "Tamer", "title": "Python", "category": "Development"},
    {"id": 2, "instructor": "Mustafa", "title": "Java", "category": "Development"},
    {"id": 3, "instructor": "Tamer", "title": "C++", "category": "Development"},
    {"id": 4, "instructor": "Faruk", "title": "C#", "category": "Development"},
    {"id": 5, "instructor": "Kaan", "title": "Machine Learning", "category": "AI"},
    {"id": 6, "instructor": "Ahmet", "title": "Deep Learning", "category": "AI"}
]

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.get("/hello")
async def hello_world():
    return {"message": "Hello World"}


@app.get("/courses")
async def get_all_courses():
    return courses_db

#Path Parameters

@app.get("/courses/title/{course_title}")
async def get_course_title(course_title: str):
    for course in courses_db:
        if course.get("title").casefold() == course_title.casefold():
            return course
    return {"message": "Course not found"}

@app.get("/courses/id/{course_id}")
async def get_course_id(course_id: int):
    for course in courses_db:
        if course.get("id") == course_id:
            return course
    return {"message": "Course not found"}

#Query Parameters

@app.get("/courses/")
async def get_courses_by_category(category: str):
    course_list = []
    for course in courses_db:
        if course.get("category").casefold() == category.casefold():
            course_list.append(course)
    return course_list

@app.get("/courses/{course_instructor}")
async def get_instructor_category_by_query(course_instructor: str, category: str):
    course_list = []
    for course in courses_db:
        if (course.get("instructor").casefold() == course_instructor.casefold()
                and course.get("category").casefold() == category.casefold()):
            course_list.append(course)
    return course_list


@app.post("/courses/create_course")
async def create_course(new_course = Body()):
    courses_db.append(new_course)
    return new_course

@app.put("/courses/update_course")
async def update_course(updated_course = Body()):
    for index in range(len(courses_db)):
        if courses_db[index].get("id") == updated_course.get("id"):
            courses_db[index] = updated_course
            return {"message": "Course updated successfully"}

@app.delete("/courses/delete_course/{course_id}")
async def delete_course(course_id: int):
    for index in range(len(courses_db)):
        if courses_db[index].get("id") == course_id:
            courses_db.pop(index)
            break