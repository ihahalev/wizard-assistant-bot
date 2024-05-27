from datetime import datetime, timedelta, date

from .constants import format, created_at_format

def to_json(dict_data):
    json_data = {}
    for key, rec in dict_data.items():
        if type(rec) in [list,tuple,set,frozenset]:
            list_rec = []
            for iter_rec in rec:
                list_rec.append(recurcive_get(key, iter_rec))
            json_data[key] = list_rec
        else:
            json_data[key] = recurcive_get(key, rec)
    return json_data

def recurcive_get(key, rec):
    if isinstance(rec, (datetime, timedelta, date)):
        rec = datetime.strftime(rec, created_at_format if key == "created_at" else format)
    elif hasattr(rec, '__dict__'):
        rec = rec.to_json()
    return rec