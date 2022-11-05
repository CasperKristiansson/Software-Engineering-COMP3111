class Team:
    def __init__(self, students) -> None:
        self.students = students
        self.k1_energy_avg = 0
        self.k2_energy_avg = 0
        # self.calculate_energy_avg()

    def calculate_energy_avg(self):
        self.k1_energy_avg = sum(student.k1_energy for student in self.students) / len(self.students)
        self.k2_energy_avg = sum(student.k2_energy for student in self.students) / len(self.students)

    def __str__(self) -> str:
        return f"Team: {self.students}"


class Process:
    def __init__(self) -> None:
        pass


if __name__ == "__main__":
    p = Process()
    print(p)

    team = Team(["A", "B", "C"])
