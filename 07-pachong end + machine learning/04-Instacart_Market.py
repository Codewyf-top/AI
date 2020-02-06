import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
with open ('aisles.csv')as path_aisies:
    aisles = pd.read_csv(path_aisies)
with open ('order_products__prior.csv')as order_products_prior:
    order_products_prior = pd.read_csv(order_products_prior)
    # print(order_products_prior)
with open ('orders.csv')as orders:
    orders = pd.read_csv(orders)
    # print(orders)
with open ('products.csv')as products:
    products = pd.read_csv(products)
    # print(products)

#合并数据
tmp= pd.merge(left=aisles,right=products,on=["aisle_id"])

tmp= pd.merge(left=tmp,right=order_products_prior,on=["product_id"])

tmp= pd.merge(left=tmp,right=orders,on=["order_id"])
# print(tmp)

#3、构建user_id和aisle之间关系
#交叉表
#将user_id 做为行索引，将aisle 作为列索引进行交叉表建立
result = pd.crosstab(index=tmp['user_id'],columns=tmp['aisle'])
# print(result)

#4、数据降维——1、数据量大 2、数据之间某些数据相关性高 3、为了减小数据量
#n_components 如果为整数，则表明最后合成几个特征
#如果为小数，则表示保留多少特性
pca=PCA(n_components=0.8)#创建实例
data = pca.fit_transfomr(result)#进行数据降维，返回降维后的数据
# print(data)
#5、进行K-means聚类
km = KMeans(n_clusters=3)#构建kmeans估计器实例
km.fit(data)#训练数据
y_predict = km.predict(data)#预测数据

#6、进行预测评估——轮廓系数
score = silhouette_score(data[:1000],y_predict[:1000])#越趋近于1效果越好
print(score)