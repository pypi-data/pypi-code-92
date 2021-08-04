# -*-coding: utf-8 -*-
"""
    @Author : panjq
    @E-mail : pan_jinquan@163.com
    @Date   : 2021-07-30 17:04:51
"""

import torch.nn as nn
import torch.utils.data as torch_utils
from torch.utils.data.dataset import Dataset
from torch.utils.data.dataloader import DataLoader
from ..engine import comm


def build_dataloader(dataset: Dataset,
                     batch_size: int,
                     num_workers: int,
                     shuffle: bool = True,
                     persistent_workers: bool = True,
                     phase: str = "train",
                     **kwargs) -> DataLoader:
    """
    :param dataset:
    :param batch_size:
    :param num_workers:
    :param shuffle:
    :param persistent_workers:如为False，数据加载器运行完一个Epoch后会关闭worker进程,
                              在分布式训练，会出现每个epoch初始化多进程的问题
                              如果为True，会保持worker进程实例激活状态
    :param phase:
    :param kwargs:
    :return:
    """
    assert phase in ["train", "test", "val"]
    sampler = None
    if comm.get_world_size() > 1 and phase == "train":
        sampler = torch_utils.distributed.DistributedSampler(dataset,
                                                             num_replicas=comm.get_world_size(),
                                                             rank=comm.get_local_rank(),
                                                             shuffle=shuffle)
        shuffle = False  # sampler option is mutually exclusive with shuffle
    dataloader = torch_utils.DataLoader(dataset,
                                        batch_size=batch_size,
                                        num_workers=num_workers,
                                        sampler=sampler,
                                        shuffle=shuffle,
                                        persistent_workers=persistent_workers,
                                        **kwargs)
    return dataloader


def build_model_parallel(model: nn.Module,
                         device_ids=None,
                         **kwargs) -> nn.Module:
    """
    :param model:
    :param device_ids:
    :param kwargs:
    :return:
    """
    print("device_ids:{},device:{}".format(device_ids, comm.get_device(device_ids)))
    model.to(comm.get_device(device_ids))
    # use DistributedDataParallel
    if comm.get_world_size() > 1:
        model = nn.parallel.DistributedDataParallel(model,
                                                    device_ids=[comm.get_device(device_ids)],
                                                    output_device=comm.get_device(device_ids))
    else:
        # use DataParallel
        model = nn.DataParallel(model, device_ids=device_ids, output_device=comm.get_device(device_ids), **kwargs)
    return model
