#'https://www.worlddata.info/' 


from func import tag_cl
# from datetime import date
import requests 
import os
import re


####


home = os.getcwd()
os.mkdir('Project_Data')
os.chdir('Project_Data')

web_url = 'https://www.worlddata.info/'

continet = 'asia/'
# continet = '/'
# continet = '/'
# continet = '/'
# continet = '/'
# continet = '/'
# continet = '/'

# lst_coun_asi = ['afghanistan', 'armenia', 'azerbaijan', 'bahrain', 'bangladesh', 'bhutan', 'brunei', 'cambodia', 'china', 'cyprus', 'georgia', 'india', 'indonesia', 'iran', 'iraq', 'japan', 'jordan', 'kazakhstan', 'kuwait', 'kyrgyzstan', 'laos', 'lebanon', 'malaysia', 'maldives', 'mongolia', 'myanmar', 'nepal', 'north-korea', 'oman', 'pakistan', 'palestine', 'philippines', 'qatar', 'russia', 'saudi-arabia', 'singapore', 'south korea', 'sri lanka', 'syria', 'taiwan', 'tajikistan', 'thailand', 'timor-leste', 'turkey', 'turkmenistan', 'arab-emirates', 'uzbekistan', 'vietnam', 'yemen']

# lst_coun_asi = ['afghanistan', 'azerbaijan']

lst_coun_asi = ['iran']


####

for coun in lst_coun_asi:
    folder_name = coun
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    print(f'STRG /////////{coun}///////')
    # os.mkdir('proj_d')
    # os.chdir('proj_d')
    final_url = web_url + continet + coun +'/index.php'
    response = requests.get(final_url)
    html_data = response.text

# Population


# Overall Population 

    #-------
    result_pop = re.findall(r'Population:</a>\S{1,}</div>', html_data)
    if len(result_pop) > 0:
     pop_c = tag_cl(result_pop)         
     print(result_pop)
    else:
         pop_c = ['No data']
         print(pop_c)



# Population per km²

    #-------
    result_pop_per = re.findall(r'Population per km²:</a>\S{1,}</div>', html_data)
    if len(result_pop_per) > 0:
     pop_per = tag_cl(result_pop_per)         
     print(pop_per)
    else:
         pop_per = ['No data']
         print(pop_per)


# Life expectancy males

    #-------
    result_males = re.findall(r'Life expectancy males:</a>&#216; \S{1,} years</div>', html_data)
    if len(result_males) > 0:
     pop_mal = tag_cl(result_males)         
     print(pop_mal)
    else:
         pop_mal = ['No data']
         print(pop_mal)



# Life expectancy females

    #-------
    result_Life = re.findall(r'Life expectancy females:</div>&#216; \S{1,} years</div>', html_data)
    if len(result_Life) > 0:
     pop_fmal = tag_cl(result_Life)         
     print(pop_fmal)
    else:
         pop_c = ['No data']
         print(pop_fmal)


# Birth rate

    #-------
    result_Birth_rate = re.findall(r'Birth rate:</div>\S{1,} ‰</div>', html_data)
    if len(result_Birth_rate) > 0:
     pop_btr = tag_cl(result_Birth_rate)         
     print(pop_btr)
    else:
         pop_btr = ['No data']
         print(pop_btr)



# Death rate

    #-------
    result_Death_rate = re.findall(r'Death rate:</div>\S{1,} ‰</div>', html_data)
    if len(result_Death_rate) > 0:
     pop_dtr = tag_cl(result_Death_rate)         
     print(pop_dtr)
    else:
         pop_dtr = ['No data']
         print(pop_dtr)

    
# Males/Females

    #-------
    result_Males_Females = re.findall(r'Males/Females:</div>\S{1,} : \S{1,}</div>', html_data)
    if len(result_Males_Females) > 0:
     pop_mf = tag_cl(result_Males_Females)         
     print(pop_mf)
    else:
         pop_mf  = ['No data']
         print(pop_mf)


####


# Economy


# GDP

    #-------
    result_GDP = re.findall(r'GDP:</td><td>\S{1,} ', html_data)
    if len(result_GDP) > 0:
     pop_GDP = tag_cl(result_GDP)         
     print(pop_GDP)
    else:
         pop_GDP = ['No data']
         print(pop_GDP)



# Tourism receipts

    #-------
    result_Tourism = re.findall(r'Tourism receipts</a>:</td><td>\S{1,} ', html_data)
    if len(result_Tourism) > 0:
     pop_TRS = tag_cl(result_Tourism)         
     print(pop_TRS)
    else:
         pop_TRS = ['No data']
         print( pop_TRS)



# Debt rate

    #-------
    result_Debt = re.findall(r'Debt rate\S{,4}:</td><td>\S{1,} %', html_data)
    if len(result_Debt) > 0:
     pop_DBT = tag_cl(result_Debt)         
     print(pop_DBT)
    else:
         pop_c = ['No data']
         print(pop_DBT)



