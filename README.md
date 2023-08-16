# 202307_SamsungTutorial

# Day-1
## Environment Setup
It is a good practice to create a virtual environment before installing packages. You can do so either with pip or anaconda. Pip usually comes preinstalled with python while anaconda needs to be installed (See instructions [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html)). 

### Pip
```
python3 -m venv <virtual_env_name>
source /path/to/venv/bin/activate
pip install numpy
pip install matplotlib
pip install opencv-python
```

### Conda
```
conda create -n <virtual_env_name> python=3
conda activate <virtual_env_name>
conda install -c anaconda numpy
conda install -c conda-forge opencv
conda install -c conda-forge matplotlib
```

**To use a locally created virtual env on jupyter notebook**, you may use this: https://medium.com/@nrk25693/how-to-add-your-conda-environment-to-your-jupyter-notebook-in-just-4-steps-abeab8b8d084

## File Structure and Usage Instructions
- `Day01_Notebook.ipynb`: Notebook containig the questions/tasks for the day
- `public`: The audience doesn't need to code up everything from scratch. They can use one of these scripts. For tasks where no corresponding script is provded, it means you need to code up the task on your own (You can reus code from your own previous tasks)
- `private`: The reference codes for all the tasks. However, these codes also have a few bugs here and there, introduced intentionally. 
- `annotated`: The modified/updated scripts from the in-person session. These should have the working code.
- `notes.md`: A reference document with rough description of possible expected errors and solutions for different tasks


# Day-2
## Environment Setup
The same environment as Day-1 can be used.
## File Structure and Usage Instructions
It's self explanatory

# Debugging Suggestions
In case you get some errors while running the scripts, check the below two things before anything else:
1. If the specified paths are correct. The directory structure was modified somewhat. So some paths might have got messed up.
2. If `plt.show()` command is present. Since we used a notebook where in most cases we can get by without using `plt.show()` also, there are places where `plt.show()` hasn't been used. However, if you are running this on your local PC, without a notebook, then you would need to add `plt.show()` wherever relevant.
