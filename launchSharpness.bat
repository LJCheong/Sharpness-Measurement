@echo off

:loop
python C:\Users\emp9124379\PycharmProjects\Sharpness-Measurement\cameraMain.py
timeout /t 1 >nul
echo "Image collection done, would you like to acquire another set?"
set /p choice=Do you want to continue (Y/N)?
if /i "%choice%"=="N" (
	goto endloop
) else (
	echo "Proceed to re-run image acquisition script"
	goto loop
)
:endloop
echo "Proceed to measure sharpness"
python C:\Users\emp9124379\PycharmProjects\Sharpness-Measurement\sharpnessMain.py
echo "Image sharpness successfully collected."

pause Press any key to exit...
exit