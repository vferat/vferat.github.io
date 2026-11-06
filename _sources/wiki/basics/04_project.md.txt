# New Python project cheatsheet

## Create a new GitHub repository

TODO

## Create a new Python environment

```{warning}
No pity for people using the (base) environment.
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

- VS Code:
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
before using any of the following commands.

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

**Recommended:** create a `requirements.txt` file to keep track of all the packages you are installing, so you can easily share or recreate your environment:

```text
pandas
seaborn
nilearn==1.2
statsmodels
```

You can then install all the packages listed in `requirements.txt` using:

```bash
pip install -r requirements.txt
```

## Start coding


``````{warning}
Make sure to activate the environment you want to work with:

```bash
conda activate {env_name}
```
before using any of the following commands.

``````

- Spyder:
```bash
spyder
```

- Jupyter:
```bash
jupyter notebook
```
or
```bash
jupyter lab
```


- VS Code:

Open a folder in VS Code: <kbd>File</kbd> -> <kbd>Open Folder</kbd>. Then:

- For a new `.py` file: in the bottom right corner, next to `Python`, choose your `{env_name}` environment.
- For a new `.ipynb` file: in the top right corner, click `Select Kernel` and select your `{env_name}` environment.

VS Code saves your kernel choices, so you don't have to do this every time you open your project.



