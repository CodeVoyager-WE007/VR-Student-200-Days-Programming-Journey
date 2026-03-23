#第五天：VR设备参数批量检测（for循环+列表）
#定义VR设备参数列表：每个元素为（设备名，分辨率，刷新率）
vr_devices = [
  ("Quest 3","2222*3333",90),
  ("Pico 4","4444*5555",90),
  ("Valve Index","6666*7777",144),
  ("PS VR2","8888*9999",120),
]
#遍历列表，批量检测刷新率是否达标（达标阀值 ：>=90Hz）
print("【VR设备刷新率检测报告】")
for device in vr_devices:
  name,red,fps = device #解包元组，拆分设备信息
  if fps >= 90:
      status = "达标"
  else:
    status = "不达标"
  print(f"设备：{name}|分辨率：{red}|刷新率：{fps}Hz | 状态：{status}")
        #统计达标设备数量
  qualified = [d for d in vr_devices if d[2] >= 90]
  print(f"\n检测总结：共{len(vr_devices)}台设备，达标{len(qualified)}台")