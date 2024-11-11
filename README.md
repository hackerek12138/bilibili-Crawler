# bilibili-Crawler
# 项目概述
本项目是一个Python脚本，用于从Bilibili（哔哩哔哩）网站爬取指定视频的视频流和音频流，并将其保存为本地文件。脚本利用requests库发送HTTP请求，使用正则表达式（re模块）解析HTML内容，并通过json模块处理JSON数据。

# 依赖库
requests：用于发送HTTP请求。
re：用于正则表达式匹配和解析HTML内容。
json：用于处理JSON数据。
确保在运行脚本之前已经安装了这些库。如果没有安装，可以使用以下命令安装：

bash
pip install requests
# 使用说明
配置Cookie：
你需要提供一个有效的Bilibili Cookie，以便脚本能够模拟登录状态并访问需要权限的内容。
将cookie变量的值替换为你自己的Bilibili Cookie。
设置视频BV号：
在脚本中，bv变量指定了要爬取的视频的BV号。
更改bv变量的值为你想要爬取的视频的BV号。
运行脚本：
直接运行脚本文件。脚本将发送HTTP请求到Bilibili，解析视频和音频的URL，并将它们保存为本地文件。
# 脚本流程
发送请求：
使用requests.get方法发送GET请求到指定的Bilibili视频页面。
请求头中包含用户代理（User-Agent）和Cookie，以模拟登录状态。
解析HTML：
使用正则表达式提取视频标题。
提取包含视频信息的JSON字符串。
处理JSON数据：
将JSON字符串解析为Python字典。
提取视频和音频的baseUrl。
下载并保存文件：
发送请求到视频和音频的URL，获取视频和音频内容。
将视频内容保存为.mp4文件，将音频内容保存为.mp3文件。
# 注意事项
Cookie有效性：
确保提供的Cookie是有效的，并且没有过期。
如果Cookie失效，你可能需要重新登录Bilibili并获取新的Cookie。
视频权限：
该脚本只能访问公开的视频内容。对于需要会员权限或其他特殊权限的视频，你可能无法成功爬取。
法律风险：
请确保你遵守Bilibili的使用条款和法律法规。未经授权的下载和分发可能构成侵权。
文件保存路径：
确保在脚本运行的目录中存在名为video的文件夹，或者根据需要修改文件保存路径。
示例
python
# 示例Cookie（请替换为你自己的Cookie）
cookie = "你的Bilibili Cookie"
 
# 示例BV号（请替换为你想要爬取的视频的BV号）
bv = "BV1Ccm1YdEKz"
运行脚本后，你将在video文件夹中看到以视频标题命名的.mp4和.mp3文件。
