import numpy as np
import cv2 as cv
 
img = cv.imread("bo.jpg")  #读取当前路径下的图像文件lena,jpg
cv.imshow("bo",img)        # 显示图像，窗口标题未:lena
cv.waitKey(0)                #等待用户输入
cv.destroyAllWindows()       #用户一旦输入任意键后，程序关闭窗口
