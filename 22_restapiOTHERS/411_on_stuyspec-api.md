Collected Knowledge & Wisdom on
# Stuyvesant Spectator API
---
## Provides:
This API provides data on The Spectator's articles and contributors

### Pain factor: 2

### Key Provisioning:     

No key required for public/unprivileged endpoints

### Quotas:
- No quotas, but please don't spam the API. We are in the process of rewriting the website though

---

## The Good:
- You can get data about articles
## The Bad:
- Server is sometimes down due to excessive CPU-intensive API calls
## The Ugly:
- You can't query articles or users based on slug. There is a GraphQL API for that type of stuff


**Location:** https://api.stuyspec.com/

**Routes:**

```https://api.stuyspec.com/articles/<id>``` 
- Fetch an article given the id. Returns data like `id`, `title`, `slug`, `content`, `volume`, `issue`, `is_published`, `created_at`, `updated_at`, `section_id`, `rank`, `summary`, and `preview`

```https://api.stuyspec.com/users/<id>```
- Fetches a user's basic information given id

```https://api.stuyspec.com/media/<id>```
- Fetches title, media, thumbnail, attachment URLs given id

**All of the above routes could be requested without id, but please don't spam. Thanks**
---

Accurate as of (last update):    2021-11-22

Contributors:
David Chen, pd7   
Jing Feng, pd7  

---

##Tested By: LimeTricycles

- While the card states that you can find an article given the id, which is true, we were unable to find any trace of the article id from the stuyspec.com website. 
- Thus, while there is no way to initially access the article without the article id, we were able to discover that you can search for articles using the article name instead, which is not mentioned in the documentation.
- The above is not the case for writers. We were not able to access writer data because of the lack of id.
- I was thinking about the usefulness of this API and tried to search by is_published to sort by newest articles, but was unable to do so without trying to download every single article and then using a json to sort through is_published. Sorry for crashing the API and the stuyspec.com website for about 30 minutes D:
- Your API card says last update was 2021.

Tested as of:    2022-11-29

Contributors:
Ravindra Mangar, pd7  
Jun Hong Wang, pd7   

---
