# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "d1b9e7b1-405a-4c6b-a7b3-f517963ce0d8",
# META       "default_lakehouse_name": "LH_Bronze",
# META       "default_lakehouse_workspace_id": "b067fcf2-7a3f-493a-bb7a-55aeb4d5c6ee",
# META       "known_lakehouses": [
# META         {
# META           "id": "d1b9e7b1-405a-4c6b-a7b3-f517963ce0d8"
# META         },
# META         {
# META           "id": "07189705-1a8c-42cc-b8ef-9a6e4c1a7ba8"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

from pyspark.sql.functions import round

# Load hardware sales CSV from Bronze Lakehouse
csv_path = "abfss://ComputerEquipmentSales_DevWorkspace@onelake.dfs.fabric.microsoft.com/LH_Bronze.Lakehouse/Files/dev_hardware_sales_data.csv"
df = spark.read.option("header", "true").option("inferSchema", "true").csv(csv_path)

# Add a new column "UnitPrice"
df_with_unit_price = df.withColumn("UnitPrice", round(df["Total"] / df["Quantity"], 2))

# Save as Delta Table in Silver Lakehouse
silver_lakehouse_path = "abfss://ComputerEquipmentSales_DevWorkspace@onelake.dfs.fabric.microsoft.com/LH_Silver.Lakehouse/Tables/dbo/hardware_sales"
df_with_unit_price.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save(silver_lakehouse_path)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
