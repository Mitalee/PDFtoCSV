import csv
import re
 
def clean_data(csv_path):
	new_array = []
	builder = []
	with open(csv_path, 'r',encoding="utf-8") as csv_file:
		reader = csv.reader(csv_file)
		for row in reader:
			if row not in [[],' ']:
				chance = row[0]
				if 'see' in chance:
					if len(row[0]) < 55:
						if row[0][0] != '(':
							new_array.append(row[0])
							pass
				else:
					check_title = re.search(r'[A-Za-z]+:',chance)
					if check_title:
						builder.append(chance)
					else:
						grab = re.search(r'[A-Z][a-z]*',chance)
						if grab:
							tot = grab.group()
							if len(tot) > 1:
								print(tot)
		
clean_data('extract2.csv')