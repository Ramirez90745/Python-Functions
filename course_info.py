"""
course_info.py
CSC500 - Module 7 Critical Thinking Assignment
----------------------------------------------
Prompts the user for a course number and displays the course's
room number, instructor, and meeting time.

Author: Laurieann (Solutions Specialist)
"""

# Dictionaries mapping course numbers to details
ROOM_NUMBERS = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411",
}

INSTRUCTORS = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee",
}

MEETING_TIMES = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m.",
}


def lookup_course(course_code: str):
    """
    Given a course code (any case), return a dictionary with details or None if not found.
    """
    key = course_code.strip().upper()
    if key in ROOM_NUMBERS:
        return {
            "course": key,
            "room": ROOM_NUMBERS[key],
            "instructor": INSTRUCTORS[key],
            "time": MEETING_TIMES[key],
        }
    else:
        return None


def main():
    print("Course Info Lookup")
    print("-------------------")
    user_input = input("Enter a course number (e.g., CSC101): ").strip()
    result = lookup_course(user_input)
    if result:
        print(f"Course:      {result['course']}")
        print(f"Room Number: {result['room']}")
        print(f"Instructor:  {result['instructor']}")
        print(f"Meeting Time:{' ' if len(result['time']) < 8 else ''} {result['time']}")
    else:
        print("Sorry, that course was not found. Please check the number and try again.")


if __name__ == "__main__":
    main()
