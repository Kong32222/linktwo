'''

7.有 41 只猴子围成一圈并从第1只猴子开始编号,然后从猴群中选出一只猴子为大王。
选大王的方法是: 从第1只猴子开始报数, 每轮从1报到3,凡是报到3的猴子将被淘汰, 接着从下一只猴子开始新一轮报数。
每一轮报数会淘汰一只猴子,最后剩下的一只猴子被选为大王。请问当选大王的猴子是第几号?

'''
def find_monkey_king(total_monkeys, step):  
    # 初始化猴子列表，从1编号到total_monkeys  
    monkeys = list(range(1, total_monkeys + 1))  
    index = 0  # 当前报数的起始位置  
  
    while len(monkeys) > 1:  
        # 计算要淘汰的猴子的索引（从0开始）  
        index = (index + step - 1) % len(monkeys)  
        # 淘汰该猴子  
        monkeys.pop(index)  
  
    # 返回最后剩下的猴子的编号  
    return monkeys[0]  
  
# 总猴子数和报数的步长  
total_monkeys = 41  
step = 3  
  
# 找到大王猴子的编号  
monkey_king = find_monkey_king(total_monkeys, step)  
print(f"当选大王的猴子是第{monkey_king}号") 
        

 
