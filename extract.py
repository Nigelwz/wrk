#!/usr/bin/python3
import math

def parse_one(one):
    ret = {}
    for l in one.split('\n'):
        if l.find('requests') > 0:
            ret['rate'] = int (l.split('requests')[0].strip())
            #print("hel")
        #if l.find('test @ http://') > 0:
        #    ret['host'] = l.split('://')[1].split('/')[0].strip()
        #elif l.find('start length') == 0:
        #    ret['size'] = l.split(' ')[-1].strip()
        #elif l.find('threads and') > 0:
        #    ret['threads'] = int(l.split('threads and')[0].strip())
        #    ret['conns'] = int(l.split('threads and')[1].split('connections')[0].strip())
        #elif l.find('    Latency') == 0:
        #    ret['l_avg'] = ms(l[len('    Latency'):].lstrip().split(' ')[0])
        #elif l.find('     50%') == 0:
        #    ret['l_50'] = ms(l[len('     50%'):].strip())
        #elif l.find('     90%') == 0:
        #    ret['l_90'] = ms(l[len('     90%'):].strip())
        #elif l.find('     99%') == 0:
        #    ret['l_99'] = ms(l[len('     99%'):].strip())
        #elif l.find('Requests/sec:') == 0:
        #    ret['qps'] = float(l[len('Requests/sec:'):].strip())
        #elif l.find('Transfer/sec:') == 0:
            #    ret['mbps'] = mb(l[len('Transfer/sec:'):].strip())
    return ret


def print_result(conn, thread):
    file_name = "./report/report_%d_%d.txt"%(conn, thread)

    with open(file_name) as f:
        all = f.read().strip()
        out = []
        for one in all.split('----------------------------------------------------\n'):
            r = parse_one(one)
            for k, v in r.items():
                if v > 0:
                    print("%d, %d, result: %d"%(conn, thread, v))
        #for o in out:
        #    print('\t'.join([str(i) for i in o]))

if __name__ == '__main__':
    for i in range(1, 10):
        conn = i * 100
        for j in range(1, 8):
            print_result(conn, j)

