# Student Performance Tracker

This Python script is designed to track student performance by calculating individual and class averages based on scores entered for each student. It also determines if each student is "Passing" or "Needs Improvement" based on a set passing score.

## Code Structure

The code is divided into two main classes and a main function:

1. *Student Class*
2. *PerformanceTracker Class*
3. *Main Function*

### 1. Student Class

The Student class represents each student's data, specifically their name and scores.

#### Attributes:
- name: A string representing the student's name.
- scores: A list of integers representing the student's scores.

#### Methods:
- calculate_average(): Calculates and returns the average of the student's scores.
- is_passing(passing_score=40): Checks if all scores are above or equal to the specified passing_score (default is 40). Returns True if the student is passing, otherwise False.

### 2. PerformanceTracker Class

The PerformanceTracker class is used to manage multiple students and their performance data.

#### Attributes:
- students: A dictionary where each key is a student's name, and the value is a Student object.

#### Methods:
- add_student(name, scores): Adds a new student to the students dictionary.
- calculate_class_average(): Calculates and returns the average score across all students.
- display_student_performance(): Prints the performance of each student, including name, average score, and passing status.

### 3. main Function

The main function provides the user interface for adding students and scores, displaying student performance, and calculating the class average.

#### User Interaction
1. Prompts the user to enter student names and scores for three subjects.
2. Adds each student and their scores to the PerformanceTracker.
3. Displays each student's average score and passing status.
4. Finally, prints the class average.

### Example Usage

1. *Add Students and Scores*:
   - Enter a student's name.
   - Enter scores for three subjects.
   - Type 'exit' when done adding students.

2. *Display Results*:
   - Shows each student's name, average score, and passing status.
   - Displays the class average.


*** Conclusion ***

The Student Performance Tracker is a simple yet effective Python script to monitor and analyze student performance. By leveraging object-oriented principles, it ensures modularity and scalability. Whether for academic purposes or quick evaluations, this script provides a solid foundation for performance tracking and can be easily customized to meet different requiremet.