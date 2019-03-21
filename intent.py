from single_predict import predicts


sentences = ['交通方便；环境很好；服务态度很好 房间较小上',
             '太差了，空调的噪音很大，设施也不齐全，携程怎么会选择这样的合作伙伴']
dic = predicts(sentences)
print(dic)
