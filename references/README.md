- current

```markdown
> 第一类 摘取自html l-container

# c-announce-box(简陋的小说名与作者名超链接)
## c-announce c-announce--rensaiheader
<a><br>\n作者：\n<a>


# p-novel(小说正文和标题)

## c-pager c-pager--box(导航栏，结尾也是)

## p-novel__body

### p-novel__subtitle

#### p-novel__subtitle-episode

### js-novel-text p-novel__text
#### px【p,可能是文本，可能br；除本层之外其余层级均为div】

## c-pager c-pager--box

> 第二类 摘取自website l-container
> 与ua相关。
# l-main

## c-announce-box(小说名与作者超链接)

## p-novel

### c-pager c-pager--center(导航)

### p-novel__title p-novel__title--rensai(标题)

### p-novel__body(正文与后话)

#### js-novel-text p-novel__text(正文 由许多个p构成，若直接空白转行则p中只有一个br)

#### js-novel-text p-novel__text p-novel__text--afterword(后话)
```

+ 上班要求

  + 下班前，**写下[日报](https://docs.zuoyebang.cc/home?ddtab=true)**；
    这个是个人空间，在这个空间里面创建目录，然后每日日报写一个文件就行。日报内容可以写当前工作内容，进度和遇到的问题等等；把事情说明白就行。
+ 命令行使用代理端口（一次性)：export https_proxy='http://127.0.0.1:7890'
+ linux

  + 文件传输：
    + python3 -m http.server 8081 --bind    10.250.16.85 --directory ./
    + wget -r -np -nH --cut-dirs=0 http://10.250.19.11:8081/
    + tar -cvf step3.tar *.py
  + ls -lrht
  + pwd
  + cat
  + mv【！】
  + mkdir
  + cd
  + df -h
  + mkdir -p utils && vim utils/user_agents.txt
  + :wq
  + exit
  + grep -m 1 "actual_link_count" logs/running_shell.log【获取某文件含特定内容的第一行】
  + 获取某文件夹下特定文件的最后一个含有特定内容的行
    ```shell
    for file in $(find logs -type f -name '*yomou*'); do
        grep '当前进度' "$file" | tail -n 1
    done

    ```

  - RateLimiter
  - c测试中 获取进度完整显示新版

    ```bash
    # 在脚本开头定义变量
    LOG_DIR="logs"   # 日志目录
    PATTERN="*bookrix*"                    # 文件名包含的模式
    SEARCH_TERM="当前进度"               # 查找的文本模式

    # 查找符合条件的文件并按修改时间排序输出每个文件中最后一行包含SEARCH_TERM的内容
    find "$LOG_DIR" -type f -name "$PATTERN" -print0 | xargs -0 stat --format='%Y %n' | sort -n | cut -d ' ' -f 2- | while read file; do
        grep "$SEARCH_TERM" "$file" | tail -n 1
    done

    ```

    - crontab 未能正确运行的有效代码（告警）
      ```shell
      sh -x alertRobot/t_md.sh source /home/homework/.bashrc >> ./alertRobot/alertLogs/monitor.$(date +"%Y%m%d") 2>&1
      ```
+ 登陆：
+ ssh shuiyuanzhi@10.34.0.68    跳到relay上，
+ 然后ssh homework@10.57.76.63就可以登录海外这台机器了
+ 登陆国内服务器：ssh homework@172.29.218.186
+ **scp test.txt homework@172.29.218.186:/data/nfs3/zhangliuzhen**
+ **mv test.txt /data/nfs3/download/tmp_zlz**
+ **scp test.txt homework@172.29.218.186:/data/nfs3/zhangliuzhen**
+ 查看情况：

> tail -n1 -f novel_homepage-process-yomou_JP_novel_bySYZ_PROCESSOR1.json

