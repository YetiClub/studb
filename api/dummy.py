from studentmanager import db, Student

student_1 = Student(userId='jed@test.com', user_name='jed', user_designation='admin',
                    password='12345678', referral_code_id=9210938822)
db.session.add(student_1)
db.session.commit()
student_2 = Student(userId='jed2@test.com', user_name='jed2', user_designation='',
                    password='12345678', referral_code_id=9210938822)
db.session.add(student_2)
db.session.commit()
