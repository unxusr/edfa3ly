Feature: Add item from NON automated product link
	Scenario: Add NON automated product to the cart
		Given i have a link and go to the cart page
		When i insert the link in the item url
		Then the product details should Not be loaded
		And i have to insert all product details
		And i click on the Add item button
		Then the cart icon should has positive value

