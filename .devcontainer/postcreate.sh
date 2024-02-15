# install python3
sudo apt update
sudo apt install -y python3-pip

# install libs for update.py
pip3 install --user lunr==0.5.5
pip3 install --user requests
pip3 install --user pyyaml
pip3 install --user markdown==2.6.9
pip3 install --user pygments==2.1.3

# fix error "libmodelc_shared.so: libXext.so.6: cannot open shared object file: No such file or directory"
sudo apt install -y libxtst6 libxt6
sudo ln -s /usr/local/lib/R/lib/libR.so /lib/x86_64-linux-gnu/libR.so

# download content from other repositories
python3 update.py --download docs refdoc
python3 update.py --download asset-portal games-showcase

# python3 update.py --download codepad
# python3 update.py --download examples