"""
汽车租赁：编写一个程序，询问用户要租赁什么样的汽车，并打印一条消息，
如 “Let me see if I can find you a Subaru”。
"""
car = input("What kind of car would you like? ")

print("Let me see if I can find you a %s." % car.title())
