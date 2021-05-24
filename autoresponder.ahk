F7::
Click, 3
Send, ^c
Sleep 500
Run pythonw autoresponder.pyw Use %Clipboard%
Return

!F7::
InputBox, UserTrigger, Type in a trigger., , 640, 480
InputBox, UserResponse, Type in a response., , 640, 480
Run pythonw autoresponder.pyw CreatingResponse %UserTrigger% | %UserResponse%
Return

+F7::
InputBox, DeleteTrigger, Type in the trigger which you would like to remove., , 640, 480
Run pythonw autoresponder.pyw DeleteResponse %DeleteTrigger%
Return

!+F7::
Run, tandr.json
Return