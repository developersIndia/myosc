<p align="center">
  <p align="center">
  <a href=""><img src="https://github.com/Bhupesh-V/moc/blob/main/assets/logo.png?raw=true" alt="moc-action-logo" height="400px"></a>
  </p>
</p>


## ❓ Usage

### Example workflow

- You can use the following workflow as it is, just copy/paste in a file named `my-contributions.yml` inside your [workflows](https://github.com/Bhupesh-V/moc/tree/main/.github/workflows) folder.
- You can manually trigger builds but the recommended way is to add cron build.
- The push action is performed by [ad-m/github-push-action](https://github.com/ad-m/github-push-action)

```yaml
name: My Contributions

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Self Test 👀
        id: selftest
        uses: Bhupesh-V/moc@main
        with:
          username: "${{ github.actor }}"
          filename: "my-prs.md"
      - name: Commit files ✅
        run: |
          git config --local user.name  ${{ github.actor }}
          git add .
          git commit -m "Automated Commit: generate contributions file"
      - name: Push changes
        uses: ad-m/github-push-action@master
        with:
          branch: main
          github_token: ${{ secrets.GITHUB_TOKEN }}
          force: true

```

### Inputs

moc accepts following input variables.

- `username` (required) : Your github username.
- `filename` (optional) : A filename for the new markdown file, defaults to README.md


## Author [![bhupesh-twitter-image](https://kutt.it/bhupeshimself)](https://twitter.com/bhupeshimself)

👤 **[Bhupesh Varshney](https://bhupesh-v.github.io)** 

## ☺️ Show your support

Support me by giving a ⭐️ if this project helped you! or just [![Twitter URL](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fgithub.com%2FBhupesh-V%2Ftil%2F)](https://twitter.com/intent/tweet?url=https://github.com/Bhupesh-V/til&text=til%20via%20@bhupeshimself)

<a href="https://liberapay.com/bhupesh/donate">
  <img alt="Donate using Liberapay" src="https://liberapay.com/assets/widgets/donate.svg" width="100">
</a>
<a href="https://ko-fi.com/bhupesh">
  <img title="ko-fi/bhupesh" alt="Support on ko-fi" src="https://user-images.githubusercontent.com/34342551/88784787-12507980-d1ae-11ea-82fe-f55753340168.png" width="185">
</a>


## 📝 License

Copyright © 2020 [Bhupesh Varshney](https://github.com/Bhupesh-V).<br />
This project is [GPLV3](https://github.com/Bhupesh-V/memer-action/blob/master/LICENSE) licensed.
