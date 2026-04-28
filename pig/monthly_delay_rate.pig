dataset_raw = LOAD '/198*.csv' USING PigStorage(',') AS (Year:chararray, Month:chararray, DayofMonth:chararray, DayOfWeek:chararray, DepTime:chararray, CRSDepTime:chararray, ArrTime:chararray, CRSArrTime:chararray, UniqueCarrier:chararray, FlightNum:chararray, TailNum:chararray, ActualElapsedTime:chararray, CRSElapsedTime:chararray, AirTime:chararray, ArrDelay:chararray, DepDelay:chararray, Origin:chararray, Dest:chararray, Distance:chararray, TaxiIn:chararray, TaxiOut:chararray, Cancelled:chararray, CancellationCode:chararray, Diverted:chararray, CarrierDelay:chararray, WeatherDelay:chararray, NASDelay:chararray, SecurityDelay:chararray, LateAircraftDelay:chararray);

valid = FILTER dataset_raw BY Year != 'Year' AND Month IS NOT NULL AND Month != '';

mo_raw = FOREACH valid GENERATE (int)Month AS M,
    (((ArrDelay IS NOT NULL AND ArrDelay != 'NA' AND (float)ArrDelay > 0) OR
      (DepDelay IS NOT NULL AND DepDelay != 'NA' AND (float)DepDelay > 0)) ? 1 : 0) AS IsDelay;

mo_grp = GROUP mo_raw BY M;

mo_rate = FOREACH mo_grp {
    total = COUNT(mo_raw);
    dlay = SUM(mo_raw.IsDelay);
    GENERATE group AS Month, (double)dlay/(double)total AS DelayRate;
};

rmf /q_month_delay_rate;
STORE mo_rate INTO '/q_month_delay_rate' USING PigStorage(',');
