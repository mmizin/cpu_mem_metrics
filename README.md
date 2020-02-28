# cpu_mem_metrics
This script helps you to get CPU and memory information

## Getting Started

These instructions will tell you how to run our script to find out basic information of your machine

### Prerequisites

You don't need to install any additional components or soft

## Running the bash script 

Open terminal and go to the work directory

```angular2
chmod +x metrics  #assign execute permission to a file

```
Get information about CPU run command
```angular2
./metrics cpu
```

Get information about memory run command
```angular2
./metrics mem
```

## Running the python script 
Open terminal and go to the work directory  
Create python virtual environment
```angular2
python -m venv venv
```
Activate virtual environment   
```angular2
source venv/bin/activate
```
Install dependencies from requirements.txt file
```angular2
pip install -r requirements.txt 
```
Get information about CPU run command
```angular2
python metrics.py cpu
```

Get information about memory run command
```angular2
python metrics.py mem
```

## Authors

* **Mykola Mizin** - *Initial work* 
