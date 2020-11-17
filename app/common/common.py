import re
from urllib.parse import quote_plus


def get_querys(request):
    rslt = dict()
    for key, value in request.query_params.items():
        rslt[key] = value

    return rslt


def make_url(basic_url: str, query_data: dict):
    full_url = basic_url + "?"
    len_query = len(query_data)

    for index, (key, value) in enumerate(query_data.items()):
        # 한글이 있을경우 유니코드화
        if re.compile('[ㄱ-ㅎㅏ-ㅣ가-힣]+').search(value) != None:
            value = quote_plus(value)

        if index == len_query-1:
            full_url += key + "=" + value
        else:
            full_url += key + "=" + value + "&"

    return full_url



