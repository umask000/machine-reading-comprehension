# -*- coding: utf-8 -*-
# @author : caoyang
# @email: caoyang@163.sufe.edu.cn
# 全局变量设定

import os
import torch
import platform

DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
PLATFORM = platform.system()

# -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*-
# 1. 数据文件夹
DATA_DIR = 'data'

DATASET_DIR = os.path.join(DATA_DIR, 'dataset')
PREPROCESSED_DIR = os.path.join(DATA_DIR, 'preprocessed')
STOPWORD_DIR = os.path.join(DATA_DIR, 'stopword')
USERDICT_DIR = os.path.join(DATA_DIR, 'userdict')

# -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*-
# 2. 模型文件夹
MODEL_DIR = 'model'

CHECKPOINT_DIR = os.path.join(MODEL_DIR, 'checkpoint')
# -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*-
# 3. 图片文件夹
IMAGE_DIR = 'image'


# -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*-
# 4. 日志文件夹
LOGGING_DIR = 'logging'

# -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*-
# 5. 临时文件夹
TEMP_DIR = 'temp'

# -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*-



