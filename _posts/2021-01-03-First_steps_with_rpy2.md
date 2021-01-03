---
layout: post
title: First steps with rpy2
tags: r python statistics
---

# How to install in Docker
I haven't found a way to install it via pipenv, so I added the following lines
directly to my Dockerfile
```
RUN apt-get update && apt-get install -y r-base
RUN pip install rpy2
```
Yes, don't forget to install R before installing `rpy2`.

# How to install and load a R package
Default package should come with your R installation so that you can direclty
load them by doing
``` 
my_r_package_loaded = rpackages.importr("my_r_package")
``` 
You can then use your loaded R package like a module. For instance,
```
my_r_package_loaded.this_amazing_script(var1=1.0, var2='hello', var3=3.4)
```

But for specific packages, like here the `TOSTER` packace, you can do
this
```
from rpy2 import robjects
import rpy2.robjects.packages as rpackages

utils = rpackages.importr('utils')
utils.chooseCRANmirror(ind=1)
utils.install_packages("TOSTER")
```

# How to run a R script in a notebook
Given the script is in the same directory as your notebook, you can do
```
import rpy2.robjects as robjects
r = robjects.r
r.source('my_first_r_script.r')
```

# How to plot from R using rpy2

```
import rpy2.robjects as robjects
from rpy2.robjects.lib import grdevices
from IPython.display import Image, display

with grdevices.render_to_bytesio(grdevices.jpeg, width=1024, height=896, res=150) as img:
    r.source('my_first_r_plot.r')
    
display(Image(data=img.getvalue(), format='jpeg', embed=True))
```
More on the plotting can be found in this demo
[notebook](https://github.com/marsja/jupyter/blob/master/Rpy2%20and%20R%20plots%20in%20a%20Jupyter%20Notebook!.ipynb)
