# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

import os
import sys

# 1. تحديد المسار الأساسي بشكل صحيح
base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

# 2. تحديد الملفات المرفقة
def get_data_files():
    data_files = []
    files_to_add = [
        ('data/alarm-sound.mp3', 'data'),
        ('logs/fire_detection.log', 'logs'),
        ('models/best_nano_111.pt', 'models'),
        ('models/kaggle developed models/best_large.pt', 'models/kaggle developed models'),
        ('models/kaggle developed models/best_medium.pt', 'models/kaggle developed models'),
        ('models/kaggle developed models/best_small.pt', 'models/kaggle developed models'),
        ('src/fire_detector.py', 'Real-Time-Smoke-Fire-Detection-YOLO11/src')

    ]
    
    for src, dest in files_to_add:
        full_path = os.path.join(base_dir, src)
        if os.path.exists(full_path):
            data_files.append((full_path, dest))
        else:
            print(f"تحذير: الملف {full_path} غير موجود")
    
    return data_files

# 3. إعدادات PyInstaller
a = Analysis(
    ['src/main.py'],  # المسار النسبي للملف الرئيسي
    pathex=[base_dir],
    binaries=[],
    datas=get_data_files(),
    hiddenimports=[
        'ultralytics',
        'cvzone',
        'torch',
        'numpy',
        'python-dotenv==1.0.0',
        'opencv-python',
        'requests',
        'python-telegram-bot==20.3'
        'pygame',
        'cryptography',
        'fire_detector'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['tkinter'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

# 4. إعداد الملف التنفيذي
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='FireDetectionSystem',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon=os.path.join(base_dir, 'data', 'Fire.ico')
)