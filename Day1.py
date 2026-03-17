#第一天：计算设备使用时长
name = input("请输入你的名字：")
use_time = float(input("请输入今天使用VR设备的时间（分钟）："))
hours = use_time /60
print(f"{name},你今天使用VR设备{hours:.2f}小时")