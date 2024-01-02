import divar
import time

divar_obj = divar.Divar("https://divar.ir/s/tehran/real-estate")
links = divar_obj.all_posts()

def searcher(string,outf="checked_links",inf="checked_links"):
    with open(outf, 'a') as f1:
        if not string in open(inf).readlines():
            f1.write(string+"\n")
            print("done")
def id_generator(link):
	return link[-8:]
while True:
	link_id = id_generator(links[0])
	searcher(link_id)
	time.sleep(40)
