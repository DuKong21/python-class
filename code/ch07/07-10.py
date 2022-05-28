def mkp(**kwargs):
    for key in kwargs:
        print('{}: {}'.format(key, kwargs[key]), end=" ")
    print()

mkp(여자친구=6, 마마무=4)
mkp(엑소=9, 트와이스=9, 블랙핑크=4, 방탄소년단=7)

cofe = {'에소프레소':2500, '아메리카노':2800, "카페라떼":3200}
mycar = {"브랜드":"현대", "모델":"제네시스", "년도":2016}
mkp(**cofe)
mkp(**mycar)