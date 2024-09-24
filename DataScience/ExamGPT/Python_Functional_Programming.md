## Q1: Exercise 1: Analyzing Healthcare Data with Functional Programming

**Background:**  
You have a dataset that includes patient information for a clinical study. Each entry in the dataset is a tuple containing the patient's ID, age, diagnosis (either "Healthy" or "Disease"), and blood pressure readings as a list of integers.

**Dataset Example:**

```python
patients = [
    (101, 29, "Healthy", [120, 80, 118, 82]),
    (102, 47, "Disease", [140, 90, 135, 89]),
    (103, 35, "Healthy", [115, 75, 117, 76]),
    (104, 62, "Disease", [160, 100, 158, 99]),
    # Add more patients as needed
]
```

### Tasks:

1. **Filter Healthy Patients:**  
   Write a function using list comprehension and a lambda function to filter out and return only the healthy patients from the dataset.

   **Answer:**
   ```python
   healthy = list(filter(lambda x: x[2] == "Healthy", patients))
   print(healthy)
   ```

2. **Calculate Average Blood Pressure:**  
   Using a lambda function, write a code snippet that calculates the average systolic blood pressure (first number in each reading) for all patients. Use the `map()` function to apply the lambda function across the dataset.

   **Answer:**
   ```python
   avgSystolic = list(map(lambda x: (x[3][0] + x[3][2]) / 2, patients))
   print(avgSystolic)
   ```

3. **Identify High-Risk Patients:**  
   Define "high-risk" patients as those with any systolic blood pressure reading over 140. Write a function using list comprehension and a lambda function to filter out and return a list of high-risk patient IDs.

   **Answer:**
   ```python
   isRisk = lambda x: x[3][0] > 140 or x[3][2] > 140
   risky = [x[0] for x in patients if isRisk(x)]
   print(risky)
   ```

4. **Sort Patients by Age:**  
   Use the `sorted()` function with a lambda function to sort the dataset by the age of the patients in descending order.

   **Answer:**
   ```python
   byAge = sorted(patients, key=lambda x: x[1], reverse=True)
   print(byAge)
   ```

---

## Q2: Exercise 2: Marketing Analytics with Functional Programming

**Background:**  
You have a dataset containing marketing campaign data for a series of products. Each entry in the dataset is a dictionary with the following key-value pairs: `product_id` (integer), `campaign_name` (string), `region` (string), `sales` (integer), and `returns` (integer).

**Dataset Example:**

```python
campaign_data = [
    {"product_id": 1, "campaign_name": "Summer Sale", "region": "North", "sales": 150, "returns": 5},
    {"product_id": 2, "campaign_name": "Winter Fest", "region": "South", "sales": 200, "returns": 20},
    {"product_id": 3, "campaign_name": "Summer Sale", "region": "East", "sales": 180, "returns": 15},
    {"product_id": 4, "campaign_name": "Monsoon Magic", "region": "West", "sales": 250, "returns": 10},
    # More products can be added as needed
]
```

### Tasks:

1. **Group Sales by Campaign:**  
   Write a function using `reduce()` from `functools` and a lambda function to accumulate total sales for each campaign.

   **Answer:**
   ```python
   done = []
   total_sales = {}
   for data in campaign_data:
       if data["campaign_name"] in done:
           continue
       done.append(data["campaign_name"])
       perCampaign = [x for x in campaign_data if x["campaign_name"] == data["campaign_name"]]
       total = reduce(lambda acc, x: acc + x["sales"], perCampaign, 0)
       total_sales[data["campaign_name"]] = total
   print(total_sales)
   ```

2. **Calculate Return Rate:**  
   Use a combination of `map()` and `filter()` to calculate the return rate (returns divided by sales) for each product. Exclude any products with zero sales.

   **Answer:**
   ```python
   notZero = list(filter(lambda x: x["sales"] > 0, campaign_data))
   getRate = lambda x: x["returns"] / x["sales"]
   returnRates = list(map(lambda x: (x["product_id"], getRate(x)), notZero))
   print(returnRates)
   ```

