## Minimum Working Example: SMAA

This is a minimum working example demonstrating SMAAx1 (High preset).

Compared to the reference program, its not bit-exact but its pretty close and should be visually indistinguishable.

I've included a small python program that will compare the output of my demo with the output of the reference program.
Dependencies of that python program are the Python Imagining library and Numpy, so remember to install them with pip first.
Run it by doing `python compare.py`.

Regarding the reference program that I use, I compile it myself from the source here: https://github.com/iryoku/smaa/tree/master/Demo/DX10
The latest offical binary is of version 2.8, but there had been many commits on the master branch since.
From my test, the output from release 2.8 and the current master branch is different.

Here's how I compile the program:

- I'm using Visual Studio 2019 16.9.4 with the "Desktop developement with C++" environment installed.
- Download and install the June 2010 DirectX SDK.
- Upon opening the solution, retarget the project to the latest Windows SDK and Platform Toolset when prompted (for me, it's Windows SDK 10.0 and Platform Toolset v142).
- Add the library `legacy_stdio_definitions.lib` to the linker.
  - Right click on "Demo" in the Solution Explorer and click on "Properties".
  - On the left pane, go to "Configuration Properties" > "Linker" > "Input".
  - On the right pane, click on the value of "Additional Dependencies" and select "<Edit>" from the dropdown.
  - Add "legacy_stdio_definitions.lib" into the list.
- Switch over to the Release configuration and compile it.
- At this point, 3 build erros should occur:
  - DXUTenum.cpp (line 3975): Cast the paramer of `abs` to `long`. e.g. `long(...)`
  - DXUTmisc.cpp (line 1372): Change the type of argument `strFile` to `const WCHAR*`
  - Demo.cpp (line 165): Remove the function `float`
- The first time you run the program after compiling there will be a lot of Symbol loading and the program may seem to freeze, please wait patiently.
