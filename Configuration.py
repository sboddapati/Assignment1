import configparser
import json
import os
from flask import Flask, jsonify

# nitialize Flask app
app = Flask(__name__)

# configuration file path
CONFIG_FILE = "config.ini"
OUTPUT_JSON = "config_output.json"

def parse_config_file(file_path):
    
   #Parse the configuration file and store values in a dictionary
   #:param file_path: Path to the configuration file
   #return: Dictionary containing parsed key-value pairs
   
    config = configparser.ConfigParser()
    data = {}
    
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError("Configuration file not found! ")
        
        config.read(file_path)
        for section in config.sections():
            data[section] = {key: value for key, value in config.items(section)}
        
        # Save parsed data as JSON
        with open(OUTPUT_JSON, "w") as json_file:
            json.dump(data, json_file, indent=4)
        
        print("Configuration file parsed and saved successfully!")
        return data
    except Exception as e:
        print(f"Error reading config file: {e}")
        return {}

@app.route("/get-config", methods=["GET"])
def get_config():
    # Define an API endpoint to fetch configuration data
    #return: JSON response containing the configuration data
    
    try:
        with open(OUTPUT_JSON, "r") as json_file:
            data = json.load(json_file)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": f"Failed to load config: {e}"})

if __name__ == "__main__":
    # Parse config file and start Flask server
    parse_config_file(CONFIG_FILE)
    print(" Starting Flask server on http://127.0.0.1:5000")
    app.run(debug=True)
