def h(*name):
    for e in name:
        print('안녕, {}!' .format(e))

h('나타샤')
h('수빈', '현수', '지효')
h(*['방탄소년단', '여자친구'])