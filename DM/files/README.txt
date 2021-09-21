I have used Anaconda based Python interpreter, version 3.8.8. Please use Anaconda only for execution. 

Also following packages have been used:
1. pandas
2. math
3. json

The data files used are:-
1) http://data.covid19india.org/csv/latest/cowin_vaccine_data_districtwise.csv
2) https://data.covid19india.org/csv/latest/districts.csv
3) http://censusindia.gov.in/pca/DDW_PCA0000_2011_Indiastatedist.xlsx
4) neighbor-districts.json

All the executable bash files are contained in 'scripts' folder and the names are as under:

case-generator.sh                  vaccinated-count-generator.sh
complete-vaccination-generator.sh  vaccinated-ratio-generator.sh
edge-generator.sh                  vaccination-population-ratio-generator.sh
peaks-generator.sh                 vaccine-type-ratio-generator.sh

EXCEPTION: Since there is no bash file name given for question 1, I have combined question 1 and question 2 under one bash file that is 'edge-generator.sh'. However, the output of each question still remains the same. 

 
Steps for execution:
- Open a terminal window in the same folder where you unzip the given file. (PS: This folder should contain the file 'assign1.sh')
- Run the executable file, assign1.sh, using the command, "./assign1.sh"
- You will find all the resultant CSV files in the 'output' directory
- There are 24 files in the output directory 


Question specific analysis:
1. On succesful execution document is made called 'neighbor-districts-modified.json' which is the changed adaptation of 'neighbor-districts.json' that will contains the adjusted districts alongside the neighbors as indicated by the information given on the 'https://www.covid19india.org/'. The quantity of districts consolidated were 620. 

2. Here we are using the file generated in the previous question to make an undirected graph which is then reported in the form of key value pairs. Since the graph is undirected, I have taken care that the entries like (a,b) and (b,a) do not occur simultaneously. Files created: edge_graph.csv

3. The dataset used was 'https://data.covid19india.org/csv/latest/districts.csv'. Removal of cumulation in the data has been taken care of. Files created: cases-month.csv, cases-week.csv, cases-overall.csv

4. The dataset used for getting the cases was 'https://data.covid19india.org/csv/latest/districts.csv'. This file also had cumulative data which is removed using a method called shfit and subtract. The file 'https://data.covid19india.org/csv/latest/district_wise.csv' has been used for the district codes. Files created: district-peeks.csv, state-peeks.csv, overall-peeks.csv

5. The dataset used is 'http://data.covid19india.org/csv/latest/cowin_vaccine_data_districtwise.csv'.  Files created: district-vaccinated-count-month.csv, district-vaccinated-count-overall.csv, district-vaccinated-count-week.csv, state-vaccinated-count-overall.csv, state-vaccinated-count-state.csv, state-vaccinated-count-week.csv


6. The data for population has been taken from 'http://censusindia.gov.in/pca/DDW_PCA0000_2011_Indiastatedist.xlsx'. For vaccination data, 'http://data.covid19india.org/csv/latest/cowin_vaccine_data_districtwise.csv' is used and the final sets of ratios are calculated. Files created:district-vaccination-population-ratio.csv, overall-vaccination-population-ratio.csv, state-vaccination-population-ratio.csv

7. Dataset used is same as the previous one. Here we are calculating the ratios of different types of vaccines administered in India. The places where Covaxin is not available, we get the ratio as 'inf'. Files created: district-vaccine-type-ratio.csv, state-vaccine-type-ratio.csv, overall-vaccine-type-ratio.csv. 

8.Input datasets: http://data.covid19india.org/csv/latest/cowin_vaccine_data_districtwise.csv gives the number of people vaccinated, http://censusindia.gov.in/pca/DDW_PCA0000_2011_Indiastatedist.xlsx gives the population numbers on the basis of district/state. Files created: district-vaccinated-dose-ratio.csv, state-vaccinated-dose-ratio.csv, overall-vaccinated-dose-ratio.csv

9.Input datasets: (http://data.covid19india.org/csv/latest/cowin_vaccine_data_districtwise.csv) for vaccination related information. The rate of vaccination for every state has been calculated based on the total doses administered in the last week, that is August 8, 2021 to August 14, 2021. Files creaated: complete-vaccination.csv


NOTE: The execution time is ~2 mins. Please be patient. 
