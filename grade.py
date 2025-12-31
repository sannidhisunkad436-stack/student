import sys

def calculate_grade(avg):
    if 90 <= avg <= 100:
        return "S"
    elif 80 <= avg < 90:
        return "A"
    elif 65 <= avg < 80:
        return "B"
    elif 50 <= avg < 65:
        return "C"
    elif 40 <= avg < 50:
        return "D"
    else:
        return "F"

def get_student_result(name, dept, semester, m1, m2, m3):
    avg = (m1 + m2 + m3) / 3
    grade = calculate_grade(avg)

    return (
        f"Name: {name}, Department: {dept}, Semester: {semester}, "
        f"Average: {avg:.2f}, Grade: {grade}"
    )

if __name__ == "__main__":
    print("=== Student Result Program ===")

    try:
        if len(sys.argv) == 7:
            name = sys.argv[1]
            dept = sys.argv[2]
            semester = sys.argv[3]
            m1 = int(sys.argv[4])
            m2 = int(sys.argv[5])
            m3 = int(sys.argv[6])
        else:
            name = input("Enter Student Name: ")
            dept = input("Enter Department: ")
            semester = input("Enter Semester: ")
            m1 = int(input("Enter Subject 1 Marks: "))
            m2 = int(input("Enter Subject 2 Marks: "))
            m3 = int(input("Enter Subject 3 Marks: "))

        print("\n=== Entered Student Details ===")
        print("Name:", name)
        print("Department:", dept)
        print("Semester:", semester)
        print("Marks:", m1, m2, m3)

        result = get_student_result(name, dept, semester, m1, m2, m3)
        print("\nFinal Result:")
        print(result)

    except ValueError:
        print("Invalid input! Please enter numeric marks.")
