#定义一个VR设备类（图纸）
class VRDevice:
    #初始化方法：创建对象时自动调用，给属性赋值
 def __init__(self,name,resolution,refresh_rate,price):
     self.name = name     #属性：设备名称
     self.resolution = resolution   #属性：分辨率
     self.refresh_rate = refresh_rate     #属性：刷新率
     self.price = price         #属性：价格
      #方法：打印设备信息（你Day9里的print_vr_info升级成类方法）
 def show_info(self):
     print(f"【设备信息：{self.name}】")
     print(f"分辨率：{self.resolution}")
     print(f"刷新率：{self.refresh_rate}Hz")
     print(f"价格：{self.price}元\n")
         #根据图纸创建具体对象（实例）
quest3 = VRDevice("Quest 3","2064*2208",90,2999)
pico4 = VRDevice("Pico 4","2160*2160",90,2499)
psvr2 = VRDevice("PS VR2","2000*2040",120,4499)
#调用对象的方法
quest3.show_info()
pico4.show_info()
psvr2.show_info()