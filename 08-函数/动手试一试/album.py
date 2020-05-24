"""
专辑：编写一个名为 make_album()的函数，它创建一个描述音乐专辑的字典。这个函数应该接受歌手的名字和专辑名，
并返回一个包含这两项信息的字典。使用这个函数创建三个表示不同专辑的字典，并打印每个返回的值，以核实字典正确
地存储了专辑的信息。
给函数 make_album()添加一个可选参数，以便能够存储专辑包含的歌曲数。如果调用这个函数时指定了歌曲数量，就将
这个值添加到表示专辑的字典中。调用这个函数，并至少在一次调用中指定专辑包含的歌曲数。
"""


def make_album(artist, title, tracks=int()):
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
    }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict


album = make_album('the beatles', "sgt. pepper's lonely hearts club band")
print(album)

album = make_album('lady gaga', 'the fame', 13)
print(album)
