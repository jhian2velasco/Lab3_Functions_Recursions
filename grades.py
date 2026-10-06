# grades.py
def compute_average(scores):
    return sum(scores) / len(scores)

def assign_grade(avg):
    if avg >= 90:
        return "A"
    if avg >= 80:
            return "B"
    if avg >= 70:
            return "C"
    if avg >= 60:
            return "D"
    else:
          return "F"
def generate_remark (grade):
      remarks = {
            "A": "Excellent Performancе",
            "B": "Good Performance",
            "C": "Satisfactory Performance",
            "D": "Needs Improvement",
            "F": "Failing Status"
      }
      return remarks.get(grade, "Invalid Grade")