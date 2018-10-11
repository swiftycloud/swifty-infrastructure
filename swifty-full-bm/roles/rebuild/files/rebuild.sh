cd /root/src/swifty
echo 'export GOPATH=/root/src/swifty/vendor:/root/src/swifty' >> $HOME/.bashrc
source $HOME/.bashrc
make deps
make swifty/golang
make swifty/swift
make swifty/python
make swifty/nodejs
make swifty/ruby
