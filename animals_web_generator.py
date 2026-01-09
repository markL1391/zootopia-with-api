import json

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
    animals_data = fetch_animals_from_api("Fox")
    template_html = load_template("animals_template.html")


    # Replace placeholder in template
    animals_info = generate_animals_info(animals_data)
    final_html = template_html.replace("__REPLACE_ANIMALS_INFO__", animals_info)

    # Write final HTMl file
    write_html("animals.html", final_html)

if __name__ == "__main__":
    main()