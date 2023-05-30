import argparse

def config_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--Cuda', default=True)
    parser.add_argument('--classes_path', default='model_data/voc_classes.txt')
    parser.add_argument('--model_path', default='model_data/voc_weights_resnet.pth')
    parser.add_argument('--input_shape',default=[600, 600])
    parser.add_argument('--backbone', type=str, default='resnet50')
    parser.add_argument('--pretrained', type=bool, default=False)
    parser.add_argument('--anchors_size', default=[8, 16, 32])
    parser.add_argument('--Freeze_Epoch', type=int, default=50)
    parser.add_argument('--freeze_batch_size', type=int, default=4)
    parser.add_argument('--UnFreeze_Epoch', type=int ,default=100)
    parser.add_argument('--Unfreeze_batch_size',type=int, default=4)
    parser.add_argument('--Init_lr', default=1e-4)
    parser.add_argument('--Min_lr', default=1e-6)
    parser.add_argument('optimizer_type', default='adam', type=str)
    parser.add_argument('momentum', default=0.9)
    parser.add_argument('weight_decay', default=0)
    parser.add_argument('lr_decay_type', default='cos')
    parser.add_argument('save_period', default=5)
    parser.add_argument('save_dir', default='logs')
    parser.add_argument('eval_flag', default=True)
    parser.add_argument('eval_period', default=1)
    parser.add_argument('num_workers', default=4)
    parser.add_argument('train_annotation_path', default='2007_train.txt')
    parser.add_argument('val_annotation_path', default='2007_val.txt')
    parser.add_argument('--fp16', default=False)
    parser.add_argument('Freeze_Train', default=True)
    parser.add_argument('Init_Epoch', default=0)



    return parser

# parser = config_parser()
# args = parser.parse_args()
# print(args.model_path)
# print(type(args.input_shape))
