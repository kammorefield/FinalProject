import json, requests

def main():
  base_url = "https://api.openweathermap.org/data/2.5/weather"
  appid = "ec755a1ad64926efccaaf4a6b108d079"
  city = input("Please enter a city or zip code: ")

  #Check if the entered data is valid to proceed
  if city.isnumeric() or city.isalpha():
    url = f"{base_url}?q={city}&units=imperial&APPID={appid}"
    print()

    #Establish connection and send request
    #!!!Find out how to configure try/except statement for checking connection!!!
    response = requests.get(url)
    unformated_data = response.json()

    forecast(unformated_data)

    #Ask the user if they would like to run the program again
    global choice
    choice = input("Do you want to enter another location Please type 'Y' for yes and 'N' for no: ").upper()
    print()
  else:
    print("The data you entered is not valid. Please try again.")
    print()


#Define function to retrieve and print the forecast variables
def forecast(data):
  temp = data["main"]["temp"]
  print(f"The temperature is {temp} degrees.")

  feels_like = data["main"]["feels_like"]
  print(f"It feels like {feels_like} degrees.")
  
  temp_max = data["main"]["temp_max"]
  print(f"The maximum temperature is {temp_max} degrees.")

  humidity = data["main"]["humidity"]
  print(f"The humidity level is {humidity}.")

  wind_speed = data["wind"]["speed"]
  print(f"The wind speed is {wind_speed} mph.")


#Loop to allow program to run multiple times
#!!!Exiting only works when the program is run an odd number of times. Fix this!!!
again = True
while again:
  main()
  if choice == 'Y':
    main()
  elif choice == 'N':
    print("Goodbye!")
    break