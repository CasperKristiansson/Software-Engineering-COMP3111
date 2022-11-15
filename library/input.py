"""Contains the classes for managing the input part of the
the program.
"""

__author__ = "Michell Dib"
__email__ = "mdib@connect.ust.hk"

import pandas as pd

pd.options.mode.chained_assignment = None

class Input:
    def __init__(self) -> None:
        self.df = None
        self.uploaded_file = None
        self.students = []
        self.file_is_uploaded = False

    def render_data(self, filename):
        self.df = pd.read_csv(filename)

        for _, row in self.df.iterrows():
            self.students.append(row)


class Student:
    def __init__(self,stu_id,stu_name,email,k1_energy,k2_energy,k3_tick1,k3_tick2,my_pref,concerns):
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
    print(i)
