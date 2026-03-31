#父类：基础角色（定义接口）
class Character:
  def __init__(self,name,hp):
    self.name = name
    self.hp = hp #生命值
#通用攻击方法（子类必须重写）
  def attack(self,target):
    pass #空实现，留给子类去写
#子类1：玩家（继承Character）
class Player(Character):
  def __init__(self,name,hp,weapon):
    super().__init__(name,hp)
    self.weapon = weapon#玩家特有属性：武器
    #重写attack方法：玩家用武器攻击
  def attack(self,target):
    damage = 20
    target.hp -= damage
    print(f"【玩家{self.name}】用{self.weapon}攻击了{target.name},造成{damage}点伤害！")
    print(f"{target.name}剩余生命值：{target.hp}")
    #子类2：敌人（继承Character）
class Enemy(Character):
  def __init__(self,name,hp,attack_type):
    super().__init__(name,hp)
    self.attack_type = attack_type #敌人特有属性：攻击类型
#重写attack方法：敌人用自身攻击类型攻击
  def attack(self,target):
    damage = 15
    target.hp -= damage
    print(f"【敌人{self.name}】用{self.attack_type}攻击了{target.name},造成{damage}点伤害！")
    print(f"{target.name}剩余生命值：{target.hp}")
#程序入口
if __name__=="__main__":
#创建角色
    player = Player("勇者",100,"圣剑")
    enemy = Enemy("哥布林",80,"狼牙棒")
#多态调用：同一个attack(),不同对象表现不同
    player.attack(enemy)#玩家攻击敌人
    print("-"*30)
    enemy.attack(player)  #敌人攻击玩家