from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()


class Class(Base):
    __tablename__ = 'Class'

    ClassID = Column('Class ID', Integer, primary_key=True, autoincrement=True)
    Name = Column(String, nullable=False)
    Speciality = Column(String, nullable=False)
    students = relationship('EducationSeeker', back_populates='clas')


class EducationSeeker(Base):
    __tablename__ = 'Education seeker'
    StudentID = Column('Student ID', Integer, primary_key=True, autoincrement=True)
    Full_name = Column('Full Name', String, nullable=False)
    Grades = Column(Integer, nullable=False)
    ClassID = Column('Class ID', Integer, ForeignKey('Class.Class ID', onupdate='CASCADE', ondelete='CASCADE'),
                     nullable=False)
    clas = relationship('Class', back_populates='students')



class Subject(Base):
    __tablename__ = 'Subject'
    SubjectID = Column('Subject ID', Integer, primary_key=True, autoincrement=True)
    Hours = Column(Integer, nullable=False)
    Name = Column(String, nullable=False)


class LayOut(Base):
    __tablename__ = 'Lay out'
    Lay_outID = Column('Lay out ID', Integer, primary_key=True, autoincrement=True)
    teacher_id = Column('Teacher ID', Integer, ForeignKey('Teacher.Teacher ID', onupdate='CASCADE', ondelete='CASCADE'),
                        nullable=False)
    SubjectID = Column('Subject ID', Integer, ForeignKey('Subject.Subject ID', onupdate='CASCADE', ondelete='CASCADE'),
                       nullable=False)
    teacher = relationship('Teacher', foreign_keys=[teacher_id])
    subject = relationship('Subject')

class Teacher(Base):
    __tablename__ = 'Teacher'
    teacher_id = Column('Teacher ID', Integer, primary_key=True, autoincrement=True)
    Full_name = Column('Full Name', String, nullable=False)
    Experience = Column(Integer, nullable=False)
    Qualification_category = Column('Qualification category', String, nullable=False)
    lay = relationship('LayOut', foreign_keys=[LayOut.teacher_id], overlaps="teacher")

class Studying(Base):
    __tablename__ = 'Studying'
    StudyingID = Column('Studying ID',Integer, primary_key=True, autoincrement=True)
    ClassID = Column('Class ID',Integer, ForeignKey('Class.Class ID', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    SubjectID = Column('Subject ID',Integer, ForeignKey('Subject.Subject ID', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    class_ = relationship('Class')
    subject = relationship('Subject')

engine = create_engine('postgresql://postgres:admin@localhost:5434/postgres', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

class Model:
    def create_all(self):
        Base.metadata.create_all(engine)

    def add_class(self, name, spec):
        class_ = Class(Name=name, Speciality=spec)
        session.add(class_)
        session.commit()

    def update_class(self, class_id, name, spec):
        class_ = session.query(Class).get(class_id)
        if class_:
            class_.Name = name
            class_.Speciality = spec
            session.commit()
            return 1
        else:
            return 0
    def delete_class(self, class_id):
        class_ = session.query(Class).get(class_id)
        studying = session.query(Studying).filter_by(ClassID=class_id).first()
        if class_ and not studying:
            session.delete(class_)
            session.commit()
            return "Class deleted succesfully"
        else:
            return "There is no such class id"

    def add_education_seeker(self, name, grades, class_id):
        class_ = session.query(Class).get(class_id)
        if class_:
            education_seeker = EducationSeeker(Full_name = name, Grades = grades, ClassID = class_id)
            session.add(education_seeker)
            session.commit()
            return 1
        else:
            return 0

    def update_education_seeker(self, student_id, name, grade, class_id):
        class_ = session.query(Class).get(class_id)
        education_seeker = session.query(EducationSeeker).get(student_id)
        if class_ and education_seeker:
            education_seeker.Full_name = name
            education_seeker.Grades = grade
            education_seeker.ClassID = class_id
            session.commit()
            return 1
        else:
            return 0

    def delete_education_seeker(self, student_id):
        education_seeker = session.query(EducationSeeker).get(student_id)
        if education_seeker:
            session.delete(education_seeker)
            session.commit()
            return 1
        else:
            return 0

    def add_subject(self, hours, name):
        subject = Subject(Hours=hours, Name=name)
        session.add(subject)
        session.commit()

    def update_subject(self, subject_id, hours, name):
        subject = session.query(Subject).get(subject_id)
        if subject:
            subject.Hours = hours
            subject.Name = name
            session.commit()
            return 1
        else:
            return 0
    def delete_subject(self, subject_id):
        subject = session.query(Subject).get(subject_id)
        laying = session.query(LayOut).filter_by(SubjectID=subject_id).first()
        studying = session.query(Studying).filter_by(ClassID=subject_id).first()
        if subject and not laying and not studying:
            session.delete(subject)
            session.commit()
            return 1
        else:
            return 0

    def add_teacher(self, name, exp, qual):
        teacher = Teacher(Full_name=name, Experience=exp, Qualification_category=qual)
        session.add(teacher)
        session.commit()

    def update_teacher(self, teacher_id, name, exp, qual):
        teacher = session.query(Teacher).get(teacher_id)
        if teacher:
            teacher.Full_name = name
            teacher.Experience = exp
            teacher.Qualification_category = qual
            session.commit()
            return 1
        else:
            return 0

    def delete_teacher(self, teacher_id):
        teacher = session.query(Teacher).get(teacher_id)
        laying = session.query(LayOut).filter_by(TeacherID=teacher_id).first()
        if teacher and not laying:
            session.delete(teacher)
            session.commit()
            return 1
        else:
            return 0

    def add_laying(self, teach_id, subject_id):
        teacher = session.query(Teacher).get(teach_id)
        subject = session.query(Subject).get(subject_id)
        if teacher and subject:
            lay_out = LayOut(TeacherID=teach_id, SubjectID=subject_id)
            session.add(lay_out)
            session.commit()
            return 1
        else:
            return 0

    def update_laying(self, laying_id, teach_id, subject_id):
        laying = session.query(LayOut).get(laying_id)
        teacher = session.query(Teacher).get(teach_id)
        subject = session.query(Subject).get(subject_id)
        if laying and teacher and subject:
            laying.TeacherID = teach_id
            laying.SubjectID = subject_id
            session.commit()
            return 1
        else:
            return 0

    def delete_laying(self, laying_id):
        laying = session.query(LayOut).get(laying_id)
        if laying:
            session.delete(laying)
            session.commit()
            return 1
        else:
            return 0

    def add_studying(self, class_id, subject_id):
        class_ = session.query(Class).get(class_id)
        subject = session.query(Subject).get(subject_id)
        if class_ and subject:
            studying = LayOut(ClassID=class_id, SubjectID=subject_id)
            session.add(studying)
            session.commit()
            return 1
        else:
            return 0

    def update_studying(self, studying_id, class_id, subject_id):
        studying = session.query(LayOut).get(studying_id)
        class_ = session.query(Class).get(class_id)
        subject = session.query(Subject).get(subject_id)
        if studying and class_ and subject:
            studying.ClassID = class_id
            studying.SubjectID = subject_id
            session.commit()
            return 1
        else:
            return 0

    def delete_studying(self, studying_id):
        studying = session.query(Studying).get(studying_id)
        if studying:
            session.delete(studying)
            session.commit()
            return 1
        else:
            return 0
