# Introduction to Python

Python is a high-level, object oriented, interpreted programming language {footcite}`pythonabout`

- high-level: code closely resembles human language and logic: users can focus more on the problem they are trying to solve rather than the intricacies of how the computer executes the code (i.e. how memory is allocated, pointers, types)
- interpreted: the code is executed line by line by an interpreter software (on-the-fly), rather than being compiled into machine code before execution. This allows for Dynamic Typing, Interactivity, Portability
- object oriented: a programming paradigm based on the concept of "objects," which can contain data (attributes) and code (methods) to manipulate that data.
The object 'apple' does not only have a weight apple.weight but can also change itself apple.fall()

## About Python

**Simplicity and readability:** Python is a high-level programming language, which means its syntax is closer to human language and thus easier to understand. It also allows for more focus on the problem-solving aspects of programming for neuroimaging, rather than getting bogged down in complex syntax.

**Multipurpose:** Python is a general-purpose programming language, meaning it can be used for a wide variety of tasks. In the context of neuroscience research, Python can be used for data analysis, machine learning, image processing, and even creating interactive visualizations of neuroimaging data. Beyond neuroscience, Python is used in web development, game development (with game engines like Pygame), and much more.

**Portability:** Python is a portable language. It can run on various operating systems like Windows, Mac OS, and Linux. This means that Python scripts written on one system can typically be run on another without requiring modification.

**License-Free and Open-Source:** Python is both license-free and open-source. You do not need to pay to use or distribute Python. Its open-source nature means that its source code is freely available. This allows for a large community of developers to contribute to its development, resulting in a robust language with a wide array of libraries and modules.

**Integration with Other Environments and Tools:** Python can easily integrate with other software and tools, making it a versatile choice for neuroimaging research. It can interface with C/C++ libraries, can be embedded in applications, and can interact with other programming languages.

## The choice of Python for neuroimaging

### For Education

Python's simplicity and readability make it an ideal programming language for educational purposes. Its high-level syntax is closer to human language, making it more accessible for beginners. Python is also license-free and open-source, which means students don't need to purchase a license or software, nor do they need to be on a school network to use Python. This makes Python a cost-effective and flexible choice for both educational institutions and students.

### For Developers

Python's lack of licensing requirements makes it a convenient choice for working in remote environments. This includes:

- High-Performance Computing (HPC): HPC are remote computing environment usedto run complexe scripts that usually requires a lot of computational resources.
- Workers (such as GitHub Workers) Workers are background processes that handle tasks like sending notifications, executing long-running scripts

### For Researchers

Python's open-source nature promotes collaboration, reproducibility, and transparency in neuroimaging research. Code and tools can be freely shared and scrutinized by the community, fostering a collaborative environment. This openness also aids in the reproducibility of research, as other researchers can easily access, understand, and validate the code used in neuroimaging studies.


### Python's Core Functionalities and External Libraries

Python, as a programming language, provides a set of core functionalities that are sufficient for basic programming tasks. These include data types, control flow structures, and basic input/output operations. However, one of the strengths of Python lies in its extensibility through external libraries.

External libraries in Python are additional packages that can be imported into your Python environment to provide extra functionality. These libraries can range from those that provide mathematical functions (like NumPy), to those that provide machine learning capabilities (like scikit-learn), to those that provide neuroimaging-specific tools (like MNE and Nilearn).

These libraries are maintained by a variety of entities. Some are maintained by large institutions or companies, such as SciPy (maintained by a community of volunteers and managed by NumFOCUS, a non-profit), or TensorFlow (maintained by Google). Others are maintained by individual developers or small teams, contributing their expertise to the Python community.

This ecosystem of libraries greatly extends the capabilities of Python, allowing it to be used for an almost infinite range of tasks. It also means that Python can be as lightweight or as feature-rich as you need it to be, depending on which libraries you choose to use.

### Most important python librairies for data sciences

Although there are thousands of libraries, some are used much more than others. For data and time series analysis, which are key in neuroscience, it is important to familiarize yourself with the main ones:

::::{grid} 3
:gutter: 1

:::{grid-item-card} Numpy
:columns: 3
:img-top: https://github.com/numpy/numpy/blob/main/branding/logo/logomark/numpylogoicon.png?raw=true
:class-img-top: sd-avatar-xl
:link: https://numpy.org/doc/stable/index.html
+++
Numeric
:::

:::{grid-item-card} Scipy
:columns: 3
:img-top: https://raw.githubusercontent.com/scipy/scipy.org/db9fafb1d431f963f7962bd926171d6cead89a0a/static/images/logo.svg
:class-img-top: sd-avatar-xl
:link: https://scipy.org/
+++
Signal processing
:::

:::{grid-item-card} Matplotlib
:columns: 3
:img-top: https://matplotlib.org/stable/_images/sphx_glr_logos2_001.png
:class-img-top: sd-avatar-xl
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
:class-img-top: sd-avatar-xl
:link: https://pandas.pydata.org/
+++
Tables (csv)
:::

