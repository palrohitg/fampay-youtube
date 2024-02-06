# :metal:	Fampay Youtube
- Fampay Youtube Service helps you fetch latest video's thumbnail with some other details.  
- There will be one perodic job, that will update the latest videos, add new video in databases;


## High Level Design: 
![LogService](https://github.com/palrohitg/logservice/assets/40069230/453bdaae-9c19-4fac-8232-b9f116a95de9)

## :computer: Tech Stack
    
* [Django](https://www.django-rest-framework.org/)
* [Postgres](https://www.postgresql.org//)
* [Python](https://www.python.org/)
* [Docker](https://www.docker.com/)



## :running_woman: Local Installation Guide : 

1. Clone the repository by using Git Client: 

         git clone https://github.com/palrohitg/fampay-youtube.git

2. To Setup and Run Application + DataBase + CRON: 

        chmod +x application_container_start.sh
        ./application_container_start.sh




## CURL Request Response 

1. Get Video Details 
```commandline
curl --location 'http://localhost:9002/api/details' \
--header 'Cookie: csrftoken=jH2qzTXI1DfSRW01HlHj0mJq49lqiMJ5BAGf6pZKhIfiz6YoLim14bD6V06tde7v'
```

2. Create API Key 
```commandline
curl --location 'http://localhost:8000/api/create-key' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=jH2qzTXI1DfSRW01HlHj0mJq49lqiMJ5BAGf6pZKhIfiz6YoLim14bD6V06tde7v' \
--data '{
    "key" : "testing"
}'
```

## 📜 LICENSE

  [MIT](https://github.com/palrohitg/fampay-youtube.git) 