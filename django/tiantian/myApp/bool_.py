# 1 : add
# 2 : update
# 4 : delete
# 8 : query
rs = {
    1: 'add',
    2: 'update',
    4: 'delete',
    8: 'query'
}
rights = 0
rights = 1 | 2 | 8
def addRight(right):
    global rights
    rights |= right
def exists(right):
    if rights & right == right:
        print('你有%s的权限'%rs.get(right))
        return True
    else:
        print('你没有%s的权限' % rs.get(right))
        return False
def remove(right):
    global rights
    if exists(right):
        rights ^= right
        print('你删除%s的权限' % rs.get(right))
addRight(1)
addRight(2)
exists(1)
remove(1)