:::{grid-item-card} Scikit-learn
:columns: 3
:img-top: https://github.com/scikit-learn/scikit-learn/blob/main/doc/logos/scikit-learn-logo.svg?raw=true
:class-img-top: sd-avatar-xl
:link: https://scikit-learn.org/stable/

+++
Machine Learning
:::

:::{grid-item-card} OS
:columns: 3
:img-top: https://s3.dualstack.us-east-2.amazonaws.com/pythondotorg-assets/media/files/python-logo-only.svg
:class-img-top: sd-avatar-xl
:link: https://docs.python.org/3/library/os.html
+++
Path, Files
:::

:::
::::

### Neuroimaging libraires

::::{card-carousel} 2


:::{card} Psychopy
:img-top: https://github.com/psychopy/psychopy/blob/dev/docs/source/_static/psychopy256.png?raw=true
:class-img-top: sd-avatar-xl
:link: https://www.psychopy.org/
+++
Creating experiments
:::

:::{card} NiLearn
:img-top: https://github.com/nilearn/nilearn/blob/main/doc/logos/nilearn-logo.png?raw=true
:class-img-top: sd-avatar-xl
:link: https://nilearn.github.io/stable/index.html
+++
fMRI Analysis (ICA, GLM, Decoding)
:::

:::{card} MNE-python
:img-top: https://github.com/mne-tools/mne-python/blob/main/doc/_static/mne_logo.svg?raw=true
:class-img-top: sd-avatar-xl
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
:img-top: https://github.com/ACCLAB/DABEST-python/blob/master/nbs/images/DABEST-square-outline.svg?raw=true
:class-img-top: sd-avatar-xl
:link: https://acclab.github.io/DABEST-python/
+++
Estimation Statistics
:::


:::{card} Nipype
:img-top: https://github.com/nipy/nipype/blob/master/doc/_static/nipype-banner-bg.png?raw=true
:class-img-top: sd-avatar-xl
:link: https://nipype.readthedocs.io/en/latest/index.html
+++
Neuroimaging pipelines
:::


::::


## Package Managers

Package managers are tools that help you install and manage software libraries and dependencies. In Python, the two most common package managers are **PyPI** and **Conda**.

### PyPI

PyPI, or the Python Package Index, is a repository of software for the Python programming language. It helps you find and install software developed and shared by the Python community. You can use pip, a package installer for Python, to install packages from PyPI.

### Conda

Conda is a package manager that works with any language but is particularly popular with Python and R projects. It can manage environments, install packages, and more. Conda is included in Anaconda and Miniconda.

## Environment Managers

An environment manager is a tool that allows you to maintain separate environments, each with its own set of packages and dependencies. This is particularly useful when different projects require different versions of the same package.

For example, running `pip freeze` in your terminal will display a list of all the Python packages installed in your current environment, along with their versions:

```bash
>>> pip freeze
graphviz==0.20.3
joblib==1.4.2
numpy==1.26.4
packaging==24.0
pipdeptree==2.19.1
scikit-learn==1.4.2
scipy==1.13.0
setuptools==68.2.2
threadpoolctl==3.5.0
wheel==0.43.0
```

### Why using a environment manager ?

Different versions of the same package can have different APIs. For example, consider the following two versions of NumPy:

::::{tab-set}

:::{tab-item} Numpy '1.26.4'

```python
>>> import numpy as np
>>> np.__version__
'1.26.4'
>>> np.percentile([1,2,3], q=95, method='linear')
2.9
```

:::

:::{tab-item} Numpy '1.21.0'

```python
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

As you can see, the `percentile` function in NumPy version 1.26.4 accepts a `method` argument, but the same function in version 1.21.0 does not. This can lead to errors if your code depends on a specific version of a package. By using an environment manager, you can ensure that your project has exactly the right versions of its dependencies.

API changes:


::::{tab-set}

:::{tab-item} Numpy '1.23.0'

```python
>>> import numpy as np
>>> np.__version__
'1.23.0'
>>> np.array([np.iinfo(np.int32).min]*10, dtype=np.int32) // np.int32(-1)
array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=int32)
```

:::

:::{tab-item} Numpy '1.26.4'

```python
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

On the second example, the same operation results in an overflow warning and an array of the minimum possible 32-bit integers instead of an array of zeros.. the behavior of the floor division operation has changed between these two versions of NumPy. This is a clear example of why it's important to manage your project's dependencies carefully, as changes in package versions can lead to unexpected results.

### Managing dependencies conflicts

Managing your project's environment is a crucial aspect of any programming project, and this is especially true when working with Python. Conda is a popular tool for environment management in Python. It allows you to create isolated environments, each with their own installed packages, which can help prevent conflicts between package versions.

```{footbibliography}
```