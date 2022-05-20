def char_range(start, stop, step=1):
    stop_modifer = 1
    start_code = ord(start)
    stop_code = ord(stop)
    
    if start_code > stop_code:
            step *= -1
            stop_modifer *= -1
            
    for value in range(start_code, stop_code + 1, stop_modifer, step):
       yield chr(value)