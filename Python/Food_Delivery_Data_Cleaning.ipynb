import pandas as pd

df = pd.read_csv("Food Delivery.csv")

#1. Remove Duplicate Records

df = df.drop_duplicates()

#2. Handle missing Customer_Rating

df["Customer_Rating"] = df["Customer_Rating"].replace(0, np.nan)

#3. Handle missing Delivery_Time

df["Delivery_Time"] = df["Delivery_Time"].replace(0, np.nan)

#4. Clean extra spaces in City

df ["City"] = df["City"].str.strip()

#5. Standardize City names

df["City"] = df["City"].str.title()

#6. Standardize Payment Method values

df["Payment_Method"] = df["Payment_Method"].str.upper()

#7. Clean the currency symbol from Order_Values

df["Order_Value"] = df["Order_Value"].str.replace("?","").str.replace(",","").astype(float)

#8. Cnvert Order_Value to numeric

df["Order_Value"] = pd.to_numeric(df["Order_Value"])

#9. Check and handle invalid Delivery_Time

df["Delivery_Time"] = df["Delivery_Time"].replace(-5,None)
df["Delivery_Time"] = df["Delivery_Time"].fillna(df["Delivery_Time"].median())

#10. Convert Order_Date to proper date format

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

#11. Check Customer_Rating for invalid values

Missing Customer_Rating values were retained as NaN because imputing a rating could introduce artificial customer feedback and affect customer
satisfaction analysis.

#12. Export cleaned dataset

df.to_csv("Food_Delivery_Cleaned.csv", index=False)
