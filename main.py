from notion_client import Client
import pprint
import os
from dotenv import load_dotenv

load_dotenv()

notion_token = os.environ.get("NOTION_TOKEN")
notion_page_id = os.environ.get("NOTION_PAGE_ID")
notion_database_id = os.environ.get("NOTION_DATABASE_ID")

# simplepage_url = https://www.notion.so/teste-d795e0a64647446e88d9bdfde79872b6

# database_url = https://www.notion.so/Blog-Database-3129ecab36b74596ab52783ccd8340ff


def write_text(client, page_id, text, type):
    client.blocks.children.append(
        block_id=page_id,
        children=[
            {
                "object": "block",
                "type": type,
                type: {"rich_text": [{"type": "text", "text": {"content": text}}]},
            }
        ],
    )


def main():
    client = Client(auth=notion_token)
    page_response = client.pages.retrieve(notion_page_id)
    # database = client.databases.retrieve(notion_database_id)

    write_text(client, notion_page_id, "Hello, World!", "quote")

    pprint.pprint(page_response)
    # print(database)


if __name__ == "__main__":
    main()
