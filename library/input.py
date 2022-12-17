"""Contains the classes for managing the input part of the
the program.
"""

__author__ = "Michell Dib"
__email__ = "mdib@connect.ust.hk"

import pandas as pd


class Input:
    """This class represents an Input class

    Attributes:
        df (pandas.DataFrame): dataframe of the input file
        uploaded_file (str): name of the uploaded file
        students (list): list of students in the input file
        file_is_uploaded (bool): whether a file has been uploaded


    Methods:
        render_data: renders the data from the input file
    """
    def __init__(self) -> None:
        """Initializes the input class by initialising the students list,
        uploaded file, dataframe, file_is_uploaded boolean to False.
        

        Args:
            None
        """
        self.df = None
        self.uploaded_file = None
        self.students = []
        self.file_is_uploaded = False

    
    def render_data(self, filename):
        """Renders the data from the input file by reading the file and
        creating a dataframe. It also creates a list of students.

        Args:
            filename (str): name of the uploaded file
        
        Returns:
            None
        """
        self.df = pd.read_csv(filename)
        for _, row in self.df.iterrows():
            self.students.append(Student(row['stu_id'], row['stu_name'], row['email'], row['k1_energy'], row['k2_energy'], row['k3_tick1'], row['k3_tick2'], row['my_pref'], row['concerns']))


class Student:
    """This class represents a student

    Attributes:
        stu_id (str): student id
        stu_name (str): student name
        email (str): student email
        k1_energy (str): student's k1 energy level
        k2_energy (str): student's k2 energy level
        k3_tick1 (str): student's k3_tick1 energy level
        k3_tick2 (str): student's k3_tick2 energy level
        my_pref (str): student's preference
        concerns (str): student's concerns
        
    Methods:
        None
    """
    def __init__(self, stu_id, stu_name, email, k1_energy, k2_energy, k3_tick1, k3_tick2, my_pref, concerns):
        """Initializes the student
        
        Args:
            stu_id (str): student id
            stu_name (str): student name
            email (str): student email
            k1_energy (str): student's k1 energy level
            k2_energy (str): student's k2 energy level
            k3_tick1 (str): student's k3_tick1 energy level
            k3_tick2 (str): student's k3_tick2 energy level
            my_pref (str): student's preference
            concerns (str): student's concerns
        """
        self.stu_id = stu_id
        self.stu_name = stu_name
        self.email = email
        self.k1_energy = k1_energy
        self.k2_energy = k2_energy
        self.k3_tick1 = k3_tick1
        self.k3_tick2 = k3_tick2
        self.my_pref = my_pref
        self.concerns = concerns

if __name__ == "__main__":
    i = Input()
    #i.render_data(r'data/Sample_Student_Data_File.CSV')
    print(i)
