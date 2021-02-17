#!/bin/bash

chrome_version=$(google-chrome --version | awk '{print $3}' )
echo "Chrome version: $chrome_version"
version_prefix=$(echo $chrome_version | awk -F. '{print $1"."$2"."$3}')

wget --version > /dev/null 2>&1

if [ $? -eq 0 ]; then
    echo "use wget to download chrome drive."
    code=$(wget -q -O - https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$version_prefix)
    file_url="https://chromedriver.storage.googleapis.com/"$code"/chromedriver_linux64.zip"
    dir_url="https://chromedriver.storage.googleapis.com/index.html?path=$code/"

    echo "Downloading chrome drive from: $dir_url, if failed or can't connect network, please download yourself and upload to this host"
    wget $file_url -O chromedriver_linux64.zip
else
    echo "use curl to download chrome drive."
    code=$(curl https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$version_prefix)
    file_url="https://chromedriver.storage.googleapis.com/"$code"/chromedriver_linux64.zip"
    dir_url="https://chromedriver.storage.googleapis.com/index.html?path=$code/"

    echo "Downloading chrome drive from: $dir_url, if failed or can't connect network, please download yourself and upload to this host"

    curl -O $file_url
fi

unzip chromedriver_linux64.zip
