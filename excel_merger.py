#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Excel文件合并工具
支持选择多个Excel文件，合并后导出为CSV格式
"""

import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import pandas as pd
import os
from datetime import datetime


class ExcelMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Excel文件合并工具")
        self.root.geometry("700x500")
        self.root.resizable(True, True)

        # 存储选择的文件路径列表
        self.input_files = []
        # 输出文件路径
        self.output_file = ""

        # 创建界面
        self.create_widgets()

    def create_widgets(self):
        """创建界面组件"""
        # 主容器
        main_frame = tk.Frame(self.root, padx=10, pady=10)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # ======== 输入文件列表区域 ========
        input_label = tk.Label(main_frame, text="输入文件列表:",
                              font=("Arial", 10, "bold"))
        input_label.pack(anchor=tk.W, pady=(0, 5))

        # 创建带滚动条的文本框显示文件列表
        input_frame = tk.Frame(main_frame)
        input_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        self.input_text = scrolledtext.ScrolledText(
            input_frame,
            height=10,
            width=80,
            font=("Consolas", 9),
            state=tk.DISABLED,
            bg="#f0f0f0"
        )
        self.input_text.pack(fill=tk.BOTH, expand=True)

        # ======== 输出文件区域 ========
        output_label = tk.Label(main_frame, text="输出文件:",
                               font=("Arial", 10, "bold"))
        output_label.pack(anchor=tk.W, pady=(10, 5))

        output_frame = tk.Frame(main_frame)
        output_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 15))

        self.output_text = scrolledtext.ScrolledText(
            output_frame,
            height=3,
            width=80,
            font=("Consolas", 9),
            state=tk.DISABLED,
            bg="#f0f0f0"
        )
        self.output_text.pack(fill=tk.BOTH, expand=True)

        # ======== 按钮区域 ========
        button_frame = tk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=(10, 0))

        # 导入按钮
        import_btn = tk.Button(
            button_frame,
            text="导入文件",
            command=self.import_files,
            width=12,
            height=2,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 10, "bold"),
            cursor="hand2"
        )
        import_btn.pack(side=tk.LEFT, padx=5)

        # 合并按钮
        merge_btn = tk.Button(
            button_frame,
            text="合并文件",
            command=self.merge_files,
            width=12,
            height=2,
            bg="#2196F3",
            fg="white",
            font=("Arial", 10, "bold"),
            cursor="hand2"
        )
        merge_btn.pack(side=tk.LEFT, padx=5)

        # 清空按钮
        clear_btn = tk.Button(
            button_frame,
            text="清空列表",
            command=self.clear_list,
            width=12,
            height=2,
            bg="#FF9800",
            fg="white",
            font=("Arial", 10, "bold"),
            cursor="hand2"
        )
        clear_btn.pack(side=tk.LEFT, padx=5)

        # 关闭按钮
        close_btn = tk.Button(
            button_frame,
            text="关闭程序",
            command=self.close_app,
            width=12,
            height=2,
            bg="#f44336",
            fg="white",
            font=("Arial", 10, "bold"),
            cursor="hand2"
        )
        close_btn.pack(side=tk.RIGHT, padx=5)

    def import_files(self):
        """导入Excel文件"""
        files = filedialog.askopenfilenames(
            title="选择Excel文件",
            filetypes=[
                ("Excel files", "*.xlsx *.xls"),
                ("All files", "*.*")
            ]
        )

        if files:
            # 添加新文件到列表（避免重复）
            for file in files:
                if file not in self.input_files:
                    self.input_files.append(file)

            # 更新显示
            self.update_input_display()
            messagebox.showinfo("成功", f"已导入 {len(files)} 个文件")

    def update_input_display(self):
        """更新输入文件列表显示"""
        self.input_text.config(state=tk.NORMAL)
        self.input_text.delete(1.0, tk.END)

        if self.input_files:
            for idx, file in enumerate(self.input_files, 1):
                self.input_text.insert(tk.END, f"{idx}. {file}\n")
        else:
            self.input_text.insert(tk.END, "（暂无文件）")

        self.input_text.config(state=tk.DISABLED)

    def update_output_display(self, file_path):
        """更新输出文件显示"""
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, file_path)
        self.output_text.config(state=tk.DISABLED)

    def merge_files(self):
        """合并Excel文件"""
        if not self.input_files:
            messagebox.showwarning("警告", "请先导入Excel文件！")
            return

        try:
            # 定义列映射关系：源文件列名 -> 输出文件列名
            column_mapping = {
                '供应商名称': 'Vendor Name',
                '维谛组织': 'OU Name',
                '发票代码': 'invoicecode',
                '发票号': 'invoice no',
                '订单号': 'PoNo',
                '物料编码': 'ITEM',
                '行号': 'Line Num',
                '数量': 'QuantitY',
                '单价(不含税)': 'Price',
                '总价(不含税)': 'Total(Pre-tax)',
                '税额': 'TAX AMT',
                '送货日期': 'Deliver date'
            }

            # 输出文件的列顺序（包含空列）
            output_columns = [
                'Vendor Name', 'OU Name', 'invoicecode', 'invoice no',
                'PoNo', '', 'ITEM', 'Line Num', 'QuantitY', 'Price',
                'Total(Pre-tax)', 'TAX AMT', 'Deliver date', 'TAX CODE'
            ]

            # 读取所有Excel文件并合并
            all_data = []

            for idx, file in enumerate(self.input_files, 1):
                try:
                    # 读取Excel文件
                    # skiprows=7 跳过前7行（第1-6行是描述，第7行是标题）
                    # header=0 表示跳过后的第一行作为列名
                    df = pd.read_excel(file, skiprows=7, header=0)

                    # 去除列名两端的空格
                    df.columns = df.columns.str.strip()

                    # 创建新的DataFrame，按照输出列顺序重新组织
                    new_df = pd.DataFrame()

                    # 映射源文件列到输出列
                    for source_col, target_col in column_mapping.items():
                        if source_col in df.columns:
                            new_df[target_col] = df[source_col]
                        else:
                            # 如果源文件中没有这一列，创建空列
                            new_df[target_col] = ''

                    # 添加空列（PoNo和ITEM之间）
                    new_df.insert(5, '', '')

                    # 添加TAX CODE列（默认为空）
                    new_df['TAX CODE'] = ''

                    # 确保列的顺序与output_columns一致
                    new_df = new_df[output_columns]

                    all_data.append(new_df)
                    print(f"已读取文件 {idx}/{len(self.input_files)}: {os.path.basename(file)}")

                except Exception as e:
                    messagebox.showerror("错误", f"读取文件失败：{os.path.basename(file)}\n错误信息：{str(e)}")
                    return

            # 合并所有数据
            merged_df = pd.concat(all_data, ignore_index=True)

            # 生成输出文件名
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            default_filename = f"merged_invoice_{timestamp}.csv"

            # 选择保存位置
            output_file = filedialog.asksaveasfilename(
                title="保存合并后的文件",
                defaultextension=".csv",
                initialfile=default_filename,
                filetypes=[
                    ("CSV files", "*.csv"),
                    ("All files", "*.*")
                ]
            )

            if output_file:
                # 保存为CSV文件（使用UTF-8编码，带BOM以支持Excel打开中文）
                merged_df.to_csv(output_file, index=False, encoding='utf-8-sig')

                # 更新输出显示
                self.output_file = output_file
                self.update_output_display(output_file)

                # 显示成功信息
                messagebox.showinfo(
                    "成功",
                    f"文件合并成功！\n\n"
                    f"合并文件数：{len(self.input_files)}\n"
                    f"总数据行数：{len(merged_df)}\n"
                    f"输出列数：{len(merged_df.columns)}\n"
                    f"保存位置：{output_file}"
                )

        except Exception as e:
            messagebox.showerror("错误", f"合并文件时发生错误：\n{str(e)}")

    def clear_list(self):
        """清空文件列表"""
        if self.input_files:
            result = messagebox.askyesno("确认", "确定要清空文件列表吗？")
            if result:
                self.input_files.clear()
                self.update_input_display()
                messagebox.showinfo("成功", "文件列表已清空")

    def close_app(self):
        """关闭程序"""
        result = messagebox.askyesno("确认", "确定要关闭程序吗？")
        if result:
            self.root.quit()
            self.root.destroy()


def main():
    """主函数"""
    root = tk.Tk()
    app = ExcelMergerApp(root)

    # 设置窗口关闭事件
    root.protocol("WM_DELETE_WINDOW", app.close_app)

    # 运行主循环
    root.mainloop()


if __name__ == "__main__":
    main()
