<p align="center">
  <p align="center">
  <a href=""><img src="https://github.com/Bhupesh-V/moc/blob/main/assets/logo.png?raw=true" alt="moc-action-logo" height="400px"></a>
  </p>
</p>

[![Integration Test](https://github.com/developersIndia/moc/actions/workflows/integration.yml/badge.svg?branch=main)](https://github.com/developersIndia/moc/actions/workflows/integration.yml) ![GitHub](https://img.shields.io/github/license/developersIndia/moc?color=%23848484&label=License&logo=GitHub) ![Discord](https://img.shields.io/discord/669880381649977354?color=%237289da&label=Discord&logo=Discord) ![Subreddit subscribers](https://img.shields.io/reddit/subreddit-subscribers/developersIndia?style=social)

## Folk's using `moc`

- [**`Bhupesh-V's` list of contributions**](https://github.com/Bhupesh-V/my-contributions)
- [`+ Add yourself`](https://github.com/developersIndia/moc/pulls)


## ❓ Usage

### Example workflow

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
      uses: developersIndia/moc@main
      with:
        username: "${{ github.actor }}"
        filename: "README.md"
```

### Inputs

moc accepts following input variables.

- `username` (required) : Your github username.
- `filename` (optional) : A filename for the new markdown file, defaults to README.md

## 📝 License

This project is [GPLV3](https://github.com/Bhupesh-V/memer-action/blob/master/LICENSE) licensed.