3. **Max Sales Product:**  
   Use the `max()` function with a lambda to determine the product with the highest sales in a given region.

   **Answer:**
   ```python
   def maxPerRegion(region):
       perRegion = [x for x in campaign_data if x["region"] == region]
       maximum = max(perRegion, key=lambda x: x["sales"])
       return maximum
   ```

4. **Campaign Effectiveness:**  
   Define a metric "effectiveness" as \((\text{sales} - \text{returns}) / \text{sales}\). Write a function using list comprehension to calculate and return a list of all campaigns where the effectiveness is above 90%.

   **Answer:**
   ```python
   effectiveness = lambda x: (x["sales"] - x["returns"]) / x["sales"]
   effective = [x for x in campaign_data if effectiveness(x) > 0.9]
   print(effective)
   ```

---

## Q3: Exercise 3: Weather Analytics with Functional Programming

**Background:**  
You have a dataset containing weather data recorded over a week at various locations. Each entry in the dataset is a dictionary with the following key-value pairs: `day` (string), `location` (string), `temperature` (float in Celsius), `humidity` (percentage), and `wind_speed` (km/h).

**Dataset Example:**

```python
weather_data = [
    {"day": "Monday", "location": "CityA", "temperature": 22.5, "humidity": 45, "wind_speed": 15},
    {"day": "Monday", "location": "CityB", "temperature": 18.0, "humidity": 55, "wind_speed": 10},
    {"day": "Tuesday", "location": "CityA", "temperature": 24.0, "humidity": 50, "wind_speed": 20},
    {"day": "Tuesday", "location": "CityB", "temperature": 20.0, "humidity": 60, "wind_speed": 8},
    # More entries can be added as needed
]
```

### Tasks:

1. **Generate Temperature Differences:**  
   Write a generator expression to calculate the temperature difference for each location from one day to the next. Only consider consecutive days for the same location.

   **Answer:**
   ```python
   def getDiffs():
       days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
       done = []
       diffs = []
       for data in weather_data:
           if data["location"] in done:
               continue
           done.append(data["location"])
           gen = (x for x in weather_data if x["location"] == data["location"])
           Consecs = list(filter(lambda x, y: days.index(y["day"]) - days.index(x["day"]) == 1 or 
                                   days.index(y["day"]) - days.index(x["day"]) == -6, gen))
           diff = Consecs[1]["temperature"] - Consecs[0]["temperature"]
           diffs.append((data["location"], diff))
       return diffs
   ```

2. **Humidity Sorted by Wind Speed:**  
   Use `sorted()` with `map()` to list all humidity readings sorted by increasing wind speed.

   **Answer:**
   ```python
   tups = list(map(lambda x: (x["wind_speed"], x["humidity"]), weather_data))
   byWind = sorted(tups, key=lambda x: x[0])
   for i in range(len(byWind)):
       print(byWind[i][1])  # It is asking for the humidity only as output
   ```

3. **Average Temperature:**  
   Calculate the average temperature across all data points using `reduce()` from `functools`.

   **Answer:**
   ```python
   def getAvg():
       total = reduce(lambda acc, x: x["temperature"] + acc, weather_data, 0)
       return total / len(weather_data)

   print("The average temperature is", getAvg())
   ```

4. **Most Stable Weather Location:**  
   Define stability of weather by the least variation in temperature throughout the week.

   **Answer:**
   ```python
   done = []
   diffs = []
   for data in weather_data:
       if data["location"] in done:
           continue
       done.append(data["location"])
       perCity = [x for x in weather_data if x["location"] == data["location"]]
       diffs.append((data["location"], perCity[1]["temperature"] - perCity[0]["temperature"]))

   minimum = min(diffs, key=lambda x: x[1])
   print(minimum)
   ```
```
