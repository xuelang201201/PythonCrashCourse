"""遍历整个列表"""
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    # print(magician)
    print("%s, that was a great trick!" % magician.title())
    print("I can't wait to see your next trick, %s.\n" % magician.title())

print("Thank you, everyone. That was a great magic show!")
