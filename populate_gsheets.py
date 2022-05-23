import gspread

sa = gspread.service_account(filename='credentials.json')
sh_cashaam = sa.open('Related Investors -Cashaam')
sh_asis = sa.open('Related investors -Asisvisa')
sh_nkenne = sa.open('Related Investors -NKENNE')
sh_piggyback = sa.open('Related Investors -PiggyBack')
sh_kadogo = sa.open('Related Investors -Kadogo')
sh_investors = sa.open('Investors List')
worksheet_cashaam = sh_cashaam.worksheet('Orgs')
worksheet_asis = sh_asis.worksheet('Sheet1')
worksheet_nkenne = sh_nkenne.worksheet('Sheet1')
worksheet_piggyback = sh_piggyback.worksheet('Sheet1')
worksheet_kadogo = sh_kadogo.worksheet('Sheet1')
worksheet_investors = sh_investors.worksheet('Sheet1')
all_values_cashaam = worksheet_cashaam.get()
all_values_asis = worksheet_asis.get()
all_values_nkenne = worksheet_nkenne.get()
all_values_piggyback = worksheet_piggyback.get()
all_values_kadogo = worksheet_kadogo.get()
all_investors = worksheet_investors.get()
company_names = []
counter = 1
for investors in all_investors:
    company_names.append(investors[4])
for company in all_values_cashaam:
    for each_investor in company_names:
        if company[2] in each_investor and len(company) < 4:
            index = company_names.index(each_investor)
            company_people = worksheet_investors.row_values(index + 1)
            worksheet_cashaam.update('D'+ str(counter), company_people[1])
            worksheet_cashaam.update('E'+ str(counter), company_people[5])
    
    counter += 1
company_names = []
counter = 1
for investors in all_investors:
    company_names.append(investors[4])
for company in all_values_asis:
    for each_investor in company_names:
        if company[1] in each_investor and len(company) < 4:
            index = company_names.index(each_investor)
            company_people = worksheet_investors.row_values(index + 1)
            worksheet_asis.update('C'+ str(counter), company_people[1])
            worksheet_asis.update('D'+ str(counter), company_people[5])
    
    counter += 1
company_names = []
counter = 1
for investors in all_investors:
    company_names.append(investors[4])
for company in all_values_nkenne:
    for each_investor in company_names:
        if company[1] in each_investor and len(company) < 4:
            index = company_names.index(each_investor)
            company_people = worksheet_investors.row_values(index + 1)
            worksheet_nkenne.update('C'+ str(counter), company_people[1])
            worksheet_nkenne.update('D'+ str(counter), company_people[5])
    
    counter += 1
company_names = []
counter = 1
for investors in all_investors:
    company_names.append(investors[4])
for company in all_values_piggyback:
    for each_investor in company_names:
        if company[1] in each_investor and len(company) < 4:
            index = company_names.index(each_investor)
            company_people = worksheet_investors.row_values(index + 1)
            worksheet_piggyback.update('C'+ str(counter), company_people[1])
            worksheet_piggyback.update('D'+ str(counter), company_people[5])
    
    counter += 1
company_names = []
counter = 1
for investors in all_investors:
    company_names.append(investors[4])
for company in all_values_kadogo:
    for each_investor in company_names:
        if company[1] in each_investor and len(company) < 4:
            index = company_names.index(each_investor)
            company_people = worksheet_investors.row_values(index + 1)
            worksheet_kadogo.update('C'+ str(counter), company_people[1])
            worksheet_kadogo.update('D'+ str(counter), company_people[5])
    
    counter += 1