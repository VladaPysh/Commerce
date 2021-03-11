# Commerce
An eBay-like e-commerce auction site that allows users to post auction listings, place bids on listings, comment on those listings, and add listings to a “watchlist.”

Demo: https://youtu.be/BinZOXTGBFM

- Create Listing: Users are able to visit a page to create a new listing. They can specify a title for the listing, a text-based description, upload an image and set what the starting bid should be.
- Active Listings Page: The default route lets users view all of the currently active auction listings.
- Listing Page: Clicking on a listing takes users to a page specific to that listing. On that page, users view all details about the listing, including the current price. If the user is signed in, the user can add the item to their “Watchlist.” If the item is already on the watchlist, the user is able to remove it.
If the user is signed in, the user can bid on the item. The bid must be at least as large as the starting bid, and must be greater than any other bids that have been placed. If the user is signed in and is the one who created the listing, the user has the ability to “close” the auction from this page, which makes the highest bidder the winner of the auction and makes the listing no longer active. If a user is signed in on a closed listing page, and the user has won that auction, the page says so. Users are able to add comments to the listing page or remove their own comments.
- Watchlist: displays all of the listings that a user has added to their watchlist. Clicking on any of those listings them to that listing’s page.
- Categories: Clicking on the name of any category takes the user to a page that displays all of the active listings in that category.
- Search: Users are able to search for a specific item providing its name.
