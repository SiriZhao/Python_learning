from time import sleep

def progress_bar(sleep_time):
    print("正在加载...")
    
    for i in range(101):
        print(f"\r{'█' * i}{'░' * (100 - i)} {i}%", end="", flush=True)
        sleep(sleep_time)

    print("\n进度完成！")

progress_bar(0.05)  # 调用进度条函数，设置每0.05秒更新一次进度条
