COURSES = [
    {'id': 'WEB101', 'title': 'Web Applications', 'seats': 3},
    {'id': 'DS201', 'title': 'Distributed Systems', 'seats': 0},
    {'id': 'DB101', 'title': 'Databases', 'seats': 5},
]

def list_courses():
    return COURSES

def get_course(course_id):
    return next((course for course in COURSES if course['id'] == course_id), None)
