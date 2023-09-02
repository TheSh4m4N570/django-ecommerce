
class Cart:

    def __init__(self, request):

        self.session = request.session
        # returning user - obtain his or her existing session
        cart = self.session.get('session_key')

        # a new user - generate a new session
        if 'session_key' not in request.session:
            cart = self.session['session'] = {}

        self.cart = cart

    def add(self, product, product_qty):
        product_id = str(product.id)
        if product_id in self.cart:
            self.cart[product_id]['qty'] = product_qty
        else:
            self.cart[product_id] = {'price': str(product.price), 'qty': product_qty}

        self.session.modified = True

    def __len__(self):
        return sum(item['qty'] for item in self.cart.values())