from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd


def scrape_toyota_website():
    # Create an instance of the Chrome WebDriver
    driver = webdriver.Chrome()

    try:
        # Open the website / webpage
        driver.get('https://www.toyota.com/all-vehicles/')

        # Wait for the page to load
        time.sleep(5)

        # Find the cars grid element
        cars_grid = driver.find_element(By.CLASS_NAME, "vehicles-grid")

        # Find all the vehicle cards
        cars = cars_grid.find_elements(By.CLASS_NAME, "vehicle-card")

        # Initialize an empty list to store the extracted data
        data = []

        for car in cars:
            car_brand = car.get_attribute("data-aa-series-brand")
            car_name = car.get_attribute("data-series")
            car_price = car.get_attribute("data-basemsrp")
            model_year = car.get_attribute("data-year")

            # Append the data to the list
            data.append({'Brand': car_brand, 'Model': car_name, 'Year': model_year, 'Price': car_price})

        # Create a DataFrame from the extracted data
        df = pd.DataFrame(data)
        
        #check sample of the data 
        print(df.head())

        # Save the DataFrame to an Excel file
        df.to_excel('Toyota_cars_data.xlsx', index=False)

        # Print a success message
        print("Data extraction and saving completed successfully.")

    finally:
        # Close the current tab
        driver.close()

        # Quit the browser
        driver.quit()

if __name__ == "__main__":
    scrape_toyota_website()
