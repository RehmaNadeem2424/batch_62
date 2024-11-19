# STUDENT PERFORMANCE TRACKER:
class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def calculate_average(self):
        return sum(self.scores) / len(self.scores)

    def is_passing(self, passing_score=40):
         return all(score >=passing_score for score in self.scores)

class PerformanceTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name, scores):
        self.students[name] = Student(name, scores)

    def calculate_class_average(self):
        total_score = sum(student.calculate_average() for student in self.students.values())
        return total_score / len(self.students) if self.students else 0

    def display_student_performance(self):
        for student in self.students.values():
            avg_score = student.calculate_average()
            status = "Passing" if student.is_passing() else "Needs Improvement"
            print(f"Student: {student.name}, Average Score: {avg_score:.2f}, Status: {status}")


def main():
    tracker = PerformanceTracker()

    while True:
        name = input("Enter student name (or 'exit' to finish): ")
        if name.lower() == 'exit':
            break

        try:
            scores = [int(input(f"Enter score for subject {i + 1}: ")) for i in range(3)]
            tracker.add_student(name, scores)
        except ValueError:
            print("Invalid input. Please enter numeric scores.")

    print("\n--- Student Performance ---")  
    tracker.display_student_performance()

    class_average = tracker.calculate_class_average()
    print(f"\nClass Average: {class_average:.2f}")

main()