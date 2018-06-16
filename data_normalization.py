import pandas as pd
import collections
jd_df =pd.read_csv("restaurants_jd.csv",names=["Name","Address","Rating","Contact","Votes","URL","Timings"])
zomato_df=pd.read_csv("restaurant_zomato.csv",names=["Name","Contact","Address","Rating","Cost/2","Timings","Votes"])
final_out=[]
stopwords=["cafe","restaurant","the","restro","restaur..","r..","&","and","lounge","motel","hotel","resort","n"]
#
name_percent_list1=[]
name_percent_list2=[]

def matching(str1,str2):
    a=0
    name_pl2=0
    name_pl1=0
    str1 = str(str1).lower().strip()
    str2 = str(str2).lower().strip()
    list1 = list(set(str1.split(" ")))
    list2 = list(set(str2.split(" ")))
    combined=list1+list2
    counter=collections.Counter(combined)
    for i in stopwords:
        if(i in counter):
            counter.pop(i)
    for i in counter.values():
        if i>1:
            a=a+1

    #print(counter)
    name_pl1=(a/len(list1))*100
    name_pl2=(a/len(list2))*100
    return name_pl1,name_pl2

for x in jd_df.Name:
    for y in zomato_df.Name:
        percentages=[]
        percentages=matching(x,y)
        name_percent_list1.append(percentages[0])
        name_percent_list2.append(percentages[1])


# print("name matching 1")
# for x in name_percent_list1:
#     print(x)
# print("********************************************************")
# print("name matching 2")
# for x in name_percent_list2:
#     print(x)
# print("********************************************************")
address_percent1=[]
address_percent2=[]

for x in jd_df.Address:
    for y in zomato_df.Address:
        percentages=[]
        percentages=matching(x,y)
        address_percent1.append(percentages[0])
        address_percent2.append(percentages[1])


# print("address matching 1")
# for x in address_percent1:
#     print(x)
#
# print("********************************************************")

#
# print("address matching 2")
# for x in address_percent2:
#     print(x)
#
#
# print("********************************************************")

def clean_numbers(number):
    number=str(number)
    number = number.replace(" ","")
    number = number.replace("-","")
    number = number.replace("(", "")
    number = number.replace(")", "")
    number = number.replace("+", "")
    number = number.replace(" ", "")
    return number
#
# def match_contacts(number1,number2):
#     a=0
#     nummber1=str(number1)
#     number2=str(number2)
#     number1_list=clean_numbers(number1).split(",")
#     number2_list=clean_numbers(number2).split(",")
#
#     for i in range(0,len(number1_list)):
#         number1_list[i]= number1_list[i][-10:0]
#     for i in range(0,len(number2_list)):
#         number2_list[i] = number2_list[i][-10:0]
#     for x in number1_list:
#
#     for i in counter.values():
#         if i>1:
#             a=a+1
#
#     percentage1 = (a/len(number1_list))*100
#     percentage2 = (a/len(number2_list))*100
#     return percentage1, percentage2
#
#
# contact_percent1 = []
# contact_percent2 = []
#
# for x in jd_df.Contact:
#     for y in zomato_df.Contact:
#         percentages= []
#         percentages =match_contacts(x,y)
#         contact_percent1.append(percentages[0])
#         contact_percent2.append(percentages[1])
# print(contact_percent1)
#
#
# with open('train_data_complete.csv', 'w') as train:
#     for i in range(len(name_percent_list1)):
#         train.write(str(name_percent_list1[i]) + "," + str(name_percent_list2[i]) +"," + str(address_percent1[i]) + "," +str(address_percent2[i]) +"\n")






