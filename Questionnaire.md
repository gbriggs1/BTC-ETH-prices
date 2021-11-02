# Answers to the Questionare

**1.** Are there any sub-optimal choices( or short cuts taken due to limited time ) in your implementation?

Due to some unfimiliarity with HTML, I had to hardcode some of the design of the front-end (such as indenting and spacing). This also lead to me altering data in flask to leave less of the implementation to the HTML script.

**2.** Is any part of it over-designed? ( It is fine to over-design to showcase your skills as long as you are clear about it)

The only feature that I included that could be considered an 'over-design' was the 'refresh' button. By clicking this it allows you to update the prices and recommendations on your page.

**3.** If you have to scale your solution to 100 users/second traffic what changes would you make, if any?

Currently, every time the page is refreshed, the server script makes a request to both the Kraken and the Coinbase API. With a large amount of users, you would not want each user making their own requests to the APIs every time they open and refresh the page - both for efficiency and for potential limits on the amount of requests the APIs allow. To avoid this, we could be frequently making API requests on a single node and reading the responses into a database and the server would gather its information from the database rather than making an API request every time. This way, no matter how many users are on the site, it would have the same frequency of requests. 

**4.** What are some other enhancements you would have made, if you had more time to do this implementation

With more time, I would have formatted my HTML to be more readable and easier to build upon for future work. I would have also liked to add more design to the webpage as well as features (such as linking directly to the Coinbase or Kraken website).  
