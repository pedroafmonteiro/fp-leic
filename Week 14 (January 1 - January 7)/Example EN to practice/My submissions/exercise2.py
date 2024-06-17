def shopping(alist, stock):
    spent = 0
    missing = alist.copy()
    for wanted in alist.keys():
        for items in stock.keys():
            quantity, price = stock[items]
            if wanted == items:
                if alist[wanted] > quantity:
                    rest = alist[wanted] - quantity
                    missing[wanted] -= quantity
                    spent += price * quantity  # Corrected line
                else:
                    quantity -= alist[wanted]  # Incorrect line
                    spent += price * alist[wanted]
                    del missing[wanted]
    return (spent, missing)