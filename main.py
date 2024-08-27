import wallhavenapi
import time
wallhaven_api= wallhavenapi.WallhavenApiV1(api_key="API_KEY")

i = 1
walls_list = []
while True:
    wallpapers_page = wallhaven_api.search(q="id:113998", purities=[wallhavenapi.Purity.sfw], atleast=(1920, 1080), ratios=[(16, 9)], page=i)["data"]
    if len(wallpapers_page) == 0:
        break
    for wallpaper in wallpapers_page:
        walls_list.append(wallpaper["id"])
    i += 1

for wall in walls_list:
    wallhaven_api.download_wallpaper(wall, "walls/{}.jpg".format(wall))

# import os
# walls_links=[]
# walls_files = os.listdir("walls")
# for i in range(len(walls_files)):
#     wall_id = walls_files[i].split(".")[0]
#     try:
#         wallpaper_url = wallhaven_api.wallpaper(wall_id)['data']['path']
#     except:
#         time.sleep(60)
#         wallpaper_url = wallhaven_api.wallpaper(wall_id)['data']['path']
#     walls_links.append(wallpaper_url)
#     print(f"{i}/{len(walls_files)}")
#     if i % 10 == 0:
#         time.sleep(7)
#     # two_letters = wallname[0:2]
#     # walls_links.append(f"https://w.wallhaven.cc/full/{two_letters}/wallhaven-{wallname}.jpg")

print(walls_links)