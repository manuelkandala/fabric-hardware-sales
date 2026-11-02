# Fabric Hardware Sales

A small data engineering project built in Microsoft Fabric as part of a course. It reads raw hardware sales data from a Bronze lakehouse, cleans it, adds a calculated column and saves the result as a Delta table in a Silver lakehouse.

## Architecture

```
CSV file (LH_Bronze, Files)  ->  PySpark notebook  ->  Delta table (LH_Silver, dbo.hardware_sales)
```

This follows the medallion pattern: raw data in Bronze, cleaned and structured data in Silver.

## What the notebook does

1. Reads the CSV file from the Bronze lakehouse with header and schema inference.
2. Removes duplicate rows with `dropDuplicates()`.
3. Adds a `UnitPrice` column calculated as `Total / Quantity`, rounded to two decimals.
4. Writes the result as a Delta table in the Silver lakehouse, schema `dbo`.
5. Reads the table back to verify the row count.

## Tech

- Microsoft Fabric (Lakehouse, Notebooks)
- PySpark and Spark SQL
- Delta Lake
- OneLake (ABFS paths)

## Data

Sample hardware sales data from the course. Columns: `Date`, `Category`, `Product`, `Quantity`, `Total`, plus the calculated `UnitPrice`.

## Notes

- The Silver lakehouse has schemas enabled, so the table path must include `dbo` (`Tables/dbo/hardware_sales`). Without it, Fabric treats the folder as a schema and shows it as "Unidentified".
- Workspace and lakehouse names are specific to my course environment and need to be changed to run the notebook elsewhere.

## Author

Manuel Kandala, [LinkedIn](https://www.linkedin.com/in/manuel-k-9362ab163/)
