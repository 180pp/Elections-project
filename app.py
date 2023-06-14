# -*- coding:UTF-8 -*-
import matplotlib.pyplot as plt
plt.rc('font', family='S-Core Dream')
# 데이터 불러오기

# [40]
import pandas as pd

df = pd.read_excel("data/이념적성향_변동.xlsx", )
df['연도'] = df['연도'].astype('str')
df['구분'] = df['구분'].replace({
    "매우보수적": "보수",
    "다소보수적": "보수",
    "매우진보적": "진보",
    "다소진보적": "진보",
    "중도적" : "중도"
})

df2 = df.groupby(['세대', '연도', '구분'])['비율'].agg('sum').reset_index()
df2

# [41]
df20s = df2[df2['세대'] == '19~29세']
df30s = df2[df2['세대'] == '30~39세']
# 20대와 30대의 비율 차이
# [89]
import seaborn as sns

custom_palette = ['#E61E2B', '#808080', '#004EA1']

fig, ax = plt.subplots(figsize=(10, 6), ncols=2)
sns.lineplot(data = df20s, x = '연도', y = '비율', hue = '구분', ax = ax[0], palette=custom_palette)
ax[0].set_title("19~29세의 이념성향 추이", size=22)
ax[0].set_ylim(0, 100)

sns.lineplot(data = df30s, x = '연도', y = '비율', hue = '구분', ax = ax[1], palette=custom_palette)
ax[1].set_title("30대의 이념성향 추이", size=22)
ax[1].set_ylim(0, 100)
plt.legend(loc="best")
plt.show()

# 갤럽정당지지도
# [75]
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_excel('data/정당지지도_데이터.xlsx')
df['date'] = pd.to_datetime(df[['연도', '주']].astype(str).agg('-W'.join, axis=1) + '-5', format='%Y-W%W-%w')
df

# [77]
df['정당'].unique()
array(['국민의힘', '더불어민주당', '정의당', '무당층'], dtype=object)
# [86]
custom_palette = ['#E61E2B', '#004EA1', '#FFED00', '#808080']

fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(df, x = 'date', y = '10~20', hue = '정당', palette=custom_palette)
ax.set_title("10-20대")
plt.savefig("output/10-20.png", dpi='figure')
plt.show()

# [87]
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(df, x = 'date', y = '30대', hue = '정당', palette=custom_palette)
ax.set_title("30대")
plt.savefig("output/30.png", dpi='figure')
plt.show()
#
# 성별에 따른 정당 지지도의 흐름
# [95]
custom_palette = ['#E61E2B', '#004EA1', '#FFED00', '#808080']

fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(df, x = 'date', y = '남자', hue = '정당', palette=custom_palette)
ax.set_title("정당별 남자 지지도", size=22)
plt.savefig("output/남자.png", dpi='figure')
plt.show()

# [96]
custom_palette = ['#E61E2B', '#004EA1', '#FFED00', '#808080']

fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(df, x = 'date', y = '여자', hue = '정당', palette=custom_palette)
ax.set_title("정당별 여자 지지도", size=22)
plt.savefig("output/여자.png", dpi='figure')
plt.show()

# 1년 뒤
# [101]
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_excel('data/정당지지도_데이터_2023.xlsx')
df['date'] = pd.to_datetime(df[['연도', '주']].astype(str).agg('-W'.join, axis=1) + '-5', format='%Y-W%W-%w')
df

# [108]
custom_palette = ['#E61E2B', '#004EA1', '#FFED00', '#808080']

fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(df, x = 'date', y = '10~20', hue = '정당', palette=custom_palette, errorbar=None)
ax.set_title("10-20대")
plt.savefig("output/10-20_2023.png", dpi='figure')
plt.show()

# [109]
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(df, x = 'date', y = '30대', hue = '정당', palette=custom_palette, errorbar=None)
ax.set_title("30대")
plt.savefig("output/30.png", dpi='figure')
plt.show()

# 세대별 남성 여성 지지도 차이
# [114]
df = pd.read_excel("data/102030th.xlsx")
df.head()

# [120]
df['date'] = pd.to_datetime(df[['연도', '월']].astype(str).agg('-'.join, axis=1), format='%Y-%m')
df.head()

# [128]
custom_palette = ['#E61E2B', '#004EA1', '#808080']

fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(df, x = 'date', y = '10_20_man', hue = '정당', palette=custom_palette, errorbar=None)
ax.set_title("18-29세 남성", size = 26)
ax.set_ylabel("%")
plt.savefig("output/10_20_man.png", dpi='figure')
plt.show()

# [129]
custom_palette = ['#E61E2B', '#004EA1', '#808080']

fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(df, x = 'date', y = '10_20_woman', hue = '정당', palette=custom_palette, errorbar=None)
ax.set_title("18-29세 여성", size=26)
ax.set_ylabel("%")
plt.savefig("output/10_20_woman.png", dpi='figure')
plt.show()

# [132]
custom_palette = ['#E61E2B', '#004EA1', '#808080']

fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(df, x = 'date', y = '30_man', hue = '정당', palette=custom_palette, errorbar=None)
ax.set_title("30대 남성", size = 26)
ax.set_ylabel("%")
plt.savefig("output/30_man.png", dpi='figure')
plt.show()

# [134]
custom_palette = ['#E61E2B', '#004EA1', '#808080']

fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(df, x = 'date', y = '30_woman', hue = '정당', palette=custom_palette, errorbar=None)
ax.set_title("30대 여성", size=26)
ax.set_ylabel("%")
plt.savefig("output/30_woman.png", dpi='figure')
plt.show()

# 수도권
# [11]
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_excel('data/정당지지도_데이터.xlsx')
df['date'] = pd.to_datetime(df[['연도', '주']].astype(str).agg('-W'.join, axis=1) + '-5', format='%Y-W%W-%w')
df

# [4]
custom_palette = ['#E61E2B', '#004EA1', '#FFED00', '#808080']

fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(df, x = 'date', y = '서울', hue = '정당', palette=custom_palette, errorbar=None)
ax.set_title("서울")
plt.savefig("output/서울.png", dpi='figure')
plt.show()

# [13]
custom_palette = ['#E61E2B', '#004EA1', '#FFED00', '#808080']

fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(df, x = 'date', y = '인천/경기', hue = '정당', palette=custom_palette, errorbar=None)
ax.set_title("인천/경기")
plt.savefig("output/인천경기.png", dpi='figure')
plt.show()

