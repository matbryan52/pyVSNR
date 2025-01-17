# pyVSNR
VSNR (Variational Stationary Noise Remover) algorithm in python

![](pyVSNR/data/fib_sem_comp.png)

## Description

This repository contains a Python wrapper around the CUDA implementation
of the 2D image denoising code given in 
 [https://github.com/pierre-weiss/VSNR_2D-3D_GPU](https://github.com/pierre-weiss/VSNR_2D-3D_GPU).

It completes the 2D-CPU/GPU port from MATLAB to python realized in
[https://github.com/patquem/pyvsnr](https://github.com/patquem/pyvsnr)

 
## Installation

    $ pip install git+https://github.com/CEA-MetroCarac/pyVSNR.git

In case of problem during CUDA execution (typically OSError or 'access memory error'),
it may be necessary to **recompile** the shared library from source (see below).

## Requirements

- numpy
- matplotlib, skimage (for examples and tests execution only)

A working CUDA installation and compatible GPU. Tested and compiled
for CUDA 11.

## Usage


```python
from pyVSNR import vsnr2d
from skimage import io

# read the image to correct
img = io.imread('image.tif')

# filters definition (Gabor and Dirac filters combination)
filter1 = {'name':'Gabor', 'noise_level':20, 'sigma':(3, 40), 'theta':210}
filter2 = {'name':'Dirac', 'noise_level':10}
filters = [filter1, filter2]

# image processing
img_corr = vsnr2d(img, filters, nite=20, nblocks='auto')

...
```
For more details concerning usage and parameters, refer to the Pierre Weiss 
 [website](https://www.math.univ-toulouse.fr/~weiss/PageCodes.html).
 
## Examples

Some applicative examples are given in 
[examples.py](examples.py), and below:


**Gaussian noise removal example** :

```python
from pyVSNR.examples import ex_camera_gaussian_noise 
ex_camera_gaussian_noise() 
```
![](data/camera_gaussian_noise_comp.png)
 
**Stripes removal example** :

```python
from pyVSNR.examples import ex_camera_stripes 
ex_camera_stripes()
```
![](data/camera_stripes_comp.png)

**Curtains removal example** :

```python
from pyVSNR.examples import ex_camera_curtains 
ex_camera_curtains()
```
![](data/camera_curtains_comp.png)

**Curtains removal example on real image (FIB-SEM)** :

```python
from pyVSNR.examples import ex_fib_sem
ex_fib_sem(show_plot=True)
```
![](data/fib_sem_comp.png)


## Shared library re-compilation

If you encounter shared library load errors then you may need
to recompile from source. This requires a working CUDA installation
with `nvcc` compiler. The source code is distributed with this package
and is found in the install directory, find this using:

```bash
python -c 'import pyVSNR; print(pyVSNR.PRECOMPILED_PATH)'
```

Navigate to this directory and re-compile for your system using the following, on linux:

```bash
cd ...
nvcc -lcufft -lcublas --compiler-options '-fPIC' -o libvsnr2d.so --shared vsnr2d.cu
```

and on Windows:

```powershell
cd ...
nvcc -lcufft -lcublas -o libvsnr2d.dll --shared vsnr2d.cu
```

## Authors informations

This is a port to python of the original code developed by Jean EYMERIE
and Pierre WEISS.

All credit goes to the original authors.

In case you use the results of this code with your article, please don't forget
to cite:

- Fehrenbach, Jérôme, Pierre Weiss, and Corinne Lorenzo. "*Variational algorithms to remove stationary noise: applications to microscopy imaging.*" IEEE Transactions on Image Processing 21.10 (2012): 4420-4430.
- Fehrenbach, Jérôme, and Pierre Weiss. "*Processing stationary noise: model and parameter selection in variational methods.*" SIAM Journal on Imaging Sciences 7.2 (2014): 613-640.
- Escande, Paul, Pierre Weiss, and Wenxing Zhang. "*A variational model for multiplicative structured noise removal.*" Journal of Mathematical Imaging and Vision 57.1 (2017): 43-55.

