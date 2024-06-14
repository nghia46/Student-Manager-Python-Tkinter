import sqlite3
from tools import generate_random_id

connString = r".\StudentDB"

class Student:
    def __init__(self, id, name, age, gpa):
        self.id = id
        self.name = name
        self.age = age
        self.gpa = gpa

    @classmethod
    def from_db(cls, student_data):
        id, name, age, gpa = student_data
        return cls(id, name, age, gpa)

    @staticmethod
    def get_all_students():
        conn = sqlite3.connect(connString)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Student")
        rows = cursor.fetchall()
        conn.close()
        return [Student.from_db(row) for row in rows]

    @staticmethod
    def get_student_by_id(student_id):
        conn = sqlite3.connect(connString)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Student WHERE id = ?", (student_id,))
        rows = cursor.fetchall()
        conn.close()
        return [Student.from_db(row) for row in rows]
    @staticmethod
    def search_student_by_name(student_name):
        conn = sqlite3.connect(connString)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Student WHERE name LIKE ?", (f"%{student_name}%",))
        rows = cursor.fetchall()
        conn.close()
        return [Student.from_db(row) for row in rows]
    @staticmethod
    def update(id, new_name, new_age, new_gpa):
        conn = sqlite3.connect(connString)
        cursor = conn.cursor()
        try:
            cursor.execute("UPDATE Student SET name = ?, age = ?, gpa = ? WHERE id = ?", (new_name, new_age, new_gpa, id))
            conn.commit()
            if cursor.rowcount > 0:
                print(f"Student: {id}, {new_name}, {new_age}, {new_gpa} has been updated successfully!")
                return True
            else:
                print("No student found with the provided ID")
                return False
        except Exception as e:
            print("Error updating student:", e)
            return False
        finally:
            conn.close()

    @staticmethod
    def delete(student_id):
        conn = sqlite3.connect(connString)
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM Student WHERE id = ?", (student_id,))
            conn.commit()
            if cursor.rowcount > 0:
                print("Student with ID {} deleted successfully".format(student_id))
                return True
            else:
                print("No student found with ID {}".format(student_id))
                return False
        except Exception as e:
            print("Error deleting student:", e)
            return False
        finally:
            conn.close()

    @staticmethod
    def add_new_student(new_name, new_age, new_gpa):
        new_id = generate_random_id()
        conn = sqlite3.connect(connString)
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO Student (id, name, age, gpa) VALUES (?, ?, ?, ?)", (new_id, new_name, new_age, new_gpa))
            conn.commit()
            print(f"Student: {new_id}, {new_name}, {new_age}, {new_gpa} has been added!")
            return True
        except Exception as e:
            print("Error adding new student:", e)
            return False
        finally:
            conn.close()