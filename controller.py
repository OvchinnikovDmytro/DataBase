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
                    self.update_class()
                elif choice == '3':
                    self.delete_class()
                elif choice == '4':
                    break
            elif choice == '2':
                choice = self.show_education_seeker()
                if choice == '1':
                    self.add_education_seeker()
                elif choice == '2':
                    self.update_education_seeker()
                elif choice == '3':
                    self.delete_education_seeker()
                elif choice == '4':
                    break
            elif choice == '3':
                choice = self.show_subject()
                if choice == '1':
                    self.add_subject()
                elif choice == '2':
                    self.update_subject()
                elif choice == '3':
                    self.delete_subject()
                elif choice == '4':
                    break
            elif choice == '4':
                choice = self.show_teacher()
                if choice == '1':
                    self.add_teacher()
                elif choice == '2':
                    self.update_teacher()
                elif choice == '3':
                    self.delete_teacher()
                elif choice == '4':
                    break
            elif choice == '5':
                choice = self.show_laying()
                if choice == '1':
                    self.add_laying()
                elif choice == '2':
                    self.update_laying()
                elif choice == '3':
                    self.delete_laying()
                elif choice == '4':
                    break
            elif choice == '6':
                choice = self.show_studying()
                if choice == '1':
                    self.add_studying()
                elif choice == '2':
                    self.update_studying()
                elif choice == '3':
                    self.delete_studying()
                elif choice == '4':
                    break
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
        self.view.show_message("8. Exit")
        return input("Enter your choice: ")

    def show_class(self):
        self.view.show_message("\nClass Menu:")
        self.view.show_message("1. Add Class")
        self.view.show_message("2. Update Class")
        self.view.show_message("3. Delete Class")
        self.view.show_message("4. Quit")
        return input("Enter your choice: ")

    def show_subject(self):
        self.view.show_message("\nClass Menu:")
        self.view.show_message("1. Add Subject")
        self.view.show_message("2. Update Subject")
        self.view.show_message("3. Delete Subject")
        self.view.show_message("4. Quit")
        return input("Enter your choice: ")

    def show_education_seeker(self):
        self.view.show_message("\nEducation seeker Menu:")
        self.view.show_message("1. Add Education seeker")
        self.view.show_message("2. Update Education seeker")
        self.view.show_message("3. Delete Education seeker")
        self.view.show_message("4. Quit")
        return input("Enter your choice: ")

    def show_teacher(self):
        self.view.show_message("\nTeacher Menu:")
        self.view.show_message("1. Add Teacher")
        self.view.show_message("2. Update Teacher")
        self.view.show_message("3. Delete Teacher")
        self.view.show_message("4. Quit")
        return input("Enter your choice: ")

    def show_laying(self):
        self.view.show_message("\nLay out Menu:")
        self.view.show_message("1. Add Lay out")
        self.view.show_message("2. Update Lay out")
        self.view.show_message("3. Delete Lay out")
        self.view.show_message("4. Quit")
        return input("Enter your choice: ")

    def show_studying(self):
        self.view.show_message("\nStudying Menu:")
        self.view.show_message("1. Add Studying")
        self.view.show_message("2. Update Studying")
        self.view.show_message("3. Delete Studying")
        self.view.show_message("4. Quit")
        return input("Enter your choice: ")

    def add_class(self):
        name, spec = self.view.get_class_input()
        self.model.add_class(name, spec)
        self.view.show_message("Class added successfully!")

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

    def add_education_seeker(self):
        name, grades, class_id = self.view.get_student_input()
        res = self.model.add_education_seeker(name, grades, class_id)
        if res:
            self.view.show_message("Education seeker added successfully!")
        else:
            self.view.show_message("Education seeker isnt added.There is no such a class id")

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

    def add_subject(self):
        hours, name = self.view.get_subject_input()
        self.model.add_subject(hours, name)
        self.view.show_message("Subject added successfully!")

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

    def add_teacher(self):
        name, exp, qual = self.view.get_teacher_input()
        self.model.add_teacher(name, exp, qual)
        self.view.show_message("Teacher added successfully!")

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

    def add_laying(self):
        teach_id, subject_id = self.view.get_laying_input()
        res = self.model.add_laying(teach_id, subject_id)
        if res:
            self.view.show_message("Laying out added successfully!")
        else:
            self.view.show_message("Laying out isn't added no such teacher or subject id's")

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

    def add_studying(self):
        class_id, subject_id = self.view.get_studying_input()
        res = self.model.add_studying(class_id, subject_id)
        if res:
            self.view.show_message("Studying out added successfully!")
        else:
            self.view.show_message("Studying out isn't added no such class or subject id's")

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

