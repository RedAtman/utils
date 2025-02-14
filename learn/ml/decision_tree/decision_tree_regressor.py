"""
使用 决策树回归模型(DecisionTreeRegressor)来预测加州房价数据集(California Housing Dataset)的目标值。
"""

from sklearn import tree
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split

# 准备数据
housing = fetch_california_housing()
print(housing.data.shape, housing.target.shape)


x_data = housing.data
y_data = housing.target


# 设置随机种子
# 为了确保结果可复现，可以在 train_test_split 和 DecisionTreeRegressor 中设置随机种子
# random_state=42 是一个常用的随机种子值
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, random_state=42)


# 训练模型
# 决策树模型容易过拟合，可以通过调整参数来优化模型性能
# 例如，限制树的最大深度 max_depth，可以减少过拟合
model = tree.DecisionTreeRegressor(max_depth=5, random_state=42)
model.fit(x_train, y_train)


# 评估模型
# 使用测试集数据评估模型的性能。
# score 方法返回模型的 决定系数（R²），表示模型对目标值的解释能力。
model.score(x_test, y_test)


# 交叉验证
# 使用交叉验证评估模型的泛化能力。
from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, x_data, y_data, cv=5)
print("Cross-validation scores:", scores)
print("Mean score:", scores.mean())


# 可视化决策树
# 可以使用 graphviz 可视化决策树模型
import graphviz

dot_data = tree.export_graphviz(
    model, out_file=None, feature_names=housing.feature_names, filled=True
)
graph = graphviz.Source(dot_data)
graph.render("california_housing_tree")  # 保存为 PDF 文件
graph.view()  # 直接显示


# 特征重要性
# 查看决策树模型中各特征的重要性
import pandas as pd

feature_importance = pd.Series(model.feature_importances_, index=housing.feature_names)
print(feature_importance.sort_values(ascending=False))


# 测试模型
# 使用模型进行预测，输入测试数据，输出预测结果。
import numpy as np

# 创建 10 条样本，每条样本包含 8 个特征
x_test_custom = np.array(
    [
        [8.3252, 41.0, 6.984127, 1.023810, 322.0, 2.555556, 37.88, -122.23],
        [5.2500, 52.0, 5.818182, 1.073059, 496.0, 2.181818, 34.05, -118.24],
        [3.8462, 52.0, 6.281853, 1.081081, 558.0, 2.094340, 33.93, -118.41],
        [4.0368, 52.0, 4.761905, 1.097561, 565.0, 2.181818, 34.05, -118.24],
        [3.6591, 52.0, 4.931507, 1.041667, 413.0, 2.095890, 33.89, -118.40],
        [3.1200, 52.0, 4.797917, 1.061224, 371.0, 2.095890, 33.89, -118.40],
        [2.0804, 42.0, 4.294118, 1.061224, 315.0, 2.095890, 33.89, -118.40],
        [3.6912, 52.0, 4.970588, 1.061224, 330.0, 2.095890, 33.89, -118.40],
        [3.2031, 52.0, 5.477612, 1.061224, 330.0, 2.095890, 33.89, -118.40],
        [3.2705, 52.0, 5.477612, 1.061224, 330.0, 2.095890, 33.89, -118.40],
    ]
)
# 使用模型进行预测
y_pred_custom = model.predict(x_test_custom)

# 打印预测结果
print("Predicted House Prices:")
print(y_pred_custom)