+ 目录

  **172.29.218.186:/data/nfs3/download/tmp_zlz**

  **/data/nfs3/shuiyuanzhicheck_15output/**output_12-16-19:48:24.json

  ** **mv test.txt /data/nfs3/download/tmp_zlz****

  186上下载大文件：
  https://yl05-znzt.fdp-proxy.zuoyebang.cc/
  把数据放到186的目录：
  **scp endby2008-05-13_novel_data.tar.gz homework@172.29.218.186:/data/nfs3/download/tmp_syz**

  + **/v/shuiyuanzhi** 海外服务器的文件夹
  + 海外服务器：
  + /data/nfs3/shuiyuanzhi     172.29.218.186机器上的工作目录；
+ tar压缩：**tar -cvzf output.json.tar.gz output.json**
+ sh -x llm_toutiao_main.sh once_llm_toutiao_crawler_main
+ nohup sh -x llm_toutiao_main.sh once_llm_toutiao_crawler_main > once_llm_toutiao_crawler_main.log 2>&1 &+ 172.29.218.186
+ https://syosetu.com/
+ https://gamewith.jp/
+ 两个日文站点，先抓第一个小说站点
+ 
+ 小说最终输出格式

> tmp={}
> chapter_list = []
> chapter_1 = {
> 'url':'章节url',
> 'html':'章节内容'
> }
> chapter_list.append(chapter_1)
> tmp['html'] = chapter_list

* 请求所有日期：https://yomou.syosetu.com/search.php?word=&notword=&genre=&type=&mintime=&maxtime=&minlen=&maxlen=&min_globalpoint=&max_globalpoint=&minlastup=&maxlastup=&minfirstup=2004%2F04%2F01&maxfirstup=2024%2F12%2F%E3%80%90%E6%9C%80%E6%96%B0%E6%97%A5%E6%9C%9F%E3%80%91&order=new

先判断是否有导航栏，区分出p1+n；再看是否有链接列表，区分出p1+1

| 类型 | 具体特征 | 策略 | 样例链接                           |
| ---- | -------- | ---- | ---------------------------------- |
| p1+0 |          |      | https://ncode.syosetu.com/n7668ju/ |
| p1+1 |          |      | https://ncode.syosetu.com/n1574jb/ |
| p1+n |          |      | https://ncode.syosetu.com/n4234iq/ |

+ 作者和小节会含超链接。如果有多页，可通过?p=2来请求，但没有多页时，请求结果会显示请求错误
+ 作者有超链接，小节有超链接
+ 小说内容页结构
  + 章节标题：h1.p-novel__title.p-novel__title--rensai
  + 正文：div.p-novel__body
  + 顶部翻页器：div.c-pager.c-pager--center
    无目录页超链接
  + 底部翻页器：div.c-pager.c-pager--center
    + 前一页：div.c-pager__item.c-pager__item--before
    + 后一页：div.c-pager__item.c-pager__item--next
    + 目录页：div.c-pager__item
+ 小说首页结构类型
  + p1+1单页+有目录
    + p-novel__title
    + p-novel__author
    + p-novel__summary
    + p-eplist
      + 由p-eplist__chapter-title和p-eplist__sublist构成
    + p-eplist__sublist 为超链接
  + p1+0单页+所有内容在同一页
    + p-novel__title
    + p-novel__author
    + p-novel__body
  + p1+n多页
    + p-novel__title
    + p-novel__author
    + p-novel__summary
    + p-eplist
      + 由p-eplist__chapter-title和p-eplist__sublist构成
      + p-eplist__sublist 为超链接
    + c-pager
      + 含有c-pager__result-stats，其文本为“显示第 1-100 集”

> ```js
> elements = []
> Array.from(document.getElementsByTagName("a")).forEach((ele) => {
>   if (ele.getAttribute("href").includes("https://ncode.syosetu.com")) {
>     elements.push(ele.getAttribute("href"));
>   }
> });
> elements
>
> ```

# 周报week1

熟悉环境：学习作业帮工作流程，上手工位苹果设备，连接远程服务器，学习操作规范。
初步调查：进行了对 https://syosetu.com/ 网站的初步调查并进行了如下操作：
网站测试：未发现反爬虫机制。
抓取测试：随机选取了一些链接，并在海外的服务器上重复抓取10次，每次都成功获取到了一致的内容。

