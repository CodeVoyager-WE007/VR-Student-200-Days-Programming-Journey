class VRDevice:
  def __init__(self,name,price):
    self.name = name
      #私有属性：外部不能直接改
    self.__price = price
      #获取价格
  def get_price(self):
    return self.__price
   #修改价格（带安全判断）
  def set_price(self,new_price):
   if new_price > 0:
       self.__price = new_price
   else:
    print("价格不能为负数！")
  def show_info(self):
    print(f"设备：{self.name}")
    print(f"价格：{self.__price}")
if __name__ == "__main__":
    vr = VRDevice("Quest3",2999)
    vr.show_info()
      #正确修改方式
    vr.set_price(2799)
    print("修改后的价格：",vr.get_price())
      #错误示范（不会生效，还会提示）
    vr.set_price(-100)