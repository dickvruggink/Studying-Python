# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line

spain_language_spoken = 'Spanish'
switzerland_language_spoken = 'German'
print(spain_language_spoken == switzerland_language_spoken)

spain_prevalent_religion = 'Roman Catholic'
switzerland_prevalent_religion = 'Roman Catholic'
print(spain_prevalent_religion == switzerland_prevalent_religion)

spain_capital = 'Madrid'
switzerland_capital = 'Bern'
print (len(spain_capital) != len(switzerland_capital))

spain_gdp = 1714860000000
switzerland_gdp = 590710000000
print(switzerland_gdp > spain_gdp)

spain_population_growth = 0.13
switzerland_population_growth = 0.65
print(spain_population_growth and switzerland_population_growth <1) 

population_over_tenmillion = 10000000

spain_population = 47163418
switzerland_population = 8508698
print(spain_population > population_over_tenmillion | switzerland_population > population_over_tenmillion)
print(spain_population > population_over_tenmillion or switzerland_population > population_over_tenmillion)

#print(spain_population | switzerland_population > 10000000)
#print(spain_population ^ switzerland_population > 10000000)