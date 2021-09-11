# -*- coding: utf-8 -*-
import os
import h5py
import numpy as np

from vgg16 import VGGNet


def get_imlist(path):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]

#提取特征训练模型
# if __name__ == "__main__":
    #
    # db = '../smalldatasets/'
    # img_list = get_imlist(db)
    #
    # feats = []
    # names = []
    #
    # model = VGGNet()
    #
    # f1 = open('pictuer_path.txt','r')
    # paths = f1.readlines()
    #
    # for path in paths:
    #     path = path.rstrip('\n')
    #     norm_feat = model.extract_feat(path)
    #     feats.append(norm_feat)
    #     names.append(path.encode())
    #     print("extracting feature from  %s " % (path))
    #
    #
    # feats = np.array(feats)
    #
    # output = '../vgg_model'
    #
    # print("--------------------------------------------------")
    # print("      writing feature extraction results ...")
    # print("--------------------------------------------------")
    #
    # h5f = h5py.File(output, 'w')
    # h5f.create_dataset('dataset_1', data=feats)
    # h5f.create_dataset('dataset_2', data=names)
    # h5f.close()