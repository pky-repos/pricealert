### Price Alert

## Steps to run/test project
* `docker-compose up --build`
* Open http://127.0.0.1:8000/swagger/
* Create price alert for 'btc' when it touches 56500 by posting the following on http://127.0.0.1:8000/api/alerts/ - 
{
  "symbol": "btc",
  "price_limit": 56500,
  "lower_higher": "h"
}
* Look at the logs `docker-compose logs` to see alerts getting triggered every 60 seconds
* See all alerts on http://127.0.0.1:8000/api/alerts/
* Filter alerts based on 'symbol' and/or 'status'
* Search alerts 
* Delete alerts
