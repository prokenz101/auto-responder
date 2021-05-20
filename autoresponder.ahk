F7::
Click, 3
Send, ^c
Sleep 500
Run pythonw.exe aternosissues.pyw %clipboard%
Return

+F7::
Send, ^a
Sleep 250
Send, ^x
Sleep 500 
Run pythonw.exe aternosissues.pyw %clipboard%
Return

!F7::
InputBox, UserInput, Write a number., , 640, 480
InputBox, UserInput, Create new Response, Please enter a Response. You do not need to worry about capitalization., , 640, 480
