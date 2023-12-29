from model import Model
from view import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def run(self):
        while True:
            choice = self.show_menu()
            if choice == '1':
                choice = self.show_class()
                if choice == '1':
                    self.add_class()
                elif choice == '2':
                    self.view_class()
                elif choice == '3':
                    self.update_class()
                elif choice == '4':
                    self.delete_class()
                elif choice == '5':
                    self.generate_class()
                elif choice == '6':
                    self.find_class()
                elif choice == '7':
                    break
            elif choice == '2':
                choice = self.show_education_seeker()
                if choice == '1':
                    self.add_education_seeker()
                elif choice == '2':
                    self.view_education_seeker()
                elif choice == '3':
                    self.update_education_seeker()
                elif choice == '4':
                    self.delete_education_seeker()
                elif choice == '5':
                    self.generate_education_seeker()
                elif choice == '6':
                    self.find_education_seeker()
                elif choice == '7':
                    break
            elif choice == '3':
                choice = self.show_subject()
                if choice == '1':
                    self.add_subject()
                elif choice == '2':
                    self.view_subject()
                elif choice == '3':
                    self.update_subject()
                elif choice == '4':
                    self.delete_subject()
                elif choice == '5':
                    self.generate_subject()
                elif choice == '6':
                    self.find_subject()
                elif choice == '7':
                    break
            elif choice == '4':
                choice = self.show_teacher()
                if choice == '1':
                    self.add_teacher()
                elif choice == '2':
                    self.view_teacher()
                elif choice == '3':
                    self.update_teacher()
                elif choice == '4':
                    self.delete_teacher()
                elif choice == '5':
                    self.generate_teacher()
                elif choice == '6':
                    self.find_teacher()
                elif choice == '7':
                    break
            elif choice == '5':
                choice = self.show_laying()
                if choice == '1':
                    self.add_laying()
                elif choice == '2':
                    self.view_laying()
                elif choice == '3':
                    self.update_laying()
                elif choice == '4':
                    self.delete_laying()
                elif choice == '5':
                    self.generate_laying()
                elif choice == '6':
                    break
            elif choice == '6':
                choice = self.show_studying()
                if choice == '1':
                    self.add_studying()
                elif choice == '2':
                    self.view_studying()
                elif choice == '3':
                    self.update_studying()
                elif choice == '4':
                    self.delete_studying()
                elif choice == '5':
                    self.generate_studying()
                elif choice == '6':
                    break
            elif choice == '7':
                self.find()
            else:
                break

    def show_menu(self):
        self.view.show_message("\nMenu:")
        self.view.show_message("1. Class")
        self.view.show_message("2. Education Seeker")
        self.view.show_message("3. Subject")
        self.view.show_message("4. Teacher")
        self.view.show_message("5. Lay out")
        self.view.show_message("6. Studying")
        self.view.show_message("7. Find")
        self.view.show_message("8. Exit")
        return input("Enter your choice: ")

    def show_class(self):
        self.view.show_message("\nClass Menu:")
        self.view.show_message("1. Add Class")
        self.view.show_message("2. View Class")
        self.view.show_message("3. Update Class")
        self.view.show_message("4. Delete Class")
        self.view.show_message("5. Generate Class")
        self.view.show_message("6. Find Class")
        self.view.show_message("7. Quit")
        return input("Enter your choice: ")

    def show_subject(self):
        self.view.show_message("\nClass Menu:")
        self.view.show_message("1. Add Subject")
        self.view.show_message("2. View Subject")
        self.view.show_message("3. Update Subject")
        self.view.show_message("4. Delete Subject")
        self.view.show_message("5. Generate Subject")
        self.view.show_message("6. Find Subject")
        self.view.show_message("7. Quit")
        return input("Enter your choice: ")

    def show_education_seeker(self):
        self.view.show_message("\nEducation seeker Menu:")
        self.view.show_message("1. Add Education seeker")
        self.view.show_message("2. View Education seeker")
        self.view.show_message("3. Update Education seeker")
        self.view.show_message("4. Delete Education seeker")
        self.view.show_message("5. Generate Education seeker")
        self.view.show_message("6. Find Education seeker")
        self.view.show_message("7. Quit")
        return input("Enter your choice: ")

    def show_teacher(self):
        self.view.show_message("\nTeacher Menu:")
        self.view.show_message("1. Add Teacher")
        self.view.show_message("2. View Teacher")
        self.view.show_message("3. Update Teacher")
        self.view.show_message("4. Delete Teacher")
        self.view.show_message("5. Generate Teacher")
        self.view.show_message("6. Find Teacher")
        self.view.show_message("7. Quit")
        return input("Enter your choice: ")

    def show_laying(self):
        self.view.show_message("\nLay out Menu:")
        self.view.show_message("1. Add Lay out")
        self.view.show_message("2. View Lay out")
        self.view.show_message("3. Update Lay out")
        self.view.show_message("4. Delete Lay out")
        self.view.show_message("5. Generate Lay out")
        self.view.show_message("6. Quit")
        return input("Enter your choice: ")

    def show_studying(self):
        self.view.show_message("\nStudying Menu:")
        self.view.show_message("1. Add Studying")
        self.view.show_message("2. View Studying")
        self.view.show_message("3. Update Studying")
        self.view.show_message("4. Delete Studying")
        self.view.show_message("5. Generate Studying")
        self.view.show_message("6. Quit")
        return input("Enter your choice: ")

    def find(self):
        class_name, class_speciality, subject_hours_min, subject_hours_max, subject_name, teacher_experience_min, teacher_experience_max, teacher_qualification, student_grades_min, student_grades_max = self.view.get_find()
        founded, time = self.model.find(class_name, class_speciality, subject_hours_min, subject_hours_max, subject_name, teacher_experience_min, teacher_experience_max, teacher_qualification, student_grades_min, student_grades_max)
        self.view.show_founded(founded)
        self.view.show_message(f"Execution time: {time*1000}ms")

    def add_class(self):
        name, spec = self.view.get_class_input()
        self.model.add_class(name, spec)
        self.view.show_message("Class added successfully!")

    def view_class(self):
        classes = self.model.get_all_class()
        self.view.show_classes(classes)

    def update_class(self):
        class_id = self.view.get_class_id()
        name, spec = self.view.get_class_input()
        res = self.model.update_class(class_id, name, spec)
        if res:
            self.view.show_message("Class updated successfully!")
        else:
            self.view.show_message("Class is not updated.There is no such Class ID")

    def delete_class(self):
        class_id = self.view.get_class_id()
        res = self.model.delete_class(class_id)
        self.view.show_message(res)

    def generate_class(self):
        count = self.view.get_generated_num()
        self.model.generate_class(count)
        self.view.show_message("Class generated successfully!")

    def find_class(self):
        name, spec = self.view.get_class_input()
        classes = self.model.find_class(name, spec)
        self.view.show_classes(classes)

    def add_education_seeker(self):
        name, grades, class_id = self.view.get_student_input()
        res = self.model.add_education_seeker(name, grades, class_id)
        if res:
            self.view.show_message("Education seeker added successfully!")
        else:
            self.view.show_message("Education seeker isnt added.There is no such a class id")

    def view_education_seeker(self):
        students = self.model.get_all_education_seekers()
        self.view.show_students(students)

    def update_education_seeker(self):
        student_id = self.view.get_student_id()
        name, grade, class_id = self.view.get_student_input()
        res = self.model.update_education_seeker(student_id, name, grade, class_id)
        if res:
            self.view.show_message("Education seeker updated successfully!")
        else:
            self.view.show_message("Education seeker is not updated.There is no such Student ID or Class ID")

    def delete_education_seeker(self):
        student_id = self.view.get_student_id()
        res = self.model.delete_education_seeker(student_id)
        if res:
            self.view.show_message("Education seeker deleted successfully!")
        else:
            self.view.show_message("Education seeker is not deleted.There is no such Student ID")

    def generate_education_seeker(self):
        count = self.view.get_generated_num()
        self.model.generate_education_seeker(count)
        self.view.show_message("Education seeker generated successfully!")

    def find_education_seeker(self):
        grades_min, grades_max, class_id = self.view.get_student_find_input()
        student = self.model.find_education_seeker(grades_min, grades_max, class_id)
        self.view.show_students(student)

    def add_subject(self):
        hours, name = self.view.get_subject_input()
        self.model.add_subject(hours, name)
        self.view.show_message("Subject added successfully!")

    def view_subject(self):
        subjects = self.model.get_all_subject()
        self.view.show_subject(subjects)

    def update_subject(self):
        subject_id = self.view.get_subject_id()
        hours, name = self.view.get_subject_input()
        res = self.model.update_subject(subject_id, hours, name)
        if res:
            self.view.show_message("Subject updated successfully!")
        else:
            self.view.show_message("Subject is not updated.There is no such Subject ID")

    def delete_subject(self):
        subject_id = self.view.get_subject_id()
        res = self.model.delete_subject(subject_id)
        self.view.show_message(res)

    def find_subject(self):
        hours_min, hours_max, name = self.view.get_subject_find_input()
        subjects = self.model.find_subject(hours_min, hours_max, name)
        self.view.show_subject(subjects)

    def generate_subject(self):
        count = self.view.get_generated_num()
        self.model.generate_subject(count)
        self.view.show_message("Subject generated successfully!")

    def add_teacher(self):
        name, exp, qual = self.view.get_teacher_input()
        self.model.add_teacher(name, exp, qual)
        self.view.show_message("Teacher added successfully!")

    def view_teacher(self):
        teacher = self.model.get_all_teacher()
        self.view.show_teacher(teacher)

    def update_teacher(self):
        teacher_id = self.view.get_teacher_id()
        name, exp, qual = self.view.get_teacher_input()
        res = self.model.update_teacher(teacher_id, name, exp, qual)
        if res:
            self.view.show_message("Teacher updated successfully!")
        else:
            self.view.show_message("Teacher is not updated.There is no such Teacher ID")

    def delete_teacher(self):
        teacher_id = self.view.get_teacher_id()
        res = self.model.delete_teacher(teacher_id)
        self.view.show_message(res)

    def find_teacher(self):
        exp_min, exp_max, qual, hours_min, hours_max, subject_name = self.view.get_teacher_find_input()
        teachers = self.model.find_teacher(exp_min, exp_max, qual, hours_min, hours_max, subject_name)
        self.view.show_teacher(teachers)

    def generate_teacher(self):
        count = self.view.get_generated_num()
        self.model.generate_teacher(count)
        self.view.show_message("Teacher generated successfully!")

    def add_laying(self):
        teach_id, subject_id = self.view.get_laying_input()
        res = self.model.add_laying(teach_id, subject_id)
        if res:
            self.view.show_message("Laying out added successfully!")
        else:
            self.view.show_message("Laying out isn't added no such teacher or subject id's")

    def view_laying(self):
        laying = self.model.get_all_laying()
        self.view.show_laying(laying)

    def update_laying(self):
        laying_id = self.view.get_laying_id()
        teach_id, subject_id = self.view.get_laying_input()
        res = self.model.update_laying(laying_id, teach_id, subject_id)
        if res:
            self.view.show_message("Laying updated successfully!")
        else:
            self.view.show_message("Laying is not updated.There is no such Laying ID")

    def delete_laying(self):
        laying_id = self.view.get_laying_id()
        res = self.model.delete_laying(laying_id)
        if res:
            self.view.show_message("Laying deleted successfully!")
        else:
            self.view.show_message("Laying is not deleted.There is no such Laying ID")

    def generate_laying(self):
        count = self.view.get_generated_num()
        self.model.generate_laying(count)
        self.view.show_message("Laying generated successfully!")

    def add_studying(self):
        class_id, subject_id = self.view.get_studying_input()
        res = self.model.add_studying(class_id, subject_id)
        if res:
            self.view.show_message("Studying out added successfully!")
        else:
            self.view.show_message("Studying out isn't added no such class or subject id's")

    def view_studying(self):
        studying = self.model.get_all_studying()
        self.view.show_studying(studying)

    def update_studying(self):
        studying_id = self.view.get_studying_id()
        class_id, subject_id = self.view.get_studying_input()
        res = self.model.update_studying(studying_id, class_id, subject_id)
        if res:
            self.view.show_message("Studying updated successfully!")
        else:
            self.view.show_message("Studying is not updated.There is no such Studying ID")

    def delete_studying(self):
        studying_id = self.view.get_studying_id()
        res = self.model.delete_studying(studying_id)
        if res:
            self.view.show_message("Studying deleted successfully!")
        else:
            self.view.show_message("Studying is not deleted.There is no such Studying ID")

    def generate_studying(self):
        count = self.view.get_generated_num()
        self.model.generate_studying(count)
        self.view.show_message("Studying generated successfully!")