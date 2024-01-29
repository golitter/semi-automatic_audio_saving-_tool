import tkinter as tk
from tkinter import filedialog, messagebox
import requests
from bs4 import BeautifulSoup
import os


# 得到网页的标题
def get_title(url):
    try:
        # 发送GET请求获取网页内容
        response = requests.get(url)
        # 检查响应状态码，200表示请求成功
        if response.status_code == 200:
            # 使用Beautiful Soup解析HTML
            soup = BeautifulSoup(response.text, 'html.parser')
            # 找到网页中的标题标签
            title_tag = soup.find('title')
            # 提取标题文本
            if title_tag:
                return title_tag.get_text()
            else:
                return "未找到标题"
        else:
            return "__NULL__ 请求失败，状态码：" + str(response.status_code)
    except Exception as e:
        return "__NULL__ 发生异常：" + str(e)

# 将网址url中的音频保存到save_path文件内
def download_audio(url, save_path):
    try:
        # 发送GET请求获取音频文件
        response = requests.get(url, stream=True)
        # 检查响应状态码，200表示请求成功
        if response.status_code == 200:
            # 以二进制写模式打开文件，并逐块写入音频数据
            with open(save_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    f.write(chunk)
            return "音频文件下载成功！"
        else:
            return "__NULL__ 下载失败，状态码：" + str(response.status_code)
    except Exception as e:
        return "__NULL__ 发生异常：" + str(e)

# 处理网址，得到标题
def process_url1():
    url1 = entry_url1.get()
    title = get_title(url1)
    if '__NULL__' in title:
        messagebox.showerror("错误", "网址1解析错误")
    else:
        entry_title.delete(0, 'end')
        entry_title.insert(0, title)

# 保存音频
def process_url2():
    url2 = entry_url2.get()
    file_name = entry_title.get()  # 获取第二个网址的文件名部分
    file_name = file_name + ".mp3" # 加上文件后缀
    save_path = os.path.join(entry_path.get(), file_name)  # 组合文件路径
    result = download_audio(url2, save_path)
    print(result, save_path)
    if '__NULL__' in result:
        messagebox.showerror("错误", "网址2解析错误")
    else:
        messagebox.showinfo("提示", "文件下载成功！")
        entry_url1.delete(0, 'end')
        entry_url2.delete(0, 'end')
        entry_title.delete(0, 'end')
        label_result.config(text="")

# 选择目录
def browse_path():
    # 打开文件对话框选择保存路径
    download_dir = filedialog.askdirectory()
    entry_path.delete(0, 'end')
    entry_path.insert(0, download_dir)


# 窗口初始化
    
# 创建主窗口
root = tk.Tk()
root.title("半自动音频保存工具")

## 第一个网址输入框
label_url1 = tk.Label(root, text="第一个网址：")
label_url1.grid(row=0, column=0, padx=5, pady=5)
entry_url1 = tk.Entry(root, width=60)  # 调整宽度为60
entry_url1.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

# 按钮1：处理第一个网址
button_process_url1 = tk.Button(root, text="处理网址1", command=process_url1)
button_process_url1.grid(row=1, column=1, padx=5, pady=5)


# 文本框2：第一个网址的标题
entry_title = tk.Label(root, text="网址的标题：")
entry_title.grid(row=2, column=0, padx=5, pady=5)
entry_title = tk.Entry(root, width=60)  # 调整宽度为60
entry_title.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

# 第二个网址输入框
label_url2 = tk.Label(root, text="第二个网址：")
label_url2.grid(row=3, column=0, padx=5, pady=5)
entry_url2 = tk.Entry(root, width=60)  # 调整宽度为60
entry_url2.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

# 按钮2：处理第二个网址并下载音频文件
button_process_url2 = tk.Button(root, text="处理网址2并下载音频文件", command=process_url2)
button_process_url2.grid(row=4, column=1, padx=5, pady=5)


# 文件下载目录输入框
label_path = tk.Label(root, text="文件下载目录：")
label_path.grid(row=5, column=0, padx=5, pady=5)
entry_path = tk.Entry(root, width=50)  # 调整宽度为50
entry_path.grid(row=5, column=1, padx=5, pady=5)
button_browse = tk.Button(root, text="浏览", command=browse_path)
button_browse.grid(row=5, column=2, padx=5, pady=5)


# 运行主循环
root.mainloop()
