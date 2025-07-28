from fastmcp import FastMCP

mcp = FastMCP(name="Restaurant Menu")

restaurant_menu = {
    "Margherita Pizza": {
        "price": 8.99,
        "description": "Classic pizza with fresh mozzarella, basil, and tomato sauce.",
    },
    "Spaghetti Carbonara": {
        "price": 12.50,
        "description": "Traditional Italian pasta with creamy egg sauce, pancetta, and parmesan.",
    },
    "Caesar Salad": {
        "price": 7.25,
        "description": "Crisp romaine lettuce tossed with Caesar dressing, croutons, and parmesan cheese.",
    },
    "Grilled Chicken Sandwich": {
        "price": 9.75,
        "description": "Juicy grilled chicken breast with lettuce, tomato, and mayo on a toasted bun.",
    },
    "Mango Smoothie": {
        "price": 4.50,
        "description": "Refreshing smoothie made with ripe mangoes and yogurt.",
    },
    "Chocolate Lava Cake": {
        "price": 6.00,
        "description": "Warm chocolate cake with a gooey molten center, served with vanilla ice cream.",
    },
}


@mcp.tool
def get_item_details(name: str):
    """Returns details of a menu item given its name."""
    return restaurant_menu[name]


@mcp.tool
def get_complete_menu():
    """Return complete menu."""
    return restaurant_menu
