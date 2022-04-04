def flattenCodes(codeList):
    flattened_codes = []
    for code in codeList:
        flattened_codes.append("*")
        for item in code:
            flattened_codes.append(item)
    return flattened_codes

def freshPromotion(shoppingCart, codeList):
    WINNER = 1
    LOSER = 0

    flattened_code_list = flattenCodes(codeList)
    flattened_code_list_length = len(flattened_code_list)
    shopping_cart_length = len(shoppingCart)

    code_idx = 0
    shopping_cart_idx = 0

    star_idx = -1
    tmp_shopping_cart_idx = -1

    while shopping_cart_idx < shopping_cart_length:
        if code_idx < flattened_code_list_length and flattened_code_list[code_idx] in ["anything", shoppingCart[shopping_cart_idx]]:
            shopping_cart_idx += 1
            code_idx += 1
        elif code_idx < flattened_code_list_length and flattened_code_list[code_idx] == "*":
            star_idx = code_idx
            tmp_shopping_cart_idx = shopping_cart_idx
            code_idx += 1
        elif star_idx == -1:
            return LOSER
        else:
            code_idx = star_idx + 1
            shopping_cart_idx = tmp_shopping_cart_idx + 1
            tmp_shopping_cart_idx = shopping_cart_idx

    return WINNER if all(flattened_code_list[i] == "*" for i in range(code_idx, flattened_code_list_length)) else LOSER
            

def main():
    shoppingCart = ["banana", "apple", "orange", "apple", "apple", "orange", "banana"]
    codeList = [["banana", "apple", "apple"], ["anything"]]
    result = freshPromotion(shoppingCart, codeList)
    print(result)

if __name__ == "__main__":
    main()