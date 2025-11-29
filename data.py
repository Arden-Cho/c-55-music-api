from dataclasses import dataclass


@dataclass
class Music:
    id: str
    title: str
    date: str
    author: str


MUSIC_LIST = [
    Music(id="That's_Why_I_Gave_Up_on_Music", title="だから僕は音楽を辞めた", date="2019/4/10", author="ヨルシカ"),
    Music(id="Elma", title="エルマ", date="2019/4/10", author="ヨルシカ"),
    Music(id="Amy", title="エイミー", date="2019/8/28", author="ヨルシカ"),
    Music(id="Rain_with_Cappuccino", title="雨とカプチーノ", date="2019/8/28", author="ヨルシカ"),
]
