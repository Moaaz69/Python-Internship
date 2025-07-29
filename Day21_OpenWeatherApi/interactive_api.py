import requests
import json
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

API_KEY = "bf6b07c4f5c07ed0653e73b7ea56592f"  # Replace with your actual key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

console = Console()
last_result = None  # Stores last API result globally


def get_weather(city):
    try:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        console.print(f"[red]Error fetching weather: {e}[/red]")
        return None


def display_weather(data):
    try:
        city = data["name"]
        country = data["sys"]["country"]
        weather = data["weather"][0]["description"].title()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        table = Table(title="📍 Weather Report", show_lines=True)
        table.add_column("Field", style="cyan", no_wrap=True)
        table.add_column("Value", style="magenta")

        table.add_row("City", f"{city}, {country}")
        table.add_row("Weather", weather)
        table.add_row("Temperature", f"{temp}°C")
        table.add_row("Humidity", f"{humidity}%")
        table.add_row("Wind Speed", f"{wind_speed} m/s")

        console.print(table)

    except KeyError:
        console.print("[red]Invalid data format received from API.[/red]")


def save_to_file(data):
    try:
        with open("weather_result.json", "w") as f:
            json.dump(data, f, indent=4)
        console.print("[green]✅ Weather data saved to 'weather_result.json'[/green]")
    except Exception as e:
        console.print(f"[red]Error saving file: {e}[/red]")


def main():
    global last_result

    console.print(Panel.fit("🌦️ [bold blue]Welcome to OpenWeather CLI[/bold blue] 🌦️", style="bold white"))

    while True:
        console.print("\n[bold yellow]=== OpenWeather CLI ===[/bold yellow]")
        console.print("1. 🌍 Get weather by city")
        console.print("2. 💾 Save last result to file")
        console.print("3. ❌ Exit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            city = input("Enter city name: ").strip()
            data = get_weather(city)
            if data:
                display_weather(data)
                last_result = data
        elif choice == "2":
            if last_result:
                save_to_file(last_result)
            else:
                console.print("[red]No weather data to save. Please fetch data first.[/red]")
        elif choice == "3":
            console.print("[bold green]Goodbye! Stay weather-aware ☁️[/bold green]")
            break
        else:
            console.print("[red]Invalid choice. Please select 1, 2, or 3.[/red]")


if __name__ == "__main__":
    main()
