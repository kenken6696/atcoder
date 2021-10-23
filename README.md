## 進め方
[online-judge-tools](https://github.com/kmyk/online-judge-tools)が使いづらいので、[atcoder-cli](https://github.com/Tatamo/atcoder-cli#readme)を通して使う  
ojとaccの使い分けがややこしい

```
# login
oj login https://beta.atcoder.jp/

# init and get testdata
acc n abc555
cd abc555/a

# test
oj t -c 'python3 main.py'

# submit
acc submit main.py
```

## 初期設定
```
# install
pip3 install online-judge-tools
npm install -g atcoder-cli

# config
cp -R acc_config/py $(acc config-dir)
acc config default-template py

acc config default-test-dirname-format test
```

## ちなみに
pythonの場合、Shebang必須  
ないとoj submitで止まる
```
#!/usr/bin/env python3
```