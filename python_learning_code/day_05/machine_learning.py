import pandas as pd
from sklearn.tree import DecisionTreeClassifier as dtc
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib


music_data = pd.read_csv('music.csv')
x = music_data.drop(columns=['genre'])
y = music_data['genre']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# 建立模型
model = dtc()
# 训练
model.fit(x_train, y_train)
# 保存
joblib.dump(model, 'music-model')

predictions = model.predict(x_test)
print(accuracy_score(y_test, predictions))
