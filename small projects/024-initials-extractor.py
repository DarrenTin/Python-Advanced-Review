def extractor(text):
    texts = text.split()
    init = ''
    init = init.join(t[0] + '.' for t in texts)
    return init

full_names = 'Micheal Jackson', 'Lin Joe', 'Chloe Lee Hui Xin', 'Claire Yee Woh Yee'
for fn in full_names:
    init = extractor(fn)
    print(init)