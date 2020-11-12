def get_querys(request):
    rslt = dict()
    for key, value in request.query_params.items():
        rslt[key] = value

    return rslt