This tutorial will go through the basics of converting python code into an exe, which can run on any windows machine without the need for python to be installed - using py2exe library.

# How exactly does this work
Python code, when executed converts to `bytecode` 
The obvious issue here is that `.exe` window excutables is made of machine code, not bytecode - bytecode "can" be converted to machine code, but it's incredibly complex and introduces unreliability of the code.

> Neither bytecode or machine code is human readable, it's not something someone typically can understand or write.

**This is what the py2exe library does** rather than converting the bytecode into machine code > instead it just combines the python intepreter into the exe, that way python is**theoretically** on any windows machine you have the python exe on.


## installation
First you need to install py2exe like most other python libraries
```
pip install py2exe
```

Create a basic `setup.py` file with the following basic code

```python
from distutils.core import setup
import py2exe

setup(
    console=['shop.py'],
)
```

> If your code is a GUI, change `console` to `window`

Then run
```
python setup.py py2exe
```
This will create a build and dist folder. Your exe program will be in the dist folder.


py2exe doesn't allow for direct bundling of everything into one exe with no other files, but you can expand on the setup.py file to include additional options.

```python
from distutils.core import setup
import py2exe

setup(
    name="Shop Application",
    version="1.0",
    description="A sample Python application",
    author="Your awesome name",
    options={
        "py2exe": {
            "packages": ["os"],  # Include additional packages
            "excludes": ["tkinter"],  # Exclude unnecessary modules
            "bundle_files": 1,  # Bundle everything into one file
            "compressed": True,  # Compress the library archive
        }
    },
    console=[
        {
            "script": "shop.py",  # Main script
            "icon_resources": [(0, "icon.ico")],  # Optional: Add an icon
        }
    ],
    #data_files=[("assets", ["assets/file1.txt", "assets/file2.txt"])],  # Include additional files
)

```

From this, you can see it's compressed and bundled but when you try doing this, you'll notice that there's still some external files, which is how py2exe works.


## py2exe with tkinter
This should work outside the box with tkinter too for as long as you don't "exclude" the tkinter library from the setup.

For tkinter applications, follow the above tutorial for py2exe as it works exactly the same for tkinter too