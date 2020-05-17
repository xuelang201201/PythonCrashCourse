"""检测特定值是否不包含在列表中"""

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print("%s, you can post a response if you wish." % user.title())
