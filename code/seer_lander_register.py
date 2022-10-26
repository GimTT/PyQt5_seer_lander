# IMPORT PACKAGES START
import win32com.client
import seer_lander_dm_drive


# IMPORT PACKAGES END

def dm_register():  # 功能：注册dm插件（管理员身份运行）
    import os
    # 获取当前脚本路径
    path = os.getcwd()
    dm_reg_file = open(path + "\\ini" + "\\dm_reg_struct.txt", "r", encoding="gb2312")
    if dm_reg_file.read() != "True":
        # 以管理员身份regsvr32 path dm.dll
        os.system("regsvr32 " + path + "\\dm.dll")

        # 先关掉读文件流
        dm_reg_file.close()

        # 打开写文件流
        dm_reg_file = open(path + "\\ini" + "\\dm_reg_struct.txt", "w", encoding="gb2312")
        dm_reg_file.write("True")

        # 关掉写文件流
        dm_reg_file.close()

    seer_lander_dm_drive.dm = win32com.client.Dispatch('dm.dmsoft')  # 调用大漠插件

    '''
    # 此段可以打印出dm的版本
    dm = win32com.client.Dispatch('dm.dmsoft')
    # current version
    print(dm.Ver())
    '''
