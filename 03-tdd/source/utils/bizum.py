def bizum(num):
    if not isinstance(num, int):
        raise Exception("num")

    result = ""
    if num % 3 == 0:
        result += "Bi"
    if num % 5 == 0:
        result += "Zum"

    return result if result else str(num)
