from client.inventory_client import InventoryClient, getBookTitlesFromServer

"""Delegate get book titles functionality and retrieve result from server.

    Args:
        ISBNs: List of ISBN for query.

    Returns:
        List of book titles.
"""
def get_book_titles(ISBNs):
    client = InventoryClient()
    titles = getBookTitlesFromServer(client, ISBNs)
    print(titles)

if __name__ == '__main__':
    ISBNs = ["9789573264354","9780441172719"]
    get_book_titles(ISBNs)