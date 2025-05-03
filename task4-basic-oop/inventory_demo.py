from product import Product
# Example usage:
try:
    product = Product("Apple", 0.7, 150)
    print(product.display_info())
    product.add_inventory(70)
    print(product.display_info())
    product.remove_inventory(30)
    print(product.display_info())
except ValueError as e:
    print(e)
except Exception as e:
    print(f"An unexpected error occurred: {e}")