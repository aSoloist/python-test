from urllib import request, parse


def test():
    post_data = parse.urlencode([
        ('nianji', 2016),
        ('xuehao', ''),
        ('mima', ''),
        ('selec', 'http://jw.zzu.edu.cn/scripts/qscore.dll/search')
    ])

    req = request.Request('http://jw.zzu.edu.cn/scripts/qscore.dll/search')
    req.add_header('Connection', 'keep-alive')

    page = request.urlopen(req, data=post_data.encode('utf-8'))
    data = page.read()
    for k, v in page.getheaders():
        print(k, v)
    print(data.decode('gbk'))


if __name__ == '__main__':
    test()
