import sys
sys.path.append('library')
from process import Process, Team
from input import Student
import utilities


class TestProcess:
    def generate_process(self):
        df = utilities.generate_data(100, 50, 50)
        students = [Student(row['stu_id'], row['stu_name'], row['email'], row['k1_energy'], row['k2_energy'], row['k3_tick1'], row['k3_tick2'], row['my_pref'], row['concerns']) for _, row in df.iterrows()]

        return Process(students=students)

    def test_process_class(self):
        process = self.generate_process()
        assert len(process.students) == 100

    def test_generate_teams(self):
        process = self.generate_process()
        process.generate_teams()

        students_in_teams = sum(len(team) for team in process.teams)

        assert students_in_teams == 100
        assert 3 <= min(len(team) for team in process.teams) <= 4

    def test_add_above_average_student(self):
        process = self.generate_process()
        remaining_students = process.students
        remaining_students.sort(key=lambda x: (x.k1_energy, x.k2_energy), reverse=True)

        process.teams = [Team() for _ in range(33)]
        process.add_above_average_student(remaining_students)

        assert all(len(team) == 1 for team in process.teams)
        assert all(team.students[0].k1_energy >= process.students_k1_mean for team in process.teams)

    def test_add_pairs(self):
        process = self.generate_process()
        remaining_students = process.students
        remaining_students.sort(key=lambda x: (x.k1_energy, x.k2_energy), reverse=True)

        process.teams = [Team() for _ in range(33)]
        remaining_students = process.add_above_average_student(remaining_students)
        process.add_pairs(remaining_students)

        assert all(len(team) == 3 for team in process.teams)

    def test_add_remaining_student(self):
        process = self.generate_process()
        remaining_students = process.students
        remaining_students.sort(key=lambda x: (x.k1_energy, x.k2_energy), reverse=True)

        process.teams = [Team() for _ in range(33)]
        remaining_students = process.add_above_average_student(remaining_students)
        remaining_students = process.add_pairs(remaining_students)
        process.add_remaining_student(remaining_students)

        assert sum(len(team) for team in process.teams) == 100
