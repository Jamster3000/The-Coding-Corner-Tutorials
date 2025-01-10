This tutorial will go through the basics of converting python code into an exe, which can run on any windows machine without the need for python to be installed - using Pyinstaller library.

> See the shop.py file that goes with this tutorial

# How exactly does this work
Python code, when executed converts to `bytecode` 
The obvious issue here is that `.exe` window excutables is made of machine code, not bytecode - bytecode "can" be converted to machine code, but it's incredibly complex and introduces unreliability of the code.

> Neither bytecode or machine code is human readable, it's not something someone typically can understand or write.

**This is what the pyinstaller library does** rather than converting the bytecode into machine code > instead it just combines the python intepreter into the exe, that way python is**theoretically** on any windows machine you have the python exe on.

Here is some prewritten code a very simple terminal text based shopping application.

> make sure to run this code yourself before hand to ensure it works as expected.

This works better if you are able to run it in the termianl instead of an interpreter - but nonetheless should still work as expected.

# install pyinstaller
1. Open a termainl/command prompt
2. Run the command `pip install pyinstaller` (this might be slightly different on your machine or you might want a virtual environment first).

# running pyinstaller
In a terminal that can access the python code, run
`pyinstaller [filename.py]`
Depending on your device's performance, this could take several mintues.

__                                                                                                                                                __

Once the command finished running, you'll notice 1 file and two folders that have been generated from this.

- **.spec** file - This is a configuration file, you shouldn't have to worry too much about this > this is normally modified in the pyinstaller command rather than the file.
- **build** - This is where all the temp files, logs and reports are stored > once the pyinstaller command has finished, you can safetly remove this folder.
- **dist** - this contains the actual standalone excutable file.

As mentioned, the runnable execution lives in the **dist folder** any other files that are here in this folder are also required to be in the same folder as the `.exe` > there might be a **_internal** folder this contains things that is strictly required for the exe to work.




.



# Pyinstaller flags
There are flags (normally extra arguments in a command that often start with `--`) that can be added to your pyinstaller command in the terminal, below is a list of the most usful ones you may want to try out yourself.

- `--onefile` - bundles all the files and resources needed for the exe into one exe, meaning the dist would contain an exe and nothing else.
> This will make the exe larger, and potentally slower.

- `--noconsole` - This hides the terminal/console in the background so it can't be seen, this is most ideal for GUI applications where you don't need to see the terminal open up.

- `--windowed` - this is the same as `--noconsole` except just more explicit. 

- `--add-data` - This allows you to explicitly mention other files and resources that the code requires, such as data, images, etc. `pyinstaller --add-data "data/config.txt:config" script.py` for example. You can mention multiple `--add-data` flags in the command.

- `--icon` - used to specify the icon used for the executable, this is common as all exe's have an icon. For this to work you will need an `.ico` file.

- `--clean` - This cleans up anything that is already in the build folder.

- `--debug=all` - This is for testing, it allows you to see logs of warnings and errors.

- `--strip` - this removes unnecessary  symbols and data from the metadata in an attempt to decrease the size of the final .exe file.

- `--upx` (Ultimate Packaging eXecutable) - This can reduce the final size of the exe by further compressing it - Depending on the code that's being converted this can sometimes make the exe slower - more effective for large .exe's 
You have to have `upx` installed before using this, it's a seperate thing.

- `--no-upx` - obvious the oposite of using upx

- `--name` - allows you to specify a name for the .exe

There are more, but these are the usful ones that you would likely require or want to use.



## pyinstaller with tkinter
Pyinstaller should work out the box with tkinter (third party tkinter libraries, such as customtkinter requires the use of hidden-import flag)

Running
`pyinstaller simple_gui` works well with tkinter without the requirement of any other commands
