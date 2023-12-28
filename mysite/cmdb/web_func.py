from django.shortcuts import render, HttpResponseRedirect, HttpResponse
import pymysql
from surprise import Dataset, Reader, KNNBasic
from surprise.model_selection import train_test_split
from cmdb.models import BookInfo, Score
import pandas as pd

def get_data(sql):
    conn=pymysql.connect(host="localhost", user="root", password="653686", database="cmdb",charset="utf8")
    cur = conn.cursor()
    cur.execute(sql)
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results
def get_data1(sql):
    conn=pymysql.connect("localhost","root","1234","PY_Crawler",charset='utf8')
    cur = conn.cursor()
    cur.execute(sql)
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results
def search(sql,args):
    conn = pymysql.connect("localhost", "root", "1234", "PY_Crawler", charset='utf8')
    cur = conn.cursor()
    cur.execute(sql,args)
    conn.commit()
    cur.close()
    conn.close()
def check(sql,args):
    conn=pymysql.connect("localhost","root","1234","PY_Crawler",charset='utf8')
    cur = conn.cursor()
    cur.execute(sql,args)
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results
def get_name(isbn):
    conn = pymysql.connect("localhost", "root", "1234", "PY_Crawler", charset='utf8')
    cur = conn.cursor()
    sql="select name from cmdb_bookinfo where ISBN='{}'".format(isbn)
    cur.execute(sql)
    results = cur.fetchall()

    text=[]
    for it in results:
        text.append(it[0])
    res=text[0]
    for i in range(1, len(text)):
        res=get_CommonSubstr(res,text[i])
    cur.close()
    conn.close()
    return res

def get_CommonSubstr(str1, str2):#求相同子串
    lstr1 = len(str1)
    lstr2 = len(str2)
    record = [[0 for i in range(lstr2 + 1)] for j in range(lstr1 + 1)]  # 多一位
    maxNum = 0  # 最长匹配长度
    p = 0  # 匹配的起始位

    for i in range(lstr1):
        for j in range(lstr2):
            if str1[i] == str2[j]:
                # 相同则累加
                record[i + 1][j + 1] = record[i][j] + 1
                if record[i + 1][j + 1] > maxNum:
                    # 获取最大匹配长度
                    maxNum = record[i + 1][j + 1]
                    # 记录最大匹配长度的终止位置
                    p = i + 1
    return str1[p - maxNum:p]

def cold_start():
    books1=None
    sql = "select * from cmdb.cmdb_best_seller as A left join cmdb.cmdb_bookinfo as B on A.num = B.num order by A.id"
    try:
            books1 = get_data(sql)[:5]
    except:
            books1=None
    return books1

def guess_your_like(username):
    
    # 从数据库中获取数据
    scores = Score.objects.all()
    # 构造数据集
    data = {
        'user': [score.username for score in scores],
        'item': [score.num for score in scores],
        'rating': [score.score for score in scores],
    }
    df = pd.DataFrame(data)

    # 使用Surprise库的Reader类指定评分范围
    reader = Reader(rating_scale=(1, 5))

    # 加载数据
    dataset = Dataset.load_from_df(df[['user', 'item', 'rating']], reader)

    #基于用户的协同过滤
    model = KNNBasic(sim_options={'user_based': True})

    model.fit(dataset.build_full_trainset())

    # 获取用户未评分的书籍
    user_to_recommend =username
    items_rated_by_user = df.loc[df['user'] == user_to_recommend, 'item'].unique()
    all_items = df['item'].unique()
    items_to_recommend = [item for item in all_items if item not in items_rated_by_user]

    # 为用户生成推荐
    recommendations = [(item, model.predict(user_to_recommend, item).est) for item in items_to_recommend]

    
    recommendations.sort(key=lambda x: x[1], reverse=True)

    # 输出前N个推荐书籍
    N = 5
    top_recommendations = recommendations[:N]
    books1num=[]
    for item, predicted_rating in top_recommendations:
        
        books1num.append(item)
        print(f"Item: {item}, Predicted Rating: {predicted_rating:.2f}")

    #基于内容的推荐

    author=Score.objects.filter(username=username, score__gte=4).values('author')
    result = BookInfo.objects.filter(author__in=author).exclude(num__in=Score.objects.values_list('num', flat=True)).values_list('num', flat=True)
    books1num+=result

    return books1num