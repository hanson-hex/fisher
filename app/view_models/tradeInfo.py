
class TradeInfo():
    def __init__(self, goods):
        self.total = len(goods)
        self.trades = self._parse(goods)

    def _parse(self, goods):
        return [self._map_to_trade(good) for good in goods]

    def _map_to_trade(self, single):
        if single.create_datetime:
            time = single.create_datetime.strftime('%Y-%m-%d')
        else:
            time = '未知'
        return dict(
            user_name=single.user.nickname,
            id=single.id,
            time=time
        )


