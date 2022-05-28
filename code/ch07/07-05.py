def ctofahrenhite(cels):
    return cels * 9/5 + 32

def ftocelsius(fahr):
    return (fahr - 32) * 5/9

for cels in range(28, 35, 2):
    print('섭씨: {}, 화씨: {:.2f}'.format(cels, ctofahrenhite(cels)))

for fahr in range(90, 103, 3):
    print('섭씨: {:.2f}, 화씨: {}'.format(ftocelsius(fahr), fahr))