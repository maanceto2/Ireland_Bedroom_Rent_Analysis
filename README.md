# Room for Rent: Analyzing IRELAND's Shared Bedroom Market
After six months of living in Italy’s Abruzzo region and a summer spent roaming through Europe, I knew it was time for a fresh start. The question was, where in the EU would I begin this new chapter?

The two top contenders in the top of my head were Berlin and Dublin. Berlin drew me in with its vibrant nightlife–perfect for a techno goth like myself–and its renowned high quality of life. On the other hand, Dublin offered a smoother transition, with English as the primary language (a big plus since my German skills are still a work in progress), the promise of higher salaries, and the added familiar comfort of having friends and family already settled in Ireland.

In the end, the ease of integration and career opportunities tipped the scale in favour of Dublin, making it the ideal place for my new adventures. With that decision made, it was time to tackle the most critical practical consideration: What does the room rental market look like in Dublin–and across Ireland?

First Part: Collecting the Data
To gather the data I needed, I conducted a quick online search for the most popular websites for renting bedrooms in Ireland. In my opinion rent.ie stood out as the most user-friendly platform, offering the largest selection of listings in the categories I was focused on—single and double shared rooms. I focused on Dublin, since it had a lot more entries, but I also did the research for other bigger cities (Galway, Cork, Waterford and Limerick).

To collect the data, I used Python’s BeautifulSoup to scrape information on bedroom prices, descriptions, and addresses. You can check out all the code on my GitHub page. To avoid overwhelming the servers and risking a ban, I opted to retrieve the data manually page by page instead of automating the process with a loop. After a few hours fixing bugs and using ChatGPT to guide me I got several CSV files with the data I wanted. I then joined the files using a Pandas function and added it to separate directories. All the data collected and the codes are available in my GitHub page, which you can check in the contact links.



 
 
