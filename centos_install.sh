#/bin/bash

echo "前言"
echo "提示：这个脚本是我在manjaor上写的，所用的桌面环境是i3，所以如果不需要配置i3请把不相关的命令注释掉谢谢！"
echo "如果你没有意见请忽略！"
echo "----------------------------------------Gnglas"
git clone https://github.com/denstiny/Gnglas.git ~/Gnglas
#下载i3桌面环境
#sudo yum install i3
#mv Gnglas/my_i3/ .config/i3/




#i3wm 的一些截图工具
#sudo yum install peek xclip scrot
#下载一些美化的插件
#sudo yum install screenfetch
#mkdir -v ~/.config/i3/screencut/ ~/.vim/ 
mkdir -v ~/.vim/

#自动配置vim
curl -sLf https://spacevim.org/cn/install.sh | bash -s -- --install vim


#自动配置vim的配色
mv Gnglas/Image/ ~/
mv Gnglas/vimrc ~/.vim/.vintrc


#自动配置manjaror软件源需要就取消注释
#mv Gnglas/pacman.conf Gnglas/mirrorlist  /etc/
bash ~/Gnglas/.del.sh

