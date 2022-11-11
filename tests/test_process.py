import sys
sys.path.append('library')
from process import Process
import utilities


class TestProcess:
    def test_class_students(self):
        df = utilities.generate_data(100, 50, 50)
        process = Process(df)

        assert len(process.students) == 100

    def test_generate_teams(self):
        df = utilities.generate_data(100, 50, 50)
        process = Process(df)

        process.generate_teams()

        students_in_teams = sum(len(team) for team in process.teams)

        assert students_in_teams == 100
        assert 3 <= min(len(team) for team in process.teams) <= 4

    def test_add_above_average_student(self):
        df = utilities.generate_data(100, 50, 50)
        process = Process(df)

        students_df_copy = process.students.copy()
        students_df_copy.sort_values(by=['k1_energy', 'k2_energy'], inplace=True)

        process.teams = [[] for _ in range(33)]
        process.add_above_average_student(students_df_copy)

        assert all(len(team) == 1 for team in process.teams)

        assert all(team[0]['k1_energy'] >= process.students['k1_energy'].mean() for team in process.teams)

    def test_add_pairs(self):
        df = utilities.generate_data(100, 50, 50)
        process = Process(df)

        students_df_copy = process.students.copy()
        students_df_copy.sort_values(by=['k1_energy', 'k2_energy'], inplace=True)

        process.teams = [[] for _ in range(33)]
        process.add_above_average_student(students_df_copy)
        process.add_pairs(students_df_copy)

        assert all(len(team) == 3 for team in process.teams)

    def test_add_remaining_student(self):
        df = utilities.generate_data(100, 50, 50)
        process = Process(df)

        students_df_copy = process.students.copy()
        students_df_copy.sort_values(by=['k1_energy', 'k2_energy'], inplace=True)

        process.teams = [[] for _ in range(33)]
        process.add_above_average_student(students_df_copy)
        process.add_pairs(students_df_copy)
        process.add_remaining_student(students_df_copy)

        students_in_teams = sum(len(team) for team in process.teams)
        assert students_in_teams == 100
