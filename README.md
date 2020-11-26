# Test repo to see the outputs of differnt jupyter notebooks

The goal of this repo is to show different ways to remove the output of the jupyter notebook files. 

---
## Jupytext
https://jupytext.readthedocs.io/en/latest/using-pre-commit.html

A lot of possibilities. 

### Configuration
Possible to add black and flake8 to precommit of notebooks.
Can remove the output (and metadata) of all the cells. 

In python configuration file:
```python
default_cell_metadata_filter = "-hide_output"
default_cell_metadata_filter = "-all"
```
### Pre-commit
Also adds pre-commit hooks for jupyter and add a python file for each notebook:

```
#!/bin/sh
# For every ipynb file in the git index:
# - apply black and flake8
# - export the notebook to a Python script in folder 'python'
# - and add it to the git index
jupytext --from ipynb --pipe black --check flake8 --pre-commit
jupytext --from ipynb --to python//py:light --pre-commit
```
### Pairing
The plugin alows for creation of paired files like `markdown` or `python` etc. for the jupyter file which then allows for tracking the changing of the files in a managable way. (Might allow for actually reviewing the notebooks.)

*Possible issue:* I didn't find a way to revert back to `.ipynb` file so the notebook to be submitted needs to be the final version. 

---
## nbstripout
https://github.com/kynan/nbstripout


### Strip output
Strip output from IPython / Jupyter notebook (modifies the files in-place):
```console
nbstripout FILE.ipynb [FILE2.ipynb ...]
```

### Write to stdout:
Write to stdout e.g. to use as part of a shell pipeline:
```console
cat FILE.ipynb | nbstripout > OUT.ipynb
```
This command writes everything, including metadata, to shell hence probably not usefull in this situation.
