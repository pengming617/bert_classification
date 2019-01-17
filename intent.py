from predict import predicts

sentences = ['大宗减持情况查询', '今天大盘怎么样']
for sentence in sentences:
    dic = predicts([sentence])
    print(dic)
