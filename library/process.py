import itertools
import matplotlib.pyplot as plt
import utilities
import pandas as pd
pd.options.mode.chained_assignment = None


class Team:
    """This class represents a team of students

    Attributes:
        k1_energy_avg (float): average K1 energy of the team
        k2_energy_avg (float): average K2 energy of the team
        students (list): list of students in the team

    Methods:
        calculate_energy_avg: calculates the average energy of the team
        add_student: adds a student to the team
    """
    def __init__(self) -> None:
        """Initializes the team

        Args:
            None
        """
        self.k1_energy_avg = 0
        self.k2_energy_avg = 0
        self.students = []

    def calculate_energy_avg(self):
        """Calculates the average energy of the team

        Returns:
            None
        """
        self.k1_energy_avg = sum(student.k1_energy for student in self.students) / len(self.students)
        self.k2_energy_avg = sum(student.k2_energy for student in self.students) / len(self.students)

    def add_student(self, student):
        """Adds a student to the team

        Args:
            student (pandas.DataFrame): student to be added

        Returns:
            None
        """
        self.students.append(student)
        self.calculate_energy_avg()

    def __str__(self) -> str:
        return f"Team: {self.students}"

    def __len__(self):
        return len(self.students)


class Process:
    """This class represents the process of grouping students into teams

    Attributes:
        students (pandas.DataFrame): students to be grouped
        teams (list): list of teams

    Methods:
    """
    def __init__(self, students) -> None:
        """Initializes the process

        Args:
            students (pandas.DataFrame): students to be grouped
        """
        self.students = students
        self.teams = []

    def generate_teams(self):
        """Generates teams. The algorithm is as follows:
            1. Add 33 of students with above average K1 energy to different teams
            2. Perform combinations of 2 students and add the pair with the least difference in average energy to the team
            3. Add the remaining student to the team with the least difference in average energy

        Args:
            None

        Returns:
            None
        """
        students_df_copy = self.students.copy()
        students_df_copy.sort_values(by=['k1_energy', 'k2_energy'], inplace=True)

        self.teams = [Team() for _ in range(33)]
        self.add_above_average_student(students_df_copy)
        self.add_pairs(students_df_copy)
        self.add_remaining_student(students_df_copy)

    def add_above_average_student(self, students_df):
        """Adds students with above average K1 energy to different teams

        Args:
            students_df (pandas.DataFrame): students to be grouped

        Returns:
            None
        """
        students_above_mean = students_df[students_df['k1_energy'] >= self.students['k1_energy'].mean()]

        for team in self.teams:
            team.add_student(students_above_mean.iloc[len(students_above_mean) // 2])
            students_above_mean.drop(students_above_mean.index[len(students_above_mean) // 2], inplace=True)
            students_df.drop(team.students[-1].name, inplace=True)

    def add_pairs(self, students_df):
        """Adds pairs of students to different teams by creating combinations of 2
        students and adding the pair with the least difference in average energy to the team.

        Args:
            students_df (pandas.DataFrame): students to be grouped

        Returns:
            None
        """
        for team in self.teams:
            student_pairs = list(itertools.combinations(students_df.index, 2))
            min_diff = 100000
            min_diff_index = 0

            for index, pair in enumerate(student_pairs):
                k1_energy_avg = (sum(student['k1_energy'] for student in team.students) + students_df.loc[pair[0]]['k1_energy'] + students_df.loc[pair[1]]['k1_energy']) / (len(team) + 2)
                k2_energy_avg = (sum(student['k2_energy'] for student in team.students) + students_df.loc[pair[0]]['k2_energy'] + students_df.loc[pair[1]]['k2_energy']) / (len(team) + 2)
                diff = abs(k1_energy_avg - self.students['k1_energy'].mean()) + abs(k2_energy_avg - self.students['k2_energy'].mean())
                if diff < min_diff:
                    min_diff = diff
                    min_diff_index = index

            team.add_student(students_df.loc[student_pairs[min_diff_index][0]])
            team.add_student(students_df.loc[student_pairs[min_diff_index][1]])
            students_df.drop(student_pairs[min_diff_index][0], inplace=True)
            students_df.drop(student_pairs[min_diff_index][1], inplace=True)

    def add_remaining_student(self, students_df):
        """Adds the remaining student to the team with the least difference in average energy

        Args:
            students_df (pandas.DataFrame): students to be grouped

        Returns:
            None
        """
        min_diff = 100000
        min_diff_index = 0

        for index, team in enumerate(self.teams):
            k1_energy_avg = (sum(student['k1_energy'] for student in team.students) + students_df.iloc[0]['k1_energy']) / (len(team) + 1)
            k2_energy_avg = (sum(student['k2_energy'] for student in team.students) + students_df.iloc[0]['k2_energy']) / (len(team) + 1)
            diff = abs(k1_energy_avg - self.students['k1_energy'].mean()) + abs(k2_energy_avg - self.students['k2_energy'].mean())
            if diff < min_diff:
                min_diff = diff
                min_diff_index = index

        self.teams[min_diff_index].add_student(students_df.iloc[0])
        students_df.drop(students_df.index[0], inplace=True)

    def __str__(self) -> str:
        k1_energy_avg = [sum(student['k1_energy'] for student in team.students) / len(team) for team in self.teams]
        k2_energy_avg = [sum(student['k2_energy'] for student in team.students) / len(team) for team in self.teams]
        k1_k2_energy_avg = [(sum(student['k1_energy'] + student['k2_energy'] for student in team.students) / 2) / len(team) for team in self.teams]

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
    # students = pd.read_csv('data\Sample Student Data File.csv')
    utilities.df_analytics(students)

    p = Process(students)
    p.generate_teams()

    print(p)
