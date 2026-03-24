#第8天：VR设备信息文件读写与异常处理
def create_vr_device(name,resolution,refresh_rate,price):
  return{
    "name":name,
    "resolution":resolution,
    "refresh_rate":refresh_rate,
    "price":price,
  }
def print_vr_info(device_dict):
  print(f"【设备信息：{device_dict['name']}】")
  print(f"分辨率：{device_dict['resolution']}")
  print(f"刷新率：{device_dict['refresh_rate']}Hz")
  print(f"价格：{device_dict['price']}元\n")
#1.创建设备列表
vr_devices = [
  create_vr_device("Quest 3","2064*2208",90,2999),
  create_vr_device("Pico 4","2160*2160",90,2499),
  create_vr_device("PS VR2","2000*2040",120,4499),
]
#2.写入文件（异常处理）
try:
   with open("vr_devices.txt","w",encoding="utf-8")as f:
     f.write(f"VR设备信息列表\n")
     f.write(f"====================\n")
     for device in vr_devices:
       f.write(f"名称：{device['name']}\n")
       f.write(f"分辨率：{device['resolution']}\n")
       f.write(f"刷新率：{device['refresh_rate']}Hz\n")
       f.write(f"价格：{device['price']}元\n")
       f.write(f"------------\n")
     print("设备信息已成功写入 vr_device.txt")
except Exception as e:
  print(f"写入文件夹失败：{e}")
  #3.读取文件（异常处理）
  try:
    with open("vr_devices.txt","r",encoding="utf-8")as f:
      content = f.read()
    print("\n读取到文件内容：")
    print("content")
  except FileNotFoundError:
    print("文件不存在，请先执行写入操作")
  except Exception as e:
    print(f"读取文件失败:{e}")