分析与策略制定：
目标是找到所有小说的链接。
当前进度：正在研究如何高效地获取尽可能多的小说URL。
初步策略：计划利用搜索页面的时间筛选功能来获取所有小说的入口URL。搜索条件可以展示的记录上限为2000条，时间筛选的范围是从2004年4月1日至今。
预期方式：设定类似于二分法分类的遍历函数：

# 获取所有小说首页链接

+ 已知：
  搜索列表可获得1056235本小说作品（1056237/20/365=1056237/7300≈145）
  除今日外，过去的发表日期的小说数已确定；
  在检索结果页首页可获得当前检索得的总本数，在结果各页面可获得结果小说的链接、类型、N码等信息；
  检索结果页每页可显示20条小说（含首页），最多可查看100页（即每次检索最多查看检索结果中的前2000本小说）
+ ---->
  输入a日期-b日期这一最大时间范围->
  以一个月为初始时间区间，逐步、递进地进行的区间划分->
  该时间范围的本数大于2000->缩小时间范围，反之亦然；（**函数见jupyter**）
  当时间范围的本数在1900～2000，确定为一个范围；
  若时间范围已缩小至一天，但本数仍多于2000（根据平均数145推得概率可能较小）：
  附加其它分类方式，构造更细化的检索组合；
+ ---->
  继续下一个范围，直至遍历完所有范围（a日期-b日期）。
  得到完整的可查看的所有小说日期范围列表。

# 获取每本小说各页链接

+ 已知：

- 小说首页结构类型
  - 首页为单页+有目录
    - p-novel__title
    - p-novel__author
    - p-novel__summary
    - p-eplist
      - 由p-eplist__chapter-title和p-eplist__sublist构成
    - p-eplist__sublist 为超链接
  - 首页为单页+所有小说内容在首页（超短篇小说）
    - p-novel__title
    - p-novel__author
    - p-novel__body
  - 首页为多页（目录较长）
    - p-novel__title
    - p-novel__author
    - p-novel__summary
    - p-eplist
      - 由p-eplist__chapter-title和p-eplist__sublist构成
      - p-eplist__sublist 为超链接
    - c-pager
      - 含有c-pager__result-stats，其文本为“显示第 x-xxx集”

## 对每本小说

- 思路1:在检索页分析即判断出小说属于以上哪种类型，然后采取设计好的对应策略，抓取每一章的链接
- 思路2：遍历每本小说，根据页面特征（是否有章节超链接？是否有目录下一页？当前页的目录是否显示了所有章节）
  来分策略抓取章节超链接

# 最终对每章的超链接

- 服务器定时大批抓取
- 保存response.text
- 记录成功率、耗时、......
  这种方法有望有效地覆盖网站上的小说资源，助力于内容的全面获取和分析。

# tail

你可以使用 `tail` 命令来查看日志文件的内容。`tail` 命令默认会显示文件的最后10行，可以用来查看日志文件的最新内容，特别适合查看不断更新的日志。

### 常用的 `tail` 命令示例：

1. **查看文件的最后 10 行：**

   ```bash
   tail -n 10 your_log_file.log
   ```

   这会显示 `your_log_file.log` 文件的最后 10 行内容。
2. **实时查看文件内容的更新：**

   ```bash
   tail -f your_log_file.log
   ```

   这会持续输出 `your_log_file.log` 文件的最新内容，并随着文件的更新实时显示新增加的行。如果文件在运行过程中有新日志写入，它会实时显示。
3. **查看文件的最后 N 行：**

   ```bash
   tail -n N your_log_file.log
   ```

   其中 `N` 是你想查看的行数。例如，如果你要查看最后 50 行，可以运行：

   ```bash
   tail -n 50 your_log_file.log
   ```
4. **实时查看并显示更新的行数：**
   如果你想同时查看文件的最新内容并且想限制显示的行数，可以结合使用 `-n` 和 `-f` 参数。例如：

   ```bash
   tail -n 100 -f your_log_file.log
   ```

   这将显示文件的最后 100 行，并且继续跟踪文件的更新。

