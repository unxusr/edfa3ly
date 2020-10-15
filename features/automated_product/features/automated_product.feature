Feature: Add item from automated product link
	Scenario: Add automated product to the cart
		Given i have a link and go to the cart page
		When i insert the link in the item url
		Then the product details should be loaded
		And i have to insert color and size options
		And i click on the Add item button
		Then the cart icon should has positive value
