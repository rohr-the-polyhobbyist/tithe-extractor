'''
These functions help with working with data from the Scryfall API.
'''
def save_card_data_unzipped(response, DATA_CACHE_DIR=None, file_name='card_data.json'):
    """Save the unzipped card data to a file.

    Args:
        response (response.request): The response object from the request.
        path (str): The path to save the file to.
    """
    import json, os
    if DATA_CACHE_DIR is None:
        from tithe_extractor.constants import DATA_CACHE_DIR
    
    file_path = os.path.join(DATA_CACHE_DIR, file_name)
    with open(file_path, "w+", encoding="utf-8") as f:
        for item in response.json():
            json.dump(item, f)
            f.write("\n")
        print("Card data saved to unzipped file.")
    return None
def load_card_unzipped_data(file_name, DATA_CACHE_DIR=None):
    """Load the unzipped card data from the Scryfall API.

    Args:
        file_name (str): The name of the file to load.
        DATA_CACHE_DIR (str): The directory to load the file from.

    Returns:
        card_data (dict): The card data.
    """
    import os
    import json
    if DATA_CACHE_DIR is None:
        from tithe_extractor.constants import DATA_CACHE_DIR
    if file_name is None:
        raise ValueError("You must provide a file name.")
    
    file_path = os.path.join(DATA_CACHE_DIR, file_name)

    if not os.path.exists(file_path):
        raise FileNotFoundError("File does not exist.")
    
    # create a list to store extracted json objects
    extracted_objs = []
    err_count = 0
    line_count = 0
    # open the file in read mode
    with open(dpath, 'rt') as file:
        # Iterate over each line
        for line in file:
            # Parse the JSON object from the current line
            try:
                json_obj = json.loads(line)
                extracted_objs.append(json_obj)
                line_count += 1
            except json.JSONDecodeError:
                print('Line is not a valid JSON object')
                err_count += 1
    print(f"Extracted {line_count} JSON objects with {err_count} errors.")

    return extracted_objs