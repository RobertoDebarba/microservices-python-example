from nameko.rpc import rpc, RpcProxy

class Stock:
	name = "stock"
	
	@rpc
	def remove(self, product_id):
		print("Product %d was removed from stock." % product_id)

class Sale:
	name = "sale"
	stock = RpcProxy("stock")
	
	@rpc
	def sell(self, product_id):
		self.stock.send.async(product_id)
		print("Product %d was sold!" % product_id)
		return True
