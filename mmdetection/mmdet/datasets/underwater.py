#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-10-28 20:57:01
# @Author  : Ko Sung (gao.dacheng@outlook.com)
# @Link    : https://github.com/KooSung

from .coco import CocoDataset
from .registry import DATASETS


@DATASETS.register_module
class UnderWaterDataset(CocoDataset):
    CLASSES = ('holothurian', 'echinus', 'scallop', 'starfish')