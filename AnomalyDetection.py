import xlrd
import xlwt
from xlutils.copy import copy
import numpy as np
from math import exp, pi

workbook = xlrd.open_workbook("训练数据.xlsx")
sheet = workbook.sheet_by_name("Sheet5")

H = []
W = []
L = []

for i in range(1,sheet.nrows):  
    H.append(sheet.cell(i,3).value)
    W.append(sheet.cell(i,5).value)
    L.append(sheet.cell(i,4).value)


# 均值
u_L = sum(L)/len(L)
u_W = sum(W)/len(W)
u_H = sum(H)/len(H)

mu = np.array([u_H, u_L, u_W])


# 训练样本集合
x = np.array([list(i) for i in zip(*[H,L,W])])

# 协方差矩阵
z = np.zeros((3,3))

for i in range(len(H)):
    a = x[i].reshape(3,1)
    b = x[i].reshape(1,3)
    z += np.matmul(a,b)

z = z/len(H)


# 验证数据集

# 主要错误形式
# 1.高度太高或者太低
# 2.截面高宽不匹配

va = np.array([[1,2000,2000],
               [30,2000,2000],
               [10,4000,1000],
               [10,1000,4000]])

label_1 = np.zeros((len(x),1))
label_2 = np.ones((len(va),1))

# 整合数据集
data = np.append(x,va,axis=0)
labels = np.append(label_1, label_2,axis=0)



ep, f = epSelection(data, labels)












# 定义概率计算函数
def p(x,mu,z):
    # x 是新样本，应为n维的数据。n=len(mu)
    # mu : 训练样本均值
    # z : 训练样本协方差矩阵
    
    n = len(x)
    
    # 系数
    a = 1/((2*pi)**(n/2)*(np.linalg.det(z))**2)
    
    r = -0.5 * np.matmul(np.matmul((x-mu).reshape(1,n), np.linalg.inv(z)), (x-mu).reshape(n,1))
    
    return a * exp(r)  


# 挑选最合适的 ep
def epSelection(data,labels):

	dict = {}

	for i in range(10,100):
	    ep = i*10**(-31)
	    label_p = []
	    tp = 0
	    fn = 0
	    fp = 0
	    
	    for i in range(len(data)):
	        if p(data[i],mu,z)<ep:
	            label_p.append(1)
	        else:
	            label_p.append(0)
	            
	    # 得到算法预测的 label_p，计算 tp,fn,fp
	    for i in range(len(label_p)):
	        if label_p[i]==0 and labels[i]==0:
	            tp += 1
	        elif label_p[i]==0 and labels[i]==1:
	            fn += 1
	        elif label_p[i]==1 and labels[i]==0:
	            fp += 1
	        
	    # prep, rec
	    prep = tp/(tp+fp)
	    rec = tp/(tp+fn)
	    
	    F1 = 2*prep*rec/(prep+rec)
	    dict[ep] = F1

    pair = sorted(dict.items(), key=lambda x:x[1])[-1]

    return pair[0], pair[1]

        