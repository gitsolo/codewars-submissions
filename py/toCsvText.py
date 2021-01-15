# https://www.codewars.com/kata/5a34af40e1ce0eb1f5000036

def arrToString(arr): return ','.join([str(i) for i in arr])


def toCsvText(arr): return ('\n'.join([arrToString(x) for x in arr]))
