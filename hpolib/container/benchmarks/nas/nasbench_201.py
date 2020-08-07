#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" Benchmark for the NasBench201 Benchmark from hpolib/benchmarks/nas/nasbench_201.py """

from hpolib.container.client_abstract_benchmark import AbstractBenchmarkClient


class Cifar10NasBench201Benchmark(AbstractBenchmarkClient):
    def __init__(self, **kwargs):
        kwargs['data_path'] = '/home/data/NAS-Bench-201-v1_1-096897_cifar10.pth'
        kwargs['benchmark_name'] = kwargs.get('benchmark_name', 'Cifar10NasBench201Benchmark')
        kwargs['container_name'] = kwargs.get('container_name', 'nasbench_201')
        super(Cifar10NasBench201Benchmark, self).__init__(**kwargs)


class Cifar10ValidNasBench201Benchmark(AbstractBenchmarkClient):
    def __init__(self, **kwargs):
        kwargs['data_path'] = '/home/data/NAS-Bench-201-v1_1-096897_cifar10-valid.pth'
        kwargs['benchmark_name'] = kwargs.get('benchmark_name', 'Cifar10ValidNasBench201Benchmark')
        kwargs['container_name'] = kwargs.get('container_name', 'nasbench_201')
        super(Cifar10ValidNasBench201Benchmark, self).__init__(**kwargs)


class Cifar100NasBench201Benchmark(AbstractBenchmarkClient):
    def __init__(self, **kwargs):
        kwargs['data_path'] = '/home/data/NAS-Bench-201-v1_1-096897_cifar100.pth'
        kwargs['benchmark_name'] = kwargs.get('benchmark_name', 'Cifar100NasBench201Benchmark')
        kwargs['container_name'] = kwargs.get('container_name', 'nasbench_201')
        super(Cifar100NasBench201Benchmark, self).__init__(**kwargs)


class ImageNetNasBench201Benchmark(AbstractBenchmarkClient):
    def __init__(self, **kwargs):
        kwargs['data_path'] = '/home/data/NAS-Bench-201-v1_1-096897_ImageNet16-120.pth'
        kwargs['benchmark_name'] = kwargs.get('benchmark_name', 'ImageNetNasBench201Benchmark')
        kwargs['container_name'] = kwargs.get('container_name', 'nasbench_201')
        super(ImageNetNasBench201Benchmark, self).__init__(**kwargs)
