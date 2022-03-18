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
name: Build My Contributions List

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

`myosc` accepts following input variables.

- `username` (required) : Your github username.
- `filename` (optional) : A filename for the new markdown file where report will be added, defaults to README.md


### Demos

Check the [`my-prs.md`](https://github.com/developersIndia/myosc/blob/main/my-prs.md) file to see how the report looks like

### ✨ Customization

`myosc` supports custom header and footers for the README report. You can leverage this to add custom badges, licenses or any other info before and after the report

<img width="885" alt="Screenshot 2022-03-18 at 11 18 12 AM" src="https://user-images.githubusercontent.com/34342551/158944975-8e4ae9ec-ca32-44f6-8c5f-84cbf9419b4d.png">


1. Create a file named `HEADER.md` if you want to append something before the report.
2. Create a file named `FOOTER.md` if you want to append something after the report.


## 📝 License

This project is [GPLV3](https://github.com/Bhupesh-V/memer-action/blob/master/LICENSE) licensed.
