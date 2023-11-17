
<div align="center">
    
[![Author][autor-shield]][autor-url] [![Author][autor-description]][autor-url]  
[![LinkedIn][linkedin-shield]][linkedin-url] [![Whatsapp][whatsapp-shield]][whatsapp-url] [![Gmail][gmail-shield]][gmail-url]

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

  
</div>

# Notion SDK for Python

This repository provides assistance in using the Notion Python client library to interact with the Notion API using the official Notion SDK for JavaScript or Python.

## Installation

To get started, you will need to install the Notion SDK for JavaScript library. You can do this by running the following command:

```bash
npm install @notionhq/client
```

Additionally, you will need the `notion-client` library for Python. Make sure to install this library using:

```bash
pip install notion-client
```

## Usage

See the example below to understand how to use the library in your Python code:

```python
from notion_client import Client
import pprint

# Replace with your credentials
notion_token = "your_notion_secret_key"
notion_page_id = "notion_page_id"
notion_database_id = ""

def main():
    # Initialize the Notion client
    client = Client(auth=notion_token)

    # Retrieve information from the page
    page_response = client.pages.retrieve(notion_page_id)

    # Print the response in a formatted way
    pprint.pprint(page_response)

if __name__ == "__main__":
    main()
```

## Code Functions

### `write_text`

Adds a text block to a Notion page.

```python
def write_text(client, page_id, text, type):
    """
    Adds a text block to a Notion page.

    Args:
        client (Client): Notion client instance.
        page_id (str): ID of the page where the text block will be added.
        text (str): Text to be added.
        type (str): Block type (e.g., "paragraph").

    Returns:
        None
    """
    # Function implementation
```

### `write_dict_to_file_as_json`

Writes a dictionary to a JSON file.

```python
def write_dict_to_file_as_json(content, file_name):
    """
    Writes a dictionary to a JSON file.

    Args:
        content (dict): Dictionary to be written.
        file_name (str): File name.

    Returns:
        None
    """
    # Function implementation
```

### `read_text`

Reads text from a Notion page.

```python
def read_text(client, page_id):
    """
    Reads text from a Notion page.

    Args:
        client (Client): Notion client instance.
        page_id (str): Page ID.

    Returns:
        list: List of text blocks on the page.
    """
    # Function implementation
```

### `safe_get`

Gets a value from a dictionary or list using a dot-chained key string.

```python
def safe_get(data, dot_chined_keys):
    """
    Gets a value from a dictionary or list using a dot-chained key string.

    Args:
        data (dict or list): Dictionary or list to be accessed.
        dot_chined_keys (str): Dot-chained key string (e.g., "a.b.0.c").

    Returns:
        Value corresponding to the keys, or None if the key does not exist.
    """
    # Function implementation
```

### `create_blocks_from_content`

Creates a simplified representation of blocks from Notion API content.

```python
def create_blocks_from_content(client, content):
    """
    Creates a simplified representation of blocks from Notion API content.

    Args:
        client (Client): Notion client instance.
        content (list): List of Notion API blocks.

    Returns:
        list: List of simplified blocks.
    """
    # Function implementation
```

### `main`

Main function that interacts with the Notion API to retrieve information and generate JSON files.

```python
def main():
    """
    Main function that interacts with the Notion API to retrieve information and generate JSON files.
    """
    # Function implementation
```

## Additional Documentation

For more details on the Notion API and additional integration options, refer to the [official Notion API documentation](https://developers.notion.com/).

### Useful References:

- [Notion SDK for JavaScript](https://github.com/makenotion/notion-sdk-js)
- [Official Notion API Documentation](https://developers.notion.com/)

## Contributions

Contributions are welcome! Feel free to [open pull requests](https://github.com/your-username/your-python-repository/fork) or propose improvements to this repository.

**Note:** Please make sure to follow the [Python code standards](https://www.python.org/dev/peps/pep-0008/) when contributing to this project. We recommend that you fork the repository before making changes.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- AUTHOR-->
[autor-shield]: https://img.shields.io/badge/Author-00acac?
[autor-url]: https://github.com/andersonlimacrv/
[autor-description]: https://img.shields.io/badge/Anderson%20Carvalho-141321?labelColor=141321

<!-- MARKDOWN SOCIAL MEDIA-->
[linkedin-shield]: https://img.shields.io/badge/LinkedIn-%230077B5.svg?&logo=linkedin&logoColor=white&style=plastic
[linkedin-url]: https://linkedin.com/in/andersonlimacrv
[facebook-url]: https://facebook.com/andersonlimacrv
[facebook-shield]: https://img.shields.io/badge/Facebook-%231877F2.svg?&logo=Facebook&logoColor=white&style=plastic
[gmail-url]: mailto:andersonlimacrv@gmail.com
[gmail-shield]: https://img.shields.io/badge/Gmail-D14836?&logo=gmail&logoColor=white&style=plastic
[whatsapp-url]: https://wa.me/5553981004874
[whatsapp-shield]: https://img.shields.io/badge/WhatsApp-25D366?&logo=whatsapp&logoColor=white&style=plastic
[twitter-url]: https://twitter.com/andersoncrvl
[twitter-shield]: https://img.shields.io/badge/Twitter-1D9BF0.svg?&logo=Twitter&logoColor=white&style=plastic

<!-- MARKDOWN LINKS -->
[contributors-shield]: https://img.shields.io/github/contributors/andersonlimacrv/notion-client-py.svg?style=plastic
[contributors-url]: https://github.com/andersonlimacrv/notion-client-py/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/andersonlimacrv/notion-client-py.svg?style=plastic
[forks-url]:https://github.com/andersonlimacrv/notion-client-py/network/members
[stars-shield]: https://img.shields.io/github/stars/andersonlimacrv/notion-client-py.svg?style=plastic
[stars-url]: https://github.com/andersonlimacrv/notion-client-py/stargazers
[issues-shield]: https://img.shields.io/github/issues/andersonlimacrv/notion-client-py.svg?style=plastic
[issues-url]: https://github.com/andersonlimacrv/notion-client-py/issues
[license-shield]: https://img.shields.io/github/license/andersonlimacrv/notion-client-py.svg?style=plastic
[license-url]: https://github.com/andersonlimacrv/notion-client-py/blob/main/LICENSE

