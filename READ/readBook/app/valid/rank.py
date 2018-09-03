# from valid import r
#
# def add_rank_week(art_id):
#     # 判断周排行的key是否存在
#     flag = r.exists('WeekRank')
#     r.incrby('WeekRank', art_id)
#     if not flag:
#         r.expire('WeekRank', 604800) # 一周有效时间
#
#
# def get_rank_week(top):
#     return [id.decode() for id in r.zrevrange('WeekRank', 0, top-1)]
from valid import r


def week_rank(art_id):
    #判断周排行的key是否存在
    flag =  r.exists('weekRank')
    r.zincrby('weekRank',art_id)
    if not flag:
       r.expire('weekRank',604800)


def get_art(top):
    return [id.decode() for id in r.zrevrange('weekRank',0,top-1)]