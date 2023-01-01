# ModCLI

English | [简体中文](https://github.com/iamliuzy/ModCLI/blob/main/README_ZH_CN.md)

A command-line tool to manage Minecraft mods

This program is currently still in development.



## Planning functions

- Easily manage your mods with a few commands.
- Use the search function to quickly find mods.


### Example

Add the mod to the library:
```
$ modcli -add "\path\to\mod\mod.jar"
```
Search the library for mods by name:
```
$ modcli -searchName "ModName"
```
or search by tag:
```
$ modcli -searchTag "Tag"
```


## Install

Now, you can only download the source code and run it yourself:
With Python installed, run:
```
pip install -r requirements.txt
```
To install dependencies (may be a bit slow, it is recommended to go online scientifically), and run:
```
python main.py
```
to run the program.




## Contributors

- [@iamliuzy](https://www.github.com/iamliuzy)


## Link

If you have any questions or ideas, you can discuss them on the [Discussions page](https://github.com/iamliuzy/ModCLI/discussions).

If the program crashes, please report it on the [Issue page](https://github.com/iamliuzy/ModCLI/issues).
