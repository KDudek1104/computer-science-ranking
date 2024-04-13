import pandas as pd

df = pd.read_excel('dane_uczelni.xlsx')

def convert_to_float(value):
    if isinstance(value, str):
        return float(value.replace(',', '.'))
    else:
        return value

numeric_columns = ['P_ME_ZAR_STUD_P1', 'P_ME_ZAR_STUD_P4', 'P_ME_ZAR_ETAT_DOSW_P4', 'P_ME_ZAR_ETAT_NDOSW_P4']
for column in numeric_columns:
    df[column] = df[column].apply(convert_to_float)

mean_P_ME_ZAR_STUD_P4 = df['P_ME_ZAR_STUD_P4'].mean()
mean_P_ME_ZAR_STUD_P1 = df['P_ME_ZAR_STUD_P1'].mean()
mask_P1 = df['P_ME_ZAR_STUD_P1'].isnull()
df.loc[mask_P1, 'P_ME_ZAR_STUD_P1'] = df.loc[mask_P1, 'P_ME_ZAR_STUD_P4'] * (mean_P_ME_ZAR_STUD_P1 / mean_P_ME_ZAR_STUD_P4)

mask_P4 = df['P_ME_ZAR_STUD_P4'].isnull()
df.loc[mask_P4, 'P_ME_ZAR_STUD_P4'] = df.loc[mask_P4, 'P_ME_ZAR_STUD_P1'] * (mean_P_ME_ZAR_STUD_P4 / mean_P_ME_ZAR_STUD_P1)

mean_P_ME_ZAR_ETAT_NDOSW_P4 = df['P_ME_ZAR_ETAT_NDOSW_P4'].mean()
mean_P_ME_ZAR_ETAT_DOSW_P4 = df['P_ME_ZAR_ETAT_DOSW_P4'].mean()
mask_ETAT_DOSW_P4 = df['P_ME_ZAR_ETAT_DOSW_P4'].isnull()
df.loc[mask_ETAT_DOSW_P4, 'P_ME_ZAR_ETAT_DOSW_P4'] = df.loc[mask_ETAT_DOSW_P4, 'P_ME_ZAR_ETAT_NDOSW_P4'] * (mean_P_ME_ZAR_ETAT_DOSW_P4 / mean_P_ME_ZAR_ETAT_NDOSW_P4)

mask_ETAT_NDOSW_P4 = df['P_ME_ZAR_ETAT_NDOSW_P4'].isnull()
df.loc[mask_ETAT_NDOSW_P4, 'P_ME_ZAR_ETAT_NDOSW_P4'] = df.loc[mask_ETAT_NDOSW_P4, 'P_ME_ZAR_ETAT_DOSW_P4'] * (mean_P_ME_ZAR_ETAT_NDOSW_P4 / mean_P_ME_ZAR_ETAT_DOSW_P4)

df.to_excel('koncowe.xlsx', index=False)
