def sum(*values, **kwargs):
    hap = 0
    for v in values:
        hap += v

    for key in kwargs:
        hap += kwargs[key]
    return hap

cofe = {"value":2000, '에소프레소':2000, '아메리카노':2800, "카페라떼":3200}
print(sum(1, 2, 3, **cofe))
print(sum(*[2,3,4], **cofe))