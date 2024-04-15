from setuptools import setup 
from setuptools import find_packages

setup(name='BCscannerBWA',
      version='0.0.1',
      description='Barcode split for Cyclone',
      author='dawn',
      author_email='605547565@qq.com',
      requires= ['pandas','Levenshtein','numpy','anndata','samtools','pysam'], # 定义依赖哪些模块
      packages=find_packages(),  # 系统自动从当前目录开始找包
      license="apache 3.0",
      python_requires='>=3.6'
      )
