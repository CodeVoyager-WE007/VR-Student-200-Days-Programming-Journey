#父类：基础VR设备
class VRDevice:
  def __init__(self,name,resolution,refresh_rate,price):
    self.name = name
    self.resolution = resolution
    self.refresh_rate = refresh_rate
    self.price = price

  def show_info(self):
    print(f"【{self.name}】")
    print(f"分辨率：{self.resolution}")
    print(f"刷新率：{self.refresh_rate}Hz")
    print(f"价格：{self.price}元")
#子类1：一体机VR（继承VRDevice）
class StandaloneVR(VRDevice):
  def __init__(self,name,resolution,refresh_rate,price,battery_life):
  #调用父类的__init__,复用父类代码
    super().__init__(name,resolution,refresh_rate,price)
  #子类自己的新属性：续航
    self.battery_life = battery_life
  #重写show_info方法，添加续航信息
  def show_info(self):
    super().show_info()#先调用父类的show_info
    print(f"续航：{self.battery_life}小时\n")
  #子类2：PC端VR（继承VRDevice）
class PCVR(VRDevice):
   def __init__(self,name,resolution,refresh_rate,price,tracking_type):
    super().__init__(name,resolution,refresh_rate,price)
      #子类自己的新属性：追踪类型
    self.tracking_type = tracking_type
      #重写show_info方法
   def show_info(self):
    super().show_info()
    print(f"追踪类型：{self.tracking_type}\n")
#入口：只有直接运行时才执行
if __name__ == "__main__":
  #创建一体机VR对象
    quest3 = StandaloneVR("Quest 3","2064*2208",90,2999,3)
  #创建PC VR对象
    psvr2 = PCVR("PS VR2","2000*2040",120,4499,"眼动追踪")
  #调动方法（多态：不同子类表现不同）
    quest3.show_info()
    psvr2.show_info()