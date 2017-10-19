from multiprocessing import Pool
from functools import partial
import time


def call_script(number, name ):
    max_time = 5
    number = number +1

    if name == "A":
        for i in range(0,max_time):
            print "Hey i'm A. " + str(number)
            time.sleep(1)

    elif name == "B":
        for i in range(0, max_time):
            print "Hey i'm B. " + str(number)
            time.sleep(1)
    else:
        print "I don't know."


if __name__ == '__main__':
    pool = Pool()
    # Apply Async
    func_a = partial(call_script, 0, "A")
    func_b = partial(call_script, 0, "B")
    res_a = pool.apply_async(func_a, ())
    res_b = pool.apply_async(func_b, ())
    res_a.get()
    res_b.get()

    # n_type = ["A", "B", "C"]
    # func = partial(call_script, 0)
    # multiple_results = [pool.apply_async(func, (i))for i in n_type]
    # [res.get() for res in multiple_results]

    # Map Async
    # pool.map_async(call_script, ["A","A","A"])
    # pool.map_async(call_script, ["B","B","B"])


    # pool.imap_unordered(call_script, ["A", "A", "A"])
    # pool.imap_unordered(call_script, ["B", "B", "B"])



    pool.close()
    pool.join()


# from multiprocessing import Pool
#
# def f(x):
#     return x*x
#
# if __name__ == '__main__':
#     p = Pool(5)
#     print(p.map(f, [1, 2, 3]))