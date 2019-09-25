# -*- mode: python -*-
# tmpmain_manual.spec

block_cipher = None

a = Analysis(['tmpmain.py'],
    pathex=['/home/jacques/repos/jmnel/dromedary-fix/compiletest',
    '/home/jacques/repos/jmnel/dromedary-fix/compiletest/tmp'],
    binaries=[],
    datas=[('README.txt', 'doc')],
    hiddenimports=['PySide2.QtWidgets','PySide2.QtCore'],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

# -w only
exe = EXE( pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='tmpmain',
    debug=False,
    bootloader_ignore_signlas=False,
    strip=False,
    upx=True,
    console=False )
coll = COLLECT(exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=False,
    name='tmpmain')
