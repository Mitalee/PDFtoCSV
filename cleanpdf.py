import csv
import re
 
def clean_data(csv_path):
	new_array = []
	with open(csv_path, 'r') as csv_file:
		reader = csv.reader(csv_file)
		for row in reader:
			row = ''.join(row)
			dots = re.findall(r'(?:[A-Z])l{1}(?:[A-Z])',row)
			if dots:
				for l in dots:
					huh = row.index(l)
					new_row = row[:huh+1] + ' OVAL ' + row[huh + 1 :]
					row = new_row
			main_cat = re.findall(r'[A-Z]{2,}',row)
			word_bank = ['OVAL', 'ACE']
			if main_cat:
				for word in main_cat:
					if word not in word_bank:
						huh2 = row.index(word)
						tots = len(word)
						new_row = row[:huh2] + ' {0} '.format(word) + row[huh2 + tots:]
						row = new_row
						word_bank.append(word)
			
			mini_cat = re.findall(r'l?[A-Z]{1}[a-z]+[A-Z,a-z]*:',row)
			if mini_cat:
				for i in mini_cat:
					main_text = re.search(r'l[A-Z]{1}[a-z]*[A-Z,a-z]*:',i)
					if main_text:
						i = main_text.group()
					loc = row.index(i)
					leng = len(i)
					next_row = row[:loc] + 'OVAL {0} '.format(i) + row[loc + leng :]
					row = next_row
			get_see = re.findall(r'[A-Z]{1}\s?[a-z]*see[A-Za-z]*-?[A-Za-z]*',row)
			if get_see:
				for item in get_see:				
					LOC = row.index(item)
					apple = item.replace(' ','').replace('see',' see ').replace('NSAIDs',' NSAIDs OVAL ')
					patt = re.findall(r'[a-z][A-Z]',apple)
					if patt:
						for j in patt:
							cap = j[0]+ ' OVAL '+ j[1]
							apple = apple.replace(j, cap)
					lang = len(item)
					apple = 'OVAL ' + apple + 'OVAL'
					n_row = row[:LOC] + apple + row[LOC + lang :]
					row = n_row
			cake = row.replace('TRIANGLE', 'OVAL TRIANGLE').replace('OVAL OVAL ', '').replace('TRIANGLE OVAL', 'TRIANGLE').replace('TRIANGLE  OVAL', 'TRIANGLE')
			pat = re.findall(r' l[A-Z][A-Za-z]*:',cake)
			if pat:
				for pa in pat:
					huh4 = cake.index(pa)
					la = len(pa)
					if huh4 != '0':
						pear = 'OVAL ' + pa
						new_ite = cake[:huh4] + pear + cake[huh4 + la :]
						cake = new_ite
			cake = cake.replace('ACEI nhibitors', 'ACE Inhibitors').replace('channeOVALOVAL  lB', 'channelB')
			p = re.findall(r'[a-z][A-Z][a-z]+ OVAL',cake)
			if p:
				for blah in p:
					huh5 = cake.index(blah)
					l = len(blah)
					banana = 'OVAL ' + blah
					new_it = cake[:huh5 + 1] + banana + cake[huh5 + l :]
					cake = new_it
			cake = cake.split('OVAL')
			array = []
			for blah in cake:
				if blah[:3] == '  l':
					blah = blah[3:]
				if blah[:2] == ' e':
					blah = blah[2:]
				array.append(blah)
			for item in array:
				tickle = re.search(r'\d*Appendix.*',item)
				if tickle:
					spo = item.index(tickle.group())
					item = item[:spo]
				new_array.append(item)
		
	with open('extract2.csv', 'w', encoding="utf-8") as csv_file:
		writer = csv.writer(csv_file)
		for a in new_array:
			if a not in [' l','']:
				cont = re.search(r'\(continued\)',a)
				if cont:
					pass
				else:
					split_up = re.search(r'[A-Z][a-z]*TRIANGLE',a)
					if split_up:
						fix = split_up.group().replace('TRIANGLE','')
						writer.writerow([fix])
					else:
						writer.writerow([a])
	
clean_data('pdf-extract.csv')

#https://drive.google.com/file/d/1aHNlIPaXpK3-2Toek2CqqJAuzY55h8ST/view