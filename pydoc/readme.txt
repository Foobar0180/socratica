Pydoc

The pydoc module automatically generates documentation from Python modules. The 
documentation can be presented as pages of text on the console, served to a Web 
browser, or saved to HTML files. 

> python -m pydoc
> python -m pydoc math

> python
>>> help(pow) ## interactive help

> python -m pydoc -k ftp # search all modules for the keyword 'ftp'
> python -m pydoc ftplib

> python -m pydoc -p 314 ## starts a webserver on port 314 to view documentation

> python -m pydoc -b ## starts the pydoc server on an available port

> mkdir pydoc_demo
> cd pydoc_demo
> python -m pydoc -w <name of function, class or module e.g. json>
> start json.html