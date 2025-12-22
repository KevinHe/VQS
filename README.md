# VQS - Excel 文件合并工具

这是一个基于Python开发的Excel文件合并工具，提供了友好的图形界面，可以在Windows系统上直接运行。

## 功能特性

- ✅ 图形化界面操作，简单易用
- ✅ 支持批量导入多个Excel文件（.xlsx, .xls）
- ✅ 自动合并相同格式的Excel文件
- ✅ 导出为CSV格式文件
- ✅ 实时显示输入文件列表和输出文件路径
- ✅ 支持UTF-8编码，完美支持中文

## 系统要求

### 使用exe版本（推荐给最终用户）
- Windows 7 及以上版本
- 无需安装Python

### 使用Python版本（开发者）
- Windows 7 及以上版本
- Python 3.7 或更高版本

## 快速开始（使用exe文件）

**如果你收到了exe文件，可以直接使用：**

1. 双击运行 `Excel合并工具.exe`
2. 无需安装Python或任何依赖包
3. 直接开始使用（跳转到"操作说明"部分）

## 安装步骤（开发者/从源码运行）

### 1. 安装Python

如果还没有安装Python，请访问 [Python官网](https://www.python.org/downloads/) 下载并安装。

**注意**：安装时请勾选 "Add Python to PATH" 选项。

### 2. 安装依赖包

打开命令提示符（CMD）或PowerShell，进入项目目录，运行以下命令：

```bash
pip install -r requirements.txt
```

或者手动安装依赖：

```bash
pip install pandas openpyxl
```

## 使用方法

### 方式一：双击运行（推荐）

1. 双击 `excel_merger.py` 文件即可运行
2. 如果无法双击运行，请右键选择"打开方式" → "Python"

### 方式二：命令行运行

打开命令提示符，进入项目目录，运行：

```bash
python excel_merger.py
```

## 操作说明

1. **导入文件**
   - 点击"导入文件"按钮
   - 在弹出的对话框中选择一个或多个Excel文件
   - 选中的文件会按顺序显示在"输入文件列表"中

2. **合并文件**
   - 点击"合并文件"按钮
   - 程序会自动读取并合并所有Excel文件
   - 选择保存位置和文件名
   - 合并完成后会在"输出文件"区域显示文件路径

3. **清空列表**
   - 点击"清空列表"按钮可以清空当前的输入文件列表

4. **关闭程序**
   - 点击"关闭程序"按钮或窗口的关闭按钮退出程序

## 注意事项

- 所有输入的Excel文件应具有相同的列结构（列名和列数相同）
- 合并后的文件会保存为CSV格式，使用UTF-8编码（带BOM），可在Excel中直接打开
- 建议在合并前备份原始文件
- 如果文件较大，合并过程可能需要一些时间，请耐心等待

## 文件说明

- `excel_merger.py` - 主程序文件
- `requirements.txt` - Python依赖包列表
- `build_exe.bat` - 打包脚本（将程序打包成exe）
- `README.md` - 使用说明文档

## 常见问题

**Q: 提示"找不到模块"错误？**

A: 请确保已安装所有依赖包，运行 `pip install -r requirements.txt`

**Q: 合并后的CSV文件在Excel中打开中文乱码？**

A: 本工具已使用UTF-8-BOM编码，应该不会出现乱码。如果仍有问题，请尝试用记事本打开CSV文件，然后"另存为"时选择ANSI编码。

**Q: 可以合并不同格式的Excel文件吗？**

A: 可以尝试，但建议所有文件具有相同的列结构，否则可能会出现数据错位。

## 打包成exe文件（开发者）

如果你需要将程序打包成exe文件分发给其他用户，请按照以下步骤操作：

### 方法一：使用打包脚本（推荐）

1. 确保已安装所有依赖：
   ```bash
   pip install -r requirements.txt
   ```

2. 双击运行 `build_exe.bat` 脚本

3. 等待打包完成，生成的exe文件位于 `dist\Excel合并工具.exe`

### 方法二：手动打包

1. 安装PyInstaller：
   ```bash
   pip install pyinstaller
   ```

2. 运行打包命令：
   ```bash
   pyinstaller --onefile --windowed --name "Excel合并工具" excel_merger.py
   ```

3. 打包完成后，exe文件位于 `dist` 目录

### 打包说明

- `--onefile`: 打包成单个exe文件
- `--windowed`: 不显示命令行窗口（GUI程序）
- `--name`: 指定生成的exe文件名
- 生成的exe文件约50-100MB（包含所有依赖库）
- 首次运行可能需要几秒钟启动时间（解压临时文件）

### 分发说明

打包完成后，你可以：
1. 直接分发 `dist\Excel合并工具.exe` 文件给用户
2. 用户无需安装Python或任何依赖包
3. 双击exe文件即可运行
4. 建议同时提供简单的使用说明

## 许可证

本项目采用 MIT 许可证，详见 LICENSE 文件。
