import json
import data_fetcher
BASE_URL = "https://api.api-ninjas.com/v1/animals"#

def fetch_animals_from_api(animal_name: str):
    api_key = os.getenv("API_NINJAS_KEY")

    response = requests.get(
        BASE_URL,
        params={"name": animal_name},
        headers={"X-Api-Key": api_key}
    )
    data = response.json()
    return data

def load_data(file_path):
  """ Loads a JSON file and return its content. """
  with open(file_path, "r") as handle:
    return json.load(handle)

def load_template(file_path):
    """ Loads and returns the HTML template. """
    with open(file_path, "r") as file:
        return file.read()

def write_html(file_path, content):
    """ Writes the given content to an HTML file. """
    with open(file_path, "w") as file:
        file.write(content)

def add_if_exists(source_dict, key, label):
    """ Returns a formatted list item if key exists in source_dict, else empty string. """
    if key in source_dict:
        return ('<li class="card__list-item">'
                  f"<strong>{label}:</strong> {source_dict[key]}</li>\n")
    return ""

def serialize_animal(animal):
    """Serializes a single animal object into an HTML list item."""
    # Animal info string
    output = ""
    output += '<li class="cards__item">'

    # Title.
    if "name" in animal:
        output += f'<div class="card__title"> {animal["name"]}</div>\n'

    output += '<div class="card__text">\n'
    output += '<ul class="card__list">\n'

    characteristics = animal.get("characteristics", {})
    taxonomy = animal.get("taxonomy", {})

    # Diet.
    output += add_if_exists(characteristics, "diet", "Diet")
    # Type.
    output += add_if_exists(characteristics, "type", "Type")
    # Scientific name.
    output += add_if_exists(taxonomy, "scientific_name", "Scientific name")
    # Lifespan.
    output += add_if_exists(characteristics, "lifespan", "Lifespan")
    # Color.
    output += add_if_exists(characteristics, "color", "Color")


    # Locations (first one).
    if "locations" in animal and len(animal["locations"]) > 0:
        output += ('<li class="card__list-item">'
                   f"<strong>Locations:</strong> {animal['locations'][0]}</li>\n")

    output += '  </ul>\n'

    # Slogan
    if "slogan" in characteristics:
        output += f'<p class="card__slogan">{characteristics["slogan"]}</p>\n'

    # Close text container and card.
    output += '  </div>\n'
    output += '</li>\n'

    return output

def generate_animals_info(animals_data):
    """ Generates HTML for all animals. """
    animals_info = ""
    for animal in animals_data:
        animals_info += serialize_animal(animal)
    return animals_info


def main():
    """
    This program generates an HTML file displaying information about various animals
    by loading data from a JSON file and populating an HTML template.
    """

    # Load animal data.
    animal_name = input("Enter a name of an animal: ").strip()
    animals_data = data_fetcher.fetch_data(animal_name)
    template_html = load_template("animals_template.html")


    # Replace placeholder in template depending on API reponse.
    if len(animals_data) == 0:
        animals_info = (f'<h2>We searched high and low, but the animal '
                        f'"<strong>{animal_name}</strong>" seems to be on vacation.<h2>'
                        f'<p>Maybe try another name?</p>'
                        )
    else:
        animals_info = generate_animals_info(animals_data)
    final_html = template_html.replace("__REPLACE_ANIMALS_INFO__", animals_info)

    # Write finial HTMl file
    write_html("animals.html", final_html)
    print("Website was successfully generated to the file animals.html.")

if __name__ == "__main__":
    main()