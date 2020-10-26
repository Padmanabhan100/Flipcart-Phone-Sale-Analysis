from bs4 import BeautifulSoup as bs
import requests
import time


## declaring variables
name_list = []
offer_price_list = []
real_price_list = []
expandable_upto_list = []
ram_list = []
rom_list = []
screen_list = []
rear_cam_list = []
battery_list = []
processor_list = []
stars_list = []
no_of_rating_list = []




### scraping data
for i in range(1,41):
    url = "https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={}".format(i)
    r = requests.get(url)
    soup = bs(r.content,'html.parser')



#### ALL FEATURES
    all_product_features = soup.find_all("div",attrs={"class":"_3ULzGw"})

    for product_features in all_product_features:
        features = product_features.find_all("li",attrs={"class":"tVe95H"})
        
        names = soup.find_all("div",attrs={"class":"_3wU53n"})
        offer_prices = soup.find_all("div",attrs={"class":"_1vC4OE _2rQ-NK"})
        real_prices = soup.find_all("div",attrs={"class":"_3auQ3N _2GcJzG"})

        k = 0
        
        if len(features)>=5:
            ## NAME
            name = str(names[k])
            name = name.split(">")[1].split("<")[0]
            name_list.append(name)
            
            ## OFFER_PRICE
            offer_price = str(offer_prices[k])
            offer_price = offer_price.split(">")[1].split("<")[0]
            offer_price_list.append(offer_price)
            
            ## REAL PRICE
            real_price = str(real_prices[k])
            real_price = real_price.split("-->")[1].split("<")[0]
            real_price_list.append(real_price)
            
            ## STARS
            all_stars = soup.find_all("div",attrs={"class":"hGSR34"})
            stars = str(all_stars[k])
            stars = stars.split(">")[1].split("<")[0]
            stars_list.append(stars)
            
            ## REVIEWS
            all_ratings = soup.find_all("span",{"class":"_38sUEc"})
            rating = str(all_ratings[k])
            rating = rating.split("<span>")[2].split(" R")[0].replace(",",'')
            no_of_rating_list.append(rating)
            
            
            #FEATURE LIST
            for feature in features:
                try:
                    if feature == features[0]: ## RAM ROM AND EXPANDIBILITY feature[0]
                        feature = str(feature)
                        
                        ## FOR EXPANDABLE MEMORY DATA
                        if "Expandable" in feature:
                            expandable = feature.split("Upto ")[1].split("<")[0]
                            expandable_upto_list.append(expandable) 
                            print("\n\n EXPANDABLE --- {} \n".format(expandable))
                        else:
                            expandable_upto_list.append("NOT EXPANDABLE/NOT GIVEN")
                            print("\n Not Expandable \n ")

                        ## FOR RAM DATA
                        if "RAM" in feature:
                            ram = feature.split(" RAM")[0].split(">")[1]
                            ram_list.append(ram)
                            print("\n RAM --- {} \n".format(ram))
                        else:
                            ram_list.append("NO RAM")
                            print("\n NO RAM \n ")

                        ## FOR ROM DATA
                        try:
                            if "ROM" in feature:
                                rom = feature.split(" ROM")[0].split("| ")[1]
                                rom_list.append(rom)
                                print(rom)
                            else:
                                rom_list.append("NO ROM")
                                print("\n NO ROM \n ")
                        except:
                                rom = feature.split(" ROM")[0].split(">")[1]
                                rom_list.append(rom)
                                print("\n ROM ---- {} \n ".format(rom))

                    ### SCREEN DATA
                    elif feature == features[1]:
                        feature = str(feature)
                        try:
                            screen = feature.split(">")[1].split(" cm")[0]
                            screen_list.append(screen)
                            print("\n SCREEN --- {} \n ".format(screen))
                        except:
                            screen_list.append("NaN")
                            print("\n SCREEN --- > NaN \n")

                    elif feature == features[2]:
                        feature = str(feature)

                        ## FOR REAR CAMERA
                        if "Rear" in feature:
                            rear_cam = feature.split(">")[1].split(" Rear")[0]
                            rear_cam_list.append(rear_cam)
                            print("\n REAR CAM --- {} \n".format(rear_cam))
                        else:
                            rear_cam = feature.split(">")[1].split(" |")[0]
                            rear_cam_list.append(rear_cam)
                            print("\n REAR CAM --- {} \n".format(rear_cam))

 
                    elif feature == features[3]:
                        feature = str(feature)

                        if "mAh" in feature:
                            battery = feature.split(">")[1].split("mAh")[0]
                            battery_list.append(battery)
                            print("\n Battery --- {} \n".format(battery))
                        else:
                            battery_list.append("NaN")
                            print(" \n Battery --- NaN \n")

                    elif feature == features[4]:
                        feature = str(feature)

                        if "Processor" in feature:
                            processor = feature.split(">")[1].split("<")[0]
                            processor_list.append(processor)
                            print("\n PROCESSOR --- {} \n".format(processor))
                        else:
                            processor_list.append("No Processor")
                            print("NO Processor")

                except:
                    pass

        else:
            k=k+1

## MAKING DATAFRAME

import pandas as pd

df = pd.DataFrame({"Name":name_list,"RAM":ram_list,"ROM":rom_list,"Processor":processor_list,"Rear_Cam":rear_cam_list,"Battery":battery_list,
                    "Screen_cms":screen_list,"Real Price":real_price_list,"Offer Price":offer_price_list,"Stars":stars_list,'No of Ratings':no_of_rating_list})

## CONVERTING DATAFRAME TO A CSV FILE FOR FURTHER ANALYSIS

df.to_csv("E:/Python files/FlipCart Data Scrape/phone_data.csv",index=False)



