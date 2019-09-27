# test-driven-dev
Test Driven Development

This project takes numerical data from stdin, calculates the mean and standard
deviation, and returns a plot of the data saved to the current directory.

Python files:
math_lib.py : a math library containing mean and stdev functions
test_math_lib.py : unit test file for math_lib.py
get_day.py : module containing the function read_stdin_col(col_num)
data_viz.py : a module containing functions to make plots
test_data_viz.py : unit test file for data_viz.py
viz.py : script to execute the functions

To use this project from the command line:

$ bash gen_data.sh | python viz.py --out_file hist.png --plot_type histogram

this will make a histogram using data written to stdin by gen_data.sh, and
save the plot as hist.png in the current directory.

How to install:

1. Ensure that conda is installed in your environment
If `$ conda` gives an error, install conda as required by your operating system

2. Update and configure conda

```
$ conda update --yes conda

$ conda config --add channels bioconda

$ echo ". $HOME/miniconda3/etc/profile.d/conda.sh" >> $HOME/.bashrc
```

3. Install matplotlib

```
$ conda install matplotlib
```

4. Install python and required libraries

```
$ conda install --yes python=3.6

$ conda install -y pycodestyle
```

5. Access software on [GitHub]
(https://github.com/cu-swe4s-fall-2019/test-driven-development-alisoncleonard)
