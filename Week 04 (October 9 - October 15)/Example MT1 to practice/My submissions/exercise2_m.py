# Read the grades for the 4 tests
PE1 = int(input())
PE2 = int(input())
PE3 = int(input())
PE4 = int(input())

# Check if the student failed to obtain at least 40% on either PE3 or PE4
if PE3 < 40 or PE4 < 40:
    print("RFF")
else:
    # Compute the practical grade
    best1 = max(PE1, PE2)
    best2 = max(min(PE1, PE2), max(PE3, PE4))

    practical_grade = round((best1 + best2) / 2)
    print(practical_grade)
