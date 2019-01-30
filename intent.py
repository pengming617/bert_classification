from predict import predicts

sentences = ['键盘按键设计太紧密,不好操控。反映慢。', '离长途大巴车站很近,酒店环境也算不错,下次还是首选.']
for sentence in sentences:
    dic = predicts([sentence])
    print(dic)
