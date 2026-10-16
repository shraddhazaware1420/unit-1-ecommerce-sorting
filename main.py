"""
Name: Zaware Shraddha Sandip
Roll No.: 67 | Division: B | Batch: C
Unit I Case Study: E-commerce Product Sorting
Algorithm: Merge Sort (Divide and Conquer)
"""

from dataclasses import dataclass


@dataclass
class Product:
    product_id: int
    name: str
    category: str
    price: float
    rating: float


def merge_sort(products, key):
    """Sort products by key using the merge sort algorithm."""
    if len(products) <= 1:
        return products

    middle = len(products) // 2
    left_half = merge_sort(products[:middle], key)
    right_half = merge_sort(products[middle:], key)

    return merge(left_half, right_half, key)


def merge(left, right, key):
    """Combine two sorted lists into one sorted list."""
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if key(left[left_index]) <= key(right[right_index]):
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result


def display_products(products):
    if not products:
        print("No products to display.")
        return

    print(
        f"\n{'ID':<5} {'Product':<24} {'Category':<16} "
        f"{'Price (₹)':>12} {'Rating':>8}"
    )
    print("-" * 70)

    for product in products:
        print(
            f"{product.product_id:<5} "
            f"{product.name:<24} "
            f"{product.category:<16} "
            f"{product.price:>12.2f} "
            f"{product.rating:>8.1f}"
        )


def main():
    products = [
        Product(101, "Wireless Headphones", "Electronics", 2499.00, 4.5),
        Product(102, "Running Shoes", "Footwear", 3199.00, 4.2),
        Product(103, "Python Programming", "Books", 799.00, 4.8),
        Product(104, "Smart Watch", "Electronics", 4599.00, 4.1),
        Product(105, "Travel Backpack", "Accessories", 1899.00, 4.4),
        Product(106, "Desk Lamp", "Home", 999.00, 4.0),
    ]

    sort_options = {
        "1": ("price", lambda product: product.price),
        "2": ("name", lambda product: product.name.lower()),
        "3": ("rating", lambda product: product.rating),
    }

    while True:
        print("\n=== E-commerce Product Catalog ===")
        print("1. Display all products")
        print("2. Sort products by price (low to high)")
        print("3. Sort products by name (A to Z)")
        print("4. Sort products by rating (low to high)")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            display_products(products)
        elif choice in sort_options:
            sort_name, key_function = sort_options[choice]
            sorted_products = merge_sort(products, key_function)
            print(f"\nProducts sorted by {sort_name}:")
            display_products(sorted_products)
        elif choice == "0":
            print("Thank you for using the product catalog.")
            break
        else:
            print("Invalid option. Please choose 0, 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()