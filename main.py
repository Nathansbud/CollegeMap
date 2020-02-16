from sheets import get_sheet
from enum import Enum

sheet_id = "1Fv9CeJIMJgrKab-HY_5XZH4k75tGNxDcFoqbb5Kxets"
class Status(Enum):
    REGULAR_DECISION_ACCEPT = "RDA"
    REGULAR_DECISION_YEAR_2 = "RDY"
    REGULAR_DECISION_WAITING = "RDN"
    REGULAR_DECISION_REJECT = "RDR",


    EARLY_DECISION_ACCEPT = "EDA"
    EARLY_DECISION_DEFER = "EDD"
    EARLY_DECISION_WAITING = "RDN"
    EARLY_DECISION_RESCIND = "EDC"
    EARLY_DECISION_REJECT = "EDR",

    NO_APPLY = "0"
    OTHER = ""

statuses = {
    "EDA":Status.EARLY_DECISION_ACCEPT,
    "RDA": Status.REGULAR_DECISION_ACCEPT,
    "RDY": Status.REGULAR_DECISION_YEAR_2,
    "EDN":Status.EARLY_DECISION_WAITING,
    "RDN":Status.REGULAR_DECISION_WAITING,
    "EDC":Status.EARLY_DECISION_RESCIND,
    "EDD":Status.EARLY_DECISION_DEFER,
    "RDR":Status.REGULAR_DECISION_REJECT,
    "EDR":Status.EARLY_DECISION_REJECT,
}


class Student:
    def __init__(self, name, colleges):
        self.name = name
        self.colleges = colleges

    def __repr__(self):
        return f"{self.name}: {self.colleges}"

students = {

}

def load_grade():
    sheet = get_sheet(sheet_id, "Colleges!A1:CZ1000").get("values")
    for row in sheet[1:-1]:
        student_status = {}
        for i, status in enumerate(row[1:-1]):
            if status is not None and status != 0:
                if status in statuses:
                    student_status[sheet[0][i+1]] = statuses[status]
        students[row[0]] = Student(row[0], student_status)

load_grade()
print(students["Zack"])
