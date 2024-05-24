# Installing Python

## Installing via Miniconda

Miniconda is a free minimal installer for conda, a package management and environment management system for Python and R. It's a lightweight version of the comprehensive Anaconda distribution.

To install Miniconda, follow these steps:

1. Visit the [Miniconda download page](https://docs.anaconda.com/free/miniconda/index.html).
2. Download the installer for your operating system. Make sure to choose the latest stable version.
3. Run the installer and follow the prompts on the screen.

``````{note}
If you're using Windows and prefer to use the Command Prompt (cmd) instead of the Anaconda shell (not recommended), you'll need to initialize conda for cmd. This only needs to be done once.

To do this, start the Anaconda shell and find the location of conda using the `where conda` command:

```bash
(base) C:\>where conda
C:\Users\ferat\AppData\Local\miniconda3\Library\bin\conda.bat
C:\Users\ferat\AppData\Local\miniconda3\Scripts\conda.exe
C:\Users\ferat\AppData\Local\miniconda3\condabin\conda.bat
```

Then, in your cmd, use the path of `conda.exe` to run the following conda script:

```bash
C:\Users\ferat\AppData\Local\miniconda3\Scripts\conda.exe init cmd.exe
```

This will initialize conda for the Command Prompt, allowing you to use conda commands directly from cmd.
``````

## Environment Management with Conda

To view a list of all your existing conda environments, you can use the following command:

```bash
conda env list
```

This will display a list of all your environments, along with their locations on your system.

To create a new environment, you can use the `conda create` command. This command takes two arguments: the name of the new environment (`{environment_name}`), and the version of Python you want to use in that environment (`{python_version}`):

```bash
conda create -n {environment_name} python={python_version}
```

Once you've created an environment, you'll need to activate it before you can use it. You can do this with the `conda activate` command:

```bash
conda activate {environment_name}
```

After activating an environment, your terminal will typically display the name of the current environment at the beginning of the line, usually in parentheses. This helps you keep track of which environment you're currently working in.

Once an environment is activated, all subsequent commands you run will use the Python executables and libraries installed in that environment. This isolation is what allows you to have different environments with different versions of the same package installed.

```{note}
Conda isn't just for Python - it can also be used to manage environments for the R programming language. You can learn more about this in the [Conda documentation](https://docs.anaconda.com/free/working-with-conda/packages/using-r-language/).
```