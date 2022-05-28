def sum(value, **kwargs):
    hap = value
    for key in kwargs:
        hap += kwargs[key]
        return hap

cofe = {'에소프레소':2500, '아메리카노':2800, "카페라떼":3200}
print(sum(1000, **cofe))
print(sum(value=2000, **cofe))
print(sum(**cofe, value=2000))