### 常见用途：

- 查看日志文件的尾部，以便跟踪最近的日志信息。
- 在调试时，可以实时查看程序输出，检查程序运行是否正常。

### 示例：

假设你有一个日志文件 `process1.log`，你想查看其最后 10 行，可以运行：

```bash
tail -n 10 process1.log
```

如果你希望实时查看这个日志文件的内容更新，可以运行：

```bash
tail -f process1.log
```

# oss#数据从海外拖到国内机器

**比如，从**10.57.76.63拖到172.29.218.186

**注：**172.29.218.186是国内机房的机器 ，10.57.76.63是美东机器的机器

**例子如下：**

**可以打包下，节省流量。**

**tar -cvf pdf_${dt}.tar ../../yangbo11/pdf/$dt/* **

**进行上传到海外oss**

**/data/homework/ossutil64 cp -r --axupspeed=76800 pdf_${dt}.tar oss://zyb-speech-asrtrain**-out**/epub/**

**注：maxupspeed是速率，单位是kbyte/s**

| **方向**             | **能够使用的最大限速（Mb/s，这里的b表示bit）** | **kbyte/s** |
| -------------------------- | ---------------------------------------------------- | ----------------- |
| **nlp**              | **100**                                        | **12800**   |
| **语音**             | **500**                                        | **64000**   |
| **参数--maxupspeed** | **kb/s(k字节/s)**                              |                   |

**海外oss会自动同步到国内oss，这里直接下载就行**

**ossutil64  cp oss://zyb-speech-asrtrain/epub/epub.tar $dt **

**注：海外的地址中有-out,国内的没有；这是Ω一个注意的地方；**

**注：同步需要时间，所以当海外上传后，这里可能没有，需要点时间同步，可以稍后试下；**

**或者直接查看是否同步过来**

**ossutil64  ls oss://zyb-speech-asrtrain/epub/epub.tar**


简言之：

- 63传：nohup ossutil64 cp -r --maxupspeed=76800  output.tar.gz oss://zyb-speech-asrtrain-out/epub/bookrix > oss_cp_output.log 2>&1 &
- 186收

# 进阶快捷键

* ## 关键词获取进程情况

  ```sh
  KEYWORD="yomou"; FIELDS="PID\tUID\tGID\tCOMMAND\tUSER\tELAPSED\t%CPU\t%MEM"; CHINESE_FIELDS="进程ID\t用户ID\t组ID\t执行的命令名\t启动该进程的用户\t进程运行时间\t当前 CPU 使用率\t当前内存使用率"; (echo -e "$FIELDS"; echo -e "$CHINESE_FIELDS"; ps -eo pid,uid,gid,args,user,etime,%cpu,%mem --sort=-%cpu | grep "$KEYWORD" | grep -v grep | awk '{printf "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n", $1, $2, $3, $4, $5, $6, $7, $8}')
  ```
* ## 其它快捷键

### **窗口和标签管理**

| 快捷键               | 说明               |
| -------------------- | ------------------ |
| Command + N          | 打开新窗口         |
| Command + T          | 打开新标签页       |
| Command + W          | 关闭当前标签页     |
| Command + Option + D | 水平切分当前窗口   |
| Command + D          | 垂直切分当前窗口   |
| Command + 数字       | 切换到对应的标签页 |

### **光标移动**

| 快捷键      | 说明             |
| ----------- | ---------------- |
| Ctrl + A    | 移动到行首       |
| Ctrl + E    | 移动到行尾       |
| Ctrl + F    | 向前移动一个字符 |
| Ctrl + B    | 向后移动一个字符 |
| Option + ← | 向后移动一个单词 |
| Option + → | 向前移动一个单词 |

### **内容操作**

| 快捷键      | 说明                     |
| ----------- | ------------------------ |
| Command + C | 复制选中的内容           |
| Command + V | 粘贴内容                 |
| Command + X | 剪切选中的内容           |
| Command + A | 全选                     |
| Command + F | 查找文本                 |
| Ctrl + U    | 清除当前行               |
| Ctrl + K    | 删除光标位置到行尾的内容 |
| Ctrl + W    | 删除光标之前的单词       |
| Ctrl + H    | 删除光标之前的字符       |

