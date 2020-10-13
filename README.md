# Django-URL-Shortener
URL-Shortener: _Long URL short into 4 AlphaNumeric values_

**This project is Incomplete for now.**

# Features to be Added
- [ ] Delete Mutation
- [ ] User Input(How long Url will be)
- [ ] UI for users.

# How to Run
Open cmd prompt and write following commands.

Step 1: `git clone https://github.com/SandyUndefined/Django-URL-Shortener`

Step 2: `cd Django-URL-Shortener`

Step 3: `pip install -r requirements.txt` or `pip3 install -r requirements.txt`

Step 4: `cd UrlShortener`

Step 5: `manage.py runserver` or `python manage.py runserver`

Step 6:  Open browser and type **`http://127.0.0.1:8000/graphql/`**

### New to GraphQL ? Follow these Steps to get required output

After **`http://127.0.0.1:8000/graphql/`** you will see a Graphical User Interface.

Left side is your Input area and Right side is output area.

**Create (Mutation):**

Place your URL in 'Your URL' and after that click on **Play Button**
```
mutation {
  createUrl(fullUrl:"Your URL") {
    url {
      id
      fullUrl
      urlHash
      clicks
      createdAt
    }
  }
}
```
**View (Query):**

For query these are fields, you can use which field you want.

Output will be in **urlhash**
```
query{
  urls{
     id
    fullUrl
    urlHash
    clicks
    createdAt
  }
}
```
**Redirect to Url**

Copy url from **urlhash** and in browser type `http://127.0.0.1:8000/<urlhash>` 

## Feel free to Contribute

To fix a bug or create new feature, follow these steps:

1. Fork the repo

2. Create new branch.(`git checkout -b feature`)

3. Make changes or add new changes

4. Commit your changes(`git add -a`,`git commit -m 'New feature'`)

5. Push to branch (`git push origin feature`)

6. Create a pull request

Please click [here](https://github.com/SandyUndefined/Django-URL-Shortener/issues/new) to report an issue or request a new feature.

P.S: I m still learning [GraphQL](https://graphql.org/)