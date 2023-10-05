class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades_for_lectures:
                lecturer.grades_for_lectures[course] += [grade]
            else:
                lecturer.grades_for_lectures[course] = [grade]
        else:
            return 'Ошибка'
        
    def __average_grade_for_homework(self):
        count = 0
        for key, grades_list in self.grades.items():
            count_for_course = 0
            for id, grade in enumerate(grades_list, start=1):
                count_for_course += grade
                if id  == len(grades_list):
                    count += count_for_course / id 
        return count / len(self.grades)
    
    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {round(self.__average_grade_for_homework(), 2)}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}\n")
    
    def __lt__(self, other):
        return self.__average_grade_for_homework() < other.__average_grade_for_homework()
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_for_lectures = {}

    def __average_grade_for_lectures(self):
        count = 0
        for key, grades_list in self.grades_for_lectures.items():
            count_for_course = 0
            for id, grade in enumerate(grades_list, start=1):
                count_for_course += grade
                if id  == len(grades_list):
                   count += count_for_course / id 
        return count / len(self.grades_for_lectures)

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {round(self.__average_grade_for_lectures(), 2)}\n")
    
    def __lt__(self, other):
        return self.__average_grade_for_lectures() < other.__average_grade_for_lectures()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\n"    


def students_avarage_grade_for_course(students_list, course_name):
    grades_of_course = []
    for student in students_list:
        for course, grades in student.grades.items():
            if course == course_name:
                grades_of_course.extend(grades)
    count = 0
    for id, grade in enumerate(grades_of_course, start=1):
        count += grade
        if id  == len(grades_of_course):
            return f'Средняя оценка студентов за домашние задания на курсе {course_name}: {round(count / id, 2)}'

def lecturers_avarage_grade_for_course(lecturers_list, course_name):
    grades_of_course = []
    for lecturer in lecturers_list:
        for course, grades in lecturer.grades_for_lectures.items():
            if course == course_name:
                grades_of_course.extend(grades)
    count = 0
    for id, grade in enumerate(grades_of_course, start=1):
        count += grade
        if id  == len(grades_of_course):
            return f'Средняя оценка лекторов за лекции по курсу {course_name}: {round(count / id, 2)}'
        

students_list = []
lecturers_list = []

student_1 = Student('Rachel', 'Green', 'female')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Java']
student_1.finished_courses += ['JS']
students_list.append(student_1)

student_2 = Student('Monica', 'Geller', 'female')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['JS']
student_2.finished_courses += ['Java']
students_list.append(student_2)

lecturer_1 = Lecturer('Phoebe', 'Buffay')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Java']

lecturer_2 = Lecturer('Joey', 'Tribbiani')
lecturer_2.courses_attached += ['Python']
lecturer_2.courses_attached += ['JS']

student_1.rate_lecture(lecturer_1, 'Python', 10) 
student_1.rate_lecture(lecturer_1, 'Python', 8)

student_2.rate_lecture(lecturer_2, 'JS', 10) 
student_2.rate_lecture(lecturer_2, 'JS', 9)

lecturers_list.append(lecturer_1)
lecturers_list.append(lecturer_2)

reviewer_1 = Reviewer('Chandler', 'Bing')
reviewer_1.courses_attached += ['Python']
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_1.rate_hw(student_1, 'Python', 9)

reviewer_1.rate_hw(student_2, 'Python', 8)
reviewer_1.rate_hw(student_2, 'Python', 8)
reviewer_1.rate_hw(student_2, 'Python', 9)

reviewer_2 = Reviewer('Ross', 'Geller')
reviewer_2.courses_attached += ['Java']
reviewer_2.rate_hw(student_1, 'Java', 7)
reviewer_2.rate_hw(student_1, 'Java', 10)
reviewer_2.rate_hw(student_1, 'Java', 9)

print(student_1)
print(lecturer_1)
print(reviewer_1)
print(student_2)
print(lecturer_2)
print(reviewer_2)
print(student_1 > student_2)
print(lecturer_1 > lecturer_2)
print(students_avarage_grade_for_course(students_list, 'Python'))
print(lecturers_avarage_grade_for_course(lecturers_list, 'JS'))