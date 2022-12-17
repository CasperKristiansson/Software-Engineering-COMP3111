import unittest
import sys
sys.path.append('library')
from output import Output
from process import Process
from input import Input
import pandas as pd


class TestOutput(unittest.TestCase):
    def generate_process(self):
        input = Input()
        input.render_data('data\Sample_Student_Data_File.CSV')

        process = Process(input.students)

        return process

    def test_student_name_inquiry(self):
        process = self.generate_process()
        process.generate_teams()

        output = Output(process.teams)

        name_df = output.student_name_inquiry('SAFFRON, Corgipoo')

        example_df = pd.DataFrame({
                        'Team no.': [32],
                        'Teammate 1': ['HOREBOUND, Birman'],
                        'Teammate 2': ['TARRAGON, Crocodia'],
                        'Teammate 3': ['SAFFRON, Corgipoo'],
                        'K1 average energy': 46.3333,
                        'K2 average energy': 66.6667},
                        columns=('Team no.', 
                            'Teammate 1', 'Teammate 2', 'Teammate 3', 
                            'K1 average energy', 'K2 average energy'))

        pd.testing.assert_frame_equal(name_df, example_df)

    def test_student_id_inquiry(self):
        process = self.generate_process()
        process.generate_teams()

        output = Output(process.teams)

        id_df = output.student_id_inquiry('20004488')

        example_df = pd.DataFrame({
                        'Team no.': [32],
                        'Teammate 1': ['HOREBOUND, Birman'],
                        'Teammate 2': ['TARRAGON, Crocodia'],
                        'Teammate 3': ['SAFFRON, Corgipoo'],
                        'K1 average energy': 46.3333,
                        'K2 average energy': 66.6667},
                        columns=('Team no.', 
                            'Teammate 1', 'Teammate 2', 'Teammate 3', 
                            'K1 average energy', 'K2 average energy'))

        pd.testing.assert_frame_equal(id_df, example_df)

    def test_sort_based_on(self):
        list1 = ['4', '3', '5', '1', '2']
        list2 = ['b', 'c', 'a', 'e', 'd']

        list2 = Output.sort_based_on(list1, list2)

        assert list2 == ['e', 'd', 'c', 'b', 'a']
    
    def test_sort_lists(self):
        list1 = ['1', '2', '3', '4', '5']
        list2 = ['a', 'b', 'c', 'd', 'e']
        list3 = ['e', 'd', 'c', 'b', 'a']

        list1, list2, list3 = Output.sort_lists(list1, list2, list3)

        assert list1 == ['5', '4', '3', '2', '1']
        assert list2 == ['e', 'd', 'c', 'b', 'a']
        assert list3 == ['a', 'b', 'c', 'd', 'e']
    
    def test_display_chart(self):
        process = self.generate_process()
        process.generate_teams()

        output = Output(process.teams)

        chart_df = output.display_chart()

        example_k1 = [61.666666666666664, 59.0, 58.0, 57.333333333333336, 57.0, 56.666666666666664, 55.75, 55.333333333333336, 55.333333333333336, 55.333333333333336, 55.333333333333336, 55.333333333333336, 55.0, 55.0, 55.0, 55.0, 55.0, 55.0, 55.0, 55.0, 55.0, 55.0, 55.0, 55.0, 55.0, 54.666666666666664, 54.666666666666664, 54.666666666666664, 54.666666666666664, 54.333333333333336, 51.0, 49.666666666666664, 46.333333333333336]
        example_k2 = [55.0, 65.0, 65.0, 66.66666666666667, 68.33333333333333, 70.0, 71.25, 66.66666666666667, 66.66666666666667, 65.0, 65.0, 65.0, 66.66666666666667, 66.66666666666667, 65.0, 65.0, 65.0, 65.0, 65.0, 65.0, 65.0, 65.0, 65.0, 65.0, 63.333333333333336, 66.66666666666667, 66.66666666666667, 65.0, 65.0, 63.333333333333336, 66.66666666666667, 66.66666666666667, 66.66666666666667]
        example_k1_k2 = [58.33333333333333, 62.0, 61.5, 62.0, 62.666666666666664, 63.33333333333333, 63.5, 61.0, 61.0, 60.16666666666667, 60.16666666666667, 60.16666666666667, 60.833333333333336, 60.833333333333336, 60.0, 60.0, 60.0, 60.0, 60.0, 60.0, 60.0, 60.0, 60.0, 60.0, 59.16666666666667, 60.66666666666667, 60.66666666666667, 59.83333333333333, 59.83333333333333, 58.833333333333336, 58.833333333333336, 58.16666666666667, 56.5]

        example_df = pd.DataFrame({'K1':example_k1, 'K2':example_k2, 'K1 + K2':example_k1_k2})

        pd.testing.assert_frame_equal(chart_df, example_df)
        
if __name__ == '__main__':
    unittest.main()
