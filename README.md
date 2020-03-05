## 進め方
[online-judge-tools](https://github.com/kmyk/online-judge-tools)が使いづらいので、[atcoder-cli](https://github.com/Tatamo/atcoder-cli#readme)を通して使う  
ojとaccの使い分けがややこしい

```
# login
oj login https://beta.atcoder.jp/

# init and get testdata
acc n abc555

# test
cd abc555
mv tests/ test/
oj t -c 'python3 main.py'

#submit
acc submit main.py
```
ちなみにpythonの場合、Shebang必須  
ないとoj submitで止まる
```
#!/usr/bin/env python3
```