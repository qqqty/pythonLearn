from multiprocessing import Pool

import os, time, random



def long_time_task(name):

    print os.getpgid()

    start = time.time()
    time.sleep(random.random() * 5)
    end = time.time()


    print end - start



print 2131
p = Pool()

for i in range(5):
    p.apply_async(long_time_task, args=(i, ))

p.close()

p.join()



