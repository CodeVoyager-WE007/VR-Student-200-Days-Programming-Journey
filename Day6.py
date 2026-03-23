#第6天：VR设备帧率检测工具（函数封装）
def check_vr_fps(device_list,threshold= 90):
  """ 
  VR设备帧率批量检测函数
  :param device_list: 设备参数列表,每个元素为(设备名,分辨率,刷新率)
  :param threshold:达标阀值,默认90Hz
  :return:达标设备列表
  """
  print("【VR设备刷新率检测报告】")
  qualified = []
  for device in device_list:
     name,res,fps = device
     if fps >= threshold:
        status = "达标"
        qualified.append(device)
     else:
       status = "不达标"
     print(f"设备:{name}|分辨率：{res}|刷新率：{fps}Hz|状态：{status}") 

     print(f"设备:{name}|分辨率：{res}|刷新率：{fps}Hz|状态：{status}")       
     return qualified
 #定义设备列表
vr_device = [
   ("Quest 3","2222*3333",90)
   ("Pico 4","4444*5555",90) 
   ("Valve Index","6666*7777",144)
   ("PS VR2","8888*9999",120)
 ]
 #调用函数，默认阀值90Hz
result_90 = check_vr_fps(vr_device)
print("\n"+"="*50+"\n")
 #调用函数，自定义阀值120Hz
result_120 = check_vr_fps(vr_device,threshold=120)
 