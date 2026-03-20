#第四天：VR设备使用时长累计统计（while循环+累加）
total_minutes = 0 #初始化累计时长，初始值为0
count = 0 #初始化记录天数，初始值为0
#循环条件：输入非数字则结束，数字则累加
while True:
    day_input = input(f"请输入第{count+1}天的VR使用时长（分钟，输入非数字结束统计）:")
    if day_input.replace(".","",1).isdigit():
        day_minutes = float(day_input)
        total_minutes += day_minutes  #累加： totoal_minutes = total_ minutes + day_minutes
        count += 1 #天数+1
        print(f"已记录第{count}天，当日时长：{day_minutes:.1f}分钟，；累计时长：{total_minutes:.1f}分钟")
    else:
        print("输入非数字，结束统计！")
        break #终止while循环
#循环结束后，计算总时长(小时)并输出统计报告
if count > 0:
    total_hours = total_minutes / 60 
    print(f"\n【VR使用时长统计报告】")
    print(f"统计天数：{count}天")
    print(f"累计使用时长统计报告：{total_minutes:.1f}分钟|{total_hours:.2f}小时")
    print(f"日均使用时长:{total_minutes/count:.1f}分钟")
else:
    print("未记录任何有效时长！")