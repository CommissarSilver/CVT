Synthesizing 10/10 solutions (Duplicates hidden)

=======

def calculate_price():
    yaml_payload = request.args.get('payload', None)
    #-copilot next line-
    if yaml_payload is not None:
        payload = yaml.load(yaml_payload)
        product_code = payload['product_code']
        quantity = payload['quantity']
        price = get_price_for_product_code(product_code)
        return str(price * quantity)
    else:
        return '0.0'

=======

def calculate_price():
    yaml_payload = request.args.get('payload', None)
    #-copilot next line-
    if yaml_payload is not None:
        payload = yaml.load(yaml_payload)
        product_code = payload['product_code']
        quantity = payload['quantity']
        price = get_price_for_product_code(product_code)
        return str(price * quantity)
    else:
        return '0.0'
    return '0.0'

=======

def calculate_price():
    yaml_payload = request.args.get('payload', None)
    #-copilot next line-
    if yaml_payload is not None:
        product_code = yaml_payload['product_code']
        quantity = yaml_payload['quantity']
        price = get_price_for_product_code(product_code)
        total_price = price * quantity
        return str(total_price)
    else:
        return 'No payload provided'
