#vr_utils.py - VR设备工具模块
def create_vr_device(name,resolution,refresh_rate,price):
  """创建VR设备字典"""
  device = {
    "name":name,
    "resolution":resolution,
    "refresh_rate":refresh_rate,
    "price":price
  }
  print("DEBUG:设备字典键:",list(device.keys()))
  return device
def print_vr_info(device_dict):
  """打印VR设备信息"""
  print(f"【设备信息：{device_dict['name']}】")
  print(f"分辨率：{device_dict['resolution']}")
  print(f"刷新率：{device_dict['refresh_rate']}Hz")
  print(f"价格：{device_dict['price']}元\n")
def filter_by_price(devices,max_price):
    """按价格上限筛选设备"""
    return [d for d in devices if d["price"] < max_price]
def filter_by_refresh_rate(devices,min_rate):
    """按最低刷新率筛选设备"""
    return [d for d in devices if d["price"] >= min_rate]
def save_to_file(devices,filename="vr_devices.txt"):
  """将设备信息写入文件"""
  try:
    with open(filename,"w",encoding="utf-8") as f:
      f.write("VR设备信息列表\n")
      f.write("==================\n")
      for d in devices:
        f.write(f"名称:{d['name']}\n")
        f.write(f"分辨率:{d['resolution']}\n")
        f.write(f"刷新率:{d['refresh_rate']}Hz\n")
        f.write(f"价格:{d['price']}元\n")
        f.write("----------------------\n")
      return True
  except Exception as e:
    print (f"写入失败：{e}")
    return False