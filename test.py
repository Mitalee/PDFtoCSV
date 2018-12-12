import csv
import os
 
from miner_text_generator import extract_text_by_page
 
 
def export_as_csv(pdf_path, csv_path, title_array):
	filename = os.path.splitext(os.path.basename(pdf_path))[0]
	row_length = len(title_array)
	with open(csv_path, 'w') as csv_file:
		writer = csv.writer(csv_file)
		writer.writerow(title_array)
		for page in extract_text_by_page(pdf_path):
			text = page.replace('\u25cf',',')
			words = text.split()
			array = []
			for key,word in enumerate(words):
				key = key+1
				if key % row_length == 0:
					array.append(word)
					writer.writerow(array)
					array = []
				if key % row_length != 0:
					array.append(word)
 
 
if __name__ == '__main__':
    pdf_path = 'Resume.pdf'
    csv_path = 'Resume.csv'
    export_as_csv(pdf_path, csv_path, ['Name','Words','Stuff'])