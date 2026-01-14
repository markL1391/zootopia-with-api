# Zootopia with API

This project generates a simple animal information website based on data fetched from an external API.
The user can enter the name of an animal, and the program will generate an HTML page displaying
information about matching animals.

The project demonstrates the separation of concerns by splitting the application into two main parts:
- A data fetcher that retrieves animal data from an API
- A website generator that creates the HTML output based on the fetched data

---

## Installation

1. Clone the repository:

    
    git clone https://github.com/markL1391/zootopia-with-api


2. Navigate to the project directory:

    
    cd Zootopia-with-API 


3. Install the required dependencies:


    pip install -r requirements.txt

4. Create a `.env` file in the root directory and add your API key:

    
    API_KEY=your_api_key_here

## Usage

Run the website generator and follow the prompt:

    python3 animals_web_generator.py

Enter the name of an animal when prompted.  
The program will generate an `animals.html` file containing the results.

If no animals are found, a friendly message will be displayed instead.

## Contributing

This project was created as part of a learning exercise.
Contributions are welcome, but please keep the existing structure and coding style.