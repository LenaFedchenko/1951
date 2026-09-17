# сделать бесконечный цикл, который спрашивает как дела, 
# если ответ был плохо, то остановить цикл


while True:
    howareyou = input("how are things?")
    if howareyou == "bad" or "not really good":
        break