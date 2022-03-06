<h1 align="center">myosc</h1>
<p align="center">
  Flex your open-source contributions like a pro 🤟🏽 <br>
  A github action to list all your pull requests in a markdown file
</p>

<!-- <p align="center">
  <p align="center">
  <a href=""><img src="https://github.com/Bhupesh-V/moc/blob/main/assets/logo.png?raw=true" alt="moc-action-logo" height="400px"></a>
  </p>
</p> -->

<p align="center">
  <p align="center">
  <a href="https://github.com/developersIndia/myosc/actions/workflows/integration.yml"><img src="https://github.com/developersIndia/myosc/actions/workflows/integration.yml/badge.svg?branch=main"></a>
    <a href=""><img src="https://img.shields.io/github/license/developersIndia/myosc?color=orange&label=License&logo=GitHub"></a>
    <a href="https://discord.gg/MKXMSNC"><img src="https://img.shields.io/discord/669880381649977354?color=%237289da&label=Discord&logo=Discord"></a>
    <a href="https://www.reddit.com/r/developersIndia/"><img src="https://img.shields.io/reddit/subreddit-subscribers/developersIndia?style=social"></a>
  </p>
</p>



## ❓ Usage

- You can use the following workflow as it is, just copy/paste in a file named `my-contributions.yml` inside your workflows directory.
- You can manually trigger builds but the recommended way is to schedule the build using cron.
<!-- - The push action is performed by [ad-m/github-push-action](https://github.com/ad-m/github-push-action) -->

```yaml
name: Build Contributions List

on:
  push:
  workflow_dispatch:
  schedule:
  # run once every month
    - cron:  '0 0 1 * *'

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Generate My PRs List 👀
      uses: developersIndia/myosc@main
      with:
        username: "${{ github.actor }}"
        filename: "README.md"
```

### Inputs

myosc accepts following input variables.

- `username` (required) : Your github username.
- `filename` (optional) : A filename for the new markdown file, defaults to README.md

## Folk's using `myosc`

- [**`Bhupesh-V's` list of contributions**](https://github.com/Bhupesh-V/my-contributions)
- [`+ Add yourself`](https://github.com/developersIndia/myosc/pulls)

## 📝 License

This project is [GPLV3](https://github.com/Bhupesh-V/memer-action/blob/master/LICENSE) licensed.
