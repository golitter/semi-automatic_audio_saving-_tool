## **基于tkinter的简易界面的下载歌曲程序**。

通过输入第一个网址得到歌曲的标题，并展示到界面上，同时可以对该标题进行修改；通过输入第二个网址，将歌曲保存到以歌曲标题为名的所选目录下。**该应用程序在处理多个歌曲的下载时会节约大量时间。**

![image-20240129165224016](README.assets/image-20240129165224016.png)

## 使用

以[理查德克莱德曼 - 天空之城钢琴曲.mp3 免费下载 酷美网盘 支持外链 (kumeiwp.com)](https://www.kumeiwp.com/file/160494.html)下载该歌曲作为一个例子。

- 首先，将歌曲网址复制到`文本框：第一个网址`内。

![image-20240129165443134](README.assets/image-20240129165443134.png)

![image-20240129165505918](README.assets/image-20240129165505918.png)

- 点击`按钮：处理网址1`，得到歌曲标题。

![image-20240129165558902](README.assets/image-20240129165558902.png)

- 修改标题。（**不需要`.mp3`后缀**）

![image-20240129165623768](README.assets/image-20240129165623768.png)

- 将音频网址复制到`文本框：第二个网址`

![image-20240129165748774](README.assets/image-20240129165748774.png)

![image-20240129165803913](README.assets/image-20240129165803913.png)

- 点击`浏览`，选择下载目录

![image-20240129165847003](README.assets/image-20240129165847003.png)

- 点击`按钮：处理网址2并下载音频文件`

![image-20240129165934358](README.assets/image-20240129165934358.png)

无论成功与否，都会返回一个提示框。

![image-20240129170027449](README.assets/image-20240129170027449.png)

如果成功下载，则会将文本框内容清空，进行下一个歌曲下载。

![image-20240129170109321](README.assets/image-20240129170109321.png)

失败会有提示信息。

![image-20240129170126233](README.assets/image-20240129170126233.png)

## 函数

- 得到网页标题

```python
def get_title(url):
```

- 将网址url中的音频保存到save_path文件内

```python
def download_audio(url, save_path):
```

- 处理第一个网址

```python
def process_url1():
```

- 处理第二个网址

```python
def process_url2():
```

- 选择目录

```python
def browse_path():
```



