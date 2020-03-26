commit
my majaro linux
[xiaomo@ArchLinux ~]$ sudo pacman -Qs xf86-input-evdev 
local/xf86-input-evdev 2.10.2-1 (xorg-drivers xorg)
    X.org evdev input driver
[xiaomo@ArchLinux ~]$ 
[xiaomo@ArchLinux ~]$ xinput list 
 Virtual core pointer                        id=2    [master pointer  (3)]
    Virtual core XTEST pointer                  id=4    [slave  pointer  (2)]
    A4Tech USB Mouse                            id=10    [slave  pointer  (2)]
    SynPS/2 Synaptics TouchPad                  id=13    [slave  pointer  (2)]
    TPPS/2 IBM TrackPoint                       id=14    [slave  pointer  (2)]
 Virtual core keyboard                       id=3    [master keyboard (2)]
     Virtual core XTEST keyboard                 id=5    [slave  keyboard (3)]
     Power Button                                id=6    [slave  keyboard (3)]
     Video Bus                                   id=7    [slave  keyboard (3)]
     Video Bus                                   id=8    [slave  keyboard (3)]
     Power Button                                id=9    [slave  keyboard (3)]
     Integrated Camera                           id=11    [slave  keyboard (3)]
     AT Translated Set 2 keyboard                id=12    [slave  keyboard (3)]
     ThinkPad Extra Buttons                      id=15    [slave  keyboard (3)]

#id=13的是我的触摸板，执行xinput disable 13则会禁止，xinput enable 13则启用触摸板
[xiaomo@ArchLinux ~]$ xinput disable 13
