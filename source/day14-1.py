"""
    Day14 Visualization
    Version : 1.0
    Created : 2021.12.16
    Updated : 2021.12.16
    Author  : S.M.Lee
"""
import matplotlib.pyplot as plt

print('*' * 40)
print('Visualization')
print('*' * 40)


figure = plt.figure()
axes = figure.add_subplot(3, 40, 11)
print(axes) # 터미널에 위치 정보
plt.show()

figure2 = plt.figure()
axes11 = figure2.add_subplot(121)
axes12 = figure2.add_subplot(122)
plt.show()

figure3 = plt.figure()
axes31 = figure3.add_subplot(331)
axes35 = figure3.add_subplot(335)
axes39 = figure3.add_subplot(339)
plt.show()


# plot
figure = plt.figure()
axes = figure.add_subplot(221)
x = [0, 1, 2, 3, 4]
y = [4, 1, 3, 5, 2]
#axes.plot(x, y)
#plt.show()

y2 = [0, 8, 5, 3, 1]
axes.plot(x, y, linestyle='dotted', linewidth='10') # 좌표 그리기
axes.plot(x, y2, color='r', marker='o')
# plt.show()

# 한글처리를 위해
import matplotlib as mpl
path = 'C:/Windows/Fonts/HMFMPYUN.TTF'
name = mpl.font_manager.FontProperties(fname=path).get_name()
mpl.rc('font', family=name)

axes = figure.add_subplot(222)
x = ['봄', '여름', '가을', '겨울']
y = [4, 1, 3, 5]
axes.plot(x, y)
#plt.show()

axes = figure.add_subplot(223)
axes.bar(x, y)
plt.title('계절별 분포')
plt.xlabel('계절')
plt.ylabel('분포')
#plt.show()

# scatter
axes = figure.add_subplot(224)
x = [1, 2, 3, 4, 5, 6]
y = [6, 4, 2, 1, 7, 5]
size = [50, 100, 150, 600, 250, 300]
color = ['red', 'green', 'blue', 'orange', 'aqua', 'crimson']
axes.scatter(x, y, s=size, c=color)
plt.show()

figure2 = plt.figure()
axes = figure2.add_subplot(111)
data = [1, 2, 3, 4, 5, 6]
label = ['m1', 'm2', 'm3', 'm4', 'm5', 'm6']
axes.pie(data, labels=label, autopct='%0.1f%%')
plt.legend(label, loc='center right')
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="whitegrid")

# Load the example diamonds dataset
diamonds = sns.load_dataset("diamonds")
print(type(diamonds))

# Draw a scatter plot while assigning point colors and sizes to different
# variables in the dataset
f, ax = plt.subplots(figsize=(6.5, 6.5))
sns.despine(f, left=True, bottom=True)
clarity_ranking = ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]
sns.scatterplot(x="carat", y="price",
                hue="clarity", size="depth",
                palette="ch:r=-.2,d=.3_r",
                hue_order=clarity_ranking,
                sizes=(1, 8), linewidth=0,
                data=diamonds, ax=ax)
plt.show()