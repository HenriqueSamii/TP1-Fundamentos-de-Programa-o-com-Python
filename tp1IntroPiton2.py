import datetime
#2. Faça uma função em Python que receba do usuário a idade de uma pessoa em anos,
#meses e dias e retorne essa idade expressa em dias.
#Considere que todos os anos têm 365 dias.

dayUser = input("Insira dia - ")
monthUser = input("Insira mes - ")
yearUser = input("Insira ano - ")

dayUser = int(dayUser)
monthUser = int(monthUser)
yearUser = int(yearUser)

dateTimeNow = datetime.datetime.now()
dateTimeUser = datetime.datetime(int(yearUser), int(monthUser), int(dayUser))

pastMonthsDays = int(dateTimeNow.strftime("%j"))-int(dateTimeUser.strftime("%j"))

pastYearsInDays = (int(dateTimeNow.strftime("%Y"))-int(dateTimeUser.strftime("%Y")))*365+pastMonthsDays

print("Passaram-se " + str(pastYearsInDays) +" dias")