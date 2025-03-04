# Práctica con archivos CSV, leyendo datos de un archivo CSV.
import csv

def read_and_print_csv_data(path):
    with open(path, "r") as file:
        reader = csv.DictReader(file)
        for line in reader:
            print(line)

read_and_print_csv_data("ventas.csv")

# Práctica con archivos CSV, insertando datos en un archivo CSV.

countries_list = [
	{
		'name': 'Costa Rica',
		'capital': 'San José',
		'currency': 'Colón',
		'area_km2': '51,100',
	},
	{
		'name': 'Colombia',
		'capital': 'Bogotá',
		'currency': 'Peso Colombiano',
		'area_km2': '1,141,748',
	},
	{
		'name': 'México',
		'capital': 'Ciudad de México',
		'currency': 'Peso Mexicano',
		'area_km2': '1,972,550',
	},
]

country_headers = (
	'name',
	'capital',
	'currency',
	'area_km2',
)


def write_csv_file(path, headers, data):
    with open(path, "w", encoding="utf-8") as file:
        writer = csv.DictWriter(file,headers)
        writer.writeheader()
        writer.writerows(data)


write_csv_file("countries.csv", country_headers, countries_list)