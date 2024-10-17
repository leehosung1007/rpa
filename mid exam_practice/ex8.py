import pandas as pd

data = {
    '과목번호': ['C1', 'C2', 'C3', 'C4', 'C5', 'C6'],
    '과목명' : ['인공지능개론 ', '웃음치료', '경영학', '3D디자인', '스포츠 경영', '예술의 세계'],
    '강의실' : ['R1', 'R2', 'R3', 'R4', 'R2', 'R3'],
    '시간수' : [3, 2, 3, 4, 2, 1]
}

df = pd.DataFrame(data)
print(df, end='\n\n')

print('1번 문제')
print(df.iloc[2], end='\n\n') # 2 C3 경영학 R3 3

print('2번 문제')
print(df.iloc[0:5], end='\n\n') # 0~4 인덱스의 행만 출력된다.

print('3번 문제')
print(df.iloc[[0, 3, 5]]) # 0, 3, 5의 행만 출력된다.

print('4번 문제')
print(df.iloc[:, 3], end='\n\n') # 모든 행의 시간수만 출력된다.

print('5번 문제')
print(df.iloc[:, 0:3], end='\n\n') # 모든 행의 과목번호, 과목명, 강의실만 출력된다.

print('6번 문제')
print(df.iloc[:, [1, 3]], end='\n\n') # 모든 행의 과목명, 시간수만 출력한다.

print('7번 문제')
print(df.iloc[0:3, 1:3], end='\n\n') # 0~2 행의 과목명, 강의실만 출력한다.

print('8번 문제')
print(df.iloc[[1, 2, 5], [1, 3]], end='\n\n') # 1, 2, 5 행의 과목명, 시간수만 출력한다.

df1 = df.drop([0, 1])
print(df1, end='\n\n')