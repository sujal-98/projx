import os
import numpy as np
from helper.ocr import getOCR
# from helper.parse import getItems
# from helper.dataset_map import get_index
# from helper.food_predict import get_food_info

# Path to the directory containing JPG files
directory = os.path.join(os.getcwd(), "data", "data_jpg")
# Iterate through files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        print(filename)
        with open(os.path.join(directory, filename), 'rb') as document:
            data = getOCR(document)
            print(data);
            # items, prices, total = getItems(data)

            # foods_index = get_index(items)
            # food_data = get_food_info(foods_index)
            # food_data['price'] = np.array(prices)

            # # Uncomment the below lines if you want healthy/unhealthy prices
            # healthy = food_data.loc[food_data['healthy'] == 'yes', 'price'].sum()
            # unhealthy = food_data.loc[food_data['healthy'] == 'no', 'price'].sum()

            # print(food_data)
            # print()
            # print("Healthy: $" + str(healthy))
            # print("Unhealthy: $" + str(unhealthy))
            # print("Ratio: " + str(healthy / (healthy + unhealthy))[:4])
            # print()