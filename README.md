# yolo
## 环境配置
python3.9

pytorch1.12.1

RTX3050Ti

## 数据集
VOC数据集下载地址：[https://pan.baidu.com/s/1-1Ej6dayrx3g0iAA88uY5A]

提取码：ph32

## 预训练网络
网络参数下载地址：[https://pan.baidu.com/s/1hCV4kg8NyStkywLiAeEr3g]

提取码：6da3

下载好的模型放到model_data目录下

## 训练
`python voc_annotation.py`

`python trian.py`

## 预测
在yolo.py中修改model_path对应到自己训练的文件

`python predict.py`

然后输入预测图像地址

## Reference
[https://github.com/bubbliiiing/faster-rcnn-pytorch]
