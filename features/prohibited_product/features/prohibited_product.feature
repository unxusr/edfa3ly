Feature: Add a prohibited product
	Scenario: Try to add a prohibited product to the cart
		Given i have a prohibited product link and go to cart page
		When i add the link
		Then i should be notified that this product is not available 
