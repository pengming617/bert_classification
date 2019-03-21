利用bert预训练的中文语言模型进行文本分类

训练脚本 train.sh

批量测试脚本 predict.sh

利用模型进行单条语句测试 intent.py
注：修改single_predict.py中 get_test_examples,get_labels方法 max_seq_length，需run_classifier.py一致

chinese_L-12_H-768_A-12为预训练的相关模型和词典

data文件夹中为训练语料，验证语料，测试语料

注意：
当语料中的分类种类发生变化时，run_classifier.py文件的SimProcessor中的get_labels方法也要随之变化

参数说明：
max_seq_length  sentence的最大长度（字）
train_batch_size  batch_size的大小
