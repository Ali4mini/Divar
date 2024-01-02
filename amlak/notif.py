import divar
import time

COUNTER = 0
def searcher(string,outf="checked_links.txt",inf="checked_links.txt"):

        if string in open(inf,"r").readlines():
            print(f"{string} is here!!!")

        else:
            with open(outf, 'w') as f1:
                f1.write(string)
                print(f"{string}  is added ")
def id_generator(link):
	return link[-8:]


while True:
    divar_obj = divar.Divar("https://divar.ir/s/tehran/buy-apartment/doolab?districts=1017%2C975&user_type=personal")
    link = divar_obj.first_post()
    COUNTER += 1
    link_id = id_generator(link)
    searcher(link_id)

    time.sleep(3)
    if COUNTER == 5:
        del divar_obj
