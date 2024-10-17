import pandas as pd

# print("###### column center ######")
data = {
    '과목번호': ['C1', 'C2', 'C3', 'C4', 'C5', 'C6'],
    '과목명' : ['인공지능개론 ', '웃음치료', '경영학', '3D디자인', '스포츠 경영', '예술의 세계'],
    '강의실' : ['R1', 'R2', 'R3', 'R4', 'R2', 'R3'],
    '시간수' : [3, 2, 3, 4, 2, 1]
}

df = pd.DataFrame(data)
# print(df, end='\n\n')
# print(df.loc[2])
# print(df['과목명'])
# print(df.loc[3]['강의실'])
# print(df.loc[4, '시간수'])

sr_name = df['과목명']
# print(sr_name, end='\n\n')

sr_no = df.loc[2]
# print(sr_no, end='\n\n')

cell_name = df.loc[2]['과목명']
#print(cell_name)

df.to_csv('file.csv', index=False)

df['담당교수'] = ['홍길동', '김철수', '이영희', '박영수', '최영희', '김영수']
# print(df, end='\n\n')

df.loc[6] = ['C7', '연극수업', 'R5', 5, '김석']
# print(df, end='\n\n')
df.to_csv('file2.csv', index=False)

df1 = df.drop(['강의실'], axis=1)
# print(df1, end='\n\n')

df2 = df.drop([6], axis=0)
# print(df2, end='\n\n')

df3 = df.drop(['과목번호', '과목명', '강의실', '시간수'], axis=1)
# print(df3, end='\n\n')

df4 = df.drop([0, 1, 2, 3, 4])
# print(df4, end='\n\n')

# 범위 찾기
print('행 찾기')
print(df, end='\n\n')
print(df.loc[0:2], end='\n\n')
print(df.iloc[0:2], end='\n\n')

print('열 찾기')
print(df[['과목명', '담당교수']], end='\n\n')
print(df.loc[:, '강의실': '담당교수'], end='\n\n')

# 조건 찾기
print('행 찾기')
print(df['과목명'] == '경영학', end='\n\n')
print(df.loc[df['과목명'] == '경영학'], end='\n\n')
print(df.loc[df['시간수'] > 2], end='\n\n') 

print('셀 찾기')
print(df.loc[df['과목명'] == '경영학']['담당교수'], end='\n\n')
print(df.loc[df['과목명'] == '경영학']['담당교수'].values[0], end='\n\n')

# df.loc[3]['담당교수'] = '이경영'
df.loc[3, '담당교수'] = '이경영'
print(df, end='\n\n')

print(df.loc[df['과목명'] == '경영학', '담당교수'].values[0], end='\n\n')