import csv
import os
import re
 
from miner_text_generator import extract_text_by_page
 
 
def export_as_csv(pdf_path, csv_path):
	filename = os.path.splitext(os.path.basename(pdf_path))[0]
	with open(csv_path, 'w', encoding="utf-8") as csv_file:
		writer = csv.writer(csv_file)
		return_data = []
		go = 0
		for page in extract_text_by_page(pdf_path):
			for letter in page:
				if letter == '.':
					go = 1
				if go == 1 and letter != '.':
					if letter in [u"\u25B6"]:
						return_data.append(' TRIANGLE ')
					pattern = re.search(r'[a-zA-Z0-9]{1}',letter)
					if pattern:
						return_data.append(letter)
					else:
						if letter not in [u"\u25B6"]:
							s = letter.encode('raw_unicode_escape')
							if s in [b'\x0c']:
								return_data = ''.join(return_data)
								writer.writerow([return_data])
								return_data = []
							else:
								return_data.append(letter)
				
		writer.writerow([return_data])
 
 
if __name__ == '__main__':
    pdf_path = 'pdf-extract.pdf'
    csv_path = 'pdf-extract.csv'
    export_as_csv(pdf_path, csv_path)