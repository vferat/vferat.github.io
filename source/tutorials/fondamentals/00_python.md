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
[website](https://numpy.org/doc/stable/index.html)
Numeric
:::

:::{grid-item-card} Scipy
:columns: 3
[website](https://scipy.org/)
Signal processing
:::

:::{grid-item-card} Matplotlib
:columns: 3
[website](https://matplotlib.org/)
Plots
:::

:::
::::

::::{grid} 3
:gutter: 1

:::{grid-item-card} Pandas
:columns: 3
[website](https://pandas.pydata.org/)
Numeric
:::

:::{grid-item-card} Scikit-learn
:columns: 3
[website](https://scikit-learn.org/stable/)
Signal processing
:::

:::{grid-item-card} OS
:columns: 3
[website](https://docs.python.org/3/library/os.html)
Plots
:::

:::
::::

documentation

### A lot of libraries


## Package managers

### Pypi

### conda


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



## Ipython and

Python & conda


```{footbibliography}
```