#!/usr/bin/env python
# coding: utf-8

# # U.S. Medical Insurance Costs

# In[80]:


import csv
with open("insurance.csv") as insurance_data_csv:
    insurance_data = csv.DictReader(insurance_data_csv)
#Decalre our global variables
    regions = ["southwest", "northwest", "southeast", "northeast"]
    national = list(insurance_data)
    sw = []
    nw = []
    se = []
    ne = []
    total_age = 0
    total_bmi = 0
    total_smokers = 0
    total_charges = 0
    
#Segregate data by Region
    for row in national:
        if row['region'] == regions[0]:
            sw.append(row)
        elif row['region'] == regions[1]:
            nw.append(row)
        elif row['region'] == regions[2]:
            se.append(row)
        elif row['region'] == regions[3]:
            ne.append(row)
        
#Find out National Averages

    population = len(sw) + len(se) + len(ne) + len(nw)
    
    for row in national:
        total_age += int(row['age'])
        total_bmi += float(row['bmi'])
        total_charges += float(row['charges'])
        if row['smoker'] == 'yes':
            total_smokers += 1
        else:
            continue

    national_avg_age = round(total_age / population, 1)
    national_avg_bmi = round(total_age / population, 1)
    national_avg_smokers = round(total_smokers / population, 3)* 100
    national_avg_charges = round(total_charges / population, 2)
    
#Print National Averages
    print("""
In our data, the average age was {} with an average BMI of {}. 
Approximatley {}% of the population smokes. 
The average Insurance Premium charges are ${}.
    """.format(national_avg_age, national_avg_bmi, national_avg_smokers, national_avg_charges))
    
#Iterate through out Regions and find population percentage
    for region in regions:
        region_list = []
        if region == regions[0]:
            region_list = sw
        if region == regions[1]:
            region_list = nw
        if region == regions[2]:
            region_list = se
        if region == regions[3]:
            region_list = ne
        
        population_percent = round(len(region_list) / population, 3) * 100
    

#Declare Region Variables
        region_population = len(region_list)
        ages_total = 0
        bmi_total = 0
        smokers_total = 0
        charges_total = 0
        
#Iterate data to establish Region totals
        for data in region_list:
            ages_total += int(data['age'])
            bmi_total += float(data['bmi'])
            charges_total += float(data['charges'])
            if data['smoker'] == 'yes':
                smokers_total += 1
            else:
                continue
                
#Create Average Region Data   
        ages_avg = round(ages_total / region_population, 1)
        bmi_avg = round(bmi_total / region_population, 1)
        smokers_avg = round(smokers_total / region_population, 3) * 100
        charges_avg = round(charges_total / region_population, 2)
    
#Print Region Data Findings
        print("The {} region represents {}% of our data.".format(region, population_percent))
    
        if ages_avg > national_avg_age:
            print("The average age in the {} was {}. This was above the national average.".format(region, ages_avg))
        elif ages_avg < national_avg_age:
            print("The average age in the {} was {}. This was below the national average.".format(region, ages_avg))
        else:
            print("The average age in the {} was {}. This is on par with the national average.".format(region, ages_avg))
        
        if bmi_avg > national_avg_bmi:
            print("The average BMI in the {} was {}. This was above the national average.".format(region, bmi_avg))
        elif bmi_avg < national_avg_bmi:
            print("The average BMI in the {} was {}. This was below the national average.".format(region, bmi_avg))
        else:
            print("The average BMI in the {} was {}. This is on par with the national average.".format(region, bmi_avg))
        
        if smokers_avg > national_avg_smokers:
            print("Approximatley {}% of the {} population smokes. This was above the national average.".format(smokers_avg, region))
        elif smokers_avg < national_avg_smokers:
            print("Approximatley {}% of the {} population smokes. This was below the national average.".format(smokers_avg, region))
        else:
            print("Approximatley {}% of the {} population smokes. This is on par with the national average.".format(smokers_avg, region))
  

        if charges_avg > national_avg_charges:
            print("The average Insurance Premium charges in the {} region are ${}. This was above the national average.".format(region, charges_avg))
        elif charges_avg < national_avg_charges:
            print("The average Insurance Premium charges in the {} region are ${}. This was below the national average.".format(region, charges_avg))
        else:
            print("The average Insurance Premium charges in the {} region are ${}. This is on par with the national average.".format(region, charges_avg))
            
        print("")

        


# #### 

# In[63]:





# In[ ]:




