"""
梦想的度假胜地：编写一个程序，调查用户梦想的度假胜地。使用类似与 “If you could visit
one place in the world, where would you go?” 的提示，并编写一个打印调查结果的代码块。
"""
name_prompt = "\nWhat's your name? "
place_prompt = "If you could visit one place in the world, where would you go?"
continue_prompt = "\nWould you like to let someone else respond? (yes/no) "

responses = {}

while True:
    name = input(name_prompt)
    place = input(place_prompt)

    responses[name] = place

    repeat = input(continue_prompt)
    if repeat != 'yes':
        break

print("\n--- Results ---")
for name, place in responses.items():
    print("%s would like to visit %s." % (name.title(), place.title()))
