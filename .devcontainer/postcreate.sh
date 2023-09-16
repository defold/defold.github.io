sudo apt update
sudo apt install -y python3-pip

# requirements
pip3 install --user lunr==0.5.5
pip3 install --user requests
pip3 install --user pyyaml
pip3 install --user markdown==2.6.9
pip3 install --user pygments==2.1.3

# update the site with updated content from external sources/repositories
python3 update.py --download docs refdoc

# python2 update.py --download codepad examples assets

# the above command fails because of the error:

# Working...Reading classes...Unable to load library 'SpineExt':
# libSpineExt.so: cannot open shared object file: No such file or directory
# libSpineExt.so: cannot open shared object file: No such file or directory
# Native library (linux-aarch64/libSpineExt.so) not found in resource path ([file:/tmp/tmpn2ly7mln/examples-master/build/plugins/defold-spine/plugins/share/pluginSpineExt.jar])