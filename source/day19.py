"""
    Day19 Pandas
    Version : 1.0
    Created : 2021.12.30
    Updated : 2021.12.30
    Author  : S.M.Lee
"""
import myutils as mu
import pandas as pd
import numpy as np


data = {'Name':['Poe', 'Crisie', 'Queen', 'Doyle'],
        'Math':[90, 80, 70, 60],
        'Music':[50, 90, 85, 100]}

df = pd.DataFrame(data)
print(df)

mu.cprintTitle('set_index')
ndf1 = df.set_index('Name') # 옮기기만 함 n=0
print(ndf1)

ndf2 = df.set_index(['Math'])
print(ndf2)

ndf3 = df.set_index(['Math', 'Music'])
print(ndf3)

ndf4 = df.set_index('Music', drop=False)    # 인덱스, 데이터 모두 유지 n=2
print(ndf4)

mu.cprintTitle('reindex')
df = pd.DataFrame(data, index=['r0', 'r1', 'r2', 'r3'])
print(df)

nindex = ['r0', 'r1', 'r3', 'r4']
ndf = df.reindex(nindex, fill_value='888')
print(ndf)

nindex = ['r0', 'r1']
ndf = df.reindex(nindex, fill_value='888')
print(ndf)

nindex = ['s0', 's1', 's2', 's3']
ndf = df.reindex(nindex, fill_value='888')
print(ndf)  # idx n을 바꾸면 value도 전부 바뀜

mu.cprintTitle('reset_index')
print(df)
# 인덱스 -> 데이터
ndf = df.reset_index()
print(ndf)
# 데이터 버림
ndf = df.reset_index(drop=True)
print(ndf)
# 담을 변수 필요 없이 영구적으로 바뀜
df.reset_index(drop=True, inplace=True)
print(df)

mu.cprintTitle('sort_index')
ndf = df.set_index('Name')
print(ndf)
ndf2 = ndf.sort_index(ascending=False)
print(ndf2)

mu.cprintTitle('append')
import makedata as md
df1 = pd.DataFrame(md.make_data(5))
df2 = pd.DataFrame(md.make_data(5))
#1
print('df1:\n', df1)
print('df2:\n', df2)
df3 = df1.append(df2)
print('df3:\n', df3)
df4 = df3.reset_index(drop=True)
print('df4:\n', df4); print()
#2
df6 = df1.append(df2, ignore_index=True)
print('df6:\n', df6); print()   #1 == #2

mu.cprintTitle('concat')
df3 = pd.concat([df1, df2]).reset_index(drop=True)
print('df3:\n', df3); print()
df4 = pd.concat([df1, df2], axis=1).reset_index(drop=True)
print('df3:\n', df3); print()
df5 = pd.concat([df3, df1], axis=1).reset_index(drop=True)
print('df5:\n', df5); print()
df6 = pd.concat([df3, df1], axis=1, join='inner').reset_index(drop=True)
print('df6:\n', df6); print() # inner 공통적인 것만 뽑는다

mu.cprintTitle('group by')      # 공통된 특징으로 하나로 묶을 수 있다.
g_df = pd.DataFrame(md.make_data())
print(g_df); print()

mu.cprintTitle('size()')
# size 옵션을 주면 groupby함수를 시각화 할 수 있음
g_df2 = g_df.groupby('Name').size()
g_df3 = g_df.groupby('Name').size().reset_index(name='counts')
print(g_df2)
print(g_df3)

mu.cprintTitle('agg(min), agg(max), agg(mean), agg(median), agg(sum)')
# print(g_df.groupby('Name').agg(min).reset_index()); print()
print('min\n', g_df.groupby('Name').agg('min')); print()
print('max\n', g_df.groupby('Name').agg('max')); print()
print('mean\n', g_df.groupby('Name').agg('mean')); print()
print('median\n', g_df.groupby('Name').agg('median')); print()
print('sum\n', g_df.groupby('Name').agg('sum')); print()
df = g_df.groupby('Name').agg(['min','max','mean','median','sum']).reset_index()
print('all\n', df)

col_data = {
        'Name': df['Name'],
        'Min': df['Age']['min'],
        'Max': df['Age']['max'],
        'Mean': df['Age']['mean'],
        'Median': df['Age']['median'],
        'Sum': df['Age']['sum'],
}

n_df = pd.DataFrame(col_data)
print(n_df)
print()
print('describe()\n', n_df.describe())
print()

n_df2 = n_df.rename(columns={'Name':'Author Name', 'Min':'choisogap'})
print(n_df2)

n_df2.to_excel('foo.xlsx', sheet_name='한글도되냐', engine='xlsxwriter', encoding='utf-8-sig')
