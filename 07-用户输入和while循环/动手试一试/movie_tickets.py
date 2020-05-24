"""
电影票：有家电影院根据观众的年龄收取不同的票价：不到 3 岁的观众免费；3~12 岁的观众为 10 美元；
超过 12 岁的观众为 15 美元。请编写一个循环，在其中询问用户的年龄，并指出其票价。
"""
prompt = "How old are you?"
prompt += "\nEnter 'quit' when you are finished. "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        price = 0
    elif age < 12:
        price = 10
    else:
        price = 15

    if price == 0:
        print("You can watch movie for free.")
    else:
        print("Your ticket is $%d." % price)
