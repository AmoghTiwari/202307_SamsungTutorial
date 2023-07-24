# 202307_SamsungTutorial

**Github Repo**:  https://github.com/AmoghTiwari/202307_SamsungTutorial <br/>
**Colab Notebook**: https://tinyurl.com/yxpptysj

# Day-1
## Environment Setup
It is a good practice to create a virtual environment before installing packages. You can do so either with pip or anaconda. Pip usually comes preinstalled with python while anaconda needs to be installed (See instructions [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html)). 

### Pip
```python3 -m venv <virtual_env_name>
source venv/bin/activate
pip install numpy
pip install matplotlib
pip install opencv-python
```

### Conda
```conda create -n <virtual_env_name> python=3
conda activate <virtual_env_name>
conda install -c anaconda numpy
conda install -c conda-forge opencv
conda install -c conda-forge matplotlib
```

**To use a locally created virtual env on jupyter notebook**, you may use this: https://medium.com/@nrk25693/how-to-add-your-conda-environment-to-your-jupyter-notebook-in-just-4-steps-abeab8b8d084

## Instructions to Use


# Day-2
## Environment Setup
