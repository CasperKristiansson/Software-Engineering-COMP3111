import itertools
import matplotlib.pyplot as plt
import utilities
import pandas as pd
pd.options.mode.chained_assignment = None


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
        self.__add_pairs(students_df_copy)
        self.__add_remaining_student(students_df_copy)

    def __add_above_average_student(self, students_df):
        students_above_mean = students_df[students_df['k1_energy'] >= self.students['k1_energy'].mean()]

        for team in self.teams:
            team.append(students_above_mean.iloc[len(students_above_mean) // 2])
            students_above_mean.drop(students_above_mean.index[len(students_above_mean) // 2], inplace=True)
            students_df.drop(team[-1].name, inplace=True)

    def __add_pairs(self, students_df):
        for team in self.teams:
            student_pairs = list(itertools.combinations(students_df.index, 2))
            min_diff = 100000
            min_diff_index = 0

            for index, pair in enumerate(student_pairs):
                k1_energy_avg = (sum(student['k1_energy'] for student in team) + students_df.loc[pair[0]]['k1_energy'] + students_df.loc[pair[1]]['k1_energy']) / (len(team) + 2)
                k2_energy_avg = (sum(student['k2_energy'] for student in team) + students_df.loc[pair[0]]['k2_energy'] + students_df.loc[pair[1]]['k2_energy']) / (len(team) + 2)
                diff = abs(k1_energy_avg - self.students['k1_energy'].mean()) + abs(k2_energy_avg - self.students['k2_energy'].mean())
                if diff < min_diff:
                    min_diff = diff
                    min_diff_index = index

            team.append(students_df.loc[student_pairs[min_diff_index][0]])
            team.append(students_df.loc[student_pairs[min_diff_index][1]])
            students_df.drop(student_pairs[min_diff_index][0], inplace=True)
            students_df.drop(student_pairs[min_diff_index][1], inplace=True)

    def __add_remaining_student(self, students_df):
        min_diff = 100000
        min_diff_index = 0

        for index, team in enumerate(self.teams):
            k1_energy_avg = (sum(student['k1_energy'] for student in team) + students_df.iloc[0]['k1_energy']) / (len(team) + 1)
            k2_energy_avg = (sum(student['k2_energy'] for student in team) + students_df.iloc[0]['k2_energy']) / (len(team) + 1)
            diff = abs(k1_energy_avg - self.students['k1_energy'].mean()) + abs(k2_energy_avg - self.students['k2_energy'].mean())
            if diff < min_diff:
                min_diff = diff
                min_diff_index = index

        self.teams[min_diff_index].append(students_df.iloc[0])
        students_df.drop(students_df.index[0], inplace=True)

    def __str__(self) -> str:
        k1_energy_avg = [sum(student['k1_energy'] for student in team) / len(team) for team in self.teams]
        k2_energy_avg = [sum(student['k2_energy'] for student in team) / len(team) for team in self.teams]
        k1_k2_energy_avg = [(sum(student['k1_energy'] + student['k2_energy'] for student in team) / 2) / len(team) for team in self.teams]

        plt.plot(k1_energy_avg, label="k1_energy_avg")
        plt.plot(k2_energy_avg, label="k2_energy_avg")
        plt.plot(k1_k2_energy_avg, label="k1_k2_energy_avg")
        plt.legend()
        plt.show()

        return f"""
        Difference between the min and max k1_energy_avg: {max(k1_energy_avg) - min(k1_energy_avg)}
        Difference between the min and max k2_energy_avg: {max(k2_energy_avg) - min(k2_energy_avg)}
        Difference between the min and max k1_k2_energy_avg: {max(k1_k2_energy_avg) - min(k1_k2_energy_avg)}
        """


if __name__ == "__main__":
    students = utilities.generate_data(100, 64, 64)
    utilities.df_analytics(students)

    p = Process(students)
    p.generate_teams()

    print(p)
