#1
password = input("Введите пароль: ")      #ввод

if len(password) < 8:       #проверканадлину
    print("Слишком короткий пароль")
if len(password) >= 8:
    print("Пароль принят")




#2
status = input("Введите статус сервера (online/offline): ")

if status == "online":       #проверканаверность
    print("Связь установлена")
else:
    print("Связь потеряна")



#3

level = int(input("Введите уровень угрозы (1-100): "))

if 1 <= level <= 30:
    print("Низкий уровень угрозы")
elif 31 <= level <= 70:
    print("Средний уровень угрозы")
elif 71 <= level <= 100:
    print("Критический уровень угрозы")
else:
    print("Ошибка ввода")



#4

checksum_original = input("Введите оригинальную контрольную сумму: ")
checksum_current = input("Введите текущую контрольную сумму: ")

status = "Файл не изменён" if checksum_original == checksum_current else "Файл повреждён"

print(status)




#5

event_code = input("Введите код события (ERR/WRN/INF): ")

match event_code:
    case "ERR":
        print("Ошибка системы")
    case "WRN":
        print("Предупреждение")
    case "INF":
        print("Информационное сообщение")
    case _:
        print("Неизвестный код события")