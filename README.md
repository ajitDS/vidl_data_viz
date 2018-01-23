# Vanderbilt Institute for Digital Learning - Data Visualization

__Collaborators__: 

1. Kate Brady ([katherine.a.brady@vanderbilt.edu](mailto:katherine.a.brady@vanderbilt.edu))
2. Victor Calderon ([victor.calderon@vanderbilt.edu](mailto:victor.calderon@vanderbilt.edu))
3. Gayathri Narasimham ([gayathri.narasimham@vanderbilt.edu](mailto:gayathri.narasimham@Vanderbilt.Edu))

**Description**:

A working group put on by the [Vanderbilt Institute for Digital Learning](https://www.vanderbilt.edu/vidl/) to talk about data visualization.

**Location**:

The workshop meets at Kirkland Hall. For directions: [https://goo.gl/maps/W17uyp6MF1t](https://goo.gl/maps/W17uyp6MF1t)

# Topics
1. Sep - [Tableau](https://public.tableau.com/profile/atakan.okan#!/vizhome/Workshop_3/Dashboard1)
1. Oct - iPython Notebooks
1. Nov - Seaborn
1. Jan - Libraries for Non-Numerical Visualization

# Live Version

You can execute the iPython Notebooks in this repository by **clicking** the following button:

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/kbrady/vidl_data_viz/master)

## Installing Environment & Dependencies

To use the scripts in this repository, you must have _Anaconda_ installed on the systems that will be running the scripts. This will simplify the process of installing all the dependencies.

If you are unsure if you have Anaconda on your machine run `conda -h` in your terminal. This should bring up a help message. If you get a command not found error, follow the installation instructions [here](https://docs.anaconda.com/anaconda/install/).  After installation, you may still need to add Anaconda to your path variable. If `conda -h` still doesn't work, see instructions on adding Anaconda to your path in the Anaconda installation instructions.

For reference on Anaconda environments, see: [https://conda.io/docs/user-guide/tasks/manage-environments.html](https://conda.io/docs/user-guide/tasks/manage-environments.html)

The package counts with a __Makefile__ with useful functions. You must use this Makefile to ensure that you have all the necessary _dependencies_, as well as the correct _conda environment_. 

* Show all available functions in the _Makefile_

```
$:  make show-help
    
    Available rules:
    
    clean               Delete all compiled Python files
    environment         Set up python interpreter environment - Using environment.yml
    remove_environment  Delete python interpreter environment
    test_environment    Test python environment is setup correctly
    update_environment  Update python interpreter environment
```

* __Create__ the environment from the `environment.yml` file:

```
    make environment
```

* __Activate__ the new environment __vidl_viz__.

```
    source activate vidl_viz
```

* To __update__ the `environment.yml` file (when the required packages have changed):

```
  make update_environment
```

* __Deactivate__ the new environment:

```
    source deactivate
```