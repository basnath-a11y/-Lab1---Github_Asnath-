import csv

def get_assignment_details():
    """Collects and validates assignment details from the user."""
    while True:
        name = input("Enter assignment name: ").strip()
        if name:
            break
        print("Assignment name cannot be empty.")

    while True:
        category = input("Enter category (FA/SA): ").strip().upper()
        if category in ["FA", "SA"]:
            break
        print("Invalid category! Must be 'FA' or 'SA'.")

    while True:
        try:
            grade = float(input("Enter grade (0–100): "))
            if 0 <= grade <= 100:
                break
            print("Grade must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            weight = float(input("Enter weight (positive number): "))
            if weight > 0:
                break
            print("Weight must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")

    return {
        "Assignment": name,
        "Category": category,
        "Grade": grade,
        "Weight": weight,
        "WeightedScore": (grade / 100) * weight
    }


def print_summary(assignments):
    print("\n===== GRADE SUMMARY =====")

    total_FA = sum(a["WeightedScore"] for a in assignments if a["Category"] == "FA")
    total_SA = sum(a["WeightedScore"] for a in assignments if a["Category"] == "SA")

    total_grade = total_FA + total_SA
    gpa = (total_grade / 100) * 5.0

    print(f"Total FA Weighted: {total_FA:.2f}")
    print(f"Total SA Weighted: {total_SA:.2f}")
    print(f"Final Grade: {total_grade:.2f}%")
    print(f"GPA: {gpa:.2f}")

    # Pass/Fail Logic
    fa_weight_sum = sum(a["Weight"] for a in assignments if a["Category"] == "FA")
    sa_weight_sum = sum(a["Weight"] for a in assignments if a["Category"] == "SA")

    passed_FA = total_FA >= (fa_weight_sum * 0.50)
    passed_SA = total_SA >= (sa_weight_sum * 0.50)

    if passed_FA and passed_SA:
        print("Status: PASS")
    else:
        print("Status: FAIL (Failed category requirements)")


def save_to_csv(assignments):
    with open("grades.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Assignment", "Category", "Grade", "Weight"])
        for a in assignments:
            writer.writerow([a["Assignment"], a["Category"], a["Grade"], a["Weight"]])

    print("\nData saved to grades.csv")


def main():
    assignments = []

    print("===== Grade Generator =====")

    while True:
        assignments.append(get_assignment_details())
        again = input("Add another assignment? (y/n): ").strip().lower()
        if again != 'y':
            break

    print_summary(assignments)
    save_to_csv(assignments)


if __name__ == "__main__":
    main()
