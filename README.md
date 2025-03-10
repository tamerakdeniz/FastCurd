# 🚀 FastCurd - FastAPI Course Management System

A simple and efficient course management system built with FastAPI that provides CRUD operations for managing courses.

## 📋 Features

- Get all courses
- Get course by title
- Get course by ID
- Get courses by category
- Get courses by instructor and category
- Create new courses
- Update existing courses
- Delete courses

## 🛠️ Installation

1. Clone the repository:

```bash
git clone https://github.com/tamerakdeniz/FastCurd.git
cd FastCurd
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On Unix or MacOS
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## 🚀 How to Run

1. Start the server:

```bash
uvicorn main:app --reload
```

2. Open your browser and navigate to:

```
http://localhost:8000
```

3. Access the interactive API documentation at:

```
http://localhost:8000/docs
```

## 📚 API Endpoints

### GET Endpoints

- `/` - Welcome message
- `/courses` - Get all courses
- `/courses/title/{course_title}` - Get course by title
- `/courses/id/{course_id}` - Get course by ID
- `/courses/?category={category}` - Get courses by category
- `/courses/{course_instructor}?category={category}` - Get courses by instructor and category

### POST Endpoint

- `/courses/create_course` - Create a new course

### PUT Endpoint

- `/courses/update_course` - Update an existing course

### DELETE Endpoint

- `/courses/delete_course/{course_id}` - Delete a course by ID

## 💻 Example Course Structure

```json
{
  "id": 1,
  "instructor": "Tamer",
  "title": "Python",
  "category": "Development"
}
```

## 🛠️ Technologies Used

- FastAPI
- Uvicorn
- Python 3.x
