This tutorial will go through the basics of converting python code into an exe, which can run on any windows machine without the need for python to be installed - using nuitka library.


Unlike other tools and libraries out there, this one works different. It first translates python code into efficent C code, then it compiles that C code into an exe.

> when programming in C, typically it is compiled into an exe everytime it is executed.

You may notice that running the exe doesn't cause any installed antivirus to throw a fit over it. This is because the way other libraries and tools bundle and combine the python code and python intpreter - which is very similar to how malware is created and distributed - an exe created with C code is nothing more than compiling it which doesn't set the antivirus off since there are no obvious bad actions going on.

Also, if you're a fan of keeping your intellectual property to yourself without any theft, Nuitka makes it pratically impossible to reverse engineer the code back to what it was because of how the converstion and compiling works.


## installation
First install nuitka
```
pip install nuitka
```

Once that's installed, prepare your python file, then run in a terminal:
```
nuitka --standalone shop.py
```

Running this command for the first time, you may get a question in the terminal

```bash
Nuitka will make use of Dependency Walker (https://dependencywalker.com) tool
to analyze the dependencies of Python extension modules.

Is it OK to download and put it in 'C:\Users\[user]\AppData\Local\Nuitka\Nuitka\Cache\DOWNLO~1\depends\x86_64'.

Fully automatic, cached. Proceed and download? [Yes]/No : 
```

This is simply asking if it can download an additional tool which helps it with DLL's and even more useful with missing DLLs.


.


### Here is an... almost overwhelming list of commands and options you can use.

- **--standalone** Creates a standalone executable (bundling it all together
- **--onefile** THis packages everything into one file.
- **--no-pyi-launcher** Disables use of the python executable launcher

#### Performance
- **--ito** Enables link-time optimization to improve performance
- **--no-optimization** disables all optimization used, this is most useful for debugging.
- **--trace-functions** Traces function calls in the output, this helps with debugging.

- **--follow-imports** This ensures that all dependencies are included in the exe including indirectly used ones.

- **--debug** enables debug mode for tracing errors and gathering information.
- **--trace-cc** shows the command being run by the C compiler.
- **--no-cache-dir** disables the use of any cache during the process.

- **--no-conversion** stops Nuitka from attempting to convert any python files into .pyc or .pyo files.
- **--no-pytz** disables the use of pytz packages, which are commonly bundled with python applications.

- **--icon=[icon-file]** an icon that can be used for the exe program
- **--windows-disable-console** disables the console window.



## Nuitka with Tkinter
Only one additional flag is required to make Tkinter work as an exe (not listed above).

the `--enable-plugin=tk-inter` flag is required to include tkinter otherwise the exe will not work.
e.g.,
```bash
nuitka --enable-plugin=tk-inter --standalone simple_gui.py
```