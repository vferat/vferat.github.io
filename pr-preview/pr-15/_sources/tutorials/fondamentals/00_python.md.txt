# Introduction to Python

Python is a high-level, object oriented, interpreted programming language {footcite}`pythonabout`

- high-level: code closely resembles human language and logic: users can focus more on the problem they are trying to solve rather than the intricacies of how the computer executes the code (i.e. how memory is allocated, pointers, types)
- interpreted: the code is executed line by line by an interpreter software (on-the-fly), rather than being compiled into machine code before execution. This allows for Dynamic Typing, Interactivity, Portability
- object oriented: a programming paradigm based on the concept of "objects," which can contain data (attributes) and code (methods) to manipulate that data.
The object 'apple' does not only have a weight apple.weight but can also change itself apple.fall()

## The choice of python for neuroimaging

simplicity and readability
multipurpose
Portability 
License-Free and Open-Source
Integration with Other Environments and Tools

### For education

Python's simplicity and readability (high-level) make it an ideal programming language for educational purposes.
License-Free and Open-Source

### For research

This openness promotes collaboration, reproducibility, and transparency in neuroimaging research, as code and tools can be shared and scrutinized by the community.


::::{grid} 3
:gutter: 1

:::{grid-item-card} Numpy
:columns: 3
:img-top: https://github.com/numpy/numpy/blob/main/branding/logo/logomark/numpylogoicon.png?raw=true
:link: https://numpy.org/doc/stable/index.html
+++
Numeric
:::

:::{grid-item-card} Scipy
:columns: 3
:img-top: https://raw.githubusercontent.com/scipy/scipy.org/db9fafb1d431f963f7962bd926171d6cead89a0a/static/images/logo.svg
:link: https://scipy.org/
+++
Signal processing
:::

:::{grid-item-card} Matplotlib
:columns: 3
:img-top: https://matplotlib.org/stable/_images/sphx_glr_logos2_001.png
:link: https://matplotlib.org/
+++
Plots
:::

:::
::::

::::{grid} 3
:gutter: 1

:::{grid-item-card} Pandas
:columns: 3
:img-top: https://pandas.pydata.org/static/img/pandas_mark.svg
:link: https://pandas.pydata.org/
+++
Tables (csv)
:::

:::{grid-item-card} Scikit-learn
:columns: 3
:img-top: https://github.com/scikit-learn/scikit-learn/blob/main/doc/logos/scikit-learn-logo.svg
:link: https://scikit-learn.org/stable/
+++
Machine Learning
:::

:::{grid-item-card} OS
:columns: 3
:img-top: https://s3.dualstack.us-east-2.amazonaws.com/pythondotorg-assets/media/files/python-logo-only.svg
:link: https://docs.python.org/3/library/os.html
+++
Operating System (path, files)
:::

:::
::::


### A lot of libraries

::::{card-carousel} 2

:::{card} NiLearn
:img-top: https://github.com/nilearn/nilearn/blob/main/doc/logos/nilearn-logo.png
:link: https://nilearn.github.io/stable/index.html
+++
fMRI Analysis (ICA, GLM, Decoding)
:::

:::{card} MNE-python
:img-top: https://github.com/mne-tools/mne-python/blob/main/doc/_static/mne_logo.svg
:link: https://mne.tools/stable/index.html#
+++
M/EEG - Intra - fNIRS 
:::

:::{card} fMRIprep
:link: https://fmriprep.org/en/stable/index.html
+++
fMRI Preprocessing
:::

:::{card} dabest
:img-top: https://github.com/ACCLAB/DABEST-python/blob/master/nbs/images/DABEST-square-outline.svg
:link: https://acclab.github.io/DABEST-python/
+++
Estimation Statistics
:::


:::{card} Nipype
:img-top: https://github.com/nipy/nipype/blob/master/doc/_static/nipype-banner-bg.png
:link: https://nipype.readthedocs.io/en/latest/index.html
+++
Neuroimaging pipelines
:::


::::


## Package managers


### Pypi

### conda

## Environment manager

### Why using a environment manager ?

API changes:

::::{tab-set}

:::{tab-item} Numpy '1.26.4'

```
>>> import numpy as np
>>> np.__version__
'1.26.4'
>>> np.percentile([1,2,3], q=95, method='linear')
2.9
```

:::

:::{tab-item} Numpy '1.21.0'

```
>>> import numpy as np
>>> np.__version__
'1.21.0'
>>> np.percentile([1,2,3], q=95, method='linear')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
File "<__array_function__ internals>", line 4, in percentile
TypeError: _percentile_dispatcher() got an unexpected keyword argument 'method'
```

:::

::::


API changes:


::::{tab-set}

:::{tab-item} Numpy '1.23.0'

```
>>> import numpy as np
>>> np.__version__
'1.23.0'
>>> np.array([np.iinfo(np.int32).min]*10, dtype=np.int32) // np.int32(-1)
array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=int32)
```

:::

:::{tab-item} Numpy '1.26.4'

```
>>> import numpy as np
>>> np.__version__
'1.26.4'
>>> np.array([np.iinfo(np.int32).min]*10, dtype=np.int32) // np.int32(-1)
<stdin>:1: RuntimeWarning: overflow encountered in floor_divide
array([-2147483648, -2147483648, -2147483648, -2147483648, -2147483648,
    -2147483648, -2147483648, -2147483648, -2147483648, -2147483648],
    dtype=int32)
```

:::

::::


#### Managing dependencies conflicts



#### Reproducibility




## Installing python

### install miniconda

https://docs.anaconda.com/free/miniconda/index.html

use the latest stable version


``````{note}
On windows, if you want to use cmd instead of the anaconda shell ( no recommended), you might need to initialize (only once) conda for cmd. for that, start the anaconda shell, find conda location using "where conda".

```
(base) C:\>where conda
C:\Users\ferat\AppData\Local\miniconda3\Library\bin\conda.bat
C:\Users\ferat\AppData\Local\miniconda3\Scripts\conda.exe
C:\Users\ferat\AppData\Local\miniconda3\condabin\conda.bat
```

Now, on your cmd, use the path of conda.exe to run the following conda script:

```
C:\Users\ferat\AppData\Local\miniconda3\Scripts\conda.exe init cmd.exe
```

``````




### environment managment

conda env list

conda create -n python=

conda activate



``````{note}
conda can also be used to manage R environments
https://docs.anaconda.com/free/working-with-conda/packages/using-r-language/

``````


### Code editors

#### Spider

#### Jupyter




```{footbibliography}
```