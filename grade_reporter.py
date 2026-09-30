# List of learners' scores
scores = [85, 72, 61, 45, 90]

passed = 0
failed = 0
total = 0

# Go through every score and determine the grade
for score in scores:
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"

    print(f"Score: {score} - Grade: {grade}")

    # Count passes and failures
    if score >= 50:
        passed += 1
    else:
        failed += 1

    # Add each score to the running total
    total += score

# Calculate the average
average = total / len(scores)

print(f"Passed: {passed}")
print(f"Failed: {failed}")
print(f"Average: {round(average, 1)}")