"""Contains the classes for managing the process part of the
the program.
"""
__author__ = "Casper Kristiansson"
__email__ = "cok@connect.ust.hk"

import itertools
import matplotlib.pyplot as plt
# import library.utilities as utilities
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
        self.k1_k2_energy_avg = 0
        self.students = []

    def calculate_energy_avg(self):
        """Calculates the average energy of the team

        Returns:
            None
        """
        self.k1_energy_avg = sum(student.k1_energy for student in self.students) / len(self.students)
        self.k2_energy_avg = sum(student.k2_energy for student in self.students) / len(self.students)
        self.k1_k2_energy_avg = (self.k1_energy_avg + self.k2_energy_avg) / 2

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
        self.students_k1_mean = 0
        self.students_k2_mean = 0
        self.teams = []

        self.calculate_mean()

    def calculate_mean(self):
        """Calculates the mean of K1 and K2 energy

        Args:
            None

        Returns:
            None
        """
        k1_values = [student.k1_energy for student in self.students]
        k2_values = [student.k2_energy for student in self.students]

        self.students_k1_mean = sum(k1_values) / len(k1_values)
        self.students_k2_mean = sum(k2_values) / len(k2_values)

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
        remaining_students = self.students
        remaining_students.sort(key=lambda x: (x.k1_energy, x.k2_energy), reverse=True)

        self.teams = [Team() for _ in range(33)]
        remaining_students = self.add_above_average_student(remaining_students)
        remaining_students = self.add_pairs(remaining_students)
        remaining_students = self.add_remaining_student(remaining_students)

    def add_above_average_student(self, remaining_students):
        """Adds students with above average K1 energy to different teams

        Args:
            remaining_students (list of library.input.Student): students that have not been added to a team

        Returns:
            remaining_students (list of library.input.Student): students that have not been added to a team
        """

        students_above_mean = [student for student in remaining_students if student.k1_energy >= self.students_k1_mean]

        for team in self.teams:
            student = students_above_mean[len(students_above_mean) // 2]
            team.add_student(student)

            students_above_mean.remove(student)
            remaining_students.remove(student)

        return remaining_students

    def add_pairs(self, remaining_students):
        """Adds pairs of students to different teams by creating combinations of 2
        students and adding the pair with the least difference in average energy to the team.

        Args:
            remaining_students (list of library.input.Student): students that have not been added to a team

        Returns:
            remaining_students (list of library.input.Student): students that have not been added to a team
        """
        for team in self.teams:
            student_pairs = list(itertools.combinations(remaining_students, 2))
            min_diff = 100000
            min_diff_index = 0

            for index, pair in enumerate(student_pairs):
                k1_energy_avg = (team.k1_energy_avg + pair[0].k1_energy + pair[1].k1_energy) / (len(team) + 2)
                k2_energy_avg = (team.k2_energy_avg + pair[0].k2_energy + pair[1].k2_energy) / (len(team) + 2)

                diff = abs(k1_energy_avg - self.students_k1_mean) + abs(k2_energy_avg - self.students_k2_mean)
                if diff < min_diff:
                    min_diff = diff
                    min_diff_index = index

            team.add_student(student_pairs[min_diff_index][0])
            team.add_student(student_pairs[min_diff_index][1])

            remaining_students.remove(student_pairs[min_diff_index][0])
            remaining_students.remove(student_pairs[min_diff_index][1])

        return remaining_students

    def add_remaining_student(self, remaining_students):
        """Adds the remaining student to the team with the least difference in average energy

        Args:
            remaining_students (list of library.input.Student): students that have not been added to a team

        Returns:
            remaining_students (list of library.input.Student): students that have not been added to a team
        """
        min_diff = 100000
        min_diff_index = 0

        for index, team in enumerate(self.teams):
            k1_energy_avg = (team.k1_energy_avg + remaining_students[0].k1_energy) / (len(team) + 1)
            k2_energy_avg = (team.k2_energy_avg + remaining_students[0].k1_energy) / (len(team) + 1)

            diff = abs(k1_energy_avg - self.students_k1_mean) + abs(k2_energy_avg - self.students_k2_mean)
            if diff < min_diff:
                min_diff = diff
                min_diff_index = index

        self.teams[min_diff_index].add_student(remaining_students[0])
        remaining_students.remove(remaining_students[0])

        return remaining_students

    def __str__(self) -> str:
        k1_energy_avg = [team.k1_energy_avg for team in self.teams]
        k2_energy_avg = [team.k2_energy_avg for team in self.teams]
        k1_k2_energy_avg = [team.k1_k2_energy_avg for team in self.teams]

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
    # students = utilities.generate_data(100, 64, 64)
    # students = pd.read_csv(r'../data/Sample_Student_Data_File.CSV')
    # utilities.df_analytics(students)

    # p = Process(students)
    # p.generate_teams()

    # print(p)

    from input import Input

    i = Input()
    i.render_data(r'data/Sample_Student_Data_File.CSV')

    p = Process(i.students)
    p.generate_teams()
    print(p)
