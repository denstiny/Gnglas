#/bin/bash

echo "前言"
echo "提示：这个脚本是我在manjaor上写的，所用的桌面环境是i3，所以如果不需要配置i3请把不相关的命令注释掉谢谢！"
echo "如果你没有意见请忽略！"
echo "----------------------------------------Gnglas"
#下载i3桌面环境
sudo pacman -S i3 feh compton
#i3wm 的一些截图工具
pacman -S peek xclip scrot
#下载一些美化的插件
sudo pacman  -S screenfetch
mkdir ~/.config/i3/screencut/ ~/.vim/ 
#自动配置vim
curl -sLf https://spacevim.org/cn/install.sh | bash -s -- --install vim
#自动配置vim的配色
git clone git@github.com:denstiny/Gnglas.git ~/Gnglas
mv Gnglas/Image/ ~/
mv Gnglas/my_i3/ .config/i3/
mv Gnglas/vimrc ~/.vim/.vintrc
#自动配置manjaror软件源需要就取消注释
#mv Gnglas/pacman.conf Gnglas/mirrorlist  /etc/
bash ~/Gnglas/.del.sh

