import time

# 设置专注时间（以秒为单位）
focus_time = 25 * 60

# 开始计时
start_time = time.time()

# 等待直到计时结束
while True:
    # 计算已经过去的时间
    elapsed_time = time.time() - start_time

    # 如果时间已经过了专注时间，则退出循环
    if elapsed_time >= focus_time:
        break

    # 打印剩余时间
    remaining_time = int(focus_time - elapsed_time)
    print("Remaining Time: ", remaining_time, " seconds ")

    # 等待一秒钟
    time.sleep(1)

# 专注时间已经结束
print("Focus time over!")
