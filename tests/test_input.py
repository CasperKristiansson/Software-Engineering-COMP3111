import unittest
import sys
sys.path.append('library')
from input import Input, Student
import utilities
import pandas as pd

class TestInput(unittest.TestCase):
    def test_create_student(self):
        test_student = Student("test_id", "test_name", "test_email", "test_k1", "test_k2", "test_k3_tick1", "test_k3_tick2", "test_pref", "test_concerns")
        self.assertEqual(test_student.stu_id, "test_id")
        self.assertEqual(test_student.stu_name, "test_name")
        self.assertEqual(test_student.email, "test_email")
        self.assertEqual(test_student.k1_energy, "test_k1")
        self.assertEqual(test_student.k2_energy, "test_k2")
        self.assertEqual(test_student.k3_tick1, "test_k3_tick1")
        self.assertEqual(test_student.k3_tick2, "test_k3_tick2")
        self.assertEqual(test_student.my_pref, "test_pref")
        self.assertEqual(test_student.concerns, "test_concerns")
        print("test_create_student passed")

    def test_create_input(self):
        test_input = Input()
        self.assertEqual(test_input.df, None)
        self.assertEqual(test_input.uploaded_file, None)
        self.assertEqual(test_input.students, [])
        self.assertEqual(test_input.file_is_uploaded, False)
        print("test_create_input passed")

    def test_render_data(self):
        test_input = Input()
        test_input.df = pd.read_csv(r'data/Sample_Student_Data_File.CSV')
        #test_input.render_data(r'data/Sample_Student_Data_File.CSV')
        pd.testing.assert_frame_equal(test_input.df, pd.read_csv(r'data/Sample_Student_Data_File.CSV'))
        pd.testing.assert_series_equal(test_input.df['stu_id'], pd.read_csv(r'data/Sample_Student_Data_File.CSV')['stu_id'])
        pd.testing.assert_series_equal(test_input.df['stu_name'], pd.read_csv(r'data/Sample_Student_Data_File.CSV')['stu_name'])
        pd.testing.assert_series_equal(test_input.df['email'], pd.read_csv(r'data/Sample_Student_Data_File.CSV')['email'])
        pd.testing.assert_series_equal(test_input.df['k1_energy'], pd.read_csv(r'data/Sample_Student_Data_File.CSV')['k1_energy'])
        pd.testing.assert_series_equal(test_input.df['k2_energy'], pd.read_csv(r'data/Sample_Student_Data_File.CSV')['k2_energy'])
        pd.testing.assert_series_equal(test_input.df['k3_tick1'], pd.read_csv(r'data/Sample_Student_Data_File.CSV')['k3_tick1'])
        pd.testing.assert_series_equal(test_input.df['k3_tick2'], pd.read_csv(r'data/Sample_Student_Data_File.CSV')['k3_tick2'])
        pd.testing.assert_series_equal(test_input.df['my_pref'], pd.read_csv(r'data/Sample_Student_Data_File.CSV')['my_pref'])
        pd.testing.assert_series_equal(test_input.df['concerns'], pd.read_csv(r'data/Sample_Student_Data_File.CSV')['concerns'])
        print("test_render_data passed")
    
if __name__ == '__main__':
    unittest.main()
