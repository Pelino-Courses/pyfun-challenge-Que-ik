
from student import Student
from instructor import Instructor
from course import Course
from enrollment import EnrollmentManager
from teaching_assistant import TeachingAssistant

def demo():
    print("\n\tWelcome to University Enrollment System")

    stud1 = Student("Kenny", "S141")
    ins = Instructor("Dr. Bob", "I102")
    t_ass = TeachingAssistant("Kent", "TA503")

    course1 = Course("Discrete Mathematics", "CS101")

    course1.assign_instructor(ins)

    em = EnrollmentManager()
    em.enroll(stud1, course1)
    em.enroll(t_ass, course1)

    print(f"\nCourse: {course1}")
    print("Enrolled students:")
    for student in course1:
        print(f"  - {student}")

    print(f"\nInstructor: {course1.instructor}")
    print(f"Teaching Assistant Role: {t_ass.get_role()}")


if __name__ == "__main__":
    demo()