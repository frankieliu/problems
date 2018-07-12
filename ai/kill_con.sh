pgrep -a python | grep con_pro | awk -e '{print $1}' | xargs -I {} kill -9 {}
