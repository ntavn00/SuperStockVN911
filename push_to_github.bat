@echo off
chcp 65001 >nul
title Day Super Stock V3.0 len GitHub
echo ========================================================
echo   DANG DAY MA NGUON SUPER STOCK V3.0 LEN GITHUB
echo   Repo: https://github.com/ntavn00/SuperStockVN911.git
echo ========================================================
echo.
echo Neu day la lan dau tien, cua so trinh duyet se mo ra de ban
echo bam "Sign in with your browser" (Xac nhan dang nhap GitHub).
echo.
cd /d "%~dp0"
git push -u origin main
echo.
if %errorlevel% equ 0 (
    echo ========================================================
    echo   [THANH CONG] Da day toan bo ma nguon len GitHub!
    echo   Xem tai: https://github.com/ntavn00/SuperStockVN911
    echo ========================================================
) else (
    echo ========================================================
    echo   [CHUA HOAN TAT] Vui long thu lai hoac kiem tra dang nhap.
    echo ========================================================
)
echo.
pause
