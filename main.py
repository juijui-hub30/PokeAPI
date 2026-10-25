import random
import requests

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower().strip()}"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()
            return {
                "name": data["name"].capitalize(),
                "height": data["height"],
                "weight": data["weight"],
            }
        elif response.status_code == 404:
            print(f"Error: Pokémon '{pokemon_name}' not found in PokeAPI database.")
            return None
        else:
            print(f"Server Error: Received status code {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Network Error: Could not connect to PokeAPI. ({e})")
        return None


def start_game():
    pokemon_pool = ["pikachu", "charizard", "bulbasaur", "squirtle", "eevee", "mewtwo", "lucario"]
    print("==================================================")
    print("        WELCOME TO THE POKEAPI GUESSING GAME      ")
    print("==================================================")
    print("Fetching game data from PokeAPI... Please wait.\n")

    target_name = random.choice(pokemon_pool)
    pokemon_stats = fetch_pokemon_data(target_name)

    if not pokemon_stats:
        print("Failed to start the game due to an API or network issue.")
        return

    print("I am thinking of a Pokémon with the following attributes:")
    print(f" -> Height: {pokemon_stats['height']}")
    print(f" -> Weight: {pokemon_stats['weight']}")
    print("\nCan you guess which Pokémon it is?")
    attempts = 3

    for attempt in range(1, attempts + 1):
        guess = input(f"\nAttempt {attempt}/{attempts} - Enter your guess: ").strip()
        if not guess:
            print("Invalid input. Please type a valid Pokémon name.")
            continue
        if guess.lower() == pokemon_stats["name"].lower():
            print("\n🎉 CONGRATULATIONS! YOU WIN! 🎉")
            print(f"Excellent job! It was indeed {pokemon_stats['name']}.")
            break
        else:
            print("Incorrect guess!")
    else:
        print(f"You've run out of attempts. The correct Pokémon was: {pokemon_stats['name']}.")

if __name__ == "__main__":
    start_game()