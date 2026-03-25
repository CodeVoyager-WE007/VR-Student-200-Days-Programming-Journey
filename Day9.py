#Day9 -主程序：导入模块并使用
from vr_utils import(
  create_vr_device,
  print_vr_info,
  filter_by_price,
  filter_by_refresh_rate,
  save_to_file
)
if __name__=="__main__":
#1.创建设备列表
 vr_device = [
    create_vr_device("Quest 3","2064*2208",90,2999),
    create_vr_device("Pico 4","2160*2160",90,2499),
    create_vr_device("Valve Index","1440*1600",144,6888),
    create_vr_device("PS VR2","2000*2040",120,4499),
    create_vr_device("Quest 2","1832*1920",90,1999),
    create_vr_device("Vive Pro 2","2448*2448",120,5999),
]
#2.打印所有设备信息
print("=======所有VR设备信息=======")
for d in vr_device:
   print_vr_info(d)
   #3.价格筛选（<5000元）
   budget_devices = filter_by_price(vr_device,5000)
   print("===价格<5000元的设备===")
   for d in budget_devices:
      print(f"-{d['name']}:{d['price']}元")
      #4.刷新率筛选（>=120Hz）
   high_refresh_devices = filter_by_refresh_rate(vr_device,120)
   print("\n===刷新率>=120Hz的设备===")
   for d in high_refresh_devices:
      print(f"-{d['name']}:{d['refresh_rate']}Hz")
      #5.保存到文件
      if save_to_file(vr_device):
         print("\n所有设备信息已保存到vr_device.txt")
