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
    def __init__(self, students) -> None:
        self.students = students
        self.teams = []

    def generate_teams(self):
        students_df_copy = self.students.copy()
        students_df_copy.sort_values(by=['k1_energy', 'k2_energy'], inplace=True)

        self.teams = [[] for _ in range(33)]
        self.__add_above_average_student(students_df_copy)

    def __add_above_average_student(self, students_df):
        students_above_mean = students_df[students_df['k1_energy'] >= self.students['k1_energy'].mean()]

        for team in self.teams:
            team.append(students_above_mean.iloc[len(students_above_mean) // 2])
            students_above_mean.drop(students_above_mean.index[len(students_above_mean) // 2], inplace=True)
            students_df.drop(team[-1].name, inplace=True)

    for index, row in students_df.iterrows():
        k1_energy_avg = (sum(student['k1_energy'] for student in teams[0]) + row['k1_energy']) / (len(teams[0]) + 1)
        k2_energy_avg = (sum(student['k2_energy'] for student in teams[0]) + row['k2_energy']) / (len(teams[0]) + 1)
        diff = abs(k1_energy_avg - df['k1_energy'].mean()) + abs(k2_energy_avg - df['k2_energy'].mean())
        if diff < min_diff:
            min_diff = diff
            min_diff_index = index

    teams[0].append(students_df.loc[min_diff_index])
    students_df.drop(min_diff_index, inplace=True)

    return teams


if __name__ == "__main__":
    p = Process()
    print(p)

    team = Team(["A", "B", "C"])
