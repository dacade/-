1.在fofa_api中修改成你的email和你的key

2.pip3 install -r requirements.txt

3.python3 -s 搜索内容 -n 下载的数目

当搜索内容为多语句时，请使用双引号包含搜索内容，并且使用反斜杠转移搜索内容中的双引号。

eg： python3 fofa_api.py -s tomcat -n 1000

     python3 fofa_api.py -s "body=\"111.aspx\" && body=\"asp\"" -n 10000
