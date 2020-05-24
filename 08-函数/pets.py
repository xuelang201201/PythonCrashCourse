def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a %s." % animal_type)
    print("My %s's name is %s." % (animal_type, pet_name.title()))


describe_pet('hamster', 'harry')
