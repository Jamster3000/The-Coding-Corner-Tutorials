This tutorial will cover the following tools/libraries to transform your python code into a runable exe program for any windows system with or without python installed.

__                                                     __
- **Pyinstaller**
- **CX_Freeze**
- **Nuitka**
- **py2exe**
- **pyoxidizer**
__                                                     __
Click on any the links above to go straight to the section to include that library/tool

> NOTE: This tutorial assumes that you're developing on windows.



# Breakdown of the packaging tools
## Pyinstaller
Most popular tool for creating standalone executables from python for windows, linux, and macOS. This is beginner-friendly! This works well for most applications but can lead to larger executable sizes which then affects it's performance.
**Difficulty**: Easy to moderate, depending on the complexity of the program.
**Best for**: quick packaging/testing, ease of use.

## CX_Freeze
Similar tool for pyinstaller but it's more supported with python 3.x. it's lightweight and supports windows, macOS, and linux. This offers more control over packaging and customization compared to Pyinstaller but erquires more configuration.
**Difficulty**: Moderate, requires some configuration
**Best for**: those that need more control over packaging.

## Nuitka
Converts python code into C and then compiles it into an exe. THis results in faster execution and a smaller executables than other options. It offers a performance boost, especially for computationally intensive applications. Alos has great support for external libraries.
**Difficulty**: Easy to moderate.
**Best for**: Performance-focused applications.

## Py2exe
A tool that converts python code to windows exe files, only supports windows. It's been around for a long time and is limited compared to other options.
**Difficult**: Easy to use,.
**Best for**: Windows only applications where only simplicity is key.

## Pyoxidizer
This is a newer tool using rust language to create the standalone executable. It offers good performance and smaller file sizes. It's especially well-suited for a modern packaging needs but has a large steeper learning curve due to it's unique approach to python to exe and it's use of rust. Tutorial doesn't cover GUI with this.
**Difficulty** Hard+ due to using rust and very little documentation for it.
**Best for**: Advanced users looking for a small, efficient executables, and those that are familiar enough with rust.