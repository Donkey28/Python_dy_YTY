n, m = map(int, input().split())
image = []
# 读取图像像素值
for _ in range(n):
    row = list(map(int, input().split()))
    image.append(row)

blurred_image = [row[:] for row in image]

# 处理中间像素点
for i in range(1, n - 1):
    for j in range(1, m - 1):
        # 计算当前像素及其上下左右相邻像素的灰度值总和
        total = image[i][j] + image[i - 1][j] + image[i + 1][j] + image[i][j - 1] + image[i][j + 1]
        # 计算平均值并四舍五入
        blurred_image[i][j] = round(total / 5)

# 输出模糊处理后的图像
for row in blurred_image:
    print(" ".join(map(str, row)))

