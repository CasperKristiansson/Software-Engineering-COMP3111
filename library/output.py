"""Contains the classes for managing the output part of the
the program.
"""
__author__ = "Nicole Wijkman"
__email__ = "nwijkman@connect.ust.hk"

import pandas as pd
pd.options.mode.chained_assignment = None


class Output:
    def __init__(self, teams) -> None:
        self.teams = teams

    def student_name_inquiry(self, name_input):
        for team in self.teams:
            for student in team.students:
                if student["stu_name"] == name_input:
                    return True
        
        return False

    def student_id_inquiry(self, id_input):
        for team in self.teams:
            for student in team.students:
                if student.stu_id == id_input:
                    return True
        
        return False

    def display_chart(self):
        k1_avg = []
        k2_avg = []
        k1_k2_avg = []

        for team in self.teams:
            k1_avg.append(team.k1_energy_avg)
            k2_avg.append(team.k2_energy_avg)
            k1_k2_avg.append(team.k1_k2_energy_avg)

        k1_avg.sort(reverse=True)
        zipped_pairs_1 = zip(k1_avg, k2_avg)
        zipped_pairs_2 = zip(k1_avg, k1_k2_avg)
        sorted_k2 = [x for _, x in sorted(zipped_pairs_1)]
        sorted_k1_k2 = [x for _, x in sorted(zipped_pairs_2)]

        df_chart = pd.DataFrame({'k1 AVG':k1_avg, 'k2 AVG':sorted_k2, 'k1 k2 AVG':sorted_k1_k2})
        #df_chart = pd.DataFrame({'k1 AVG':k1_avg, 'k2 AVG':sorted_k2})
        return df_chart