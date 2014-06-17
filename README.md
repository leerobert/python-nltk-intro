NLTK Installation Guide
====

## Mac Install Guide

#### Install Homebrew (a simple package repo for Mac)
    
     ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"

#### Install Python 2.7
     brew install python 

#### Install easy_install
     curl https://bootstrap.pypa.io/ez_setup.py -o - | python
     
If you don't have curl installed, brew install curl to install the curl package.

#### Install pip (python package manager)

     sudo easy_install pip

#### Install NLTK and its dependencies
    sudo pip install -U numpy pyyaml nltk pyenchant

#### Test the Install
    python 
    >>> import nltk

## Ubuntu Install Guide

Ubuntu follows many of the same steps but using apt-get as the package repo. Here are the commands to run:

    sudo apt-get install easy_install 
    wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py -O - | sudo python 
    sudo easy_install pip 
    sudo apt-get install python-dev 
    sudo pip install -U numpy 
    sudo pip install -U pyyaml nltk
    sudo apt-get install python-matplotlib

Lastly, test the install with:

    python
     >>> import nltk
