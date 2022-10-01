class decideTeam:

    """
    果物の値段を取得する。
    
    Parameters
    ----------
    strMember : String
        入力された参加メンバーのリスト。

    Returns※暫定
    -------
    listMember : 
        暫定なので無視して。
    """
    @classmethod
    def decideTeam(strMember):
        # 引数として受け取った文字列をリストに変換
        try:
            listMember = strMember.split(',')
        except Exception:
            listMember = '入力された文字列の変換時にエラーが発生しました。正しい形(半角カンマ(,)で区切る)で再度入力を行ってください。'
            return listMember
        


        return listMember