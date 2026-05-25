import products
import store


def start(best_buy_store: store.Store):
    while True:

        print("\n   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        user_input = input("Please choose an option (1-4): ").strip()

        if user_input == "1":

            print("\n--- Products in Store ---")
            active_products = best_buy_store.get_all_products()
            for index, product in enumerate(active_products, start=1):
                # Nutzen der show()-Methode aus der Product-Klasse
                print(f"{index}. ", end="")
                product.show()

        elif user_input == "2":
            # Gesamte Produktanzahl anzeigen
            total_quantity = best_buy_store.get_total_quantity()
            print(f"\nTotal amount of items in store: {total_quantity}")

        elif user_input == "3":
            # Eine Bestellung aufgeben
            print("\n--- Make an Order ---")
            active_products = best_buy_store.get_all_products()


            for index, product in enumerate(active_products, start=1):
                print(f"{index}. ", end="")
                product.show()

            shopping_list = []
            print("\n(Leave product number empty or type '0' to finish your order)")

            while True:
                prod_choice = input("Which product do you want to buy? (Enter number): ").strip()
                if prod_choice == "" or prod_choice == "0":
                    break

                try:
                    prod_index = int(prod_choice) - 1
                    if 0 <= prod_index < len(active_products):
                        selected_product = active_products[prod_index]

                        qty_choice = input(f"How many '{selected_product.name}' do you want?: ").strip()
                        quantity = int(qty_choice)

                        shopping_list.append((selected_product, quantity))
                        print(f"Added {quantity}x {selected_product.name} to cart.")
                    else:
                        print("Invalid product number. Please try again.")
                except ValueError:
                    print("Please enter valid numbers.")

            if shopping_list:
                try:
                    total_cost = best_buy_store.order(shopping_list)
                    print(f"\nOrder successful! Total cost: {total_cost} dollars.")
                except ValueError as error:
                    print(f"\nOrder failed: {error}")
            else:
                print("\nOrder canceled. Cart is empty.")

        elif user_input == "4":

            print("\nThank you for shopping at Best Buy! Goodbye!")
            break
        else:
            print("Invalid input. Please choose a number between 1 and 4.")


def main():

    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250)
    ]

    # Store initialisieren
    best_buy = store.Store(product_list)

    # UI starten
    start(best_buy)


if __name__ == "__main__":
    main()
