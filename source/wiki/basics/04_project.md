# New python project Cheatsheet

## Create a new Github repository

TODO

## Create a new python environment

```{warning}
NO pity for people using the (base) environment.
```


```bash
conda create -n {env_name} python={python_version}
```

## Setup your IDE

- Spyder:
```bash
conda activate {env_name}
pip install spyder
```

- Jupyter:
```bash
conda activate {env_name}
pip install jupyter
```

- VS code:
```bash
conda activate {env_name}
pip install ipykernel
```


## Install your libraries

Libraries can be installed whenever you want.

``````{warning}
Make sure to activate the environment you want to work with:

```bash
conda activate {env_name}
```
before using any of the following commands

``````

- Using pip

```bash
pip install {library_name}
```

- Using conda
```bash
conda install {library_name}
```

You can specify the library version using `==`

```bash
pip install {library_name}=={library_version}
conda install {library_name}=={library_version}
```

**Recommendend:** create a `requirements.txt` file to keep track of all package your are installing, so you can easily share or recreate you environment:

```txt
pandas
seaborn
nilearn==1.2
statsmodels
```

You can then install all packages listed in the `requirements.txt` using:

```bash
pip install -r requirements.txt
```

## Start coding


``````{warning}
Make sure to activate the environment you want to work with:

```bash
conda activate {env_name}
```
before using any of the following commands

``````

- Spyder:
```bash
pip spyder
```

- Jupyter:
```bash
pip jupyter notebook
```
or 
```bash
pip jupyter lab
```


- VS code:

Open a new VS code folder: <kbd>File</kbd> -> <kbd>Open Folder</kbd>:
    - create a new `.py` file, on the bottom right corner, next to `python` choose your `{env_name}` environment.
    - create a new `.ipynb` file, on the top right corner, click `select kernel` and select your `{env_name}` environment

VS code save your kernel choices so you don't have to do it every time you open your project.



