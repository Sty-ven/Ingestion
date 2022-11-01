{{
    config(materilaized="view")
}}

select
    --location
    cast("Country_Region" as text) as Country,
    cast("Lat" as float) as Latitude,
    cast("Long_" as float) as Longitude,

    --datetime
    cast("Last_Update" as timestamp) as Last_update,

    --covid details
    cast("Confirmed" as integer) as Confirmed,
    cast("Deaths" as integer) as Deaths,
    cast("Recovered" as integer) as Recovered,
    cast("Active" as integer) as Active,
    cast("Incident_Rate" as float) as Incident_Rate,
    cast("Case_Fatality_Ratio" as float) as Fatality_Ratio


from {{ source('staging', 'covid_data') }} 
limit 100
