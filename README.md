## captain-chen.github.io

This repository contains the source files used by [Pelican](https://getpelican.com/) to generate the content for [captain-chen.github.io](https://captain-chen.github.io/) I use as my portfolio. The website uses simple CSS to make sure the content is readable on both desktop and mobile devices. 

There are two distinct branches:
* The [src](https://github.com/captain-chen/captain-chen.github.io/tree/src) branch contains the source files.
* The [gh-pages](https://github.com/captain-chen/captain-chen.github.io/tree/gh-pages) branch is used by GitHub Actions to deploy the static website.

I build the site locally using [ghp-import](https://github.com/c-w/ghp-import) then commit and deploy my changes to the `gh-pages` branch. The rest of the deployment is taken care of by GitHub Actions.