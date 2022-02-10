# Setup


## Info
Due to company security (shorewall) I was not able to fully  test `docker-compose` file. 
Please check configuration file and setup variables accordingly (see `/etl/conf/config.ini`).
Additionally I added inside docker-compose file `network_mode: host` property to make it works
no my linux machine.
Below instructions assumes that there is no security challange when it comes to setup docker-compose.


## Run 
1. Make sure `data` folder is owned by `4096` user.
2. Run command: `docker-compose build`
3. Run command: `docker-compose up`
4. See logs or go to pgadmin service to check loaded data.


## Structure

| File                  | Description |
| ----------------------| ------------- |
| db.init-db.sql        | Db initializing script |
| etl/conf/config.ini   | Configuration script   |
| etl/helper/helper.py  | Helpers functions      |
| data/raw_urls.csv     | Data                   |
