import test_numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

# # 데이터 준비
# x = np.arange(0, 6, 0.1)
# y1 = np.sin(x)
# y2 = np.cos(x)

# # 그래프 그리기
# plt.plot(x, y1, label="sin")
# # cos함수는 점선으로
# plt.plot(x, y2, linestyle="--", label="cos") 
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title('sin & cos')
# plt.legend()
# plt.show()

# 이미지 열기
img = imread('poreshe.png')
plt.imshow(img)
plt.show()

