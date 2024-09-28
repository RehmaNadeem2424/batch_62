def manage_student_database():
    # Step 1: Initialize the program with an empty list and a counter for student IDs
    students = []
    student_id = 1
    
    # Step 2: Handle user input
    while True:
        # Ask for student name input
        name = input("Please enter the student's name (or type 'stop' to finish): ").strip()
        
        # Check if the user wants to stop the input process
        if name.lower() == 'stop':
            break
        # Step 3: Check for duplicate names
        # If the name is already in the student list, print a message
        if any(student[1].lower() == name.lower() for student in students):
            print("This name is already in the list.")
        else:
            # Add the student to the list with a unique ID
            students.append((student_id, name))
            student_id += 1

    # Step 4: Display the complete list of students
    print("\nComplete List of Students (Tuples):")
    print(students)

    # Step 5: Display each student's ID and name individually
    print("\nList of Students with IDs:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}")

    # Step 6: Calculate and display statistics
    total_students = len(students)
    total_name_length = sum(len(student[1]) for student in students)
    longest_name_student = max(students, key=lambda x: len(x[1]))
    shortest_name_student = min(students, key=lambda x: len(x[1]))

    # Display statistics
    print(f"\nTotal number of students: {total_students}")
    print(f"Total length of all student names combined: {total_name_length}")
    print(f"The student with the longest name is: {longest_name_student[1]}")
    print(f"The student with the shortest name is: {shortest_name_student[1]}")

# Step 7: Call the
manage_student_database()
#function to execute the program
manage_student_database() 