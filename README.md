# Dino
There is a CSV file with raw data of user’s requests to a server for one day.
https://drive.google.com/file/d/0B8K6jIyGsfV-VGs1VkU1cnJ0NUk/view?usp=sharing
Each request has timestamp(ts), api name(api_name) , http method(mtd) and response http code(cod).
You need to implement two scripts using Python.
First script should generate a metric and upload it to MySQL DB from this raw data.
Metric description:
                Count of response with 5xx http code for each api_name*http_method pair for each 15 min.
SQL table should have following fields:
                timeframe_start, api_name, http_method, count_http_code_5xx, is_anomaly
Second one should find, and mark anomaly metric based on its statistic distribution.
Anomaly detection algorithm:
                Assume that the metric for each api_name*http_method pair belongs to normal distribution,
                If value of metric is outside of plus 3th-sigma (3σ) range, mark value as anomaly.
Please upload description and scripts to GitHub and provide a link to us.