# Unemployment rate(ILOEST)

    #-------
    result_Unemployment = re.findall(r'Unemployment rate</a><span style="font-size:.8em">\(ILOEST\)\S{1,} ', html_data)
    if len(result_Unemployment) > 0:
     pop_UER = tag_cl(result_Unemployment)         
     print(pop_UER)
    else:
         pop_UER = ['No data']
         print(pop_UER)



# Inflation rate

    #-------
    result_Inflation = re.findall(r'Inflation rate</a>:</td><td>\S{1,} ', html_data)
    if len(result_Inflation) > 0:
     pop_IFR = tag_cl(result_Inflation)         
     print(pop_IFR)
    else:
         pop_IFR = ['No data']
         print(pop_IFR)



# Corruption index

    #-------
    result_Corruption = re.findall(r'Corruption index</a>:</td><td>\S{1,} \(\w{1,}\s{,1}\w{1,}\)</td>', html_data)
    if len(result_Corruption) > 0:
     pop_CRI = tag_cl(result_Corruption)         
     print(pop_CRI)
    else:
         pop_CRI = ['No data']
         print(pop_CRI)



# Energy consumption

    #-------
    result_Energy = re.findall(r'Energy consumption</a>:</td><td>\S{1,} ', html_data)
    if len(result_Energy) > 0:
     pop_EGC = tag_cl(result_Energy)         
     print(pop_EGC)
    else:
         pop_EGC = ['No data']
         print(pop_EGC)



####


# Land use


# Urban areas


    #-------
    result_Land = re.findall(r'Land use</h2><table class="std100 hover"><tr><td>\S{1,} ', html_data)
    if len(result_Land) > 0:
     pop_LAN = tag_cl(result_Land)         
     print(pop_LAN)
    else:
         pop_LAN= ['No data']
         print(pop_LAN)



    #-------
    result_Urban = re.findall(r'Urban areas:</td><td>\S{1,} ', html_data)
    if len(result_Urban) > 0:
     pop_UBR = tag_cl(result_Urban)         
     print(pop_UBR)
    else:
         pop_UBR = ['No data']
         print(pop_UBR)



# Agricultural areas


    #-------
    result_Agricultural = re.findall(r'</td></tr><tr><td>\S{1,} Agricultural areas', html_data)
    if len(result_Agricultural) > 0:
     pop_AGR = tag_cl(result_Agricultural)         
     print(pop_AGR)
    else:
         pop_AGR = ['No data']
         print(pop_AGR)




    #-------
    result_Agricultural2 = re.findall(r'Agricultural areas:</td><td>\S{1,} ', html_data)
    if len(result_Agricultural2) > 0:
     pop_AGR2 = tag_cl(result_Agricultural2)         
     print(pop_AGR2)
    else:
         pop_AGR2 = ['No data']
         print(pop_AGR2)



# Forest


    #-------
    result_Forest = re.findall(r'</td></tr><tr><td>\S{1,} Forest', html_data)
    if len(result_Forest) > 0:
     pop_FR = tag_cl(result_Forest)         
     print(pop_FR)
    else:
         pop_FR = ['No data']
         print(pop_FR)




    #-------
    result_Forest2 = re.findall(r'Forest:</td><td>\S{1,} ', html_data)
    if len(result_Forest2) > 0:
     pop_FR2 = tag_cl(result_Forest2)         
     print(pop_FR2)
    else:
         pop_FR2 = ['No data']
         print(pop_FR2)



# Water areas


    #-------
    result_Water = re.findall(r'</td></tr><tr><td>\S{1,} Water areas', html_data)
    if len(result_Water) > 0:
     pop_WAT = tag_cl(result_Water)         
     print(pop_WAT)
    else:
         pop_WAT = ['No data']
         print(pop_WAT)




    #-------
    result_Water2 = re.findall(r'Water areas:</td><td>\S{1,}', html_data)
    if len(result_Water2 ) > 0:
     pop_WA2 = tag_cl(result_Water2 )         
     print(pop_WA2)
    else:
         pop_WA2 = ['No data']
         print(pop_WA2)



# Other


    #-------
    result_Others =  re.findall(r'</td></tr><tr><td>\S{1,} Others', html_data)
    if len(result_Others) > 0:
     pop_other = tag_cl(result_Others)         
     print(pop_other)
    else:
         pop_other = ['No data']
         print(pop_other)





    #-------
    result_Others2 = re.findall(r'Others:</td><td>\S{1,}', html_data)
    if len(result_Others2) > 0:
     pop_other_1 = tag_cl(result_Others2)         
     print(pop_other_1)
    else:
         pop_other_1 = ['No data']
         print(pop_other_1)


####


# Transport


# Roadways

    #-------
    result_Roadways = re.findall(r'Roadways:</td><td>\S{1,}', html_data)
    if len(result_Roadways) > 0:
     pop_RDW = tag_cl(result_Roadways)         
     print(pop_RDW)
    else:
         pop_RDW = ['No data']
         print(pop_RDW)



