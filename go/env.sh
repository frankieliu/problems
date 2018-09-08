if [ -e /import/async/cad/2018/go/bin ]; then
    pathappend /import/async/cad/2018/go/bin
elif [ -e /usr/local/go/bin ]; then
    pathappend /usr/local/go/bin
fi
export GOPATH=$(pwd)