### **历史命令管理**

| 快捷键      | 说明         |
| ----------- | ------------ |
| Ctrl + P    | 上一条命令   |
| Ctrl + N    | 下一条命令   |
| Command + ; | 查看历史命令 |

### **屏幕清理**

| 快捷键      | 说明             |
| ----------- | ---------------- |
| Command + K | 清空终端内容     |
| Ctrl + L    | 清屏并移动到顶部 |

这些快捷键可以大大提高在 iTerm2 中的工作效率，特别是在进行频繁的文本编辑和命令输入时。用户还可以根据个人习惯在 iTerm2 的 Preferences 中自定义快捷键，以适应自己的工作流程。

Vim 是一个强大的文本编辑器，拥有丰富的快捷键，可以显著提高编辑效率。以下是一些常见的 Vim 快捷键，特别关注光标移动和内容的增删改查操作。

## 光标移动快捷键

| 快捷键 | 功能描述                        |
| ------ | ------------------------------- |
| `h`  | 向左移动一位                    |
| `j`  | 向下移动一行                    |
| `k`  | 向上移动一行                    |
| `l`  | 向右移动一位                    |
| `0`  | 移动到当前行的行首              |
| `^`  | 移动到当前行的第一个非空字符    |
| `$`  | 移动到当前行的行尾              |
| `w`  | 移动到下一个单词的开头          |
| `b`  | 移动到上一个单词的开头          |
| `e`  | 移动到当前单词的结尾            |
| `gg` | 移动到文件开头                  |
| `G`  | 移动到文件末尾                  |
| `nG` | 移动到第 n 行（n 为数字）       |
| `fx` | 移动到当前行下一个字符 x 的位置 |
| `%`  | 跳转到匹配的括号                |

## 内容操作快捷键

### 插入与修改

| 快捷键 | 功能描述               |
| ------ | ---------------------- |
| `i`  | 在光标前插入文本       |
| `I`  | 在行首插入文本         |
| `a`  | 在光标后插入文本       |
| `A`  | 在行尾插入文本         |
| `o`  | 在当前行下方插入新行   |
| `O`  | 在当前行上方插入新行   |
| `cw` | 修改光标后的单词       |
| `cc` | 删除整行并进入插入模式 |

### 删除与剪切

| 快捷键         | 功能描述         |
| -------------- | ---------------- |
| `x`          | 删除光标所在字符 |
| `dw`         | 删除光标后的单词 |
| `dd`         | 删除整行         |
| `d^`, `d$` | 删除至行首或行尾 |

### 复制与粘贴

| 快捷键 | 功能描述         |
| ------ | ---------------- |
| `yy` | 复制整行         |
| `yw` | 复制光标后的单词 |
| `p`  | 在光标后粘贴内容 |
| `P`  | 在光标前粘贴内容 |

### 撤销与重做

| 快捷键       | 功能描述       |
| ------------ | -------------- |
| `u`        | 撤销上一次操作 |
| `Ctrl + r` | 恢复上一次撤销 |

## 查找与替换

### 查找

- `/str`: 查找字符串 str
- `n`: 查找下一个匹配项
- `N`: 查找上一个匹配项

### 替换

- `:s/old/new/g`: 将当前行中的 old 替换为 new
- `:%s/old/new/g`: 全文替换 old 为 new

## 保存与退出

- `:w`: 保存文件
- `:q`: 退出 Vim
- `:wq`: 保存并退出
- `:q!`: 强制退出不保存

这些快捷键在 Vim 的命令模式下使用，可以帮助用户高效地进行文本编辑。熟练掌握这些快捷键将大大提高使用 Vim 的效率[1][2][4][6]。

