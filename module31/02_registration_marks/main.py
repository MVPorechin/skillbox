import re


text = "А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666"
pattern_taxi_cars = r"\b\w\d{3}\w{2}\d{2,3}\b"
pattern_private_cars = r"\b\w{2}\d{3}\d{2,3}"

private_cars = re.findall(pattern=pattern_taxi_cars, string=text)
taxi_cars = re.findall(pattern=pattern_private_cars, string=text)
print(f'Список номеров частных автомобилей: {private_cars}\n'
      f'Список номеров такси: {taxi_cars}')