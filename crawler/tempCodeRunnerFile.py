df = pd.DataFrame(data)

# 使用Surprise库的Reader类指定评分范围
reader = Reader(rating_scale=(1, 5))

# 加载数据到Surprise的Dataset对象中
dataset = Dataset.load_from_df(df[['user', 'item', 'rating']], reader)

# 划分训练集和测试集
trainset, testset = train_test_split(dataset, test_size=0.2)

# 使用KNN基础模型，基于用户的协同过滤
model = KNNBasic(sim_options={'user_based': True})

# 训练模型
model.fit(trainset)

# 获取用户5未评分的书籍
user_to_recommend = '5'
items_rated_by_user = df.loc[df['user'] == user_to_recommend, 'item'].unique()
all_items = df['item'].unique()
items_to_recommend = [item for item in all_items if item not in items_rated_by_user]

# 为用户5生成推荐
recommendations = [(item, model.predict(user_to_recommend, item).est) for item in items_to_recommend]

# 按预测评分排序
recommendations.sort(key=lambda x: x[1], reverse=True)

# 输出前N个推荐书籍
N = 5
top_recommendations = recommendations[:N]
for item, predicted_rating in top_recommendations:
    print(f"Item: {item}, Predicted Rating: {predicted_rating:.2f}")