from pymining import itemmining
import operator
f = open("retail.txt",'r')
transactions = []
for line in f:
	# print(line)
	line = line[:-1].split(' ')
	
	line = list(map(int,line[:-1]))

	transactions.append(line)

#transactions = (('a', 'b', 'c'), ('b'), ('a'), ('a', 'c', 'd'), ('b', 'c'), ('b', 'c'))
relim_input = itemmining.get_relim_input(transactions)
report = itemmining.relim(relim_input, min_support=2)
new_report = {}
for key in report:
	if len(key) > 1:
		new_report[key] = report[key]

sorted_report = sorted(new_report.items(),key=operator.itemgetter(1),reverse=True)
for index in range(0,10):
	print(str(sorted_report[index][1]) + " " + str(sorted(list(sorted_report[index][0]))))
