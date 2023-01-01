# ModCLI

[English](https://github.com/iamliuzy/ModCLI/blob/main/README.md) | 简体中文

管理 Minecraft 模组的命令行工具

本程序目前还在开发状态。



## 计划功能

- 通过几个命令轻松管理您的模组。
- 使用搜索功能快速找到模组。


### 示例

将 mod 添加到库：
```
$ modcli -add "\\path\\to\\mod\\mod.jar"
```
按名称在库中搜索 mod：
```
$ modcli -searchName "ModName"
```
或按标签搜索：
```
$ modcli -searchTag "标签"
```


## 安装

目前仅能自行下载源代码运行：
在安装Python的情况下，运行：
```
pip install -r requirements.txt
```
以安装依赖（可能有点慢，建议科学上网），并运行：
```
python main.py
```
以运行程序。




## 贡献者

- [@iamliuzy](https://www.github.com/iamliuzy)


## 链接

如果您有任何问题或想法，可以在[Discussions页面](https://github.com/iamliuzy/ModCLI/discussions)讨论。

如果程序崩溃，请在[Issue页面](https://github.com/iamliuzy/ModCLI/issues)报告。
