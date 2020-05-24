def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a %s." % animal_type)
    print("My %s's name is %s." % (animal_type, pet_name.title()))


describe_pet('hamster', 'harry')
# 调用函数多次
describe_pet('dog', 'willie')

# 位置实参的顺序很重要
describe_pet('harry', 'hamster')

# 关键字实参
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

# 默认值
describe_pet(pet_name='willie')
describe_pet(pet_name='harry', animal_type='hamster')

# 等效的函数调用
# 一条名为Willie的小狗
describe_pet('willie')
describe_pet(pet_name='willie')

# 一只名为Harry的仓鼠
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

# 避免实参错误
# describe_pet()
