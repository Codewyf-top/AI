import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from  sklearn.metrics import silhouette_score
# 读取NBA数据球员数据
def load_NBA(file_path):
    """
    读取NBA球员数据
    :param file_path:文件路径+ 文件名称 
    :return: 数据
    """
    data = pd.read_excel(file_path)

    return data


def km_NBA(data):
    """
    进行聚类，并进行预测
    :param data: NBA球员数据
    :return: 
    """
    # 1、数据筛选  #loc用法 同时索引，第一次参数为行索引名称，第二个参数为列索引名称
    data = data.loc[:,["得分","助攻"]]

    # 进行K-means聚类
    # 1、创建k-means估计器实例
    km =KMeans(n_clusters=3)
    # 2、进行训练数据
    km.fit(data)
    # 3、进行聚类预测
    y_predict = km.predict(data)

    return  data,y_predict

def scatter_NBA(data,y_predict):
    """
    绘制图形进行分析
    :param data: 筛选后的数据
    :param y_predict: 预测结果
    :return: None
    """
    color = ["r","g","b"]
    colors = []
    for i in y_predict:
        colors.append(color[i])
    # 1、创建画布
    plt.figure()
    plt.rcParams['font.sans-serif'] = 'SimHei'  # 默认不支持中文，这行代码的意义就是让其支持中文
    plt.rcParams['axes.unicode_minus'] = False  # 默认不支持负数，这行代码的意义就是让其支持负数
    # 2、准备x，y值
    x = data.loc[:,"得分"]
    y = data.loc[:, "助攻"]
    # 绘图
    plt.scatter(x,y,color=colors)
    # 增加图名称
    plt.title("NBA球员数据聚类结果图")
    #增加横轴标签
    plt.xlabel("得分")
    # 增加纵轴标签
    plt.ylabel("助攻")
    # 增加网格曲线
    plt.grid(b=True)
    # 进行图形保存
    plt.savefig("./NBA球员数据聚类结果图.png")
    # 图形展示
    plt.show()
    # 结论
    # 聚为3类
    # 1、得分高 助攻高  分卫
    # 2、得分一般 助攻一般  锋线位置
    # 3、得分少 助攻多  中锋
def score_NBA(data,y_predict):
    """
    进行聚类结果评估
    :param data: 筛选后的球员数据
    :param y_predict: 预测结果
    :return: score
    """
    score = silhouette_score(data[:1000],y_predict[:1000])
    return  score

def main():
    """
    主函数
    :return: 
    """
    # 确定文件路径
    file_name = "./nba_data.xlsx"
    # 加载数据
    data = load_NBA(file_name)

    # 进行聚类
    data,y_predict = km_NBA(data)
    # print(y_predict[:1000])

    # 进行图形化分析
    scatter_NBA(data,y_predict)

    # 评估聚类结果
    score = score_NBA(data,y_predict)
    print(score)

if __name__ == '__main__':
    main()