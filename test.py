from divar import Divar
import time

divar = Divar(headless=True)
posts = divar.all_posts("https://divar.ir/marketplace/storeslist/tehran/toolbox")
posts = posts[3:]
print(posts)
for post in posts:
    print(divar.post_details(post))

time.sleep(10)
del divar
