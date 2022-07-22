import random
from lunar_python import Lunar
import datetime

langs = []
with open("./data/langs.txt", 'r') as f:
    langs = f.readlines()
    langs = list(map(lambda s: s.strip(), langs))

verbs = []

with open("./data/Cal_verbs.txt", 'r', encoding='utf-8') as f:
    verbs = f.readlines()

sfmt = "宜：\n{}\n忌：\n{}"


def get_huangli(salt: str):
    random.seed(salt + str(datetime.date.today()))
    today = Lunar.fromDate(datetime.datetime.now())
    r = random.choices(verbs, k=4)
    i = [t.format(lang=random.choice(langs)) for t in r]
    good = "".join(i[0:2])
    bad = "".join(i[2:4])
    return {'info': today.toFullString()+'\n', 'todo': sfmt.format(good, bad)}
