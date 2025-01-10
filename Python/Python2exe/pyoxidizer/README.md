This tutorial will go through the basics of converting python code into an exe, which can run on any windows machine without the need for python to be installed - using pyoxidizer library.

Pyoxidizer is a modern tool for great performing exe programs from python

# How exactly does this work
Python code, when executed converts to `bytecode` 
The obvious issue here is that `.exe` window excutables is made of machine code, not bytecode - bytecode "can" be converted to machine code, but it's incredibly complex and introduces unreliability of the code.

> Neither bytecode or machine code is human readable, it's not something someone typically can understand or write.

**This is what the pyoxidizer library does** rather than converting the bytecode into machine code > instead it just combines the python intepreter into the exe, that way python is**theoretically** on any windows machine you have the python exe on.


## Install
1. Install [Rust](https://rustup.rs/) - follow the instructions on the website - You won't need to do any programming in rust (you likely won't even see any rust code) but Pyoxidizer still requires it.
2. Install pyoxidizer tool, running this in terminal `cargo install pyoxidizer` - cargo is rusts's package manager like pip is for python. There are over 650 packages that are installed so this might take some time.
3. Run this in a terminal to get the version which ensures it installed `pyoxidizer --version` 

> Make sure rust is up to date, you may have issues even installing pyoxidizer otherwise

__                                                                                                                        __

- Make sure you're in a folder you can work in.
- open a terminal in this folder, then run the command `pyoxidizer init-config-file shop-application

Then cd into the `shop-application` folder that has appeared. Inside this folder, you'll see a `pyoxidizer.bzl` - This is the config file > Unfortunatley you will need to edit it too 😮‍💨 
But first, whilst you're in the `shop-application` folder, place your python file in here too.


Open the `pyoxidizer.bzl` file up in text editor, IDE, or anything else you like. If you dare take a noticable look at the content of the files, you'll see much of it is commented out.
This code you see is called `starlark` this isn't actually python as such, but a small, deterministic, and untyped scripting language - typically used for config files and such.


1. `python_config.run_module` find this line, uncomment it and change it to `python_config.run_module = "shop_application"` - this treats the python file as a module
2. find `exe = dist.to_python_executable(` this line, underneath set the name variable to whatever you want the exe to be called.
e.g.
```python
exe = dist.to_python_executable(
        name="shop",
        packaging_policy=policy,
        config=python_config,
    )
```

3. Finally, find `exe.add_python_resources(exe.read_package_root(` and uncomment the entire code block. Change the path to "." and the package to "shop__application
e.g.
```python
exe.add_python_resources(exe.read_package_root(
        path=".",  # Current directory
        packages=["shop_application"]  # No specific packages, just include all Python files
    ))
```
This adds the python file as a package (aka: module) as a resource.

This reads all the files from the current shop-application folder, and adds shop_application as package (since the file is being treat as a module.

> NOTE: You should use 
> if __name__ == "__main__":
>     main()
> In the python file, otherwise you could have problems.

Once that is done, you can save the file.
**Back to the terminal**
finally in the terminal run
```pyoxidizer run```

This will take several mintues, but once done, you have a fully working exe in the build folder (given that you go into the many folder directories). Once you're happy with that, you can even take that exe out of the folder and run it else where, everything needed is compiled and bundled into one exe.


## Other Configurations
- `policy.bytecode_optimize_level_two = True` - This can be commented out to optimise the bytecode, which can help with performance if you are having an issue with it.
- `policy.extension_module_filter = "minimal"` - Uncomment this line to reduce the size of the extension by omitting unused extensions.
- `python_config.allocator_backend` - There are three different memory allocator types (not including the default one for python. 
    - **jemalloc** A general-purpose memory allocator designed for high-performance and multi-threaded environments
    - **mimalloc** A compact, fast memory allocator for efficiency and performance
    - **snmalloc** A memory allocator focused on security, performance, and scalability

## MSI installer
Although it's not built in, it has support to use WIX Toolset to generate an installer.


## Pyoxidizer with Tkinter
This is where things get complicated. 
pyoxidizer doesn't work with tkinter out of the box, which means it requires some different commands in the config.

There is little to no resources online to answer this, the obvious solution in the config file just doesn't work as expected. So after 5+ hours of trying to figure it out, I've just figured that it's either not possible or incredibly complex.

Therefore this is the only presented tutorial of py to exe that I can't give any guidance on for Tkinter.