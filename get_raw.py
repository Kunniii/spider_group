from threading import Thread
from Spider import Spider

cookie = "__utmz=213851395.1693906636.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=213851395.35350555.1693906636.1694186978.1694192090.5; ASP.NET_SessionId=v3ieq0zvvtmnsehqa3dzwp0x; __utmc=213851395; __utmt=1; __utmb=213851395.14.10.1694192090"
spider_number = 5
spider_men = []

groups = list(range(1, 11400))


def gogo():
    while groups:
        group = groups.pop(0)
        try:
            Spider(cookie, group).run()
        except:
            with open("err.txt", "a+") as f:
                f.write(str(group))


for i in range(spider_number):
    t = Thread(target=gogo)
    t.start()
    spider_men.append(t)

for spider_man in spider_men:
    spider_man.start()
