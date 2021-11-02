# Answers to the Questionare

**1.** Are there any sub-optimal choices( or short cuts taken due to limited time ) in your implementation?

**2.** Is any part of it over-designed? ( It is fine to over-design to showcase your skills as long as you are clear about it)

**3.** If you have to scale your solution to 100 users/second traffic what changes would you make, if any?
Currently, every time the page is refreshed, the server script makes a request to both the Kraken and the Coinbase API. With a large amount of users, you would not want each user making their own requests to the API every time they open and refresh the page - both for efficiency and for potential limits on the amount of requests the APIs allow. To avoid this, we could be frequently making pull requests on a single node and reading the responses into a database and the server would gather its information from the database rather than making an API request every time. This way, no matter how many users are on the site, it would have the same frequency of requests. 

**4.** What are some other enhancements you would have made, if you had more time to do this implementation
