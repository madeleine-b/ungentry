#open csv file
#convert to json?
#get percentages of loan purpose breakdown by 
#	PctMrtgAppsHomePurch1_4m = home_purchase
#	PctMrtgAppsHomeImprov1_4m = home_improvement
#	PctMrtgAppsRefin1_4m = refinancing

import csv, pprint

percent_loan_purpose = dict()

with open('nat_hmda_tract2005_ext1.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		hp = row['PctMrtgAppsHomePurch1_4m']
		rf = row['PctMrtgAppsRefin1_4m']
		hi = row['PctMrtgAppsHomeImprov1_4m']
		values = {"Home purchase" : hp if len(hp)>0 else '0',
				"Refinancing" : rf if len(rf)>0 else '0',
				"Home improvement" : hi if len(hi)>0 else '0'}

		percent_loan_purpose[row['STFID']] = values

pp = pprint.PrettyPrinter(indent=1)
pp.pprint(percent_loan_purpose)