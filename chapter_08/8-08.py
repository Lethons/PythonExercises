def make_album(singer_name, album_name, nums=None):
    album = {
        'singer': singer_name.title(),
        'album': album_name.title(),
    }
    if nums:
        album['nums'] = nums
    return album


while True:
    singer_name = input("singer_name: ")
    album_name = input("album_name: ")
    if singer_name == 'quit' or album_name == 'quit':
        break
    print(make_album(singer_name, album_name))
