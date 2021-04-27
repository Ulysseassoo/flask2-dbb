# Flask2

## Paste as Markdown

This application looks at first like a pastebin.com, a dpaste.de or my wyz.fr, but accepts only Markdown.

One does not have to create an account to paste.

The app should allow one to choose a part of the path of the page (leaving the path blank auto-generate a path, like tinyurl does).

All pastes should be rooted on a fixed path like /articles/, so if I choose to paste with the URL "i18n", the final URL will be /articles/i18n.

While querying the URL, the pasted markdown should be rendered as HTML on the body of the page, with nothing more, nothing less.

## Bonus

- An admin zone should allow to add/edit/remove markdown pastes. The admin is under /admin/ and it's not the role of the app to block non-admin users to acces the user page.
- Write tests.
- Write a README.md.
- Format using black.
- Don't give me your venv.

## Install dependencies :

You need to 'pip install -r requirements.txt' in order to have the the dependencies
