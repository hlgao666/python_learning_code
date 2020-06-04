import pandas as pd
import graphviz
from sklearn.tree import DecisionTreeClassifier as dtc
from sklearn import tree

music_data = pd.read_csv('music.csv')
x = music_data.drop(columns=['genre'])
y = music_data['genre']

# 建立模型
model = dtc()
# 训练
model.fit(x, y)

dot_data = tree.export_graphviz(model, out_file='music-recommend.dot',
                                feature_names=['age', 'gender'],
                                class_names=sorted(y.unique()),
                                label='all',
                                rounded=True,
                                filled=True)

with open("music-recommend.dot") as f:
    dot_graph = f.read()
dot = graphviz.Source(dot_graph)
dot.view()
