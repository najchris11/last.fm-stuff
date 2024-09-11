# Last.fm Top 100 Album Selector

This Python project fetches the top 100 albums from your Last.fm profile and allows you to randomly select an album from the list. Once an album is selected, it is logged so it won't be picked again. The project also tracks changes in your top 100 albums and logs any new additions to the list, printing which albums were bumped out of the top 100.

## Features

- Fetches the top 100 albums from your Last.fm profile.
- Randomly selects an album that hasn't been picked yet.
- Logs selected albums in a JSON file to avoid repetition.
- Tracks changes in your top 100 albums and logs any new albums or those that were bumped.
- Configurable using a `mySecrets.py` file to store your Last.fm API key and username securely.

## Requirements

- Python 3.6+
- `requests` library

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/najchris11/last.fm-stuff.git
cd lastfm-album-selector
```

### 2. Create and Activate a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

#### On Windows:

```bash
python -m venv venv
.\venv\Scripts\activate
```

#### On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

With the virtual environment activated, install the required libraries:

```bash
pip install -r requirements.txt
```

### 4. Create Your `mySecrets.py` File

Copy the sample secrets file and update it with your Last.fm API key and username:

```bash
cp mySecrets.py.sample mySecrets.py
```

Edit `mySecrets.py` to include your API key and Last.fm username:

```python
# mySecrets.py

API_KEY = 'your_lastfm_api_key'
USER = 'your_lastfm_username'
```

### 5. Running the Application

The main entry point to the application is `selectAlbum.py`. Run the script to randomly select an album from your top 100:

```bash
python selectAlbum.py
```

### 6. Logging and Album Tracking

- **Selected Albums:** The script logs selected albums in a `selected_albums.json` file to avoid picking the same album twice.
- **Top 100 Albums:** The script keeps track of the top 100 albums in `current_top_albums.json`. If there are any changes in your top 100 (new additions or albums being bumped out), the script will print these changes to the console.

## Files and Structure

- `selectAlbum.py`: Main entry point for selecting an album.
- `main.py`: Contains the function to fetch the top 100 albums from Last.fm.
- `mySecrets.py.sample`: A sample secrets file template.
- `mySecrets.py`: Your personal secrets file containing your API key and username (should be kept secret and gitignored).
- `selected_albums.json`: Stores the list of albums that have been selected.
- `current_top_albums.json`: Stores the latest top 100 albums for tracking changes.

## .gitignore

The `.gitignore` file is configured to ignore:

- The `venv/` directory (your virtual environment).
- The `mySecrets.py` file (your secrets file containing sensitive information).
- The `selected_albums.json` and `current_top_albums.json` files (tracking logs).

## Contributing

Feel free to fork this repository and make your own modifications. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is open-source and available under the MIT License.
