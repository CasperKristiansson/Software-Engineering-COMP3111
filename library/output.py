"""Contains the classes for managing the output part of the
the program.
"""
__author__ = "Nicole Wijkman"
__email__ = "nwijkman@connect.ust.hk"

import pandas as pd
pd.options.mode.chained_assignment = None


class Output:
    """This class represents the output process of finding a students team
    and creating a chart that teams up performance by Team Average

    Attributes:
        teams: list of teams
        students: list of students in the team
        k1_energy_avg (float): average K1 energy of the team
        k2_energy_avg (float): average K2 energy of the team

        All attributes are taken from the Process class

    Methods:
        student_name_inquiry: finds a students team based on their name
            and returns a dataframe with the team information

        student_id_inquiry: finds a students team based on their student ID
            and returns a dataframe with the team information

        display_chart: sorts the energies by descending order based on K1 and
            then returns a dataframe with the chart information
    """

    def __init__(self, teams) -> None:
        """Initializes the process

        Args:
            teams: teams to go through
        """
        self.teams = teams

    def student_name_inquiry(self, name_input):
        """Finds a students team based on a students name

        Returns:
            a dataframe with information about the team to be
            displayed in a table
        """
        for index, team in enumerate(self.teams):
            for student in team.students:
                if str(student.stu_name) == name_input:
                    df = pd.DataFrame({
                        'Team no.': [index + 1],
                        'Teammate 1': [str(team.students[0].stu_name)],
                        'Teammate 2': [str(team.students[1].stu_name)],
                        'Teammate 3': [str(team.students[2].stu_name)],
                        'K1 average energy': [team.k1_energy_avg],
                        'K2 average energy': [team.k2_energy_avg]},
                        columns=('Team no.', 
                            'Teammate 1', 'Teammate 2', 'Teammate 3', 
                            'K1 average energy', 'K2 average energy'))

                    return df
        
        return None

    def student_id_inquiry(self, id_input):
        """Finds a students team based on a students student ID

        Returns:
            a dataframe with information about the team to be
            displayed in a table
        """
        for index, team in enumerate(self.teams):
            for student in team.students:
                if str(student.stu_id) == id_input:
                    df = pd.DataFrame({
                        'Team no.': [index + 1],
                        'Teammate 1': [str(team.students[0].stu_name)],
                        'Teammate 2': [str(team.students[1].stu_name)],
                        'Teammate 3': [str(team.students[2].stu_name)],
                        'K1 average energy': [team.k1_energy_avg],
                        'K2 average energy': [team.k2_energy_avg]},
                        columns=('Team no.', 
                            'Teammate 1', 'Teammate 2', 'Teammate 3', 
                            'K1 average energy', 'K2 average energy'))

                    return df
        
        return None

    def sort_based_on(list1, list2):
        """Sorts the list list2 based on the first list list1

        Returns:
            list2 sorted based on list1 in ascending order
        """
        array1 = list1
        array2 = list2

        zipped_pairs = zip(array1, array2)

        return [x for _, x in sorted(zipped_pairs)]

    def sort_lists(list1, list2, list3):
        """Sorts the two lists list2 and list3 based on list1,
            all in descending order

        Returns:
            list1 sorted in descending order
            list2 and list3 sorted after list1 in descending order
        """
        list2 = Output.sort_based_on(list1, list2)
        list2 = list2[::-1]

        list3= Output.sort_based_on(list1, list3)
        list3 = list3[::-1]

        list1.sort(reverse=True)

        return list1, list2, list3

    def display_chart(self):
        """Collects the information from the Process class and
            creates and returns a dataframe for the chart

        Returns:
            a dataframe with information about the chart
        """
        k1_avg = []
        k2_avg = []
        k1_k2_avg = []

        for team in self.teams:
            k1_avg.append(team.k1_energy_avg)
            k2_avg.append(team.k2_energy_avg)
            k1_k2_avg.append(team.k1_k2_energy_avg)

        k1_avg, k2_avg, k1_k2_avg = Output.sort_lists(k1_avg, k2_avg, k1_k2_avg)

        df_chart = pd.DataFrame({'K1':k1_avg, 'K2':k2_avg, 'K1 + K2':k1_k2_avg})

        return df_chart