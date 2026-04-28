dataset_raw = LOAD '/198*.csv' USING PigStorage(',') AS (Year:chararray, Month:chararray, DayofMonth:chararray, DayOfWeek:chararray, DepTime:chararray, CRSDepTime:chararray, ArrTime:chararray, CRSArrTime:chararray, UniqueCarrier:chararray, FlightNum:chararray, TailNum:chararray, ActualElapsedTime:chararray, CRSElapsedTime:chararray, AirTime:chararray, ArrDelay:chararray, DepDelay:chararray, Origin:chararray, Dest:chararray, Distance:chararray, TaxiIn:chararray, TaxiOut:chararray, Cancelled:chararray, CancellationCode:chararray, Diverted:chararray, CarrierDelay:chararray, WeatherDelay:chararray, NASDelay:chararray, SecurityDelay:chararray, LateAircraftDelay:chararray);

valid = FILTER dataset_raw BY Year != 'Year' AND ArrDelay IS NOT NULL AND ArrDelay != 'NA' AND ArrDelay != '';

car_raw = FOREACH valid GENERATE UniqueCarrier AS Carrier, (float)ArrDelay AS Delay;
car_grp = GROUP car_raw BY Carrier;
car_avg = FOREACH car_grp GENERATE group AS Carrier, AVG(car_raw.Delay) AS AvgArr;

rmf /q_carrier_best5_arr;
STORE car_avg INTO '/q_carrier_best5_arr' USING PigStorage(',');
