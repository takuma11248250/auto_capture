# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['auto_capture.py'],
             pathex=['C:\\Users\\takuma_kono\\OneDrive - 株式会社\u3000ＬＩＦＵＬＬ\u3000Ｍａｒｋｅｔｉｎｇ\u3000Ｐａｒｔｎｅｒｓ\\デスクトップ\\auto_capture'],
             binaries=[('driver/chromedriver.exe', './driver')],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='auto_capture',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
