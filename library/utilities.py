import pandas as pd
import random


def generate_data(students_amount, k1_energy_avg, k2_energy_avg):
    df = pd.DataFrame(columns=['stu_id', 'stu_name', 'email', 'k1_energy', 'k2_energy', 'k3_tick1', 'k3_tick2', 'my_pref', 'concerns'])

    for i in range(students_amount):
        df.loc[i] = [i, f"Student {str(i)}", f"student{str(i)}@gmail.com", random.randint(0, 100), random.randint(0, 100),
                     random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), "No concerns"
                     ]

    while df['k1_energy'].mean() < k1_energy_avg * 0.95 or df['k1_energy'].mean() > k1_energy_avg * 1.05:
        student = df.iloc[random.randint(0, students_amount - 1)]
        if student['k1_energy'] < 5 or student['k1_energy'] > 95:
            continue

        if df['k1_energy'].mean() > k1_energy_avg:
            df.loc[student.name, 'k1_energy'] -= random.randint(0, 5)
        else:
            df.loc[student.name, 'k1_energy'] += random.randint(0, 5)

    while df['k2_energy'].mean() < k2_energy_avg * 0.95 or df['k2_energy'].mean() > k2_energy_avg * 1.05:
        student = df.iloc[random.randint(0, students_amount - 1)]
        if student['k2_energy'] < 5 or student['k2_energy'] > 95:
            continue

        if df['k2_energy'].mean() > k2_energy_avg:
            df.loc[student.name, 'k2_energy'] -= random.randint(0, 5)
        else:
            df.loc[student.name, 'k2_energy'] += random.randint(0, 5)

    return df


def df_analytics(df):
    stats = f"""
K1 Energy:
{df['k1_energy'].describe()}
-------------

K2 Energy:
{df['k2_energy'].describe()}
-------------

K3 Tick 1:
{df['k3_tick1'].value_counts()}
-------------

K3 Tick 2:
{df['k3_tick2'].value_counts()}
-------------

Amount of rows with k1_energy over average: {len(df[df['k1_energy'] > df['k1_energy'].mean()])}
    """

    print(stats)
