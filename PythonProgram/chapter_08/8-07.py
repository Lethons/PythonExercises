def make_album(singer_name, album_name, nums=None):
    album = {
        'singer': singer_name.title(),
        'album': album_name.title(),
    }
    if nums:
        album['nums'] = nums
    return album


print(make_album('jay', 'mojiezhuo'))
print(make_album('vae', 'zidingyi', 5))
