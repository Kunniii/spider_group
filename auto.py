from Database import Database
from Processor import Processor
from threading import Thread
from Spider import Spider
from time import sleep

# with open('.cookie', 'r', encoding='utf-8') as f:
#     cookie = f.read()

# spider_number = 4
# spider_men = []

# groups = list(range(1, 36000))


# def gogo():
#     while groups:
#         group = groups.pop(0)
#         try:
#             Spider(cookie, group).run()
#         except:
#             with open("err.txt", "a+") as f:
#                 f.write(str(group))


# pre = len(groups)
# total_op = 0
# total_sec = 0


# def format_seconds(n):
#     hours, remainder = divmod(n, 3600)
#     minutes, seconds = divmod(remainder, 60)
#     return f"({format(hours,'.0f')}:{format(minutes,'.0f')}:{format(seconds,'.0f')})"


# def estimate_time():
#     global pre
#     global total_op
#     global total_sec
#     while groups:
#         sleep(1)
#         delta = abs(pre - len(groups))
#         pre = len(groups)
#         total_sec += 1
#         total_op += delta
#         avg_per_sec = total_op/total_sec
#         et_second = len(groups)/avg_per_sec
#         print(
#             f"+ {format(avg_per_sec, '.1f')}/s -- ET: {format_seconds(et_second)}   ", end='\r')
#     print()


# for i in range(spider_number):
#     t = Thread(target=gogo)
#     t.start()
#     spider_men.append(t)

# t = Thread(target=estimate_time)
# t.start()
# spider_men.append(t)

# for spider_man in spider_men:
#     spider_man.join()


processor = Processor("./downloads", worker=10)

processor.load_pickle('./hcm_raw.pkl')


# processor.run_extract_data()
# processor.to_pickle('./hcm_raw.pkl')

db = Database('hcm-23-09-09.sqlite')

for data in processor.data:
    if db.add_data(data):
        print(f"++ Added  : {data[0]}")
    else:
        print(f"-- Already: {data[0]}")

# db.add_data_many(processor.data)
