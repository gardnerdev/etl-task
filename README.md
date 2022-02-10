# Setup

Due to company security (shorewall) I was not able to run fully `docker-compose` file. 
Because of that, I commented `etl` serivce, run docker compose and communicate with 
database using `localhost` as host (see /etl/conf/config.ini). Ideally host should be set to `dwh` 
Additionally I added inside docker-compose file `network_mode: host` property to make it works
no my linux machine.
Below instructions assumes that there is no security challange when it comes to setup docker-compose.


1. Make sure `data` folder is owned by '4096' user.
2. Run command: `docker-compose build`
3. Run command: `docker-compose up`
4. See logs or go to pgadmin to check loaded data.


