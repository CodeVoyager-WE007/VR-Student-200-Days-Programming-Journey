#第二天：VR设备使用时长健康检测
user_name = input("请输入你的用户名：")
vr_minutes = float(input("请输入本次VR使用时长（分钟）："))
vr_hours = vr_minutes / 60
#条件判断：健康使用时长阀值为1.5小时（90分钟）
if vr_hours <= 1.5:
    print(f"{user_name},本次VR使用时长{vr_hours:.2f}小时，符合健康使用标准！")
else:
    over_time = vr_hours - 1.5
    print(f"{user_name},本次VR使用时长超标{over_time:.2f}小时，建议休息后再使用！")