Citations:
[1] https://draapho.github.io/2016/10/01/1604-CheatSheet-vim/
[2] https://www.cnblogs.com/lvzhenjiang/articles/16655161.html
[3] https://blog.csdn.net/AliceRainly/article/details/125486989
[4] https://blog.csdn.net/u011929670/article/details/137491472
[5] https://www.cnblogs.com/qinlulu/p/16241289.html
[6] https://www.cnblogs.com/seedoubleu/p/15535899.html

```markdown




### 总体运行逻辑
### 先运行py，生成各进程参数；然后用py运行sh，在sh中使用nohup将各进程挂载在后台
### 相关输出文件
📁 logs
    📄 f"{appname}-process-{process_name}.log"
         各进程的对应的单独日志文件，爬取过程中动态更新(对应oget_logger函数)
    📄 running_shell.log
         最外层运行的py文件日志，分组产生进程、传sys参数、调sh开启爬虫进程的相关变量、信息(对应running_shell_log函数)
📁 output
    📄 f"novel_content-process-{process_name}.json"
         结果文件，爬取的所有小说各自一行，含小说首页链接和各章html列表，
         出错的章节在列表中保留特殊标记，key、value形如：
              {"1"："ERROR:No Htmlfile",           是 p1+0类型小说能报的错误，bug为之前爬取时未保存对应的小说首页html(为代码稳健性而设置此类错误，实际未报错过)
              "10": "ERROR:Failed to Get Webpage", 网络错误，一般为443小说(章节)被删除，即"HTTPSConnectionPool(host='ncode.syosetu.com', port=443): Read timed out. (read timeout=5)"
              "21": "ERROR:Empty content"          网页内容为空
}                                                  考虑之后再到error json中遍历错误链接，若是可以解决的，就补充到对应小说末尾
    📄 f"error_content-process-{process_name}.json"
         错误文件，出现报错的小说各自一行，含小说首页来你家、报错章节链接与原因构成的列表
📁 tmp
         temp_data_YYYY-MM-dd_hh-mm-ss.txt
         将小说json分组到各进程时保存的临时文件，用于sys中传入此文件路径作为"temp_data_path"
         仅用于减小内存压力、避免反复读取原始小说链接到字典对象；仅开启进程时生成、使用，定期手动删除即可
         如果需要回溯代码运行步骤到此文件，可结合running_shell.log中的sh codes等信息



### 具体流程：首先通过sys输入参数，方便sh调用(部分参数是在代码行内定义的)

#### 所有sys参数：{python_script_path} {process_name} {start_index} {end_index} {proxies_flag} {temp_data_path}
##### 需运行时定义的参数：
start_index, links_per_group, num_groups, entire_json,proxies_flag
###### 起始小说序号，每进程链接数，进程总数，小说序号、链接字典对象，是否使用代理端口

### 通过分组产生的各进程包含的novel index、episode count
### (下面为测试30进程、每个10000个链接，每进程的小说数由索引到对应数量链接时的小说情况决定)
[{  "group_start_index": 0,"group_end_index": 9999, 
    "actual_link_count": 10000, "novel_count": 10000}, 
 {"group_start_index": 10000, "group_end_index": 19999, ...}]
 
### 结果文件格式(json line)
{"novel_homepage_url": "https://ncode.syosetu.com/n1599id/", 
"novel_content_html_dict": {"1":"<!DOCTYPE html>...</html>",
                            "2":"<!DOCTYPE html>...</html>",
                            "3":"<!DOCTYPE html>...</html>",
                            ...,
                            "101":"ERROR:Empty content",### 错误必以"ERROR"开头
}
### 错误单独记录的文件格式(json line)
{"novel_homepage_url": "https://ncode.syosetu.com/n3325ge/", 
"error_content_list": [{"novel_content_url": "https://ncode.syosetu.com/n3325ge/1/", 
                        "error_message": "HTTPSConnectionPool(host='ncode.syosetu.com', port=443): Read timed out. (read timeout=5)"},
                        {"novel_content_url":"https://xxx",
                        "error_message":"xxxxx"}
                        ]
 }




```

# github相关命令

```sh
# pull 最新修改
git pull origin main

```
