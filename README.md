# Weather Forecasting Project
 Made by [Masa Aladwan](https://github.com/MasaAladwan) and [Mohammad Moataz](https://github.com/MohammadMoataz2)

## Overview
This project aims to provide accurate weather forecasting for various cities in Jordan. The project comprises data collection, model building, data visualization using Power BI, and a web interface for user interaction. Additionally, it integrates real-time data streaming from sensors for live updates.


![Blue and Yellow Modern Data Analysis Presentation (2)](https://github.com/MohammadMoataz2/DiabetesPlatform/assets/123085286/ee05fe5e-7863-45c3-b5dd-0bc17d97b6fa)

## Project Components

### 1. Data Collection
- **Source**: Meteostat API
- **Parameters Collected**: Temperature (temp), Pressure (pres), Wind Direction (wdir), Wind Speed (wspd), Date and Time (datetime)
- **Technology Used**: Python

### 2. Data Processing and Model Building
- **Cities Covered**: Various cities in Jordan
- **Models Developed**:
  - Temperature Prediction Model
  - Pressure Prediction Model
  - Wind Direction Prediction Model
  - Wind Speed Prediction Model
- **Input**: City and Date
- **Output**: Predicted values for Temperature, Pressure, Wind Direction, and Wind Speed
- **Libraries Used**: 
  - `scikit-learn` for building machine learning models
  - `pandas` for data manipulation


### 3. Web Interface
- **Framework**: FastAPI
- **Features**:
  - User form to input City and Date
  - Display forecasted weather values
  - Two main buttons:
    1. **Dashboard**: Redirects to the Power BI dashboard displaying historical and forecasted data
    2. **Real-Time Data Streaming**: Displays real-time data from sensors

![image](https://github.com/MohammadMoataz2/DiabetesPlatform/assets/123085286/5529bd38-1616-4644-8537-720fe39f5e25)


### 4. Data Visualization
- **Tool Used**: Power BI
- **Features**:
  - Interactive dashboard
  - Date range selection from 1999 to 2023
  - City-specific weather data visualization


![image](https://github.com/MohammadMoataz2/DiabetesPlatform/assets/123085286/2be46415-c244-48b9-b5ca-75ca805572cf)


### 5. Real-Time Data Integration
- **Sensors Used**:
  - Ultrasonic Sensor HC-SR04
  - DHT11 Humidity & Temperature Sensor
- **Technology Stack**:
  - **Node-RED**: For data collection and processing from sensors
  - **Power BI**: For real-time data visualization
- **Functionality**:
  - Node-RED collects data from sensors
  - Processes data and feeds it into the pipeline
  - Sends processed data to Power BI for real-time dashboard updates

![2024-05-1920-05-15-ezgif com-video-to-gif-converter](https://github.com/MohammadMoataz2/DiabetesPlatform/assets/123085286/50752fa0-796f-4adc-b527-9a209e08f2b9)

![image](https://github.com/MohammadMoataz2/DiabetesPlatform/assets/123085286/c36c39c9-fa47-4ce4-bb88-de467736f10c)

![circ_photo](https://github.com/MohammadMoataz2/DiabetesPlatform/assets/123085286/f5c03024-2344-42cc-b0e6-cfae11c32ef9)



## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/MohammadMoataz2/WeatherForecasting.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:

    - **main.html**
    - **main.py** --> python -m uvicorn main:app --reload

2. Input your information to predict the Weather.