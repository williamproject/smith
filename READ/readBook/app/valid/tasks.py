import time

from readBook.celery import app
from valid import r


@app.task
def buy(uid, gid):
    print("----正在抢购---")
    # 判断是否抢完
    if r.hlen('qbuy')< 5:
        #下单（向下单表中增加成功购买的记录）
        #向Redis_Hash中的qbuy中存放抢购的商品信息
        if not r.hexists('qbuy', uid):
            r.hset('qbuy', uid, gid)
            msg = {'%s抢购成工%s'%(uid,  gid)}
        else:
            msg = '%s只能抢购一部%s'%(uid,  gid)
    else:
        msg = "'%s抢购失败%s'%(uid,  gid)"
    return msg