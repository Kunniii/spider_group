from requests import get
from os.path import abspath, join
from bs4 import BeautifulSoup


class Spider:
    base_url = "https://fap.fpt.edu.vn/Course/Groups.aspx"
    headers = {
        "authority": "fap.fpt.edu.vn",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "image",
        "sec-fetch-mode": "no-cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Googlebot",
    }

    def __init__(self, cookie, group) -> None:
        self.headers["cookie"] = cookie
        self.params = {"group": group}

    def save(self, content) -> None:
        with open(
            abspath(join("./downloads", str(self.params["group"]))) + ".html",
            "w+",
            encoding="utf-8",
        ) as f:
            f.write(content)

    def get_table(self, html: str):
        soup = BeautifulSoup(html, "html.parser")
        div = soup.find("div", {"id": "ctl00_mainContent_divStudents"})
        body = div.find("tbody")
        return body

    def run(self) -> None:
        res = get(self.base_url, params=self.params, headers=self.headers)
        if res.ok:
            body = self.get_table(res.text)
            self.save(str(body))
        else:
            print(f"{self.group}: ERR!")
