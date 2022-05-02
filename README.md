## 進め方
[online-judge-tools](https://github.com/kmyk/online-judge-tools)が使いづらいので、[atcoder-cli](https://github.com/Tatamo/atcoder-cli#readme)を通して使う

```
# init/add(ディレクトリに依存しない)
accna abc123/d # 最初に解きたい問題を必ず指定する

# test(問題ディレクトリ下で実行)
acct

# submit(問題ディレクトリ下で実行)
accs # pypy
acc submit main.py -- -y # python3
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

# login
oj login https://beta.atcoder.jp/

# zshrc/bashrc
alias accn='acc n'
alias acct='oj t -c "python3 main.py"'
alias accs='acc submit main.py -- -y --guess-python-interpreter pypy'

accna() {
    if [ $# != 1 ]; then
        echo accna abc123/d のように入力してください
        return 1
    fi
    if echo $1 | grep / >/dev/null; then
        contest=$(echo $1|cut -f1 -d/)
    else
        echo accna abc123/d のように入力してください
        return 1
    fi
    DIR="$HOME/Repository/atcoder/"
    if [ -d $DIR$contest ];then
        echo 参加済みだね
        cd $DIR$contest
        acc add
    else
        echo 初参加だね
        cd $DIR
        acc n $contest
    fi
    accr=$?
    if [ $accr = 0 ]; then
       cd $DIR$1
       code main.py
    fi
}
```

## ちなみに
### pythonの場合、Shebang必須
ないとoj submitで止まる
```
#!/usr/bin/env python3
```