class View:

    def get_teaching_find(self):
        class_name = input("Enter Class name: ")
        subject_name = input("Enter Subject Name: ")
        teacher_name = input("Enter Teacher Name: ")
        return  class_name, subject_name, teacher_name

    def get_find(self):
        class_name = input("Enter Class name: ")
        class_speciality = input("Enter Class specialisation: ")
        subject_hours_min = int(input("Enter Subject min hours: "))
        subject_hours_max = int(input("Enter Subject max hours: "))
        subject_name = input("Enter Subject Name: ")
        teacher_experience_min = int(input("Enter Teacher minimal experience: "))
        teacher_experience_max = int(input("Enter Teacher maximal experience: "))
        teacher_qualification = input("Enter Teacher Qualification: ")
        student_grades_min = input("Enter Students minimal grades: ")
        student_grades_max = input("Enter Students maximum grades: ")
        return class_name, class_speciality, subject_hours_min, subject_hours_max, subject_name, teacher_experience_min, teacher_experience_max, teacher_qualification, student_grades_min, student_grades_max

    def show_classes(self, classes):
        print("Classes:")
        for Class in classes:
            print(f"ID: {Class[0]}, Name: {Class[1]}, Speciality: {Class[2]}")

    def get_class_input(self):
        name = input("Enter Class name: ")
        spec = input("Enter Class specialisation: ")
        return name, spec

    def get_class_id(self):
        return int(input("Enter class ID: "))

    def show_message(self, message):
        print(message)

    def get_generated_num(self):
        return int(input("Enter number of generated entities: "))

    def show_students(self, students):
        print("Education seekers:")
        for Student in students:
            print(f"ID: {Student[0]}, Full Name: {Student[1]}, Grade: {Student[2]}, Class ID {Student[3]}")

    def get_student_input(self):
        name = input("Enter Student Full Name: ")
        grades = input("Enter Student grades: ")
        class_id = input("Enter Student class: ")
        return name, grades, class_id

    def get_student_find_input(self):
        grades_min = input("Enter Students minimal grades: ")
        grades_max = input("Enter Students maximum grades: ")
        class_id = input("Enter Student class: ")
        return grades_min, grades_max, class_id
    def get_student_id(self):
        return int(input("Enter student ID: "))

    def show_subject(self, subjects):
        print("Subjects:")
        for Subjects in subjects:
            print(f"ID: {Subjects[0]}, Hours: {Subjects[1]}, Name: {Subjects[2]}")

    def get_subject_input(self):
        hours = int(input("Enter Subject hours: "))
        name = input("Enter Subject Name: ")
        return hours, name

    def get_subject_find_input(self):
        hours_min = int(input("Enter Subject min hours: "))
        hours_max = int(input("Enter Subject max hours: "))
        name = input("Enter Subject Name: ")
        return hours_min, hours_max, name

    def get_subject_id(self):
        return int(input("Enter subject ID: "))

    def show_teacher(self, teachers):
        print("Teacher:")
        for Teachers in teachers:
            print(f"ID: {Teachers[0]}, Full Name: {Teachers[1]}, Experience: {Teachers[2]}, Qualification: {Teachers[3]}")

    def get_teacher_input(self):
        exp = int(input("Enter Teacher experience: "))
        name = input("Enter Teacher Name: ")
        qual = input("Enter Teacher Qualification: ")
        return name, exp, qual

    def get_teacher_find_input(self):
        exp_min = int(input("Enter Teacher minimal experience: "))
        exp_max = int(input("Enter Teacher maximal experience: "))
        qual = input("Enter Teacher Qualification: ")
        hours_min = int(input("Enter Subject minimal hours: "))
        hours_max = int(input("Enter Subject maximal hours: "))
        subject_name = input("Enter Subject Name: ")


        return exp_min, exp_max, qual, hours_min, hours_max, subject_name

    def get_teacher_id(self):
        return int(input("Enter Teacher ID: "))

    def show_laying(self, laying):
        print("Lay outs:")
        for Laying in laying:
            print(f"ID: {Laying[0]}, Teacher ID: {Laying[1]}, Subject ID: {Laying[2]}")

    def get_laying_input(self):
        teach_id = int(input("Enter Teacher ID: "))
        subject_id = int(input("Enter Subject ID: "))
        return teach_id, subject_id

    def get_laying_id(self):
        return int(input("Enter Laying ID: "))

    def show_studying(self, studying):
        print("Studyings:")
        for Study in studying:
            print(f"ID: {Study[0]}, Class ID: {Study[1]}, Subject ID: {Study[2]}")

    def get_studying_input(self):
        class_id = int(input("Enter Class ID: "))
        subject_id = int(input("Enter Subject ID: "))
        return class_id, subject_id

    def get_studying_id(self):
        return int(input("Enter Studying ID: "))

    def show_founded(self,founded):
        if not founded:
            print('Nothing found!')
        else:
            print(
                f"{'Student Name':<15} {'Grades':<7} {'Class Name':<15} {'Speciality':<15} {'Subject Name':<15} {'Hours':<7} {'Teacher Name':<15} {'Experience':<11} {'Qualification category':<20}")
            for row in founded:
                student_name, grades, class_name, speciality, subject_name, hours, teacher_name, experience, qualification = row
                print(
                    f"{student_name:<15} {grades:<7} {class_name:<15} {speciality:<15} {subject_name:<15} {hours:<7} {teacher_name:<15} {experience:<11} {qualification:<20}")

