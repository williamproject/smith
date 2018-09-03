def valid_required(field: str, value: str, field_cn: str, errors:dict,
                   min_length=6, max_length=20):
    '''

    :param min_length:
    :param max_length:
    :param field_cn:
    :param field:
    :param value:
    :param errors:
    :return:
    '''

    if not value.strip():
        errors[field] = '%s不能为空！' %field_cn
    elif len(value)< min_length:
        errors[field] = '%s长度小于%d' %(field_cn, min_length)
    elif len(value) > max_length:
        errors[field] = '%s长度大于%d' % (field_cn, max_length)
