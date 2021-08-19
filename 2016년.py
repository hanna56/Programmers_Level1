import pandas as pd

def solution(a, b):
    date = pd.Timestamp('2016-' + str(a) + '-' + str(b))
    return date.day_name()[:3].upper()
