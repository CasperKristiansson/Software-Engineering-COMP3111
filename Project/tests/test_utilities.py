import sys
sys.path.append('library')
import utilities


def test_generate_data():
    df = utilities.generate_data(100, 50, 50)

    assert len(df) == 100
    assert 45 < df['k1_energy'].mean() < 55
    assert 45 < df['k2_energy'].mean() < 55
