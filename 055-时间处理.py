from datetime import datetime, timedelta

while True:
    try:
        # 读取给定时刻
        time_str = input().strip()
        # 尝试解析24小时制格式
        try:
            current_time = datetime.strptime(time_str, "%Y %m %d %H %M")
        except ValueError:
            # 解析12小时制格式
            current_time = datetime.strptime(time_str, "%m-%d-%Y %I:%M %p")

        # 读取时间增量
        increment_str = input().strip()
        try:
            # 尝试解析为秒数
            increment_seconds = int(increment_str)
            increment = timedelta(seconds=increment_seconds)
        except ValueError:
            # 解析为日 时 分
            days, hours, minutes = map(int, increment_str.split())
            increment = timedelta(days=days, hours=hours, minutes=minutes)

        # 计算新时刻
        new_time = current_time + increment
        # 输出新时刻
        print(new_time.strftime("%Y-%m-%d %H:%M:%S"))
    except EOFError:
        break

