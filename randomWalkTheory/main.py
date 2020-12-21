import random
import numpy as np
import matplotlib.pyplot as plt
# plt.hist将序列绘制成直方图
plt.hist(np.random.normal(loc=0.0, scale=1.0, size=1000), bins=30)#bins直方图的柱数
plt.show()
