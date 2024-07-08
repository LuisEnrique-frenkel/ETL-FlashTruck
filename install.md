# SQLite TIA Portal ETL guide installation

## Set up project's module

To move beyond notebook prototyping, all reusable code should go into the `module/` folder package. To use that package inside your project, install the project's module in editable mode, so you can edit files in the `module` folder and use the modules inside your notebooks :

```bash
pip install --editable .
```

To use the module inside your notebooks, add `%autoreload` at the top of your notebook :

```python
%load_ext autoreload
%autoreload 2
```

Example of module usage :

```python
from module.utils.paths import data_dir
data_dir()
```

## Set up Git diff for notebooks and lab

We use [nbdime](https://nbdime.readthedocs.io/en/stable/index.html) for diffing and merging Jupyter notebooks.

To configure it to this git project :

```bash
nbdime config-git --enable
```

To enable notebook extension :

```bash
nbdime extensions --enable --sys-prefix
```

Or, if you prefer full control, you can run the individual steps:

```bash
jupyter serverextension enable --py nbdime --sys-prefix
jupyter nbextension install --py nbdime --sys-prefix
jupyter nbextension enable --py nbdime --sys-prefix
jupyter labextension install nbdime-jupyterlab
```

You may need to rebuild the extension : `jupyter lab build`