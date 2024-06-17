def budgeting(budget, products, wishlist):
    total_cost = 0
    sorted_products = sorted(products.items(), key=lambda x: x[1])  # Sort products by price

    for product, quantity in wishlist.items():
        if product in products:
            price = products[product]
            max_quantity = budget // price  # Maximum quantity that can be bought with the budget

            if quantity > max_quantity:
                wishlist[product] = max_quantity  # Adjust quantity to fit the budget
                total_cost += max_quantity * price
            else:
                total_cost += quantity * price

    if total_cost > budget:
        remaining_budget = budget - total_cost

        for product, quantity in sorted_products:
            if product in wishlist:
                price = products[product]
                max_quantity = remaining_budget // price

                if max_quantity < wishlist[product]:
                    wishlist[product] = max_quantity  # Adjust quantity to fit the remaining budget
                    remaining_budget -= max_quantity * price

                    if remaining_budget <= 0:
                        break

    return wishlist
