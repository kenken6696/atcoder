## 進め方
[online-judge-tools](https://github.com/kmyk/online-judge-tools)が使いづらいので、[atcoder-cli](https://github.com/Tatamo/atcoder-cli#readme)を通して使う

```
# init/add(ディレクトリに依存しない)
accna abc123/d # 最初に解きたい問題を必ず指定する
accna -r abc123/d # 既に解いた問題を復習する時は-rを指定
accna -b abc123/d # 復習後､元に戻すなら-b(復習したmain.pyは消える)

# test(問題ディレクトリ下で実行)
acct

# submit(問題ディレクトリ下で実行)
accs # pypy
acc submit main.py -- -y # python3
```

## 初期設定
```
# install
pip install online-judge-tools selenium chromium-chromedriver
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
    usage(){
        echo "
Usage: accna [options:<r|h>] <contest-id>/<problem-id>
    for example, accna abc123/e, accna -r abc123/d

Args:
    contest-id: you can find your contest-id in the URL
    problem-id: set problem-id you want to solve at first

Option:
    -r: use this option to review.
        backup main.py as 'bk_main.py' and replace it for acc_config/py/main.py
    -b: use this option when finishing your review
        replace main.py for bk_main.py and delete bk_main.py
        ">&2
    }
    DIR="$HOME/Repository/atcoder"
    flag_r=false
    flag_b=false
    # check args
    while getopts "rbh" OPT
    do
        case $OPT in
            r) flag_r=true;;
            b) flag_b=true;;
            h) usage && return 0;;
            *) usage && return 1;;
        esac
    done
    # remove option args
    shift $((OPTIND - 1))

    if [ $# -ne 1 ]; then
        usage && return 1
    fi
    if echo $1 | grep / >/dev/null; then
        contest_id=$(echo $1|cut -f1 -d/)
        problem_id=$(echo $1|cut -f2 -d/)
    else
        usage && return 1
    fi

    if $flag_b; then
        echo 'finishing Review...'
        if [ -e $DIR/$contest_id/$problem_id/bk_main.py ];then
            cd $DIR/$contest_id/$problem_id
            mv bk_main.py main.py
            return 0
        else
            echo 'cannot find bk_main.py:'$DIR/$contest_id/$problem_id && return 1
        fi
    fi

    if [ -e $DIR/$contest_id/$problem_id/main.py ];then
        echo 'You have already attended '$contest_id/$problem_id
        echo 'Do you want to review? <y/n>'
        read ans
        if [ $ans = 'y' ]; then
            flag_r=true
        elif [ $ans = 'n' ]; then
            return 0
        else
            return 1
        fi
    fi

    if $flag_r; then
        echo 'preparing to Review...'
        if [ -d $DIR/$contest_id/$problem_id ];then
            cd $DIR/$contest_id/$problem_id
            cp main.py 'bk_main.py'
            cp $(acc config-dir)/py/main.py .
            code main.py
            return 0
        else
            echo 'cannot find previous directory:'$DIR/$contest_id/$problem_id && return 1
        fi
    fi

    if [ -d $DIR/$contest_id ];then
        echo 'You have already attended!'
        cd $DIR/$contest_id
        acc add
    else
        echo 'You are attending '$contest_id' ...'
        cd $DIR
        acc n $contest_id
    fi
    accr=$?
    if [ $accr = 0 ] && [ -d $DIR/$contest_id/$problem_id ]; then
       cd $DIR/$contest_id/$problem_id
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