# Railways

    #-------
    result_Railways = re.findall(r'Railways:</td><td>\S{1,}', html_data)
    if len(result_Railways) > 0:
     pop_RW = tag_cl(result_Railways)         
     print(pop_RW)
    else:
         pop_RW = ['No data']
         print(pop_RW)

    
  
# Waterways

    #-------
    result_Waterways = re.findall(r'Waterways:</td><td>\S{1,}', html_data)
    if len(result_Waterways) > 0:
     pop_WAW = tag_cl(result_Waterways)         
     print(pop_WAW)
    else:
         pop_WAW = ['No data']
         print(pop_WAW)

  
    
# Reg. vehicles

    #-------
    result_Reg = re.findall(r'Reg. vehicles:</td><td>\S{1,}', html_data)
    if len(result_Reg) > 0:
     pop_REG = tag_cl(result_Reg)         
     print(pop_REG)
    else:
         pop_REG = ['No data']
         print(pop_REG)



# Airports

    #-------
    result_Airports = re.findall(r'Airports</a>:</td><td>\S{1,}', html_data)
    if len(result_Airports) > 0:
     pop_AIR = tag_cl(result_Airports)         
     print(pop_AIR)
    else:
         pop_AIR = ['No data']
         print(pop_AIR)

  

####


# lang / rili


# lan1
    result_lan = re.findall(r'\w{1,}\S{,4}</td><td>\d{1,2}.\d %</td>', html_data)
    if len(result_lan) > 0:
     pop_LAG = tag_cl(result_lan)         
     print(pop_LAG)
    else:
         pop_LAN = ['No data']
         print(pop_LAG)


# rili
    result_rili = re.findall(r'</tr><tr><td>\w{1,}</td><td>\d{1,3}.\d%</td></tr>', html_data)
    if len(result_rili) > 0:
     pop_RIL = tag_cl(result_rili)         
     print(pop_RIL)
    else:
         pop_RIL = ['No data']
         print(pop_RIL)
         
    result_rilig = re.findall(r'<tr><td>\w{1,}</td><td>\d{1,3}.\d%</td>', html_data)
    if len(result_rilig) > 0:
     pop_RILG = tag_cl(result_rilig)         
     print(pop_RILG)
    else:
         pop_RILG = ['No data']
         print(pop_RILG)
         


####

# OS


    f = open(f'{coun}_population.txt', 'w')
    f.write(pop_c[0])
    f.write('\n')
    f.write(pop_per[0])
    f.write('\n')
    f.write(pop_mal[0])
    f.write('\n')
    f.write(pop_fmal[0])
    f.write('\n')
    f.write(pop_btr[0])
    f.write('\n')
    f.write(pop_dtr[0])
    f.write('\n')
    f.write(pop_mf[0])
    f.write('\n')
    f.close()
    #----------
    f = open(f'{coun}_economy.txt', 'w')
    f.write(pop_GDP[0])
    f.write('\n')
    f.write(pop_TRS[0])
    f.write('\n')
    f.write(pop_DBT[0])
    f.write('\n')
    f.write(pop_UER[0])
    f.write('\n')
    f.write(pop_IFR[0])
    f.write('\n')
    f.write(pop_CRI[0])
    f.write('\n')
    f.write(pop_EGC[0])
    f.write('\n')
    f.close()
    #----------
    f = open(f'{coun}_language.txt', 'w')
    for item in pop_LAG:
        f.write(item)
        f.write('\n')
    f.close()
    #----------
    f = open(f'{coun}_religion.txt', 'w')
    for item in pop_RILG:
        f.write(item)
        f.write('\n')
    f.close()
    #----------
    f = open(f'{coun}_land use.txt', 'w')
    f.write(pop_LAN[0])
    f.write('\n')
    f.write(pop_UBR[0])
    f.write('\n')
    f.write(pop_UBR[0])
    f.write('\n')
    f.write(pop_AGR[0])
    f.write('\n')
    f.write(pop_AGR2[0])
    f.write('\n')
    f.write(pop_FR[0])
    f.write('\n')
    f.write(pop_FR2[0])
    f.write('\n')
    f.write(pop_WAT[0])
    f.write('\n')
    f.write(pop_WA2[0])
    f.write('\n')
    f.write(pop_other[0])
    f.write('\n')
    f.write(pop_other_1[0])
    f.write('\n')
    f.close()
    #----------
    f = open(f'{coun}_transport.txt', 'w')
    f.write(pop_RDW[0])
    f.write('\n')
    f.write(pop_RW[0])
    f.write('\n')
    f.write(pop_WAW[0])
    f.write('\n')
    f.write(pop_REG[0])
    f.write('\n')
    f.write(pop_AIR[0])
    f.write('\n')
    f.close()
    os.chdir(home + '/Project_Data')