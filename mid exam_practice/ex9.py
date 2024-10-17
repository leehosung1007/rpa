import pandas as pd

data = {'이름' : ['Kim', 'Park', 'Lee', 'Ho'],
        '국어' : [90, 58, 88, 100],
        '영어' : [100, 60, 80, 70],
        '수학' : [55, 65, 76, 88]}

# 1번 문제
df = pd.DataFrame(data)
print('2번 문제')
print(df, end='\n\n')

print('3번 문제')
print(df['이름'], end='\n\n')

print('4번 문제')
print(df.loc[1], end='\n\n')
# print(df.iloc[1], end='\n\n')

print('5번 문제')
# df.loc[3, '수학'] = 90
# df.loc[df['이름'] == 'Ho', '수학'] = 90
# df.loc[df['국어'] > 95, '수학'] = 90
# df.loc[df['영어'] == 70, '수학'] = 90
df.loc[df['수학'] == 88, '수학'] = 90
print(df, end='\n\n')

print('6번 문제')
df.loc[4] = ['oh', 100, 70, 80]
print(df, end='\n\n')

print('7번 문제')
df1 = df.drop([2], axis = 0)
print(df1, end='\n\n')