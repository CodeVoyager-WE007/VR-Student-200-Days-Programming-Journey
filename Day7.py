#第7天：VR设备信息结构化存储
def create_vr_device(name,resolution,refresh_rate,price):
  """"
  创建VR设备字典
  :param name:设备名称
  :param resolution:分辨率
  :param refresh_rate:刷新率
  :param price:价格
  :return:设备字典
  """
  return{
    "name":name,
    "resolution":resolution,
    "refresh_rate":refresh_rate,
    "price":price
  }
def print_vr_info(device_dict):
  """"
  打印VR设备信息
  :param device_dict:设备字典
  """
  print(f"【设备信息：{device_dict['name']}】")
  print(f"分辨率：{device_dict['resolution']}")
  print(f"刷新率：{device_dict['refresh_rate']}Hz")
  print(f"价格：{device_dict['price']}元\n")
    #创建设备字典列表
vr_device = [
    create_vr_device("Quest 3","2064*2208",90,2999),
    create_vr_device("Pico 4","2160*2160",90,2499),
    create_vr_device("Valve Index","1440*1600",144,6888),
    create_vr_device("PS VR2","2000*2040",120,4499),
]
    #遍历打印所有设备信息
for device in vr_device:
  print_vr_info(device)
        #按价格筛选设备（价格<5000元）
  print("【价格<5000元的VR设备】")
  budget_devices = [d for d in vr_device if d["price"] < 5000]
  for d in budget_devices:
    print(f"-{d['name']}:{d['price']}元")

    