symbols = '$%&*@'
codes=[ord(item) for item in symbols]
print(codes)



#Map / Filter

beyond_ascii=[ord(item) for item in symbols if ord(item) > 40]
print(beyond_ascii)

beyond_ascii=list(filter(lambda c: c > 40, map(ord, symbols)))
print(lambda c: c > 40, map(ord, symbols))