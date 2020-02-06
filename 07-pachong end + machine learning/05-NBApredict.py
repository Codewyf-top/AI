import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
#load nba data
def load_NBA(file_path):
    """
    读取nba球员数据
    :param file_path: 文件路径+文件名称
    :return: 
    """

    nba_data = pd.read_excel(file_path)

    return nba_data
def km_nba(data):
    """
    使用nba球员数据对球员位置进行聚类
    :param data: 数据
    :return: None
    """
    # 进行数据筛选

    data = data.ix[:,"得分","助攻"]

    #进行kmeans聚类
    km = KMeans(n_clusters=3)#构建估计器实例
    km.fit(data)#训练数据
    y_predict = km.predict(data)#进行预测

    return data,y_predict

def scatter_nba(data,y_predict):
    """
    绘图分析
    :param data: 筛选后的球员数据
    :param y_predict:预测结果
    :return: None
    """
    color = ["r","g","b"]
    colors = []
    for c in y_predict:
        colors.append(color[c])
    #创建画布
    plt.figure()
    plt.rcParams['font.sans-serif'] = 'SimHei'
    plt.rcParams['axes.unicode_minus'] = False
    #绘图
    #准备横轴数据 准备纵轴数据 数据量太大，我们只拿前300行数据进行展示
    x = data["得分"][:300]
    y = data["助攻"][:300]
    #绘制散点图
    plt.scatter(x, y,color = colors)
    #增加横轴标签
    plt.xlabel("得分")
    #增加纵轴标签
    plt.ylabel("助攻")
    #增加标题
    plt.title("NBA球员得分、助攻关系图")
    #增加网格线
    plt.grid()
    #保存图形

    plt.savefig("./nba_pos.png")
    #图形展示
    plt.show()

def nba_pos_score(data,y_predict):
    """
    进行结果评估
    :param data: 筛选后的nba球员数据
    :param y_predict: 预测结果
    :return: score
    """
    silhouette_score(data[:1000],y_predict[:1000])
def main():
    """
    主函数
    :return: 
    """
    #加载数据
    nba_data = load_NBA("./nba_data.xlsx")
    # print(nba_data)
    #利用球员数据进行预测
    data,y_predict = km_nba(nba_data)

    #进行绘图分析
    scatter_nba(data)

    #进行结果评估
    score = nba_pos_score(data,y_predict)
    print(score)
if __name__ == '__main__':
    main()

#聚类分析
#1、聚维3类
    # 得分高、助攻也高 --->分卫位置
    # 得分一般、助攻一般 --->锋线位置
    # 得分少、助攻多 ------>中锋