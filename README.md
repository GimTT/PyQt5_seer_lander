# PyQt5-SEER-Lander

#### 介绍
使用pyqt5和dm开发的赛尔号登陆器

#### 软件架构
软件架构说明
基于python3 （32位）
PyQt5
dm

#### 安装教程

1.  python版本（x86 @ 3.6.8）
2.  安装pyqt5
3.  必要修改ui时安装QtDesigne（pyqt5在新版python中不会自带QtDesigne）
4.  安装库时请换源

#### 使用说明

1.  请以管理员身份运行python
2.  打包（请将最后的参数修改为包路径）：pyinstaller -F -w seer_lander_main.py seer_lander_auto.py seer_lander_dm_drive.py seer_lander_ui_auto.py seer_lander_nono.py seer_lander_register.py seer_lander_speed.py seer_lander_ui_main.py seer_lander_ui_speed.py seer_lander_knapsack.py seer_lander_ui_free_pack.py -p ../Virtualenv/Lib/site-packages
3.  请将解释器配置到3.6.8@32位

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request
5.  特别贡献：星夜@星小夜登陆器：https://github.com/Starlitnightly/seer_py


#### 特技

1.  使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2.  Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)
3.  你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目
4.  [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
5.  Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6.  Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)
