# Problem 5
names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
scores = [88, 72, 95, 64, 81]

# -------------------------
# Task 1: Print roster
# -------------------------
print("=== CLASS ROSTER ===")

for i in range(len(names)):
    print(f"{i+1}. {names[i]} - {scores[i]}")

print("====================")

# -------------------------
# Task 2: Highest and lowest (no max/min)
# -------------------------
highest_score = scores[0]
lowest_score = scores[0]
highest_index = 0
lowest_index = 0

for i in range(1, len(scores)):
    if scores[i] > highest_score:
        highest_score = scores[i]
        highest_index = i
    if scores[i] < lowest_score:
        lowest_score = scores[i]
        lowest_index = i

print("Highest:", names[highest_index], "-", highest_score)
print("Lowest:", names[lowest_index], "-", lowest_score)

# -------------------------
# Task 3: Class average
# -------------------------
total = 0
for s in scores:
    total += s

average = total / len(scores)
print(f"Class Average: {average:.2f}")

# -------------------------
# Task 4: Letter grades
# -------------------------
print("\n--- Grade Report ---")

for i in range(len(scores)):
    score = scores[i]

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"{names[i]}: {score} -> {grade}")

# -------------------------
# Task 5: Add Frank and remove Diana
# -------------------------
names.append("Frank")
scores.append(77)

# find Diana's index and remove both
diana_index = names.index("Diana")
names.pop(diana_index)
scores.pop(diana_index)

print("\nUpdated roster length:", len(names))

# problem 4

gpa = float(input("Enter GPA (0.0–4.0): "))
credits = int(input("Enter completed credit hours: "))
prereq = input("Completed prerequisite course (yes/no): ").strip().lower()

if gpa >= 3.5 and credits >= 60 and prereq == "yes":
    print("Approved: You meet all requirements.")

elif gpa >= 3.5 and credits >= 60 and prereq != "yes":
    print("Conditionally approved: Complete the prerequisite first.")

elif gpa >= 3.0 and credits >= 45:
    print("Waitlisted: You may be admitted if space is available.")

elif gpa >= 2.0:
    print("Not eligible yet: Raise your GPA or earn more credits.")

else:
    print("Denied: GPA is below minimum threshold.")

# problem 3
