# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['display_base.py', 'global_define.py', 'seer_lander_main.py', 'seer_lander_auto.py', 'seer_lander_dm_drive.py', 'seer_lander_ui_auto.py', 'seer_lander_nono.py', 'seer_lander_register.py', 'seer_lander_speed.py', 'seer_lander_ui_main.py', 'seer_lander_ui_speed.py', 'game_window_thread.py', 'seer_lander_knapsack.py', 'seer_lander_ui_free_pack.py'],
    pathex=['../venv/Lib/site-packages'],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='display_base',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['ini\\GimTT_Lander_img.ico'],
)
